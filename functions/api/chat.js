// Cloudflare Pages Function: assistente del Quaderno di acquerello basato su Gemini.
// Senza email e senza archivio: 5 domande a settimana per connessione e un tetto complessivo
// giornaliero, contati su D1 con un'impronta dell'indirizzo IP calcolata con una chiave segreta.
// Domande e risposte non si conservano. Il prompt di sistema si genera dai dati del sito
// (scripts/genera-sito.py scrive lib/prompt-chat.js).

import { PROMPT_SISTEMA } from "../../lib/prompt-chat.js";

const MODELLO = "gemini-4-argon";
const LIMITE_SETTIMANALE = 5;
const LIMITE_GIORNALIERO = 10;
const BYTE_MASSIMI = 12000;
const GIORNI_CONSERVAZIONE = 14;

// Gli stessi indirizzi delle pagine del sito: scripts/genera-sito.py si ferma se non coincidono.
const PAGINE_VALIDE = [
  "/",
  "/principi/",
  "/studio-plein-air/",
  "/colori/",
  "/marche/",
  "/soggetti/",
  "/alberi/"
];

function rispostaJson(dati, stato = 200) {
  return new Response(JSON.stringify(dati), {
    status: stato,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}

function esadecimale(buffer) {
  return Array.from(new Uint8Array(buffer), (b) => b.toString(16).padStart(2, "0")).join("");
}

async function sha256(testo) {
  return esadecimale(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(testo)));
}

async function chiaveHmac(segreto) {
  return crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode("firma-cronologia|" + segreto),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
}

// Firma di una coppia domanda-risposta: il browser la rimanda con la cronologia, e il server
// accetta come risposte del modello solo quelle che ha firmato lui.
async function firma(chiave, domanda, risposta) {
  const dati = new TextEncoder().encode(domanda + "\u0000" + risposta);
  return esadecimale(await crypto.subtle.sign("HMAC", chiave, dati));
}

// Lunedì della settimana corrente (UTC), che fa da chiave del periodo settimanale.
function settimana(adesso) {
  const d = new Date(Date.UTC(adesso.getUTCFullYear(), adesso.getUTCMonth(), adesso.getUTCDate()));
  d.setUTCDate(d.getUTCDate() - ((d.getUTCDay() + 6) % 7));
  return d.toISOString().slice(0, 10);
}

async function conCreazione(db, eseguiQuery) {
  try {
    return await eseguiQuery();
  } catch (err) {
    if (!/no such table/i.test(String(err && err.message))) throw err;
    await db
      .prepare(
        "CREATE TABLE IF NOT EXISTS contatori (chiave TEXT NOT NULL, giorno TEXT NOT NULL, " +
          "n INTEGER NOT NULL, PRIMARY KEY (chiave, giorno))"
      )
      .run();
    return await eseguiQuery();
  }
}

// Incrementa il contatore solo se è sotto il limite, in una sola istruzione: due richieste
// simultanee non possono superarlo. Restituisce null quando il limite è raggiunto.
function incrementa(db, chiave, periodo, limite) {
  const sql =
    "INSERT INTO contatori (chiave, giorno, n) VALUES (?, ?, 1) " +
    "ON CONFLICT (chiave, giorno) DO UPDATE SET n = n + 1 WHERE n < ? RETURNING n";
  return conCreazione(db, () => db.prepare(sql).bind(chiave, periodo, limite).first());
}

function rilascia(db, chiave, periodo) {
  return db
    .prepare("UPDATE contatori SET n = n - 1 WHERE chiave = ? AND giorno = ? AND n > 0")
    .bind(chiave, periodo)
    .run();
}

async function usate(db, chiave, periodo) {
  const riga = await conCreazione(db, () =>
    db.prepare("SELECT n FROM contatori WHERE chiave = ? AND giorno = ?").bind(chiave, periodo).first()
  );
  return riga ? riga.n : 0;
}

// Cancella i contatori con più di GIORNI_CONSERVAZIONE giorni. La tabella è la stessa di
// suggerimento.js, che la pulisce con la stessa regola. Il «giorno» dei contatori settimanali è il
// lunedì: con la soglia a 13 giorni nessuna riga resta oltre 14 giorni dalla sua creazione.
function cancellaVecchi(db, adesso) {
  const soglia = new Date(adesso.getTime() - (GIORNI_CONSERVAZIONE - 1) * 86400 * 1000).toISOString().slice(0, 10);
  return conCreazione(db, () => db.prepare("DELETE FROM contatori WHERE giorno < ?").bind(soglia).run());
}

export async function onRequestPost(context) {
  const db = context.env.DB;
  const apiKey = context.env.GEMINI_API_KEY;
  if (!db || !apiKey) {
    return rispostaJson({ ok: false, errore: "L'assistente non è configurato sul server." }, 503);
  }

  const grezzo = await context.request.text();
  if (grezzo.length > BYTE_MASSIMI) {
    return rispostaJson({ ok: false, errore: "Richiesta troppo lunga." }, 413);
  }
  let body;
  try {
    body = JSON.parse(grezzo);
  } catch {
    body = null;
  }
  if (!body || typeof body !== "object" || Array.isArray(body)) {
    return rispostaJson({ ok: false, errore: "Formato della richiesta non valido." }, 400);
  }

  const adesso = new Date();
  const periodo = settimana(adesso);
  const giorno = adesso.toISOString().slice(0, 10);
  const ip = context.request.headers.get("CF-Connecting-IP") || "locale";
  const sale = context.env.SALE_IP || "chat:" + apiKey;
  const chiaveIp = "chat-ip:" + (await sha256(`${sale}|${periodo}|${ip}`)).slice(0, 24);

  if (body.azione === "stato") {
    // Lo stato si chiede a ogni pagina aperta: è il momento della pulizia.
    await cancellaVecchi(db, adesso);
    const n = await usate(db, chiaveIp, periodo);
    return rispostaJson({ ok: true, limite: LIMITE_SETTIMANALE, rimanenti: Math.max(0, LIMITE_SETTIMANALE - n) });
  }
  if (body.azione !== "chiedi") {
    return rispostaJson({ ok: false, errore: "Azione non valida." }, 400);
  }

  const domanda = String(body.domanda || "").trim().slice(0, 1000);
  if (domanda.length < 4) {
    return rispostaJson({ ok: false, errore: "Scrivi una domanda un po' più precisa (almeno 4 caratteri)." }, 400);
  }
  const paginaRaw = String(body.pagina || "/").trim();
  const pagina = PAGINE_VALIDE.includes(paginaRaw) ? paginaRaw : "/";

  // Prima si prenota la domanda, poi si chiama il modello: se la chiamata fallisce la si restituisce.
  const perIp = await incrementa(db, chiaveIp, periodo, LIMITE_SETTIMANALE);
  if (!perIp) {
    return rispostaJson(
      {
        ok: false,
        rimanenti: 0,
        limite: LIMITE_SETTIMANALE,
        errore: `Le ${LIMITE_SETTIMANALE} domande di questa settimana sono esaurite: si rinnovano il lunedì. Le sezioni del Quaderno e il calcolatore restano liberamente consultabili.`,
      },
      429
    );
  }
  const complessivo = await incrementa(db, "chat-globale", giorno, LIMITE_GIORNALIERO);
  if (!complessivo) {
    await rilascia(db, chiaveIp, periodo);
    return rispostaJson(
      { ok: false, errore: "L'assistente ha raggiunto il numero massimo di domande per oggi: riprova domani." },
      429
    );
  }
  if (complessivo.n === 1) {
    await cancellaVecchi(db, adesso);
  }

  // Cronologia: al massimo le ultime due coppie domanda-risposta, e solo se firmate dal server.
  const hmac = await chiaveHmac(context.env.CHIAVE_FIRMA || apiKey);
  const contents = [];
  const storia = Array.isArray(body.storia) ? body.storia.slice(-2) : [];
  for (const coppia of storia) {
    if (!coppia || typeof coppia !== "object") continue;
    const d = String(coppia.domanda || "").slice(0, 1000);
    const r = String(coppia.risposta || "").slice(0, 4000);
    if (!d || !r || String(coppia.firma || "") !== (await firma(hmac, d, r))) continue;
    contents.push({ role: "user", parts: [{ text: d }] }, { role: "model", parts: [{ text: r }] });
  }
  contents.push({ role: "user", parts: [{ text: `[Pagina visitata: ${pagina}]\nDomanda: ${domanda}` }] });

  let risposta = "";
  try {
    const geminiRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODELLO}:generateContent`, {
      method: "POST",
      headers: { "Content-Type": "application/json", "x-goog-api-key": apiKey },
      body: JSON.stringify({
        systemInstruction: { parts: [{ text: PROMPT_SISTEMA }] },
        contents,
        generationConfig: { thinkingConfig: { thinkingLevel: "low" }, maxOutputTokens: 2048 },
      }),
    });
    if (geminiRes.ok) {
      const dati = await geminiRes.json();
      const parti = (((dati.candidates || [])[0] || {}).content || {}).parts || [];
      risposta = parti.filter((p) => p.text && !p.thought).map((p) => p.text).join("").trim();
    }
  } catch {
    risposta = "";
  }
  if (!risposta) {
    await rilascia(db, chiaveIp, periodo);
    await rilascia(db, "chat-globale", giorno);
    return rispostaJson(
      { ok: false, errore: "L'assistente non è riuscito a rispondere in questo momento. La domanda non è stata conteggiata: riprova tra poco." },
      502
    );
  }

  return rispostaJson({
    ok: true,
    modello: MODELLO,
    domanda,
    risposta,
    firma: await firma(hmac, domanda, risposta),
    limite: LIMITE_SETTIMANALE,
    rimanenti: Math.max(0, LIMITE_SETTIMANALE - perIp.n),
  });
}

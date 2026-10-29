// Cloudflare Pages Function: riceve un suggerimento dalla casella del sito
// e apre una segnalazione pubblica (Issue) su GitHub in sinmar123/app-acquerello.

const REPO = "sinmar123/app-acquerello";

// Le stesse voci del menu «Sezione di riferimento» e gli stessi indirizzi delle pagine che
// scripts/genera-sito.py mette nel sito: il generatore si ferma se i due elenchi non coincidono.
const SEZIONI_VALIDE = [
  "Generale / Nuovo argomento",
  "Principi",
  "Teoria dei colori",
  "Confronto marche",
  "Soggetti (Alberi, Nuvole, Fiori...)",
  "Approfondimenti",
  "Eventi",
  "Opere"
];
const PAGINE_VALIDE = [
  "/",
  "/principi/",
  "/colori/",
  "/marche/",
  "/soggetti/",
  "/alberi/",
  "/approfondimenti/",
  "/eventi/",
  "/opere/"
];

// Stessa regola di chat.js: la scheda di un evento resta la pagina di partenza.
function paginaNelSito(paginaRaw) {
  const pagina = String(paginaRaw || "/").trim();
  if (PAGINE_VALIDE.includes(pagina)) return pagina;
  if (!/^\/[a-z0-9/-]+\/$/.test(pagina)) return "/";
  for (const base of PAGINE_VALIDE) {
    if (base !== "/" && pagina.startsWith(base)) return pagina;
  }
  return "/";
}

// Tetti contro gli invii automatici, contati su D1 per giorno (UTC).
const LIMITE_IP_GIORNALIERO = 5;
const LIMITE_GIORNALIERO = 30;
const BYTE_MASSIMI = 8000;
// La tabella dei contatori è la stessa di chat.js, che vi tiene anche i contatori settimanali
// (col lunedì come giorno): le due funzioni la puliscono con la stessa regola.
const GIORNI_CONSERVAZIONE = 14;

function oscuraEmail(str) {
  return String(str || "").replace(
    /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g,
    "[email rimossa per privacy]"
  );
}

// Uno spazio di larghezza zero dopo la chiocciola: GitHub non trasforma «@nome» in una menzione
// e non manda la notifica a quell'utente.
function senzaMenzioni(str) {
  return String(str || "").replace(/@(?=[A-Za-z0-9-])/g, "@\u200b");
}

function pulisci(str, massimo) {
  return senzaMenzioni(oscuraEmail(String(str || "").trim())).slice(0, massimo);
}

function rispostaJson(dati, stato = 200) {
  return new Response(JSON.stringify(dati), {
    status: stato,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}

async function sha256(str) {
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(str));
  return Array.from(new Uint8Array(digest), (b) => b.toString(16).padStart(2, "0")).join("");
}

// Incrementa il contatore (chiave, giorno) solo se è sotto il limite, in una sola istruzione:
// due richieste simultanee non possono superarlo. Restituisce null quando il limite è raggiunto.
async function incrementa(db, chiave, giorno, limite) {
  const sql =
    "INSERT INTO contatori (chiave, giorno, n) VALUES (?, ?, 1) " +
    "ON CONFLICT (chiave, giorno) DO UPDATE SET n = n + 1 WHERE n < ? RETURNING n";
  try {
    return await db.prepare(sql).bind(chiave, giorno, limite).first();
  } catch (err) {
    if (!/no such table/i.test(String(err && err.message))) throw err;
    await db
      .prepare(
        "CREATE TABLE IF NOT EXISTS contatori (chiave TEXT NOT NULL, giorno TEXT NOT NULL, " +
          "n INTEGER NOT NULL, PRIMARY KEY (chiave, giorno))"
      )
      .run();
    return await db.prepare(sql).bind(chiave, giorno, limite).first();
  }
}

export async function onRequestPost(context) {
  const token = context.env.GITHUB_SUGGERIMENTI_TOKEN;
  const db = context.env.DB;
  if (!token || !db) {
    return rispostaJson(
      {
        ok: false,
        errore:
          "Servizio di invio diretto non configurato sul server. Puoi aprire la segnalazione direttamente su GitHub.",
      },
      503
    );
  }

  const grezzo = await context.request.text();
  if (grezzo.length > BYTE_MASSIMI) {
    return rispostaJson({ ok: false, errore: "Segnalazione troppo lunga." }, 413);
  }
  let payload;
  try {
    payload = JSON.parse(grezzo);
  } catch {
    payload = null;
  }
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    return rispostaJson({ ok: false, errore: "Formato della richiesta non valido." }, 400);
  }

  // Filtro anti-bot (campo esca, invisibile a chi usa il modulo)
  if (payload.miele && String(payload.miele).trim() !== "") {
    return rispostaJson({ ok: false, errore: "Invio bloccato dal filtro automatico." }, 400);
  }

  const sezione = String(payload.sezione || SEZIONI_VALIDE[0]).trim();
  if (!SEZIONI_VALIDE.includes(sezione)) {
    return rispostaJson({ ok: false, errore: "Sezione di riferimento non valida." }, 400);
  }
  const titolo = pulisci(payload.titolo, 120);
  const testo = pulisci(payload.testo, 3500);
  const firma = pulisci(payload.firma, 60).replace(/[\r\n]+/g, " ");
  const pagina = paginaNelSito(payload.pagina);

  if (titolo.length < 4) {
    return rispostaJson(
      { ok: false, errore: "Inserisci un titolo breve (almeno 4 caratteri)." },
      400
    );
  }
  if (testo.length < 10) {
    return rispostaJson(
      { ok: false, errore: "Descrivi il suggerimento (almeno 10 caratteri)." },
      400
    );
  }

  // Tetti giornalieri: per connessione e complessivo. L'impronta dell'indirizzo IP cambia ogni
  // giorno ed è calcolata con un sale segreto, quindi non si ricostruisce dal codice pubblico.
  const giorno = new Date().toISOString().slice(0, 10);
  const ip = context.request.headers.get("CF-Connecting-IP") || "locale";
  const sale = context.env.SALE_IP || "suggerimenti:" + token;
  const impronta = (await sha256(`${sale}|${giorno}|${ip}`)).slice(0, 24);
  const perIp = await incrementa(db, `sugg-ip:${impronta}`, giorno, LIMITE_IP_GIORNALIERO);
  if (!perIp) {
    return rispostaJson(
      { ok: false, errore: "Hai già inviato diverse segnalazioni oggi: riprova domani o usa il link a GitHub." },
      429
    );
  }
  const complessivo = await incrementa(db, "sugg-globale", giorno, LIMITE_GIORNALIERO);
  if (!complessivo) {
    return rispostaJson(
      { ok: false, errore: "Raggiunto il numero massimo di segnalazioni per oggi: riprova domani o usa il link a GitHub." },
      429
    );
  }
  if (complessivo.n === 1) {
    const soglia = new Date(Date.now() - (GIORNI_CONSERVAZIONE - 1) * 86400 * 1000).toISOString().slice(0, 10);
    await db.prepare("DELETE FROM contatori WHERE giorno < ?").bind(soglia).run();
  }

  const corpo = [
    "### Suggerimento inviato dalla casella del sito",
    "",
    `- **Sezione:** ${sezione}`,
    `- **Pagina di partenza:** \`${pagina}\``,
    `- **Inviato da:** ${firma ? firma : "*Anonimo*"}`,
    "",
    "---",
    "",
    testo,
    "",
    "---",
    "*Segnalazione inviata tramite il modulo pubblico di [app-acquerello.pages.dev](https://app-acquerello.pages.dev) e rilasciata sotto licenza CC BY 4.0.*",
  ].join("\n");

  const ghRes = await fetch(`https://api.github.com/repos/${REPO}/issues`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: "application/vnd.github+json",
      "Content-Type": "application/json; charset=utf-8",
      "User-Agent": "app-acquerello-cloudflare-pages",
      "X-GitHub-Api-Version": "2022-11-28",
    },
    body: JSON.stringify({
      title: `[Suggerimento · ${sezione}] ${titolo}`,
      body: corpo,
      labels: ["suggerimento-dal-sito"],
    }),
  });

  if (!ghRes.ok) {
    return rispostaJson(
      {
        ok: false,
        errore:
          "Impossibile registrare la segnalazione in questo momento. Riprova tra poco o usa il link a GitHub.",
      },
      502
    );
  }

  const issue = await ghRes.json();
  return rispostaJson({
    ok: true,
    numero: issue.number,
    url: issue.html_url,
  });
}

// Cloudflare Pages Function: Assistente di studio sull'acquerello basato su Gemini 4 Argon
// Accesso tramite email con limite di 5 domande gratuite per utente (salvate su Cloudflare D1).

const MODELLO = "gemini-4-argon";
const LIMITE_DEFAULT = 5;
const LIMITE_IP_GIORNALIERO = 10;

const DOMINI_BLOCCATI = new Set([
  "mailinator.com",
  "tempmail.com",
  "10minutemail.com",
  "guerrillamail.com",
  "yopmail.com",
  "trashmail.com",
  "sharklasers.com",
  "example.com",
  "test.com",
]);

const PROMPT_SISTEMA = `Sei l'assistente didattico del «Quaderno di acquerello» (https://app-acquerello.pages.dev), una guida pratica aperta per chi studia l'acquerello su piccoli foglietti di prova (A5).

Conosci a fondo la struttura e le regole del Quaderno:
1. Sezione «Principi generali» (/principi/):
   - Le 3 consistenze del colore in tavolozza: «tè» (molta acqua e poco pigmento, per cieli, prati e prime velature), «latte» (acqua e pigmento bilanciati, per i toni medi), «miele» o burro morbido (pochissima acqua e colore denso, per rami, tronchi, ombre profonde e per entrare su carta umida senza fare fioriture).
   - I 3 stati della carta: «bagnata» (velo d'acqua lucido uniforme senza pozzanghere), «umida» (quando il lucido dell'acqua è appena scomparso e la carta è opaca e fresca: momento chiave per aggiungere colore morbido senza cavolfiori, spargere il sale o incidere i rami), «asciutta» (per bordi netti e pennello asciutto).
   - Regola d'oro contro le fioriture (cavolfiori / backruns): non entrare mai su carta umida con un pennello più acquoso di quello che c'è già sul foglio; su carta umida si entra solo con colore più denso (latte o miele) o con pennello scarico.

2. Sezione «Alberi ad acquerello» (/alberi/):
   - 6 esempi rappresentativi con 24 modalità tratte dai video (ciascuna con infografica in 3 fasi e video al secondo esatto):
     * A1: Abeti e conifere in gruppo (spina di pesce col ventre del tondo, punta schiacciata a ventaglio tra le dita, pennello a ventaglio, stacco in negativo).
     * A2: Abeti alti e radi contro il cielo (piani di rami orizzontali staccati lasciando aria, pennello tenuto piatto, pennello quasi asciutto di lato, tronco scavato con l'angolo del piatto umido).
     * A3: Chiome tonde d'autunno (fusione bagnato su bagnato dal giallo al terra di Siena bruciata su fondo pre-bagnato o su chioma umida, stacco contro conifere scure, tronchi incisi col bordo di una tessera).
     * A4: Siepi e cespugli nel paesaggio (fascia calda autunnale con base scura, base scura sciolta a tratti col piatto umido verso il prato, cespuglio a cupola per strati, chiome chiare contornate in negativo, ombra fredda alla base).
     * A5: Alberi invernali con fusti chiari e brina (fusti sottili col tiralinee e liquido mascherante + ombra su un solo lato, tronchi dritti col nastro di carta, sale fino sparso appena sparisce il lucido, massa scura in negativo sfumata con acqua, velo di rametti col ventaglio).
     * A6: Rami sottili e foglie brinate in primo piano (rami tirati dal basso in su alleggerendo la pressione con biforcazioni a V e Y che si incrociano, foglie scure risparmiando un filo bianco di brina poi ammorbidito col pennello appena umido).

3. Sezione «Teoria dei colori e calcolatore» (/colori/):
   - Sistema di Munsell: Tinta (hue), Valore (value, chiaro/scuro regolato dall'acqua), Croma (saturazione).
   - Sintesi sottrattiva (Kubelka-Munk): mescolare troppi pigmenti spegne il croma; spesso è meglio sovrapporre velature su carta asciutta.
   - La tavolozza ridotta a 6 colori di base (utile all'aperto o per iniziare con pochi tubetti), chiamati sempre col nome comune e il codice del pigmento (Colour Index):
     1) Giallo limone (PY175, semitrasparente)
     2) Ceruleo (PB15, blu ftalo schiarito nelle serie studio, oppure PB35/PB36 nelle serie professionali)
     3) Cremisi (PR206 o PR179/PV19)
     4) Terra di Siena bruciata (PR101, arancio-mattone caldo)
     5) Terra d'ombra bruciata (PBr7 + PY42, bruno scuro che con l'oltremare dà i neri e i grigi neutri)
     6) Blu oltremare (PB29, blu caldo granulante)
   - In studio i colori sono liberi (es. verde vescica, verde oliva, terra di Siena naturale, ocra gialla, indaco, grigio di Payne, blu di Prussia, seppia), ma con i 6 colori di base si ottengono le 12 miscele principali (M1..M12) del quaderno.

4. Sezione «Marche e tubetti» (/marche/):
   - Confronto tra Winsor & Newton Cotman, Winsor & Newton Professional, Van Gogh, Daniel Smith, Schmincke Horadam e Maimeri Blu: conta sempre la sigla del pigmento (PY, PR, PB, PBr, PG) sull'etichetta e non il nome commerciale.

Regole di risposta:
- Rispondi SEMPRE in italiano corretto, con tono cordiale, pratico e incoraggiante.
- Sii conciso e concreto (circa 100-220 parole): dai indicazioni operative che chi dipinge può provare subito sul foglietto A5 (quanta acqua, stato della carta, quale pennello e quali pigmenti usare).
- Rispondi ESCLUSIVAMENTE a domande che riguardano la pittura ad acquerello, il disegno, i colori, la carta, i pennelli o l'uso di questo sito. Se l'utente fa domande su argomenti che non c'entrano con l'acquerello o il disegno (es. programmazione, politica, matematica, traduzioni generiche, ricette di cucina), rifiuta gentilmente in una riga dicendo che questo assistente risponde solo a domande sull'acquerello e sulle guide del Quaderno.`;

function rispostaJson(dati, stato = 200) {
  return new Response(JSON.stringify(dati), {
    status: stato,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}

function validaEmail(emailRaw) {
  const email = String(emailRaw || "").trim().toLowerCase();
  if (email.length < 6 || email.length > 120) return null;
  const re = /^[a-z0-9._%+-]+@([a-z0-9.-]+\.[a-z]{2,})$/;
  const m = email.match(re);
  if (!m) return null;
  const dominio = m[1];
  if (DOMINI_BLOCCATI.has(dominio)) return null;
  return email;
}

async function hashTesto(str) {
  const buf = new TextEncoder().encode(str);
  const digest = await crypto.subtle.digest("SHA-256", buf);
  return Array.from(new Uint8Array(digest))
    .slice(0, 12)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

async function assicuraTabelle(db) {
  await db
    .prepare(
      `CREATE TABLE IF NOT EXISTS utenti_chat (
        email TEXT PRIMARY KEY,
        domande_usate INTEGER NOT NULL DEFAULT 0,
        limite_domande INTEGER NOT NULL DEFAULT 5,
        primo_accesso TEXT NOT NULL,
        ultimo_accesso TEXT NOT NULL
      )`
    )
    .run();
  await db
    .prepare(
      `CREATE TABLE IF NOT EXISTS messaggi_chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        ip_hash TEXT,
        pagina TEXT,
        domanda TEXT NOT NULL,
        risposta TEXT NOT NULL,
        token_in INTEGER,
        token_out INTEGER,
        creato_il TEXT NOT NULL
      )`
    )
    .run();
}

export async function onRequestPost(context) {
  const db = context.env.DB;
  const apiKey = context.env.GEMINI_API_KEY;

  if (!db) {
    return rispostaJson(
      { ok: false, errore: "Database della chat non ancora collegato sul server." },
      503
    );
  }

  let body;
  try {
    body = await context.request.json();
  } catch {
    return rispostaJson({ ok: false, errore: "Formato della richiesta non valido." }, 400);
  }

  const email = validaEmail(body.email);
  if (!email) {
    return rispostaJson(
      { ok: false, errore: "Inserisci un indirizzo email valido per accedere alla chat." },
      400
    );
  }

  await assicuraTabelle(db);
  const oraIso = new Date().toISOString();

  // Recupera o crea la scheda dell'utente
  let utente = await db
    .prepare("SELECT email, domande_usate, limite_domande FROM utenti_chat WHERE email = ?")
    .bind(email)
    .first();

  if (!utente) {
    await db
      .prepare(
        "INSERT INTO utenti_chat (email, domande_usate, limite_domande, primo_accesso, ultimo_accesso) VALUES (?, 0, ?, ?, ?)"
      )
      .bind(email, LIMITE_DEFAULT, oraIso, oraIso)
      .run();
    utente = { email, domande_usate: 0, limite_domande: LIMITE_DEFAULT };
  } else {
    await db
      .prepare("UPDATE utenti_chat SET ultimo_accesso = ? WHERE email = ?")
      .bind(oraIso, email)
      .run();
  }

  const azione = String(body.azione || "chiedi");
  if (azione === "stato") {
    const rimanenti = Math.max(0, utente.limite_domande - utente.domande_usate);
    return rispostaJson({
      ok: true,
      email: utente.email,
      usate: utente.domande_usate,
      limite: utente.limite_domande,
      rimanenti,
    });
  }

  // Azione: chiedi una domanda a Gemini 4 Argon
  if (!apiKey) {
    return rispostaJson(
      { ok: false, errore: "Chiave del modello AI non configurata sul server." },
      503
    );
  }

  if (utente.domande_usate >= utente.limite_domande) {
    return rispostaJson(
      {
        ok: false,
        esaurite: true,
        usate: utente.domande_usate,
        limite: utente.limite_domande,
        rimanenti: 0,
        errore:
          "Hai utilizzato tutte le 5 domande gratuite associate a questa email. Stiamo preparando una formula per chi desidera fare più domande: nel frattempo puoi usare liberamente tutte le guide e il calcolatore di miscele.",
      },
      429
    );
  }

  const domanda = String(body.domanda || "").trim().slice(0, 1000);
  if (domanda.length < 4) {
    return rispostaJson(
      { ok: false, errore: "Scrivi una domanda un po' più descrittiva (almeno 4 caratteri)." },
      400
    );
  }

  // Controllo anti-abuso per IP nelle ultime 24 ore
  const ipRaw = context.request.headers.get("CF-Connecting-IP") || "local";
  const ipHash = await hashTesto("acquerello-ip-" + ipRaw);
  const ieriIso = new Date(Date.now() - 86400 * 1000).toISOString();
  const contaIp = await db
    .prepare("SELECT COUNT(*) AS n FROM messaggi_chat WHERE ip_hash = ? AND creato_il > ?")
    .bind(ipHash, ieriIso)
    .first();

  if (contaIp && contaIp.n >= LIMITE_IP_GIORNALIERO) {
    return rispostaJson(
      {
        ok: false,
        errore:
          "È stato raggiunto il limite giornaliero di domande da questa connessione. Riprova domani.",
      },
      429
    );
  }

  // Costruisce i messaggi con eventuale breve cronologia della sessione (max 4 turni precedenti)
  const contents = [];
  if (Array.isArray(body.storia)) {
    for (const turno of body.storia.slice(-4)) {
      if (turno && (turno.ruolo === "user" || turno.ruolo === "model") && turno.testo) {
        contents.push({
          role: turno.ruolo,
          parts: [{ text: String(turno.testo).slice(0, 1200) }],
        });
      }
    }
  }
  const pagina = String(body.pagina || "/").slice(0, 80);
  contents.push({
    role: "user",
    parts: [{ text: `[Pagina visitata: ${pagina}]\nDomanda: ${domanda}` }],
  });

  const urlGemini = `https://generativelanguage.googleapis.com/v1beta/models/${MODELLO}:generateContent`;
  const geminiRes = await fetch(urlGemini, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-goog-api-key": apiKey,
    },
    body: JSON.stringify({
      systemInstruction: { parts: [{ text: PROMPT_SISTEMA }] },
      contents,
      generationConfig: {
        thinkingConfig: { thinkingLevel: "low" },
        maxOutputTokens: 2048,
      },
    }),
  });

  if (!geminiRes.ok) {
    return rispostaJson(
      {
        ok: false,
        errore:
          "L'assistente AI non è riuscito a rispondere in questo momento. La domanda non è stata scalata dal tuo conteggio: riprova tra poco.",
      },
      502
    );
  }

  const datiGemini = await geminiRes.json();
  const parti =
    ((datiGemini.candidates || [])[0] &&
      datiGemini.candidates[0].content &&
      datiGemini.candidates[0].content.parts) ||
    [];
  const pezziTesto = [];
  for (const p of parti) {
    if (p.text && !p.thought) {
      pezziTesto.push(p.text);
    }
  }
  const risposta = pezziTesto.join("").trim();
  if (!risposta) {
    return rispostaJson(
      {
        ok: false,
        errore: "Risposta vuota dal modello. La domanda non è stata scalata.",
      },
      502
    );
  }

  const uso = datiGemini.usageMetadata || {};
  const tokenIn = uso.promptTokenCount || 0;
  const tokenOut = (uso.candidatesTokenCount || 0) + (uso.thoughtsTokenCount || 0);

  // Aggiorna contatore e salva il messaggio su D1
  const nuoveUsate = utente.domande_usate + 1;
  await db
    .prepare("UPDATE utenti_chat SET domande_usate = ?, ultimo_accesso = ? WHERE email = ?")
    .bind(nuoveUsate, oraIso, email)
    .run();

  await db
    .prepare(
      "INSERT INTO messaggi_chat (email, ip_hash, pagina, domanda, risposta, token_in, token_out, creato_il) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    )
    .bind(email, ipHash, pagina, domanda, risposta, tokenIn, tokenOut, oraIso)
    .run();

  const rimanenti = Math.max(0, utente.limite_domande - nuoveUsate);
  return rispostaJson({
    ok: true,
    modello: MODELLO,
    risposta,
    usate: nuoveUsate,
    limite: utente.limite_domande,
    rimanenti,
  });
}

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

const PROMPT_SISTEMA = `Sei il consulente tecnico-didattico del «Quaderno di acquerello» (https://app-acquerello.pages.dev), un repertorio metodologico ad accesso aperto — in fase di sviluppo e progressiva estensione — dedicato allo studio sistematico della pittura ad acquerello su formati di studio ridotti (A5, 148 × 210 mm).

Conosci in dettaglio l'impianto teorico e operativo del Quaderno:
1. Sezione «Principi generali» (/principi/):
   - I 3 gradi di diluizione della miscela in tavolozza (scala di Zbukvic): «tè» (elevata frazione acquosa e minima concentrazione di pigmento, per campiture atmosferiche, cieli e prime velature di fondo), «latte» (rapporto equilibrato fra acqua e legante/pigmento, scorrevole ma coprente, per i valori tonali intermedi e la definizione delle masse), «miele» o burro ammorbidito (minima frazione d'acqua e massima densità di pigmento, per gli accenti scuri finali, le ramificazioni e per intervenire su supporto umido senza innescare riflussi d'acqua).
   - I 3 stati igrometrici della carta in cotone (300 g/m²): «bagnata» (velo d'acqua superficiale continuo a riflessione speculare, privo di ristagni localizzati), «umida» (fase di transizione in cui il riflesso speculare è appena scomparso e la superficie appare satinata e fredda al tatto: finestra operativa ottimale per depositare miscele dense a margini morbidi, applicare cloruro di sodio o incidere a sgraffito), «asciutta» (fibre stabilizzate, per velature a bordi netti e stesure a pennello scarico / drybrush).
   - Principio idrodinamico contro le fioriture (riflussi / backruns): non introdurre mai su una campitura in fase di asciugatura un pennello con carica idrica superiore a quella del supporto; su carta umida si interviene esclusivamente con miscela più concentrata (consistenza «latte» o «miele») o con pennello parzialmente scaricato su carta assorbente.

2. Sezione «Morfologia ed esecuzione degli alberi» (/alberi/) — primo modulo monografico pubblicato (in quanto primo argomento affrontato nel corso di studio; seguiranno progressivamente moduli analoghi dedicati a cieli e formazioni nuvolose, fiori ed elementi botanici, specchi d'acqua e riflessi, masse rocciose e architetture):
   - 6 tipologie arboree e vegetazionali articolate in 24 modalità esecutive tratte da dimostrazioni filmate (ciascuna corredata da tavola sinottica in 3 fasi e rimando temporizzato al secondo esatto):
     * A1: Abeti e conifere in quinte compatte (costruzione a spina di pesce col ventre del pennello tondo, apertura a ventaglio della punta tra le dita per texture frastagliate, impiego del pennello a ventaglio, profilatura in negativo dei fusti chiari).
     * A2: Conifere d'alto fusto a chioma rada (stratificazione di palchi orizzontali distanziati lasciando visibile il fondo atmosferico, tocco di piatto con pennello tondo, stesura a pennello scarico di fianco sulla grana della carta, estrazione del fusto per asportazione d'umidità con l'angolo del pennello piatto).
     * A3: Latifoglie a chioma espansa in veste autunnale (fusione bagnato su bagnato dal giallo limone alla terra di Siena bruciata su fondo pre-inumidito o internamente alla sagoma umida, risalto per contrasto simultaneo contro quinte scure di conifere, incisione dei fusti per sgraffito con spigolo rigido).
     * A4: Quinte arbustive, siepi e cespugli nel paesaggio (fascia cromatica autunnale ancorata a un'ombra basale scura, raccordo selettivo del margine inferiore col pennello piatto umido verso il piano erboso, modellazione volumetrica a cupola per velature successive, isolamento in negativo delle fronde illuminate, ombra portata fredda sul terreno).
     * A5: Fusti spogli, betulle e ramificazioni invernali (riserva dei fusti sottili tramite tiralinee e fluido mascherante con ombreggiatura cilindrica monolaterale, riserva rettilinea mediante nastro di carta strappato longitudinalmente, tessitura cristallina per cristallizzazione salina su campitura satinata, modellazione per risparmio in negativo sfumata con acqua pura, velatura di ramificazioni minute col pennello a ventaglio).
     * A6: Ramificazioni minute e fogliame brinato in primo piano (tracciamento dei rami dal basso verso l'alto con riduzione progressiva della pressione e biforcazioni ad angolo acuto, campitura delle foglie a contrasto con risparmio di un lembo chiaro marginale ammorbidito a pennello umido).

3. Sezione «Teoria del colore, ottica dei pigmenti e calcolatore» (/colori/):
   - Spazio colorimetrico di Munsell: Tinta (Hue), Valore tonale (Value, governato nell'acquerello dalla diluizione e dalla riflettanza della carta bianca), Croma (Chroma / saturazione).
   - Sintesi sottrattiva e modello di Kubelka-Munk: la miscelazione fisica di più pigmenti riduce la riflettanza selettiva e abbassa il croma; per preservare la luminosità è spesso preferibile la sovrapposizione ottica per velature trasparenti su strato asciutto.
   - Tavolozza essenziale a 6 pigmenti (configurazione per lo studio dal vero e il controllo rigoroso delle mescolanze), identificati sempre tramite denominazione tecnica e codice Colour Index:
     1) Giallo limone (PY175, benzimidazolone semitrasparente a dominante fredda)
     2) Blu ceruleo / ftalo sostituto (PB15 nelle serie studio, oppure PB35/PB36 nelle serie professionali, granitura e potere tingente differenti)
     3) Cremisi / Rosso profondo (PR206, PV19 o PR179, carminio/perilene trasparente)
     4) Terra di Siena bruciata (PR101, ossido di ferro sintetico trasparente a dominante arancio-mattone)
     5) Terra d'ombra bruciata (PBr7 o PBr7+PY42, ossido di ferro bruno che in combinazione complementare con l'oltremare genera grigi neutri e neri cromatici profondi)
     6) Blu oltremare (PB29, alluminosilicato complesso a dominante caldo-violacea, fortemente granulante)
   - Da questi 6 pigmenti primari e terrosi si ricavano le 12 miscele codificate del prontuario (M1..M12). In studio la tavolozza può essere integrata con pigmenti di comodità (verde vescica, verde oliva, terra di Siena naturale, ocra gialla PY43, indaco, grigio di Payne, blu di Prussia PB27, seppia).

4. Sezione «Merceologia e comparazione delle serie commerciali» (/marche/):
   - Analisi comparativa tra Winsor & Newton Cotman, Winsor & Newton Professional, Royal Talens Van Gogh, Daniel Smith Extra Fine, Schmincke Horadam e Maimeri Blu: la scelta tecnica si fonda sul codice del pigmento (Colour Index: PY, PR, PB, PBr, PG, PV), sul grado di trasparenza, sulla solidità alla luce (ASTM) e sul comportamento di granulazione, mai sulla sola denominazione commerciale.

Criteri di redazione delle risposte:
- Rispondi SEMPRE in italiano con un registro tecnico-didattico professionale, preciso, sobrio e autorevole, privo di espressioni colloquiali o infantili.
- Mantieni le risposte concise e strutturate (circa 120-220 parole), fornendo indicazioni esecutive verificabili sul formato di studio A5: grado di diluizione (tè, latte, miele), stato igrometrico del supporto (bagnato, umido satinato, asciutto), tipologia di pennello, dinamica del gesto e codici Colour Index dei pigmenti coinvolti.
- Rispondi ESCLUSIVAMENTE a quesiti attinenti alla pittura ad acquerello, al disegno preparatorio, alla colorimetria, ai materiali pittorici (carta, pennelli, pigmenti, leganti) o alla consultazione di questo repertorio. Qualora l'utente ponga domande estranee alla disciplina pittorica, declina con una formula breve e formale ricordando l'ambito specialistico dell'assistente.`;

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
          "Sono stati utilizzati tutti i 5 quesiti gratuiti associati a questo indirizzo email. Tutte le sezioni del repertorio e il simulatore colorimetrico restano liberamente consultabili.",
      },
      429
    );
  }

  const domanda = String(body.domanda || "").trim().slice(0, 1000);
  if (domanda.length < 4) {
    return rispostaJson(
      { ok: false, errore: "Formula un quesito più circostanziato (almeno 4 caratteri)." },
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

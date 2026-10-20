// Cloudflare Pages Function: riceve un suggerimento dalla casella del sito
// e apre una segnalazione pubblica (Issue) su GitHub in sinmar123/app-acquerello.

const REPO = "sinmar123/app-acquerello";
const SEZIONI_VALIDE = new Set([
  "Generale / Nuovo argomento",
  "Principi",
  "Alberi",
  "Teoria dei colori",
  "Confronto marche",
]);

function oscuraEmail(str) {
  if (!str) return "";
  return String(str).replace(
    /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g,
    "[email rimossa per privacy]"
  );
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

export async function onRequestPost(context) {
  const token = context.env.GITHUB_SUGGERIMENTI_TOKEN;
  if (!token) {
    return rispostaJson(
      {
        ok: false,
        errore:
          "Servizio di invio diretto non configurato sul server. Puoi aprire la segnalazione direttamente su GitHub.",
      },
      503
    );
  }

  let payload;
  try {
    payload = await context.request.json();
  } catch {
    return rispostaJson({ ok: false, errore: "Formato della richiesta non valido." }, 400);
  }

  // Filtro anti-bot (honeypot)
  if (payload.miele && String(payload.miele).trim() !== "") {
    return rispostaJson({ ok: false, errore: "Invio bloccato dal filtro automatico." }, 400);
  }

  const sezioneRaw = String(payload.sezione || "Generale / Nuovo argomento").trim();
  const sezione = SEZIONI_VALIDE.has(sezioneRaw) ? sezioneRaw : "Generale / Nuovo argomento";
  const titolo = oscuraEmail(String(payload.titolo || "").trim()).slice(0, 120);
  const testo = oscuraEmail(String(payload.testo || "").trim()).slice(0, 3500);
  const firma = oscuraEmail(String(payload.firma || "").trim()).slice(0, 60);
  const pagina = String(payload.pagina || "/").trim().slice(0, 80);

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

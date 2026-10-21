#!/usr/bin/env python3
"""Genera il sito statico del Quaderno di acquerello in site/ dai sorgenti delle sezioni in dati/<sezione>/.

Il repository è autonomo: contiene tutti i file di dati, le infografiche e gli script necessari a generare
le pagine. Oltre alle pagine scrive lib/prompt-chat.js, il prompt di sistema della chat ricavato dai dati
(il controllo «costruisci» del CI verifica che la copia nel repository sia aggiornata), e i file per i
motori di ricerca (robots.txt, sitemap.xml, favicon.svg)."""
import html
import json
import pathlib
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

APP_DIR = pathlib.Path(__file__).resolve().parent.parent
SITE_DIR = APP_DIR / "site"
DATI_DIR = APP_DIR / "dati"
SITO_URL = "https://app-acquerello.pages.dev"
REPO_URL = "https://github.com/sinmar123/app-acquerello"

SEZIONI = [
    {
        "slug": "principi",
        "numero": "1",
        "nome_form": "Principi",
        "titolo": "Principi generali: acqua, colore e carta",
        "sottotitolo": "Le tre consistenze della miscela, gli stati della carta e il rapporto fra pennello e carta, da conoscere prima degli esercizi",
        "descrizione": (
            "Tè, latte e miele; la carta asciutta, umida e bagnata e i momenti intermedi, riconoscibili dal lucido dell'acqua; "
            "il rapporto fra l'acqua del pennello e quella della carta, fioriture comprese; bordi netti e morbidi, asciugatura, "
            "carte hot press, cold press e rough. Ogni paragrafo rimanda alle sue fonti, dai corsi e dai video al minuto indicato."
        ),
        "badge": ["8 capitoli", "tè · latte · miele", "stati della carta", "fonti per ogni paragrafo"],
        "script_genera": DATI_DIR / "principi" / "genera-principi.py",
        "html_generato": DATI_DIR / "principi" / "principi.html",
    },
    {
        "slug": "studio-plein-air",
        "numero": "2",
        "nome_form": "Studio ed en plein air",
        "titolo": "Studio ed en plein air: metodo di lavoro, dotazione e tavolozze",
        "sottotitolo": "Il lavoro in studio e la pittura all'aperto a confronto, il metodo dei foglietti A5 e le 12 miscele della tavolozza ridotta",
        "descrizione": (
            "Che cosa cambia fra lo studio e la pittura dal vero: asciugatura, tavolozza, pennelli e attrezzi. Il metodo dei "
            "foglietti A5, i colori pronti della tavolozza estesa e i sei colori di base con il prontuario completo delle 12 miscele (M1-M12)."
        ),
        "badge": ["studio e aperto", "foglietti A5", "tavolozza estesa e sei colori", "12 miscele"],
        "script_genera": DATI_DIR / "studio-plein-air" / "genera-studio-plein-air.py",
        "html_generato": DATI_DIR / "studio-plein-air" / "studio-plein-air.html",
    },
    {
        "slug": "colori",
        "numero": "3",
        "nome_form": "Teoria dei colori",
        "titolo": "Teoria dei colori per l'acquerello",
        "sottotitolo": "Munsell, luce e pigmento, velature, i sei colori di base e un calcolatore di miscele",
        "descrizione": (
            "Tinta, valore e croma secondo Munsell; perché i pigmenti non si mescolano come le luci; mescolare o velare; "
            "le schede dei sei colori della tavolozza ridotta, con il nome comune e il pigmento; un calcolatore che mescola "
            "i tubetti in parti intere e cerca la miscela per un colore scelto, interamente nel browser."
        ),
        "badge": ["5 capitoli", "6 colori di base", "calcolatore di miscele", "stime da verificare sul foglietto"],
        "script_genera": DATI_DIR / "colori" / "genera-teoria-colori.py",
        "html_generato": DATI_DIR / "colori" / "teoria-colori.html",
    },
    {
        "slug": "marche",
        "numero": "4",
        "nome_form": "Confronto marche",
        "titolo": "Marche e tubetti",
        "sottotitolo": "I sei colori di base nelle serie in commercio: nome del tubetto, numero, pigmento e trasparenza",
        "descrizione": (
            "Per ognuno dei sei colori della tavolozza ridotta, il tubetto corrispondente in sei serie: Winsor &amp; Newton Cotman "
            "e Professional, Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu. Dati tratti solo dalle pagine ufficiali, con il "
            "collegamento e la data di controllo su ogni riga, e la spiegazione del perché lo stesso nome possa nascondere pigmenti diversi."
        ),
        "badge": ["6 serie", "6 colori di base", "fonte ufficiale su ogni riga", "stesso nome, pigmenti diversi"],
        "script_genera": DATI_DIR / "marche" / "genera-marche.py",
        "html_generato": DATI_DIR / "marche" / "marche.html",
    },
    {
        "slug": "soggetti",
        "numero": "5",
        "nome_form": "Soggetti (Alberi, Nuvole, Fiori...)",
        "titolo": "Soggetti: un modulo per ogni tema",
        "sottotitolo": "Sezione in crescita: S1 Alberi, siepi e arbusti è pubblicato; in preparazione cieli e nuvole, fiori, acqua e riflessi, rocce, architetture",
        "descrizione": (
            "Un modulo per ogni soggetto. Il primo, sugli alberi, raccoglie 6 esempi, 24 modalità tratte dai "
            "video con un'infografica in 3 fasi ciascuna e 31 estratti video."
        ),
        "badge": ["S1 Alberi (pubblicato)", "S2 Cieli e nuvole", "S3 Fiori", "S4-S6 in preparazione"],
        "script_genera": DATI_DIR / "soggetti" / "genera-soggetti.py",
        "html_generato": DATI_DIR / "soggetti" / "soggetti.html",
    },
    {
        "slug": "alberi",
        "in_home": False,
        "numero": "5.1",
        "nome_form": "Soggetti (Alberi, Nuvole, Fiori...)",
        "titolo": "S1 · Alberi ad acquerello",
        "sottotitolo": "Sei esempi di alberi, siepi e arbusti, sviluppati in 24 modalità tratte dai video, con un'infografica in tre fasi per ciascuna",
        "descrizione": "",
        "badge": [],
        "script_genera": DATI_DIR / "alberi" / "pit-261013-video-gesti.py",
        "html_generato": DATI_DIR / "alberi" / "pit-261014-video-gesti-alberi.html",
        # figure salvate accanto alla pagina dal generatore, da copiare con lei
        "cartelle": [DATI_DIR / "alberi" / "immagini"],
    },
]

DESCRIZIONE_HOME = (
    "Appunti di studio dell'acquerello: le tre consistenze e gli stati della carta, la teoria dei colori con un calcolatore "
    "di miscele, i tubetti marca per marca e gli esercizi sugli alberi tratti dai video."
)

OPZIONI_SEZIONE = [
    "Generale / Nuovo argomento",
    "Principi",
    "Studio ed en plein air",
    "Teoria dei colori",
    "Confronto marche",
    "Soggetti (Alberi, Nuvole, Fiori...)",
]

FUNZIONE_SUGGERIMENTI = APP_DIR / "functions" / "api" / "suggerimento.js"
FUNZIONE_CHAT = APP_DIR / "functions" / "api" / "chat.js"
PROMPT_CHAT = APP_DIR / "lib" / "prompt-chat.js"

# Soglia minima di leggibilità (indice Gulpease, calcolato da gulpease() qui sotto) dei testi di ogni pagina:
# sotto, la generazione si ferma. Misura del 21/10/2026: le pagine nel registro del manuale stanno fra 58 e 68;
# la riscrittura involuta del 20/10 dava 48 ai Principi, 49 a Studio ed en plein air e alle Marche, 51 ai Colori.
GULPEASE_MINIMO = 52


def e(testo):
    return html.escape(str(testo), quote=True)


def senza_tag(testo):
    return html.unescape(re.sub(r"<[^>]+>", "", str(testo)))


def controlla_funzioni():
    """Il menu del modulo dei suggerimenti e le pagine del sito devono coincidere con gli elenchi che le
    funzioni accettano: una voce che manca di là viene rifiutata dal server."""
    pagine = ["/"] + [f"/{s['slug']}/" for s in SEZIONI]

    def elenco(file, nome):
        m = re.search(rf"const {nome} = (\[.*?\]);", file.read_text(encoding="utf-8"), re.S)
        if not m:
            raise SystemExit(f"genera-sito: {nome} non trovato in {file.name}")
        return json.loads(m.group(1))

    for file, nome, atteso in ((FUNZIONE_SUGGERIMENTI, "SEZIONI_VALIDE", OPZIONI_SEZIONE),
                               (FUNZIONE_SUGGERIMENTI, "PAGINE_VALIDE", pagine),
                               (FUNZIONE_CHAT, "PAGINE_VALIDE", pagine)):
        trovato = elenco(file, nome)
        if trovato != atteso:
            raise SystemExit(f"genera-sito: {nome} di {file.name} è {trovato}, il sito usa {atteso}")
    for s in SEZIONI:
        if s.get("nome_form") not in OPZIONI_SEZIONE:
            raise SystemExit(f"genera-sito: la sezione {s['slug']} preseleziona «{s.get('nome_form')}», che il menu non ha")


# Parole dei nomi di serie troppo comuni per cercarle nei testi («Professional», «Extra Fine»,
# «Aquarell», il «Blu» di Maimeri Blu): della serie resta solo la parte distintiva.
PAROLE_GENERICHE = {"professional", "extra", "fine", "aquarell", "blu"}


def controlla_marche_fuori_sezione():
    """Marche e serie commerciali stanno solo in dati/marche/ (CONTRIBUTING.md § 3): altrove i colori
    si chiamano col nome comune e il codice Colour Index. Cerca i nomi di marche.json in tutti gli
    altri sorgenti delle sezioni."""
    marche = json.loads((DATI_DIR / "marche" / "marche.json").read_text(encoding="utf-8"))["marche"]
    nomi = {"winsor"}
    for m in marche:
        nomi.add(m["marca"].lower())
        parole_marca = set(m["marca"].lower().split())
        distintiva = " ".join(p for p in m["serie"].lower().split() if p not in PAROLE_GENERICHE and p not in parole_marca)
        if distintiva:
            nomi.add(distintiva)
    trovati = []
    for p in sorted(DATI_DIR.rglob("*")):
        if p.suffix not in {".json", ".csv", ".py", ".js"} or "marche" in p.parts or "spettri" in p.name:
            continue
        for n, riga in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            basso = riga.lower()
            for nome in nomi:
                if re.search(rf"(?<![a-z]){re.escape(nome)}(?![a-z])", basso):
                    trovati.append(f"{p.relative_to(APP_DIR).as_posix()}:{n} «{nome}»")
    if trovati:
        raise SystemExit("genera-sito: nomi di marche fuori dalla sezione Marche:\n  " + "\n  ".join(trovati))


def genera_prompt_chat():
    """Scrive lib/prompt-chat.js col prompt di sistema della chat, ricavato dai dati del sito: sezioni,
    consistenze e stati della carta dei Principi, tavolozza, esempi e modalità degli Alberi, moduli in
    preparazione. Così la chat non può contraddire le pagine con dati scritti a mano."""
    principi = json.loads((DATI_DIR / "principi" / "principi.json").read_text(encoding="utf-8"))
    tavolozza = json.loads((DATI_DIR / "colori" / "tavolozza.json").read_text(encoding="utf-8"))
    alberi = json.loads((DATI_DIR / "alberi" / "pit-261014-video-gesti-alberi.json").read_text(encoding="utf-8"))
    soggetti = json.loads((DATI_DIR / "soggetti" / "soggetti.json").read_text(encoding="utf-8"))
    capitoli = {c["id"]: c for c in principi["capitoli"]}

    def voci(capitolo, indice):
        liste = [b for b in capitoli[capitolo]["blocchi"] if b["tipo"] == "lista"]
        # l'etichetta colorata dello stato («bagnata», «umida»...) diventa «bagnata: ...»
        return [senza_tag(re.sub(r'<span class="pill [^"]*">([^<]*)</span>\s*', r"\1: ", v["testo"])).strip()
                for v in liste[indice]["voci"]]

    sezioni = "\n".join(f"- {s['numero']}. {s['titolo']} ({SITO_URL}/{s['slug']}/)" for s in SEZIONI)
    colori = "\n".join(
        f"- {c['nome']} ({c['pigmento']}"
        + (f", {c['trasparenza_tubetto']} nel tubetto della tavolozza" if c.get("trasparenza_tubetto") else "")
        + f"); {c['note']}"
        for c in tavolozza["colori"])
    esempi = []
    for t in alberi["alberi"]:
        sigla, nome = t["voce"].split(" ", 1)
        modalita = "; ".join(re.sub(r"^Modalità \d+:\s*", "", m["titolo"]) for m in t.get("modalita", []))
        esempi.append(f"- {sigla} {nome}. Modalità: {modalita}.")
    in_preparazione = ", ".join(s["titolo"] for s in soggetti["soggetti"] if s["stato"] != "pubblicato")
    regola = senza_tag(next(b["testo"] for b in capitoli["abbinare"]["blocchi"] if b["tipo"] == "p"))

    prompt = f"""Sei l'assistente del «Quaderno di acquerello» ({SITO_URL}), appunti di studio dell'acquerello aperti al pubblico e in fase di sviluppo. Rispondi alle domande sull'acquerello, sul disegno, sul colore, sui materiali pittorici e sull'uso del Quaderno. Ogni domanda arriva preceduta, fra parentesi quadre, dalla pagina del Quaderno che si sta consultando: serve a capire il contesto e non va citata.

Le sezioni del Quaderno:
{sezioni}

Che cosa dice il Quaderno, in sintesi. È il tuo riferimento: non contraddirlo.

Le tre consistenze della miscela, dal corso di Watercolor Fanatic:
{chr(10).join("- " + v for v in voci("consistenze", 0))}

Gli stati della carta:
{chr(10).join("- " + v for v in voci("carta-umidita", 0))}

I momenti intermedi, riconoscibili dal lucido dell'acqua:
{chr(10).join("- " + v for v in voci("carta-umidita", 1))}

La regola di fondo:
- {regola}

La tavolozza ridotta a sei colori (i colori del calcolatore sono provvisori, stimati a occhio):
{colori}

Il modulo S1, alberi, siepi e arbusti ({SITO_URL}/alberi/), con le modalità tratte dai video:
{chr(10).join(esempi)}

Moduli in preparazione: {in_preparazione}.

Come rispondere:
- In italiano, col registro di un buon manuale tecnico: termini esatti, frasi chiare, niente parlato e niente paroloni. Di norma fra 120 e 220 parole.
- Niente trattino lungo: per gli incisi si usano le virgole, i due punti o le parentesi.
- Indica la sezione del Quaderno che tratta l'argomento, con il suo indirizzo.
- Non inventare fonti, autori, video, citazioni, sigle di pigmenti o numeri. Se il Quaderno non tratta un punto, dillo, e suggerisci una prova su un foglietto.
- Ricorda che l'esito va sempre verificato sulla carta: le risposte sono una guida, non una regola.
- Rispondi solo sui temi indicati all'inizio; per il resto declina in una frase.
- Non chiedere dati personali."""
    PROMPT_CHAT.parent.mkdir(parents=True, exist_ok=True)
    testo = ("// Generato da scripts/genera-sito.py dai dati del sito: non modificare a mano.\n"
             f"export const PROMPT_SISTEMA = {json.dumps(prompt, ensure_ascii=False)};\n")
    PROMPT_CHAT.write_text(testo, encoding="utf-8", newline="\n")
    print(f"[chat] Scritto {PROMPT_CHAT.relative_to(APP_DIR).as_posix()} ({len(prompt)} caratteri)")


def blocco_chat_e_suggerimenti(sezione_predefinita: str, pagina_path: str) -> str:
    opts = []
    for opz in OPZIONI_SEZIONE:
        sel = " selected" if opz == sezione_predefinita else ""
        opts.append(f'<option value="{e(opz)}"{sel}>{e(opz)}</option>')
    options_html = "".join(opts)

    return f"""
<style>
.sugg-wrap{{max-width:820px;margin:24px auto 18px;padding:0 14px;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.sugg-box,.chat-box{{background:#fffdf8;border:1px solid #d8ccb8;border-left:4px solid #2f5e4e;border-radius:10px;padding:18px 20px;box-shadow:0 2px 8px rgba(31,28,23,.05);color:#1f1c17;margin-bottom:22px}}
.chat-box{{border-left-color:#8c4a27}}
.sugg-box h2,.chat-box h2{{margin:0 0 6px;font-size:1.15rem;color:#263529}}
.chat-box h2{{color:#6b3418}}
.sugg-sub{{margin:0 0 14px;font-size:.9rem;color:#4a4236;line-height:1.45}}
.sugg-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}}
@media(max-width:600px){{.sugg-grid{{grid-template-columns:1fr}}}}
.sugg-field{{display:flex;flex-direction:column;gap:4px;margin-bottom:12px}}
.sugg-field label{{font-size:.83rem;font-weight:600;color:#3d352b}}
.sugg-field input,.sugg-field select,.sugg-field textarea{{font:inherit;font-size:.92rem;padding:8px 10px;border:1px solid #c9bba3;border-radius:6px;background:#ffffff;color:#1f1c17}}
.sugg-field textarea{{min-height:92px;resize:vertical}}
.sugg-avviso{{background:#f5efe2;border:1px solid #dfd3be;border-radius:7px;padding:10px 12px;margin:10px 0 14px;font-size:.82rem;color:#3d352b;line-height:1.45}}
.sugg-avviso a{{color:#2f5e4e;font-weight:600}}
.sugg-actions{{display:flex;flex-wrap:wrap;align-items:center;gap:12px}}
.sugg-btn{{background:#263529;color:#f7f2e7;border:0;border-radius:7px;padding:9px 16px;font:inherit;font-size:.9rem;font-weight:600;cursor:pointer}}
.sugg-btn:hover{{background:#1c281f}}
.sugg-btn.arancio{{background:#8c4a27}}
.sugg-btn.arancio:hover{{background:#6b3418}}
.sugg-btn:disabled{{opacity:.6;cursor:wait}}
.sugg-link-gh{{font-size:.82rem;color:#5c5142;text-decoration:none}}
.sugg-link-gh:hover{{text-decoration:underline}}
.sugg-esito{{margin-top:12px;padding:10px 12px;border-radius:7px;font-size:.88rem;display:none}}
.sugg-esito.ok{{display:block;background:#e6f4ea;border:1px solid #a8dab5;color:#135225}}
.sugg-esito.err{{display:block;background:#fce8e6;border:1px solid #f5c2c0;color:#7a1c18}}
.sugg-hp{{position:absolute;left:-9999px;opacity:0;pointer-events:none;height:0;overflow:hidden}}
.chat-barra-stato{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:8px;background:#f5efe2;border:1px solid #dfd3be;border-radius:7px;padding:8px 12px;margin-bottom:12px;font-size:.84rem}}
.chat-badge-quota{{font-weight:700;color:#6b3418;padding:2px 8px;border-radius:999px;border:1px solid #d5b8a3;background:#fff8f3}}
.chat-esempi{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}}
.chat-chip{{background:#f3ece0;border:1px solid #d8ccb8;color:#3d352b;border-radius:999px;padding:4px 10px;font:inherit;font-size:.79rem;cursor:pointer;text-align:left}}
.chat-chip:hover{{background:#e6dbc8}}
.chat-messaggi{{max-height:360px;overflow-y:auto;border:1px solid #e2d7c5;border-radius:8px;background:#faf6ee;padding:12px;margin-bottom:12px;display:none;flex-direction:column;gap:10px}}
.chat-msg{{padding:10px 12px;border-radius:8px;font-size:.9rem;line-height:1.5;max-width:92%}}
.chat-msg.utente{{align-self:flex-end;background:#263529;color:#f7f2e7}}
.chat-msg.ai{{align-self:flex-start;background:#ffffff;border:1px solid #dfd5c3;color:#1f1c17}}
.chat-msg.ai p{{margin:0 0 8px}}
.chat-msg.ai p:last-child{{margin-bottom:0}}
.chat-input-row{{display:flex;gap:8px;align-items:flex-end}}
.chat-input-row textarea{{flex:1;font:inherit;font-size:.92rem;padding:8px 10px;border:1px solid #c9bba3;border-radius:6px;min-height:54px;max-height:140px;resize:vertical;background:#fff}}
.chat-nota-privacy{{margin:10px 0 0;font-size:.78rem;color:#6b5e4c;line-height:1.45}}
.chat-nota-privacy summary{{cursor:pointer;font-weight:600}}
.chat-nota-privacy p{{margin:6px 0 0}}
</style>

<section id="assistente-ai" class="sugg-wrap" aria-label="Assistente sull'acquerello basato sull'intelligenza artificiale">
  <div class="chat-box" data-pagina="{e(pagina_path)}">
    <h2>🎨 Assistente sull'acquerello</h2>
    <p class="sugg-sub">
      Domande sulla tecnica dell'acquerello, sui colori e sui materiali, o su come usare il Quaderno. Le risposte sono generate
      da un modello di intelligenza artificiale, Gemini 4 Argon di Google, istruito con un riassunto del Quaderno: possono
      contenere errori, e fa fede il testo delle sezioni. Ogni connessione dispone di <strong>5 domande a settimana</strong>;
      quando in un giorno le domande di tutti arrivano a 10, la chat riprende il giorno dopo.
    </p>
    <div class="chat-barra-stato">
      <span>Non serve registrarsi.</span>
      <span class="chat-badge-quota" id="chat-quota-label">Domande disponibili questa settimana: …</span>
    </div>
    <div class="chat-esempi">
      <span style="font-size:.79rem;color:#6b5e4c;align-self:center;margin-right:2px">Esempi di domande:</span>
      <button type="button" class="chat-chip">Perché si formano i cavolfiori quando ripasso un velo che sta asciugando?</button>
      <button type="button" class="chat-chip">Come preparo un verde scuro per le conifere in ombra con i sei colori di base?</button>
      <button type="button" class="chat-chip">Quando si sparge il sale sul velo per ottenere l'effetto brina?</button>
    </div>
    <div id="chat-messaggi" class="chat-messaggi" aria-live="polite"></div>
    <form id="form-chat-domanda">
      <div class="chat-input-row">
        <textarea id="chat-domanda-input" required minlength="4" maxlength="1000" placeholder="Scrivi qui la domanda sull'acquerello..."></textarea>
        <button type="submit" class="sugg-btn arancio" id="chat-invia-btn">Invia</button>
      </div>
    </form>
    <div id="chat-esito-err" class="sugg-esito err" role="alert"></div>
    <details class="chat-nota-privacy">
      <summary>Informativa sul trattamento dei dati della chat</summary>
      <p>Titolare del trattamento è Alessandro Sanvitale, curatore del Quaderno (account GitHub sinmar123), che si contatta aprendo una
      <a href="{REPO_URL}/issues" target="_blank" rel="noopener">segnalazione sul repository del progetto</a>.
      La domanda scritta nella chat viene inviata a Google tramite l'API Gemini al solo scopo di generare la risposta,
      insieme alle due domande e risposte precedenti della stessa conversazione e all'indirizzo della pagina consultata,
      secondo i termini del servizio di Google: non vanno scritti dati personali. Il Quaderno non chiede l'email, non usa
      cookie per la chat e non conserva né le domande né le risposte.</p>
      <p>Per applicare il limite di 5 domande a settimana registra, per non più di 14 giorni, un'impronta dell'indirizzo IP,
      calcolata con una chiave segreta e diversa ogni settimana, senza l'indirizzo in chiaro. La base giuridica è il
      legittimo interesse a impedire gli abusi del servizio (art. 6, par. 1, lett. f, del Regolamento UE 2016/679). Il sito
      è ospitato da Cloudflare. Restano i diritti previsti dagli articoli 15-22 dello stesso Regolamento e il reclamo al
      Garante per la protezione dei dati personali.</p>
    </details>
  </div>
</section>

<section id="suggerimenti" class="sugg-wrap" aria-label="Suggerimenti e correzioni">
  <div class="sugg-box">
    <h2>💬 Suggerimenti: correzioni, integrazioni e video</h2>
    <p class="sugg-sub">
      Per segnalare un errore, proporre un'integrazione o indicare un passaggio utile in un video di YouTube, con il minuto
      d'inizio e di fine. La segnalazione viene pubblicata nel registro pubblico del progetto su GitHub e vagliata prima di
      un'eventuale modifica.
    </p>
    <form id="form-suggerimento" data-pagina="{e(pagina_path)}">
      <div class="sugg-hp" aria-hidden="true">
        <label>Non compilare questo campo <input type="text" name="miele" tabindex="-1" autocomplete="off"></label>
      </div>
      <div class="sugg-grid">
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-sezione">Sezione</label>
          <select id="sugg-sezione" name="sezione">
            {options_html}
          </select>
        </div>
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-firma">Firma (facoltativa)</label>
          <input id="sugg-firma" name="firma" type="text" maxlength="60" placeholder="Vuota per un invio anonimo">
        </div>
      </div>
      <div class="sugg-field" style="margin-top:12px">
        <label for="sugg-titolo">Oggetto *</label>
        <input id="sugg-titolo" name="titolo" type="text" required minlength="4" maxlength="120" placeholder="Es. Video utile per la chioma del pino marittimo / Sigla Colour Index da correggere">
      </div>
      <div class="sugg-field">
        <label for="sugg-testo">Descrizione *</label>
        <textarea id="sugg-testo" name="testo" required minlength="10" maxlength="3500" placeholder="La proposta o la correzione. Per un video di YouTube: indirizzo e minuti d'inizio e di fine (mm:ss) del passaggio."></textarea>
      </div>
      <div class="sugg-avviso">
        <strong>Pubblicazione:</strong> l'invio non richiede registrazione. Premendo <em>Invia</em>, oggetto, descrizione, sezione,
        pagina di partenza e firma eventuale <strong>diventano pubblici</strong> nelle
        <a href="{REPO_URL}/issues" target="_blank" rel="noopener">segnalazioni del progetto su GitHub</a>,
        con licenza Creative Commons CC BY 4.0, per la revisione e l'aggiornamento del Quaderno; le condizioni complete
        sono in <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">CONTRIBUTING.md</a>.
        Per limitare gli invii a 5 al giorno il server registra, per non più di 14 giorni, un'impronta dell'indirizzo IP
        calcolata con una chiave segreta e diversa ogni giorno, senza l'indirizzo in chiaro.
        <strong>Non inserire indirizzi email, numeri di telefono o altri dati personali.</strong>
      </div>
      <div class="sugg-actions">
        <button type="submit" class="sugg-btn" id="sugg-submit">Invia</button>
        <a class="sugg-link-gh" href="{REPO_URL}/issues" target="_blank" rel="noopener">Le segnalazioni pubblicate →</a>
      </div>
      <div id="sugg-esito" class="sugg-esito" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
<script>
(function(){{
  function $(id) {{ return document.getElementById(id); }}
  function postJson(url, dati) {{
    return fetch(url, {{ method: "POST", headers: {{ "Content-Type": "application/json" }}, body: JSON.stringify(dati) }})
      .then(function (r) {{ return r.json().catch(function () {{ return {{}}; }}).then(function (j) {{ return {{ ok: r.ok, dati: j }}; }}); }});
  }}

  // --- 1. Chat con Gemini: 5 domande a settimana per connessione, nessun dato conservato ---
  var box = document.querySelector(".chat-box");
  var pagina = (box && box.getAttribute("data-pagina")) || "/";
  var etichettaQuota = $("chat-quota-label"), messaggi = $("chat-messaggi");
  var form = $("form-chat-domanda"), domandaInput = $("chat-domanda-input"), invia = $("chat-invia-btn"), errore = $("chat-esito-err");
  var storia = [];

  function formattaRisposta(testo) {{
    var esc = testo.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    esc = esc.replace(/\\*\\*(.+?)\\*\\*/g, "<strong>$1</strong>").replace(/\\*(.+?)\\*/g, "<em>$1</em>");
    return esc.split(/\\n\\n+/).map(function (b) {{ return "<p>" + b.replace(/\\n/g, "<br>") + "</p>"; }}).join("");
  }}
  function mostraQuota(rimanenti, limite) {{
    etichettaQuota.textContent = "Domande disponibili questa settimana: " + rimanenti + " su " + limite;
    var finite = rimanenti <= 0;
    domandaInput.disabled = finite;
    invia.disabled = finite;
    domandaInput.placeholder = finite ? "Le domande di questa settimana sono esaurite: si rinnovano il lunedì." : "Scrivi qui la domanda sull'acquerello...";
  }}
  function mostraErrore(testo) {{
    errore.textContent = testo;
    errore.style.display = "block";
  }}
  function aggiungi(classe, testo) {{
    var div = document.createElement("div");
    div.className = "chat-msg " + classe;
    div.textContent = testo;
    messaggi.style.display = "flex";
    messaggi.appendChild(div);
    messaggi.scrollTop = messaggi.scrollHeight;
    return div;
  }}

  if (form) {{
    postJson("/api/chat", {{ azione: "stato" }}).then(function (r) {{
      if (r.ok && r.dati.ok) mostraQuota(r.dati.rimanenti, r.dati.limite);
      else etichettaQuota.textContent = "Assistente non disponibile in questo momento";
    }}).catch(function () {{ etichettaQuota.textContent = "Assistente non disponibile in questo momento"; }});

    document.querySelectorAll(".chat-chip").forEach(function (chip) {{
      chip.addEventListener("click", function () {{
        if (!domandaInput.disabled) {{ domandaInput.value = chip.textContent; domandaInput.focus(); }}
      }});
    }});

    form.addEventListener("submit", function (ev) {{
      ev.preventDefault();
      var domanda = domandaInput.value.trim();
      if (!domanda) return;
      errore.style.display = "none";
      aggiungi("utente", domanda);
      var attesa = aggiungi("ai", "Risposta in preparazione...");
      domandaInput.value = "";
      invia.disabled = true;
      postJson("/api/chat", {{ azione: "chiedi", domanda: domanda, pagina: pagina, storia: storia }}).then(function (r) {{
        if (typeof r.dati.rimanenti === "number") mostraQuota(r.dati.rimanenti, r.dati.limite || 5);
        if (!r.ok || !r.dati.ok) {{
          messaggi.removeChild(attesa);
          mostraErrore(r.dati.errore || "Errore durante la risposta: riprova tra poco.");
          return;
        }}
        attesa.innerHTML = formattaRisposta(r.dati.risposta);
        storia.push({{ domanda: r.dati.domanda, risposta: r.dati.risposta, firma: r.dati.firma }});
        storia = storia.slice(-2);
        messaggi.scrollTop = messaggi.scrollHeight;
      }}).catch(function () {{
        messaggi.removeChild(attesa);
        mostraErrore("Errore di collegamento con il servizio: riprova tra poco.");
      }}).then(function () {{
        if (!domandaInput.disabled) invia.disabled = false;
      }});
    }});
  }}

  // --- 2. Casella dei suggerimenti pubblici ---
  var modulo = $("form-suggerimento");
  if (!modulo) return;
  var pulsante = $("sugg-submit"), esito = $("sugg-esito");
  function collegamento(href, testo) {{
    var a = document.createElement("a");
    a.href = href; a.target = "_blank"; a.rel = "noopener"; a.textContent = testo;
    return a;
  }}
  modulo.addEventListener("submit", function (ev) {{
    ev.preventDefault();
    esito.className = "sugg-esito";
    esito.textContent = "";
    var dati = {{
      sezione: modulo.sezione.value,
      firma: modulo.firma.value.trim(),
      titolo: modulo.titolo.value.trim(),
      testo: modulo.testo.value.trim(),
      miele: modulo.miele.value,
      pagina: modulo.getAttribute("data-pagina") || "/"
    }};
    pulsante.disabled = true;
    pulsante.textContent = "Invio in corso...";
    postJson("/api/suggerimento", dati).then(function (r) {{
      if (r.ok && r.dati.ok) {{
        esito.className = "sugg-esito ok";
        esito.append("Segnalazione registrata (n. " + r.dati.numero + "): ", collegamento(r.dati.url, "vedila su GitHub"), ".");
        modulo.titolo.value = "";
        modulo.testo.value = "";
        return;
      }}
      throw new Error(r.dati.errore || "Invio non riuscito.");
    }}).catch(function (err) {{
      esito.className = "sugg-esito err";
      var url = "{REPO_URL}/issues/new?title=" + encodeURIComponent("[Suggerimento · " + dati.sezione + "] " + dati.titolo) +
        "&body=" + encodeURIComponent(dati.testo);
      esito.append((err && err.message) || "Invio non riuscito.", " In alternativa si può ",
        collegamento(url, "aprire la segnalazione su GitHub con questo collegamento precompilato"), ".");
    }}).then(function () {{
      pulsante.disabled = false;
      pulsante.textContent = "Invia";
    }});
  }});
}})();
</script>
"""


def testa_comune(titolo, descrizione, pagina_path):
    """Meta description, anteprima per la condivisione e favicon, uguali per tutte le pagine."""
    return (f'<meta name="description" content="{e(descrizione)}">\n'
            f'<meta property="og:type" content="website">\n'
            f'<meta property="og:locale" content="it_IT">\n'
            f'<meta property="og:site_name" content="Quaderno di acquerello">\n'
            f'<meta property="og:title" content="{e(titolo)}">\n'
            f'<meta property="og:description" content="{e(descrizione)}">\n'
            f'<meta property="og:url" content="{SITO_URL}{pagina_path}">\n'
            f'<link rel="canonical" href="{SITO_URL}{pagina_path}">\n'
            f'<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n')


def inietta_elementi_comuni(html_pagina: str, sezione: dict, pagina_path: str) -> str:
    if 'name="description"' not in html_pagina:
        m = re.search(r"<title>(.*?)</title>", html_pagina, re.S)
        titolo = html.unescape(m.group(1)) if m else sezione["titolo"]
        html_pagina = html_pagina.replace("</head>", testa_comune(titolo, senza_tag(sezione["sottotitolo"]), pagina_path) + "</head>", 1)
    barra = (
        '<div id="barra-quaderno" style="background:#efe6d5;border-bottom:1px solid #d8ccb8;padding:6px 14px;'
        'font-size:.86rem;display:flex;justify-content:center;gap:18px;flex-wrap:wrap">'
        '<a href="../" style="color:#6b4226;text-decoration:none;font-weight:600">← Quaderno di acquerello</a>'
        '<a href="#assistente-ai" style="color:#8c4a27;text-decoration:none;font-weight:600">🎨 Assistente</a>'
        '<a href="#suggerimenti" style="color:#2f5e4e;text-decoration:none;font-weight:600">💬 Suggerimenti</a></div>\n'
    )
    if 'id="barra-quaderno"' not in html_pagina:
        html_pagina = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + "\n" + barra, html_pagina, count=1)

    blocco = blocco_chat_e_suggerimenti(sezione.get("nome_form", OPZIONI_SEZIONE[0]), pagina_path)
    if 'id="suggerimenti"' not in html_pagina:
        if "<footer" in html_pagina:
            html_pagina = html_pagina.replace("<footer", blocco + "\n<footer", 1)
        else:
            html_pagina = html_pagina.replace("</body>", blocco + "\n</body>", 1)
    return html_pagina


def genera_home(sezioni_pronte: list[dict]) -> str:
    cards = []
    for s in sezioni_pronte:
        if not s.get("in_home", True):
            continue
        badges = "".join(f'<span class="pill">{b}</span>' for b in s.get("badge", []))
        extra_btn = ""
        if s["slug"] == "soggetti":
            extra_btn = ' <a class="btn sec" href="./alberi/">Apri S1 · Alberi →</a>'
        cards.append(
            f"""<article class="card">
  <div class="card-body">
    <div class="card-head">
      <span class="sig">{s['numero']}</span>
      <div>
        <h2><a class="card-tit-link" href="./{s['slug']}/">{s['titolo']}</a></h2>
        <p class="card-sub">{s['sottotitolo']}</p>
      </div>
    </div>
    <p class="card-desc">{s['descrizione']}</p>
    <div class="pills">{badges}</div>
    <div class="btn-row"><a class="btn" href="./{s['slug']}/">Apri la sezione →</a>{extra_btn}</div>
  </div>
</article>"""
        )

    cards_html = "\n".join(cards)
    blocco_sugg = blocco_chat_e_suggerimenti(OPZIONI_SEZIONE[0], "/")
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quaderno di acquerello</title>
{testa_comune("Quaderno di acquerello", DESCRIZIONE_HOME, "/")}<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#faf6ee;color:#1f1c17;line-height:1.5}}
.testa{{padding:28px 18px 22px;background:#263529;color:#f7f2e7;text-align:center}}
.testa h1{{margin:0 0 6px;font-size:1.45rem;letter-spacing:.01em}}
.testa p{{margin:0 auto;max-width:680px;font-size:.95rem;color:#d8dfd5}}
main{{max-width:820px;margin:0 auto;padding:22px 14px 12px}}
.come-funziona{{background:#fffdf8;border:1px solid #dfd5c3;border-top:4px solid #263529;border-radius:12px;padding:18px 20px;margin-bottom:24px;box-shadow:0 2px 8px rgba(31,28,23,.05)}}
.come-funziona h2{{margin:0 0 8px;font-size:1.18rem;color:#263529}}
.come-funziona p{{margin:0 0 12px;font-size:.92rem;color:#363027}}
.cf-origine{{background:#eef4ef;border:1px solid #cadbce;border-left:4px solid #263529;border-radius:8px;padding:12px 14px;margin:0 0 14px;font-size:.91rem;color:#263529}}
.cf-origine strong{{color:#1b2b20}}
.cf-strumenti{{display:flex;flex-wrap:wrap;gap:10px;padding-top:10px;border-top:1px solid #e9e0cf;font-size:.87rem}}
.cf-link{{display:inline-flex;align-items:center;gap:5px;padding:6px 12px;border-radius:7px;font-weight:600;text-decoration:none}}
.cf-link.chat{{background:#fdf3ec;border:1px solid #e2bfa8;color:#6b3418}}
.cf-link.sugg{{background:#eef6f2;border:1px solid #b8d8c8;color:#1e4638}}
.cf-sviluppo{{background:#fbf0e3;border:1px solid #e3c6a8;border-left:6px solid #8c4a27;border-radius:8px;padding:14px 16px;margin:0 0 16px;font-size:.92rem;color:#2e2820;box-shadow:0 1px 4px rgba(140,74,39,.08)}}
.cf-sviluppo strong{{display:block;margin:0 0 4px;font-size:1.06rem;letter-spacing:.01em;color:#6b3418}}
.sezioni-tit{{margin:0 0 12px;font-size:1.12rem;color:#263529}}
.grid{{display:grid;grid-template-columns:1fr;gap:18px}}
.card{{background:#fffdf8;border:1px solid #dfd5c3;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(31,28,23,.06);transition:transform .15s ease,box-shadow .15s ease}}
.card:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(31,28,23,.12)}}
.card-tit-link{{color:inherit;text-decoration:none}}
.card-tit-link:hover{{text-decoration:underline}}
.card-body{{padding:16px 18px 18px}}
.card-head{{display:flex;align-items:flex-start;gap:12px;margin-bottom:8px}}
.sig{{display:inline-flex;align-items:center;justify-content:center;min-width:32px;height:32px;border-radius:8px;background:#263529;color:#f7f2e7;font-weight:700;font-size:.95rem;margin-top:2px}}
.card-head h2{{margin:0;font-size:1.18rem;color:#1f1c17}}
.card-sub{{margin:2px 0 0;font-size:.9rem;color:#6b5e4c;font-weight:500}}
.card-desc{{margin:10px 0 12px;font-size:.92rem;color:#363027}}
.pills{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}}
.pill{{background:#efe6d5;color:#4f3d27;border:1px solid #d8ccb8;border-radius:999px;padding:3px 10px;font-size:.78rem;font-weight:600}}
.btn-row{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.btn{{display:inline-block;background:#263529;color:#f7f2e7;padding:8px 14px;border-radius:8px;font-size:.88rem;font-weight:600;text-decoration:none}}
.btn.sec{{background:#eef4ef;color:#263529;border:1px solid #9ab5a3}}
footer{{text-align:center;padding:18px;font-size:.82rem;color:#7a6f5d;border-top:1px solid #e5dccb;margin-top:24px}}
footer a{{color:#5a4d3b}}
</style>
</head>
<body>
<header class="testa">
  <h1>Quaderno di acquerello</h1>
  <p>Appunti di studio dell'acquerello: acqua e carta, colori e tubetti, soggetti ed esercizi tratti dai video</p>
</header>
<main>
  <section class="come-funziona" aria-label="Come è organizzato il Quaderno">
    <h2>Come è organizzato il Quaderno</h2>
    <div class="cf-origine">
      <strong>Nota di metodo:</strong> chi oggi apprende una disciplina pratica dispone di una documentazione vastissima, distribuita tra manuali, schede tecniche e centinaia di ore di dimostrazioni filmate; la vera difficoltà sta nel ricondurre una materia tanto dispersa a un criterio ordinato e consultabile mentre si lavora. Gli strumenti di intelligenza artificiale permettono di compiere a monte questo lavoro di spoglio, confronto e classificazione, restituendo al momento opportuno il dato che serve per guidare la mano ed esercitarsi con maggiore sicurezza. Questo quaderno nasce dall'applicazione di tale approccio allo studio dell'acquerello: sistematizza il comportamento di acqua, carta e pigmenti, scompone e indicizza al secondo le sequenze esecutive nei video didattici e affianca al tavolo da lavoro strumenti di riscontro immediato, dal calcolatore colorimetrico all'assistente tecnico integrato nelle pagine.
    </div>
    <p>
      Il Quaderno raccoglie i procedimenti di base da provare su piccoli fogli di studio (A5, cotone 300 g/m²) ed è diviso,
      per ora, in cinque sezioni. Nei Principi e nelle Marche ogni affermazione rimanda alla sua fonte; negli Alberi ogni modalità rimanda
      al video da cui è tratta.
    </p>
    <div class="cf-sviluppo">
      <strong>Un cantiere aperto, in continua evoluzione.</strong> Il Quaderno è in costruzione: per ora conta cinque sezioni,
      altre se ne aggiungeranno e quelle esistenti vengono riviste e ampliate man mano che lo studio procede.
      La sezione 5, Soggetti, si apre con il modulo sugli alberi; gli altri moduli sono in preparazione.
    </div>
    <div class="cf-strumenti">
      <a class="cf-link chat" href="#assistente-ai">🎨 Domande sull'acquerello: l'assistente basato sull'IA (5 a settimana) ↓</a>
      <a class="cf-link sugg" href="#suggerimenti">💬 Correzioni e proposte: la casella dei suggerimenti ↓</a>
    </div>
  </section>

  <h2 class="sezioni-tit">Le sezioni</h2>
  <div class="grid">
    {cards_html}
  </div>
</main>
{blocco_sugg}
<footer>
  Quaderno di acquerello · progetto aperto su <a href="{REPO_URL}" target="_blank" rel="noopener">GitHub</a>
  (testi, dati e illustrazioni <a href="https://creativecommons.org/licenses/by/4.0/deed.it" target="_blank" rel="noopener">CC BY 4.0</a>, codice MIT)
</footer>
</body>
</html>
"""


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<path d="M32 4 C22 20 12 30 12 42 a20 20 0 0 0 40 0 C52 30 42 20 32 4 Z" fill="#283A9E" fill-opacity=".82"/>
<ellipse cx="25" cy="40" rx="5" ry="8" fill="#ffffff" fill-opacity=".45"/>
</svg>
"""


def scrivi_file_di_servizio():
    pagine = ["/"] + [f"/{s['slug']}/" for s in SEZIONI]
    (SITE_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: {SITO_URL}/sitemap.xml\n", encoding="utf-8", newline="\n")
    voci = "".join(f"  <url><loc>{SITO_URL}{p}</loc></url>\n" for p in pagine)
    (SITE_DIR / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{voci}</urlset>\n", encoding="utf-8", newline="\n")
    (SITE_DIR / "favicon.svg").write_text(FAVICON, encoding="utf-8", newline="\n")


def gulpease(html_pagina):
    """Indice Gulpease dei testi leggibili di una pagina, senza script, stili, svg, chat e suggerimenti."""
    t = re.sub(r'<section id="(assistente-ai|suggerimenti)".*?</section>', " ", html_pagina, flags=re.S)
    t = re.sub(r"<(script|style|svg|nav|footer|table)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<(br|/p|/li|/h[1-6]|/div|/td)[^>]*>", ". ", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    parole = re.findall(r"[A-Za-zÀ-ÿ0-9]+(?:['’][A-Za-zÀ-ÿ]+)?", t)
    if len(parole) < 100:
        return None
    frasi = max(1, len(re.findall(r"[.!?]+(?:\s|$)", t)))
    lettere = sum(len(re.sub(r"[^A-Za-zÀ-ÿ0-9]", "", p)) for p in parole)
    return round(89 + (300 * frasi - 10 * lettere) / len(parole))


def main():
    controlla_funzioni()
    controlla_marche_fuori_sezione()
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    sezioni_pronte, leggibilita = [], {}

    for s in SEZIONI:
        script = s["script_genera"]
        html_src = s["html_generato"]
        if script.exists():
            print(f"[{s['slug']}] Rigenerazione pagina da {script.name}...")
            subprocess.run([sys.executable, str(script), "pagina"], check=True)
        if not html_src.exists():
            raise FileNotFoundError(f"File HTML sorgente non trovato: {html_src}")

        dest_dir = SITE_DIR / s["slug"]
        dest_dir.mkdir(parents=True, exist_ok=True)
        html_text = html_src.read_text(encoding="utf-8")
        html_completo = inietta_elementi_comuni(html_text, s, f"/{s['slug']}/")
        dest_html = dest_dir / "index.html"
        dest_html.write_text(html_completo, encoding="utf-8", newline="\n")
        for cartella in s.get("cartelle", []):
            if not cartella.is_dir():
                raise FileNotFoundError(f"Cartella da pubblicare non trovata: {cartella}")
            shutil.copytree(cartella, dest_dir / cartella.name, dirs_exist_ok=True)
        leggibilita[s["slug"]] = gulpease(html_text)
        print(f"[{s['slug']}] Scritto {dest_html.relative_to(APP_DIR).as_posix()} ({dest_html.stat().st_size // 1024} KB)")
        sezioni_pronte.append(dict(s))

    index_html = SITE_DIR / "index.html"
    index_html.write_text(genera_home(sezioni_pronte), encoding="utf-8", newline="\n")
    print(f"[home] Scritto {index_html.relative_to(APP_DIR).as_posix()} ({index_html.stat().st_size // 1024} KB)")
    scrivi_file_di_servizio()
    genera_prompt_chat()

    print("[leggibilità] Gulpease: " + ", ".join(f"{k} {v}" for k, v in leggibilita.items() if v is not None))
    basse = {k: v for k, v in leggibilita.items() if v is not None and v < GULPEASE_MINIMO}
    if basse:
        raise SystemExit(f"genera-sito: leggibilità sotto {GULPEASE_MINIMO} (Gulpease) in {basse}: testi da semplificare")


if __name__ == "__main__":
    main()

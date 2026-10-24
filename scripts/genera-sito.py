#!/usr/bin/env python3
"""Genera il sito statico del Quaderno di acquerello in site/ dai sorgenti delle sezioni in dati/<sezione>/.

Il repository è autonomo: contiene tutti i file di dati, le infografiche e gli script necessari a generare
le pagine. Oltre alle pagine scrive lib/prompt-chat.js, il prompt di sistema della chat ricavato dai dati
(il controllo «costruisci» del CI verifica che la copia nel repository sia aggiornata), e i file per i
motori di ricerca (robots.txt, sitemap.xml, favicon.svg) e il file _redirects di Cloudflare Pages coi rinvii
degli indirizzi vecchi."""
import html
import json
import pathlib
import re
import shutil
import subprocess
import urllib.parse
import sys

sys.stdout.reconfigure(encoding="utf-8")

APP_DIR = pathlib.Path(__file__).resolve().parent.parent
SITE_DIR = APP_DIR / "site"
DATI_DIR = APP_DIR / "dati"
SITO_URL = "https://app-acquerello.pages.dev"
REPO_URL = "https://github.com/sinmar123/app-acquerello"

# Le sezioni nell'ordine del sito: «breve» è la voce della barra in cima a ogni pagina, «sottotitolo» la riga
# della scheda in home e la descrizione per i motori di ricerca; «modulo_di» mette la sezione, nella home,
# sotto quella che la contiene.
SEZIONI = [
    {
        "slug": "principi",
        "numero": "1",
        "breve": "Principi",
        "nome_form": "Principi",
        "titolo": "Principi generali: acqua, colore e carta",
        "sottotitolo": "Le tre consistenze della miscela, gli stati della carta e il rapporto fra pennello e carta, da conoscere prima degli esercizi; il lavoro in studio e all'aperto, con i sei colori proposti e le 12 miscele",
        "script_genera": DATI_DIR / "principi" / "genera-principi.py",
        "html_generato": DATI_DIR / "principi" / "principi.html",
    },
    {
        "slug": "colori",
        "numero": "2",
        "breve": "Teoria dei colori",
        "nome_form": "Teoria dei colori",
        "titolo": "Teoria dei colori",
        "sottotitolo": "Munsell, luce e pigmento, velature, i sei colori proposti e un calcolatore di miscele",
        "script_genera": DATI_DIR / "colori" / "genera-teoria-colori.py",
        "html_generato": DATI_DIR / "colori" / "teoria-colori.html",
    },
    {
        "slug": "marche",
        "numero": "3",
        "breve": "Marche e tubetti",
        "nome_form": "Confronto marche",
        "titolo": "Marche e tubetti",
        "sottotitolo": "I sei colori proposti nelle serie in commercio: nome del tubetto, numero, pigmento e trasparenza",
        "script_genera": DATI_DIR / "marche" / "genera-marche.py",
        "html_generato": DATI_DIR / "marche" / "marche.html",
    },
    {
        "slug": "soggetti",
        "numero": "4",
        "breve": "Soggetti",
        "nome_form": "Soggetti (Alberi, Nuvole, Fiori...)",
        "titolo": "Soggetti: un modulo per ogni tema",
        "sottotitolo": "Sezione in crescita: S1 Alberi, siepi e arbusti è pubblicato; in preparazione cieli e nuvole, fiori, acqua e riflessi, rocce, architetture",
        "script_genera": DATI_DIR / "soggetti" / "genera-soggetti.py",
        "html_generato": DATI_DIR / "soggetti" / "soggetti.html",
    },
    {
        "slug": "alberi",
        "numero": "4.1",
        "breve": "Alberi",
        "modulo_di": "soggetti",
        "nome_form": "Soggetti (Alberi, Nuvole, Fiori...)",
        "titolo": "S1 · Alberi ad acquerello",
        "sottotitolo": "Sei esempi di alberi, siepi e arbusti, sviluppati in 24 modalità tratte dai video, con un'infografica in tre fasi per ciascuna",
        "script_genera": DATI_DIR / "alberi" / "pit-261013-video-gesti.py",
        "html_generato": DATI_DIR / "alberi" / "pit-261014-video-gesti-alberi.html",
    },
    {
        "slug": "eventi",
        "numero": "5",
        "breve": "Eventi",
        "nome_form": "Eventi",
        "titolo": "Eventi",
        "sottotitolo": "Locandina, programma e fotografie di ogni evento, con il calendario e l'archivio per anno",
        "script_genera": DATI_DIR / "eventi" / "genera-eventi.py",
        "html_generato": DATI_DIR / "eventi" / "eventi.html",
        "cartelle": [DATI_DIR / "eventi" / "immagini"],
        "pagine_extra": DATI_DIR / "eventi" / "pagine",
    },
]

DESCRIZIONE_HOME = (
    "Il Quaderno nasce tra non professionisti ed è rivolto ad altri non professionisti. Appunti di studio dell'acquerello: le tre consistenze e gli stati della carta, "
    "la teoria dei colori con un calcolatore di miscele, i tubetti marca per marca, gli esercizi sugli alberi tratti dai video "
    "e il calendario degli eventi."
)

OPZIONI_SEZIONE = [
    "Generale / Nuovo argomento",
    "Principi",
    "Teoria dei colori",
    "Confronto marche",
    "Soggetti (Alberi, Nuvole, Fiori...)",
    "Eventi",
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


def riassunto_eventi():
    """Testo della chat ricavato dai file degli eventi: date, programma, locandina e foto."""
    cartella = DATI_DIR / "eventi" / "schede"
    if not cartella.is_dir():
        return "Eventi: nessun archivio presente."
    mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
            "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]

    def lunga(iso):
        anno, mese, giorno = iso.split("-")
        return f"{int(giorno)} {mesi[int(mese) - 1]} {anno}"

    blocchi = [
        "Eventi (https://app-acquerello.pages.dev/eventi/): calendario, scheda per evento e archivio per anno. "
        "Ogni scheda ha la locandina, il programma e le fotografie di chi ha partecipato. "
        "In fondo alla scheda, solo se sono indicati, ci sono link social testuali: non se ne inventano altri. "
        "Ogni foto porta la didascalia e il nome di chi l'ha scattata. "
        "Se la locandina manca, in pagina c'è scritto «locandina da aggiungere»: non se ne inventa una. "
        "Non si aggiungono racconti, schede di demo né interviste."
    ]
    for path in sorted(cartella.glob("*.json")):
        ev = json.loads(path.read_text(encoding="utf-8"))
        url = f"{SITO_URL}/eventi/{ev['anno']}/{ev['slug']}/"
        fonte = ev["fonte"]
        righe = []
        for m in ev.get("programma", []):
            riga = f"- {m['giorno'][8:10]} {mesi[int(m['giorno'][5:7]) - 1]}: {m['voce']}"
            if m.get("nota"):
                riga += f". Nota: {m['nota']}"
            righe.append(riga)
        programma = "\n".join(righe) if righe else "- Programma da aggiungere."
        if ev.get("locandina"):
            loc = ev["locandina"]
            locandina = f"{loc['credito']}. Fonte: {loc['fonte']['url']}"
        else:
            locandina = "locandina da aggiungere."
        foto = []
        for f in ev.get("foto", []):
            foto.append(f"- {f['didascalia']}. {f['credito']}.")
        social = ev.get("social")
        if social:
            righe_social = "\n".join(f"- {voce['etichetta']}: {voce['url']}" for voce in social["link"])
            testo_social = f"\n{social['titolo']}:\n{righe_social}"
        else:
            testo_social = ""
        blocchi.append(
            f"\n{ev['titolo']} ({url}). {ev['sottotitolo']}. "
            f"Dal {lunga(ev['data_inizio'])} al {lunga(ev['data_fine'])}. {ev['luogo']}. "
            f"Programma letto il {fonte['letto']} da {fonte['url']}.\n"
            f"Locandina: {locandina}\n"
            f"Programma:\n{programma}\n"
            f"Fotografie:\n" + ("\n".join(foto) if foto else "- Nessuna.")
            + testo_social
        )
    if len(blocchi) == 1:
        blocchi.append("Nessun evento in archivio.")
    return "\n".join(blocchi)


def genera_prompt_chat():
    """Scrive lib/prompt-chat.js col prompt di sistema della chat, ricavato dai dati del sito: sezioni,
    consistenze e stati della carta dei Principi, tavolozza, le 12 miscele con la convenzione delle dosi,
    esempi e modalità degli Alberi, moduli in preparazione. Così la chat non può contraddire le pagine con dati scritti a mano."""
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
        + (f", {c['trasparenza_tubetto']} nel tubetto proposto" if c.get("trasparenza_tubetto") else "")
        + f"); {c['note']}"
        for c in tavolozza["colori"])
    dosi = alberi["apertura"]["dosi"]
    convenzione = "; ".join(f"«{k}», {v}" for k, v in dosi["voci"])
    miscele = []
    for m in alberi["apertura"]["miscele"]:
        # le sigle dei tubetti fra parentesi, (BO) (TSB) (TOB), servono nella tabella del sito e non nel prompt
        ricetta = re.sub(r"\s*\((?:BO|TSB|TOB)\)", "", m["ricetta"])
        nota = f" {m['nota']}" if m.get("nota") else ""
        miscele.append(f"- {m['m']} {m['nome']}: {ricetta}. Consistenza: {m['consistenza']}.{nota}")
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

Sei colori proposti come punto di partenza: si possono ridurre, ampliare o cambiare (i colori del calcolatore sono provvisori, stimati a occhio):
{colori}

Le 12 miscele dei sei colori proposti, M1-M12 ({SITO_URL}/principi/#miscele). {dosi['testo']} Le dosi: {convenzione}.
{chr(10).join(miscele)}

Il modulo S1, alberi, siepi e arbusti ({SITO_URL}/alberi/), con le modalità tratte dai video:
{chr(10).join(esempi)}

Moduli in preparazione: {in_preparazione}.

{riassunto_eventi()}

Come rispondere:
- In italiano, col registro di un buon manuale tecnico: termini esatti, frasi chiare, niente parlato e niente paroloni. Di norma fra 120 e 220 parole.
- Niente trattino lungo: per gli incisi si usano le virgole, i due punti o le parentesi.
- Indica la sezione del Quaderno che tratta l'argomento, con il suo indirizzo.
- I sei colori del Quaderno sono una proposta di partenza, non una tavolozza fissa: si possono ridurre, ampliare o cambiare.
- Se una miscela M1-M12 ottiene il colore richiesto, indicala con sigla e nome prima di eventuali varianti.
- Non inventare fonti, autori, video, citazioni, sigle di pigmenti o numeri. Se il Quaderno non tratta un punto, dillo, e suggerisci una prova su carta.
- Nella sezione Eventi non inventare locandine, programmi, nomi o didascalie. Se manca la locandina, resta «locandina da aggiungere».
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
      <button type="button" class="chat-chip">Come preparo un verde scuro per le conifere in ombra con i sei colori proposti?</button>
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


# Barra delle sezioni in cima a ogni pagina, home compresa, che resta visibile scorrendo. Non scorre di lato:
# quando le voci non stanno su una riga vanno a capo, sul telefono più compatte. Nelle sezioni l'indice dei
# capitoli (nav.salti), fisso anch'esso, scende sotto la barra. Uno script misura l'altezza reale della barra e
# dell'indice (--barra-h e --salti-h), così scroll-padding-top tiene sotto le due barre il capitolo o la fonte
# raggiunti con un collegamento; senza script valgono le altezze di riserva qui sotto. Il margine allarga la
# barra fino ai bordi della finestra: nelle sezioni il body è centrato e largo al massimo 760-820 px, e --sb
# (larghezza della barra di scorrimento verticale, misurata dallo script; zero sui dispositivi touch, dove la
# barra di scorrimento non occupa spazio) evita lo scorrimento di lato.
BARRA_ALTEZZA = 42
STILE_BARRA = """<style id="stile-barra">
:root{--barra-h:%(altezza)dpx;--salti-h:48px}
html{scroll-padding-top:calc(var(--barra-h) + var(--salti-h) + 8px)}
#barra-quaderno{position:sticky;top:0;z-index:50;display:flex;flex-wrap:wrap;align-items:center;gap:3px 2px;min-height:%(altezza)dpx;margin:%(margine)s;
padding:5px 8px;background:#263529;font:600 .84rem/1.15 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
#barra-quaderno a{flex:none;white-space:nowrap;color:#e6ece3;text-decoration:none;padding:6px 9px;border-radius:6px}
#barra-quaderno a:hover{background:rgba(255,255,255,.12)}
#barra-quaderno a[aria-current="page"]{background:#f7f2e7;color:#263529}
#barra-quaderno .bq-n{display:inline-block;margin-right:5px;padding:2px 4px;border-radius:4px;background:rgba(255,255,255,.16);font-size:.76rem}
#barra-quaderno a[aria-current="page"] .bq-n{background:#263529;color:#f7f2e7}
#barra-quaderno .bq-spazio{flex:1 0 6px}
nav.salti{top:var(--barra-h)}
@media (max-width:600px){
:root{--barra-h:66px}
#barra-quaderno{gap:2px 1px;padding:4px 5px;font-size:.76rem}
#barra-quaderno a{padding:4px 6px}
#barra-quaderno .bq-n{margin-right:3px;padding:1px 3px;font-size:.68rem}
#barra-quaderno .bq-spazio{flex:1 0 2px}
}
</style>
"""


def stile_barra(margine: str) -> str:
    return STILE_BARRA % {"altezza": BARRA_ALTEZZA, "margine": margine}


def barra_quaderno(slug_pagina: str, profondita: int | None = None) -> str:
    """La barra con tutte le sezioni; slug_pagina è la sezione aperta, stringa vuota per la home.

    profondita è il numero di «../» per tornare alla radice del sito: 0 in home, 1 nelle sezioni,
    2 e 3 nelle pagine di un evento. Senza il parametro resta il comportamento di prima."""
    if profondita is None:
        profondita = 1 if slug_pagina else 0
    radice = "./" if profondita == 0 else "../" * profondita

    def corrente(slug):
        return ' aria-current="page"' if slug == slug_pagina else ""

    voci = [f'<a href="{radice}"{corrente("")}>Quaderno</a>']
    voci += [f'<a href="{radice}{s["slug"]}/"{corrente(s["slug"])}><span class="bq-n">{s["numero"]}</span>{e(s["breve"])}</a>'
             for s in SEZIONI]
    voci.append('<span class="bq-spazio"></span><a href="#assistente-ai">🎨 Assistente</a><a href="#suggerimenti">💬 Suggerimenti</a>')
    # altezza reale della barra e dell'indice dei capitoli, che cambia quando le voci vanno a capo
    script = ("<script>(function(){var r=document.documentElement,b=document.getElementById('barra-quaderno');if(!b)return;"
              "function m(){var s=document.querySelector('nav.salti');r.style.setProperty('--barra-h',b.offsetHeight+'px');"
              "r.style.setProperty('--salti-h',(s?s.offsetHeight:0)+'px');r.style.setProperty('--sb',(matchMedia('(pointer:coarse)').matches?0:innerWidth-r.clientWidth)+'px');}"
              "m();addEventListener('load',m);addEventListener('resize',m);if(window.ResizeObserver)new ResizeObserver(m).observe(b);})();</script>")
    return f'<nav id="barra-quaderno" aria-label="Sezioni del Quaderno">{"".join(voci)}</nav>\n{script}\n'


def inietta_elementi_comuni(html_pagina: str, sezione: dict, pagina_path: str, profondita: int | None = None) -> str:
    if 'property="og:title"' not in html_pagina:
        dichiarazione = re.search(r'<meta name="description" content="([^"]*)">', html_pagina)
        descrizione = html.unescape(dichiarazione.group(1)) if dichiarazione else senza_tag(sezione["sottotitolo"])
        if dichiarazione:
            html_pagina = html_pagina.replace(dichiarazione.group(0), "", 1)
        m = re.search(r"<title>(.*?)</title>", html_pagina, re.S)
        titolo = html.unescape(m.group(1)) if m else sezione["titolo"]
        html_pagina = html_pagina.replace("</head>", testa_comune(titolo, descrizione, pagina_path) + "</head>", 1)
    if 'id="barra-quaderno"' not in html_pagina:
        html_pagina = html_pagina.replace("</head>", stile_barra("0 calc(50% - 50vw + var(--sb, 0px) / 2)") + "</head>", 1)
        html_pagina = re.sub(
            r"(<body[^>]*>)",
            lambda m, profondita=profondita: m.group(1) + "\n" + barra_quaderno(sezione["slug"], profondita),
            html_pagina,
            count=1,
        )

    blocco = blocco_chat_e_suggerimenti(sezione.get("nome_form", OPZIONI_SEZIONE[0]), pagina_path)
    if 'id="suggerimenti"' not in html_pagina:
        if "<footer" in html_pagina:
            html_pagina = html_pagina.replace("<footer", blocco + "\n<footer", 1)
        else:
            html_pagina = html_pagina.replace("</body>", blocco + "\n</body>", 1)
    return html_pagina


# Voci del riquadro «in costruzione» della home, testo approvato dal curatore il 21/10/2026: ogni voce porta
# alla pagina o allo strumento che nomina. La voce della casella, prima in questo elenco, dal 24/10/2026
# è la frase che chiude il riquadro, così non compare due volte.
IN_COSTRUZIONE = [
    'i <a href="./principi/">principi generali su acqua, colore e carta</a>, dalle tre consistenze della miscela agli stati della carta',
    'un <a href="./alberi/">primo modulo di esercizi su alberi, siepi e arbusti</a>, con i passaggi dei video didattici indicati al secondo',
    'un <a href="./eventi/">calendario degli eventi</a>, con locandina, programma e fotografie, e l\'archivio per anno',
    'un <a href="./colori/#calcolatore">calcolatore</a> che propone, come stima, la miscela più vicina a un colore dato',
    "un <a href=\"#assistente-ai\">assistente basato sull'intelligenza artificiale</a> per le domande sulla tecnica, "
    "con un limite di 5 domande a settimana",
]


# Home: testata ad acquerello, striscia della tavolozza, schede con una figurina in SVG o CSS, nota di metodo da aprire.


def colori_tavolozza() -> list[dict]:
    return json.loads((DATI_DIR / "colori" / "tavolozza.json").read_text(encoding="utf-8"))["colori"]


def striscia_tavolozza() -> str:
    """Le sei macchie, con nome comune e pigmento, dai valori di dati/colori/tavolozza.json.

    Scelta di Sandro del 24/10/2026: in home la fila è solo immagine di presentazione, senza didascalia.
    Il nome e il pigmento restano sull'etichetta di ogni campione."""
    voci = "".join(
        f'<li title="{e(c["nome"])} ({e(c["pigmento"])})"><span class="goccia" style="--c:{e(c["srgb"])}"></span>'
        f'<span class="m-nome">{e(c["nome"])}</span><span class="m-pig">{e(c["pigmento"])}</span></li>'
        for c in colori_tavolozza())
    return f'<section class="tavolozza" aria-label="Sei colori proposti"><ul>{voci}</ul></section>'


def icona_scheda(slug: str) -> str:
    """Piccola figura della scheda in home, disegnata in SVG o CSS."""
    if slug == "principi":  # goccia sulla carta bagnata
        return ('<svg viewBox="0 0 64 64" aria-hidden="true"><ellipse cx="32" cy="53" rx="24" ry="6" fill="#7fa3cf" fill-opacity=".35"/>'
                '<path d="M32 5C25 18 17 27 17 38a15 15 0 0 0 30 0C47 27 39 18 32 5Z" fill="#3f6fb0" fill-opacity=".78"/>'
                '<ellipse cx="26" cy="37" rx="4" ry="7" fill="#fff" fill-opacity=".45"/></svg>')
    if slug == "colori":  # cerchio dei colori
        return '<span class="ruota" aria-hidden="true"></span>'
    if slug == "marche":  # tubetto
        return ('<svg viewBox="0 0 64 64" aria-hidden="true"><g transform="rotate(-28 32 32)">'
                '<rect x="19" y="5" width="26" height="5" rx="1" fill="#b9b1a3"/>'
                '<path d="M19 10H45L42 45H22Z" fill="#ece6d9" stroke="#b9b1a3" stroke-width="1.5"/>'
                '<rect x="20.5" y="20" width="23" height="14" fill="#283A9E" fill-opacity=".85"/>'
                '<rect x="27" y="45" width="10" height="4" fill="#b9b1a3"/><rect x="24" y="49" width="16" height="10" rx="2" fill="#3b3a36"/>'
                '</g><circle cx="52" cy="54" r="5" fill="#283A9E" fill-opacity=".55"/></svg>')
    if slug == "soggetti":  # cielo, nuvola, collina e acqua
        return ('<svg viewBox="0 0 64 64" aria-hidden="true"><defs><clipPath id="cp-sog"><circle cx="32" cy="32" r="28"/></clipPath></defs>'
                '<g clip-path="url(#cp-sog)"><rect width="64" height="64" fill="#cfe0ee"/><ellipse cx="24" cy="21" rx="11" ry="5" fill="#fff" fill-opacity=".9"/>'
                '<path d="M0 42Q18 26 34 38T64 34V64H0Z" fill="#6f8f5a" fill-opacity=".85"/><rect y="46" width="64" height="18" fill="#7fa3cf" fill-opacity=".8"/>'
                '<path d="M12 51h22M30 56h20" stroke="#fff" stroke-opacity=".7" stroke-width="2" stroke-linecap="round"/></g></svg>')
    if slug == "eventi":  # calendario, figura disegnata
        return ('<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="12" y="14" width="40" height="38" rx="4" fill="#fffdf8" stroke="#263529" stroke-width="2"/>'
                '<rect x="12" y="14" width="40" height="12" rx="4" fill="#263529"/><rect x="12" y="20" width="40" height="6" fill="#263529"/>'
                '<rect x="22" y="8" width="4" height="10" rx="1" fill="#263529"/><rect x="38" y="8" width="4" height="10" rx="1" fill="#263529"/>'
                '<circle cx="24" cy="36" r="3" fill="#3f6fb0"/><circle cx="34" cy="36" r="3" fill="#6f8f5a"/>'
                '<circle cx="44" cy="44" r="3" fill="#8c4a27"/></svg>')
    if slug == "alberi":  # albero con chioma e tronco
        return ('<svg viewBox="0 0 64 64" aria-hidden="true"><ellipse cx="32" cy="57" rx="22" ry="4" fill="#6f8f5a" fill-opacity=".35"/><path d="M30 58V38h4v20Z" fill="#7a5236"/><path d="M32 46l-7-6M32 43l6-5" stroke="#7a5236" stroke-width="2" stroke-linecap="round"/><circle cx="32" cy="25" r="15" fill="#4f7d45" fill-opacity=".85"/><circle cx="21" cy="32" r="10" fill="#6f9a52" fill-opacity=".8"/><circle cx="43" cy="31" r="11" fill="#3f6a3a" fill-opacity=".8"/><circle cx="27" cy="19" r="6" fill="#9cc07a" fill-opacity=".55"/></svg>')
    return ""


# Grana leggera da carta da acquerello, come rumore SVG in sfondo alla pagina.
GRANA_CARTA = "url(\"data:image/svg+xml," + urllib.parse.quote(
    "<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='g'>"
    "<feTurbulence type='fractalNoise' baseFrequency='.75' numOctaves='3' stitchTiles='stitch'/>"
    "<feColorMatrix values='0 0 0 0 .42 0 0 0 0 .35 0 0 0 0 .25 0 0 0 .09 0'/></filter>"
    "<rect width='100%' height='100%' filter='url(#g)'/></svg>", safe="/:=' ") + "\")"

STILE_HOME = """*{box-sizing:border-box}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#faf6ee @GRANA@;color:#1f1c17;line-height:1.5}
.testa{position:relative;overflow:hidden;background:#f6f1e6;color:#1b2b20;border-bottom:1px solid #e2d8c6}
.testa::before{content:"";position:absolute;inset:-15%;filter:blur(8px);background:
 radial-gradient(40% 55% at 14% 28%,rgba(63,111,176,.30),transparent 70%),
 radial-gradient(32% 48% at 42% 92%,rgba(111,143,90,.28),transparent 72%),
 radial-gradient(26% 40% at 62% 12%,rgba(150,70,40,.16),transparent 70%),
 radial-gradient(45% 65% at 88% 55%,rgba(63,111,176,.26),transparent 70%)}
.testa-in{position:relative;max-width:820px;margin:0 auto;padding:40px 18px 36px}
.testa h1{margin:0 0 8px;font-family:Georgia,"Times New Roman",serif;font-weight:700;font-size:2.15rem;line-height:1.12;color:#1b2b20}
.testa p{margin:0;max-width:520px;font-size:1.02rem;color:#2f4236}
.testa .nota{margin:14px 0 0;max-width:40rem;font-size:.98rem;line-height:1.5;color:#2f4236}
.tavolozza{max-width:820px;margin:0 auto;padding:18px 14px 0}
.tavolozza ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:8px}
.tavolozza li{display:flex;flex-direction:column;align-items:center;text-align:center;font-size:.75rem;line-height:1.25;color:#3d352a}
.goccia{width:56px;height:40px;margin-bottom:5px;background:radial-gradient(ellipse at 40% 40%,rgba(255,255,255,.22),transparent 65%),var(--c);opacity:.84;
 border-radius:58% 42% 55% 45%/52% 60% 40% 48%;box-shadow:inset 0 0 3px 1px rgba(0,0,0,.28)}
.tavolozza li:nth-child(2n) .goccia{border-radius:44% 56% 40% 60%/58% 42% 58% 42%;transform:rotate(4deg)}
.tavolozza li:nth-child(3n) .goccia{border-radius:62% 38% 50% 50%/45% 55% 45% 55%;transform:rotate(-6deg)}
.m-pig{font-size:.7rem;color:#7a6f5d}
main{max-width:820px;margin:0 auto;padding:18px 14px 12px}
.cf-origine{background:#eef4ef;border:1px solid #cadbce;border-left:4px solid #263529;border-radius:8px;padding:10px 14px;margin:0 0 16px;font-size:.91rem;color:#263529}
.cf-origine summary{cursor:pointer;font-weight:700;color:#1b2b20}
.cf-origine p{margin:8px 0 2px}
.cf-sviluppo{background:#f4efe4;border:1px solid #d8ccb8;border-left:4px solid #8c4a27;border-radius:8px;padding:12px 16px;margin:0 0 26px;font-size:.92rem;color:#2e2820}
.cf-sviluppo p{margin:0 0 6px}
.cf-sviluppo strong{color:#6b3418}
.cf-sviluppo ul{margin:0;padding-left:20px}
.cf-sviluppo ul + p{margin:10px 0 0}
.cf-sviluppo li{margin:3px 0}
.cf-sviluppo a{color:#6b3418}
.sezioni-tit{margin:0 0 12px;font-size:1.12rem;color:#263529}
.grid{display:grid;grid-template-columns:1fr;gap:10px}
.card{display:flex;align-items:flex-start;gap:12px;padding:14px 16px;background:#fffdf8;border:1px solid #dfd5c3;border-radius:12px;color:inherit;text-decoration:none;box-shadow:0 2px 8px rgba(31,28,23,.06);transition:transform .15s ease,box-shadow .15s ease}
.card:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(31,28,23,.12)}
.card.modulo{margin-left:28px}
.sig{flex:none;display:inline-flex;align-items:center;justify-content:center;min-width:34px;height:32px;padding:0 5px;border-radius:8px;background:#263529;color:#f7f2e7;font-weight:700;font-size:.95rem}
.card-txt{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.card-tit{font-size:1.08rem;font-weight:700;color:#1f1c17}
.card-sub{font-size:.88rem;color:#6b5e4c}
.card-fig{flex:none;align-self:center;display:flex;align-items:center;justify-content:center;width:60px;height:60px}
.card-fig svg{width:60px;height:60px;display:block}
.ruota{display:block;width:54px;height:54px;border-radius:50%;opacity:.85;
 background:conic-gradient(#f0d53c,#e88d2c,#c8323a,#8e2f78,#3a4fa8,#2a86a0,#4f9a48,#f0d53c);
 -webkit-mask-image:radial-gradient(circle,transparent 27%,#000 29%);mask-image:radial-gradient(circle,transparent 27%,#000 29%)}
footer{text-align:center;padding:18px;font-size:.82rem;color:#7a6f5d;border-top:1px solid #e5dccb;margin-top:24px}
footer a{color:#5a4d3b}
@media (max-width:560px){
 .testa-in{padding:26px 16px 22px}
 .testa h1{font-size:1.55rem}
 .testa p{font-size:.9rem}
 .testa .nota{font-size:.88rem}
 .tavolozza ul{grid-template-columns:repeat(3,1fr);row-gap:12px}
 .card{padding:12px 12px;gap:10px}
 .card-fig,.card-fig svg{width:46px;height:46px}
 .ruota{width:42px;height:42px}
}
""".replace("@GRANA@", GRANA_CARTA)


def genera_home(sezioni_pronte: list[dict]) -> str:
    schede = []
    for s in sezioni_pronte:
        classe = "card modulo" if s.get("modulo_di") else "card"
        figura = icona_scheda(s["slug"])
        figura = f'\n  <span class="card-fig">{figura}</span>' if figura else ""
        schede.append(f"""<a class="{classe}" href="./{s['slug']}/">
  <span class="sig">{s['numero']}</span>
  <span class="card-txt"><span class="card-tit">{s['titolo']}</span><span class="card-sub">{s['sottotitolo']}</span></span>{figura}
</a>""")
    schede_html = "\n".join(schede)
    voci = "".join(f"<li>{v}{';' if i < len(IN_COSTRUZIONE) - 1 else '.'}</li>" for i, v in enumerate(IN_COSTRUZIONE))
    blocco_sugg = blocco_chat_e_suggerimenti(OPZIONI_SEZIONE[0], "/")
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quaderno di acquerello</title>
{testa_comune("Quaderno di acquerello", DESCRIZIONE_HOME, "/")}<style>
{STILE_HOME}</style>
{stile_barra("0")}</head>
<body>
{barra_quaderno("")}<header class="testa">
  <div class="testa-in">
    <h1>Quaderno di acquerello</h1>
    <p>Appunti di studio dell'acquerello: acqua e carta, colori e tubetti, soggetti, esercizi tratti dai video ed eventi</p>
    <p class="nota">Il Quaderno nasce tra non professionisti ed è rivolto ad altri non professionisti. Raccoglie ciò che si impara strada facendo, con i limiti di chi non è un maestro, ed è aperto ai contributi di tutti gli appassionati.</p>
  </div>
</header>
{striscia_tavolozza()}
<main>
  <details class="cf-origine">
    <summary>Nota di metodo</summary>
    <p>Chi oggi apprende una disciplina pratica dispone di una documentazione vastissima, distribuita tra manuali, schede tecniche e centinaia di ore di dimostrazioni filmate; la vera difficoltà sta nel ricondurre una materia tanto dispersa a un criterio ordinato e consultabile mentre si lavora. Gli strumenti di intelligenza artificiale permettono di compiere a monte questo lavoro di spoglio, confronto e classificazione, così da aiutare a esercitarsi con più consapevolezza. Il Quaderno nasce dall'applicazione di tale approccio allo studio dell'acquerello: ordina il comportamento di acqua, carta e pigmenti, indica al secondo le sequenze esecutive nei video didattici e affianca al tavolo da lavoro strumenti di riscontro, dal calcolatore colorimetrico all'assistente tecnico integrato nelle pagine.</p>
  </details>
  <section class="cf-sviluppo" aria-label="Stato del Quaderno">
    <p><strong>Il Quaderno è in costruzione.</strong> Le sezioni esistenti vengono ampliate progressivamente e altre se ne
    aggiungeranno. Nella versione attuale il Quaderno mette a disposizione:</p>
    <ul>{voci}</ul>
    <p>Chiunque può proporre correzioni, integrazioni e video dalla <a href="#suggerimenti">casella dei suggerimenti</a>: il Quaderno è aperto ai contributi di tutti gli appassionati.</p>
  </section>

  <h2 class="sezioni-tit">Le sezioni</h2>
  <div class="grid">
    {schede_html}
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


# Indirizzi di sezioni tolte o spostate, rinviati con un 301 dal file site/_redirects di Cloudflare Pages:
# percorso vecchio, pagina nuova, ancora. La sezione Studio ed en plein air è diventata, il 22/10/2026,
# il capitolo 8 dei Principi generali. main() verifica che l'ancora esista nella pagina generata.
REINDIRIZZAMENTI = [
    ("/studio-plein-air", "principi", "studio-aperto"),
    ("/studio-plein-air/", "principi", "studio-aperto"),
    ("/studio-plein-air/index.html", "principi", "studio-aperto"),
]


def controlla_reindirizzamenti():
    for vecchio, slug, ancora in REINDIRIZZAMENTI:
        pagina = SITE_DIR / slug / "index.html"
        if not pagina.exists() or f'id="{ancora}"' not in pagina.read_text(encoding="utf-8"):
            raise SystemExit(f"genera-sito: il rinvio di {vecchio} porta a /{slug}/#{ancora}, che non esiste")


def scrivi_file_di_servizio(pagine_extra=None):
    pagine = ["/"] + [f"/{s['slug']}/" for s in SEZIONI]
    for p in pagine_extra or []:
        if p not in pagine:
            pagine.append(p)
    (SITE_DIR / "_redirects").write_text(
        "".join(f"{vecchio} /{slug}/#{ancora} 301\n" for vecchio, slug, ancora in REINDIRIZZAMENTI),
        encoding="utf-8", newline="\n")
    (SITE_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: {SITO_URL}/sitemap.xml\n", encoding="utf-8", newline="\n")
    voci = "".join(f"  <url><loc>{SITO_URL}{p}</loc></url>\n" for p in pagine)
    (SITE_DIR / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{voci}</urlset>\n", encoding="utf-8", newline="\n")
    (SITE_DIR / "favicon.svg").write_text(FAVICON, encoding="utf-8", newline="\n")


def gulpease(html_pagina):
    """Indice Gulpease dei testi leggibili di una pagina, senza script, stili, svg, chat, suggerimenti ed elenchi
    delle fonti, che citano titoli e passi nella lingua originale e si ripetono in più capitoli."""
    t = re.sub(r'<section id="(assistente-ai|suggerimenti)".*?</section>', " ", html_pagina, flags=re.S)
    t = re.sub(r'<div class="fonti-cap">.*?</div>', " ", t, flags=re.S)
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
    sezioni_pronte, leggibilita, pagine_sitemap = [], {}, []

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
        extra = s.get("pagine_extra")
        if extra is not None:
            if not extra.is_dir():
                raise FileNotFoundError(f"Pagine aggiuntive non trovate: {extra}")
            for html_extra in sorted(extra.rglob("*.html")):
                rel = html_extra.relative_to(extra)
                if rel.name != "index.html":
                    raise SystemExit(f"genera-sito: pagina non prevista in {rel.as_posix()}")
                prof = len(rel.parent.parts) + 1
                pagina_path = f"/{s['slug']}/{rel.parent.as_posix()}/"
                sorgente = html_extra.read_text(encoding="utf-8")
                dest = dest_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(
                    inietta_elementi_comuni(sorgente, s, pagina_path, prof),
                    encoding="utf-8", newline="\n")
                leggibilita[f"{s['slug']}/{rel.parent.as_posix()}"] = gulpease(sorgente)
                pagine_sitemap.append(pagina_path)
                print(f"[{s['slug']}] Scritto {dest.relative_to(APP_DIR).as_posix()} ({dest.stat().st_size // 1024} KB)")
        sezioni_pronte.append(dict(s))

    index_html = SITE_DIR / "index.html"
    index_html.write_text(genera_home(sezioni_pronte), encoding="utf-8", newline="\n")
    print(f"[home] Scritto {index_html.relative_to(APP_DIR).as_posix()} ({index_html.stat().st_size // 1024} KB)")
    scrivi_file_di_servizio(pagine_sitemap)
    controlla_reindirizzamenti()
    genera_prompt_chat()

    print("[leggibilità] Gulpease: " + ", ".join(f"{k} {v}" for k, v in leggibilita.items() if v is not None))
    basse = {k: v for k, v in leggibilita.items() if v is not None and v < GULPEASE_MINIMO}
    if basse:
        raise SystemExit(f"genera-sito: leggibilità sotto {GULPEASE_MINIMO} (Gulpease) in {basse}: testi da semplificare")


if __name__ == "__main__":
    main()

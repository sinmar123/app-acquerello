#!/usr/bin/env python3
"""Genera la sezione Eventi: calendario, scheda per evento e archivio per anno.

Uso: python genera-eventi.py pagina

Legge sezione.json e un file JSON per evento in schede/. Scrive eventi.html
(il calendario) e pagine/<anno>/index.html più pagine/<anno>/<slug>/index.html.
scripts/genera-sito.py copia il calendario in site/eventi/, inietta barra,
chat e suggerimenti, e pubblica le altre pagine insieme alla cartella immagini/.

Ogni scheda ha la locandina, il programma e le fotografie. In fondo, se il
JSON ha «social», un riquadro di link testuali. Il file idee-interviste.md
resta nel repository e non entra in queste pagine.

Il giorno «oggi», per dire se un evento è in corso, in arrivo o passato, è
quello di Europe/Rome nel momento della generazione.

Controlli: date e giorni della settimana coerenti; ogni voce del programma
apre con il suo orario; ogni foto è in immagini/ e ha credito e didascalia.
Se una foto indica un momento, quello è una voce del programma e l'ora è
nel formato 11.57: la foto sta accanto a quella voce. Le foto senza momento
restano nella sezione fotografie, e l'elenco delle foto legate segue l'ordine
del programma. La locandina, se c'è, ha file, credito, alt e fonte https, e
può avere una didascalia. Un riquadro social, se c'è, ha titolo e link https.
Nessun testo contiene «da verificare» né il trattino lungo.
Racconti, demo e interviste non sono ammessi in una scheda.
"""
import html
import json
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8")

QUI = Path(__file__).resolve().parent
SCHEDE = QUI / "schede"
IMMAGINI = QUI / "immagini"
PAGINE = QUI / "pagine"
CALENDARIO = QUI / "eventi.html"
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
        "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
GIORNI = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
TRATTINI = ("—", "–", "―")
ID_OK = re.compile(r"^[a-z0-9-]+$")
FILE_OK = re.compile(r"^[a-z0-9.-]+$")
ORA_OK = re.compile(r"^([01]\d|2[0-3])\.[0-5]\d$")
CHIAVI_VIETATE = ("racconti", "interviste", "lezioni", "collegamenti", "campi_demo", "domande")

CSS = """
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0 auto; max-width: 820px; padding: 0 14px 40px; font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
       font-size: 17px; line-height: 1.5; color: #1f1f1f; background: #fbfaf7; }
h1 { font-size: 1.45em; line-height: 1.25; margin: 18px 0 6px; color: #2c4f3a; }
h2 { font-size: 1.22em; margin: 0 0 8px; color: #2c4f3a; }
h3 { font-size: 1.05em; margin: 0 0 6px; color: #1f1c17; }
a { color: #2c6a4a; }
.sotto { color: #444; margin: 0 0 12px; }
.filo { font-size: .92em; margin: 0 0 12px; }
.filo a { font-weight: 600; text-decoration: none; }
nav.salti { position: sticky; top: 0; z-index: 5; display: flex; gap: 6px; overflow-x: auto; padding: 8px 0;
            background: #fbfaf7; border-bottom: 1px solid #e3e0d8; }
nav.salti a { flex: none; text-decoration: none; color: #2c4f3a; border: 1px solid #3d6b4f; border-radius: 16px;
              padding: 3px 12px; font-weight: 600; }
.intro, .nota { background: #eef4ef; border: 1px solid #cadbce; border-radius: 8px; padding: 10px 14px; margin: 12px 0 18px; }
.intro p, .nota p { margin: 0 0 8px; }
.intro p:last-child, .nota p:last-child { margin-bottom: 0; }
section.blocco { border-top: 3px solid #3d6b4f; padding-top: 14px; margin-top: 26px; }
.voce { background: #fffdf8; border: 1px solid #dfd5c3; border-radius: 12px; padding: 14px 16px; margin: 10px 0; }
.voce p { margin: 6px 0; }
.stato { display: inline-block; font-size: .78rem; font-weight: 700; border-radius: 999px; padding: 2px 8px; }
.stato.in_corso { background: #e3f1e8; color: #1e4638; }
.stato.in_arrivo { background: #e7eef8; color: #243e66; }
.stato.passato { background: #efe8d8; color: #5a4d3b; }
.tab { overflow-x: auto; margin: 8px 0 14px; }
table { width: 100%; border-collapse: collapse; font-size: .92em; table-layout: fixed; }
th, td { border: 1px solid #d8d2c4; padding: 6px 8px; vertical-align: top; text-align: left; }
.accanto .testo { margin: 0; }
.accanto figure.foto { margin: 10px 0 0; }
th { background: #eef4ef; color: #2c4f3a; }
th.giorno { background: #263529; color: #f7f2e7; }
caption { caption-side: bottom; text-align: left; font-size: .85em; color: #555; padding-top: 6px; }
.vuoto { color: #6b5e4c; font-style: italic; }
.nota-riga { display: block; margin-top: 4px; color: #555; font-size: .92em; }
figure.foto { margin: 12px 0; }
figure.foto img { width: 100%; max-width: 28rem; height: auto; border-radius: 8px; border: 1px solid #dfd5c3; display: block; }
figure.foto figcaption { font-size: .9em; color: #444; margin-top: 6px; }
.social { background: #fffdf8; border: 1px solid #dfd5c3; border-radius: 12px; padding: 12px 16px; margin: 22px 0 4px; }
.social h2 { font-size: 1.05em; margin: 0 0 8px; }
.social ul { margin: 0; padding-left: 1.15em; }
.social li { margin: 4px 0; }
footer { margin-top: 28px; border-top: 1px solid #ddd; padding-top: 12px; font-size: .9em; color: #444; }
"""


def e(testo):
    return html.escape(str(testo if testo is not None else ""), quote=True)


def errore(msg):
    raise SystemExit(f"eventi: {msg}")


def oggi_roma():
    return datetime.now(ZoneInfo("Europe/Rome")).date()


def data_it(iso):
    anno, mese, giorno = iso.split("-")
    return f"{int(giorno)}/{mese}/{anno}"


def data_lunga(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {MESI[d.month - 1]} {d.year}"


def intervallo(inizio, fine):
    a, b = date.fromisoformat(inizio), date.fromisoformat(fine)
    if a == b:
        return data_lunga(inizio)
    if a.year == b.year and a.month == b.month:
        return f"dal {a.day} al {b.day} {MESI[a.month - 1]} {a.year}"
    if a.year == b.year:
        return f"dal {a.day} {MESI[a.month - 1]} al {b.day} {MESI[b.month - 1]} {a.year}"
    return f"dal {data_lunga(inizio)} al {data_lunga(fine)}"


def controlla_stringhe(valore, dove):
    if isinstance(valore, str):
        if "da verificare" in valore.lower():
            errore(f"testo «da verificare» in {dove}")
        if any(t in valore for t in TRATTINI):
            errore(f"trattino lungo in {dove}")
    elif isinstance(valore, dict):
        for k, v in valore.items():
            controlla_stringhe(v, f"{dove}.{k}")
    elif isinstance(valore, list):
        for i, v in enumerate(valore):
            controlla_stringhe(v, f"{dove}[{i}]")


def paragrafi(frasi):
    return "".join(f"<p>{e(p)}</p>" for p in frasi)


def radice(prof):
    return "../" * prof


def carica_json(path):
    try:
        dati = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errore(f"{path.name} non è un JSON valido ({exc})")
    controlla_stringhe(dati, path.name)
    return dati


def controlla_social(ev):
    if "social" not in ev:
        return
    social = ev["social"]
    if not isinstance(social, dict) or not str(social.get("titolo") or "").strip():
        errore(f"{ev['id']}: social senza titolo")
    link = social.get("link")
    if not isinstance(link, list) or not link:
        errore(f"{ev['id']}: social senza link")
    visti = set()
    for voce in link:
        if not isinstance(voce, dict) or not str(voce.get("etichetta") or "").strip():
            errore(f"{ev['id']}: link social senza etichetta")
        url = str(voce.get("url") or "")
        if not url.startswith("https://") or any(c in url for c in " \t"):
            errore(f"{ev['id']}: il link social non è un https")
        if url in visti:
            errore(f"{ev['id']}: link social ripetuto")
        visti.add(url)


def stato_evento(ev, oggi):
    inizio = date.fromisoformat(ev["data_inizio"])
    fine = date.fromisoformat(ev["data_fine"])
    if inizio <= oggi <= fine:
        return "in_corso"
    if oggi < inizio:
        return "in_arrivo"
    return "passato"


def controlla_file_immagine(ev, nome, dove):
    if not FILE_OK.match(nome) or not (IMMAGINI / nome).is_file():
        errore(f"{ev['id']}: file assente in immagini/ ({dove})")


def carica_eventi():
    if not SCHEDE.is_dir():
        errore("manca la cartella schede/")
    eventi = []
    for path in sorted(SCHEDE.glob("*.json")):
        ev = carica_json(path)
        for campo in ("id", "slug", "anno", "titolo", "sottotitolo", "data_inizio", "data_fine", "luogo", "fonte"):
            if campo not in ev:
                errore(f"{path.name}: manca {campo}")
        for vietata in CHIAVI_VIETATE:
            if vietata in ev:
                errore(f"{ev['id']}: «{vietata}» non entra nella scheda")
        if path.stem != ev["id"]:
            errore(f"{path.name}: il nome del file deve essere {ev['id']}.json")
        if not ID_OK.match(ev["slug"]) or not ID_OK.match(ev["id"]):
            errore(f"{ev['id']}: slug o id non valido")
        if ev["id"] != f"{ev['slug']}-{ev['anno']}":
            errore(f"{ev['id']}: l'id atteso è {ev['slug']}-{ev['anno']}")
        inizio, fine = date.fromisoformat(ev["data_inizio"]), date.fromisoformat(ev["data_fine"])
        if fine < inizio:
            errore(f"{ev['id']}: la data di fine precede l'inizio")
        if inizio.year != fine.year or ev["anno"] != inizio.year:
            errore(f"{ev['id']}: un evento deve stare in un solo anno")
        fonte = ev["fonte"]
        for campo in ("url", "etichetta", "letto"):
            if not fonte.get(campo):
                errore(f"{ev['id']}: fonte senza {campo}")
        if not fonte["url"].startswith("https://"):
            errore(f"{ev['id']}: la fonte del programma non è un https")
        date.fromisoformat(fonte["letto"])
        controlli = ev.get("controllo_giorni", {})
        for giorno, nome in controlli.items():
            if GIORNI[date.fromisoformat(giorno).weekday()] != nome:
                errore(f"{ev['id']}: {giorno} non è un {nome}")
        visti = set()
        precedente = ""
        for m in ev.get("programma", []):
            for campo in ("id", "giorno", "fascia", "orario", "voce"):
                if campo not in m:
                    errore(f"{ev['id']}: momento senza {campo}")
            if not ID_OK.match(m["id"]) or m["id"] in visti:
                errore(f"{ev['id']}: id momento duplicato o non valido ({m['id']})")
            visti.add(m["id"])
            if m["giorno"] < precedente:
                errore(f"{ev['id']}: il programma non è in ordine di data")
            precedente = m["giorno"]
            if m["giorno"] not in controlli:
                errore(f"{ev['id']}: {m['giorno']} senza controllo del giorno")
            if m["fascia"] not in ("mattina", "pomeriggio"):
                errore(f"{ev['id']}: fascia non riconosciuta in {m['id']}")
            if not m["voce"].startswith(m["orario"]):
                errore(f"{ev['id']}: l'orario di {m['id']} non apre la voce")
        loc = ev.get("locandina")
        if loc:
            for campo in ("file", "credito", "alt", "fonte"):
                if not loc.get(campo):
                    errore(f"{ev['id']}: locandina senza {campo}")
            controlla_file_immagine(ev, loc["file"], "locandina")
            if not loc["fonte"].get("url", "").startswith("https://") or not loc["fonte"].get("etichetta"):
                errore(f"{ev['id']}: fonte della locandina incompleta")
        file_visti = set()
        for foto in ev.get("foto", []):
            for campo in ("file", "credito", "didascalia", "alt"):
                if not foto.get(campo):
                    errore(f"{ev['id']}: foto senza {campo}")
            if foto["file"] in file_visti:
                errore(f"{ev['id']}: file di foto ripetuto ({foto['file']})")
            file_visti.add(foto["file"])
            controlla_file_immagine(ev, foto["file"], foto.get("file"))
            if "momento" in foto:
                if foto["momento"] not in visti:
                    errore(f"{ev['id']}: la foto {foto['file']} indica un momento assente ({foto.get('momento')})")
                if not ORA_OK.match(foto.get("ora", "")):
                    errore(f"{ev['id']}: la foto {foto['file']} ha un'ora assente o non valida")
            elif "ora" in foto and not ORA_OK.match(foto.get("ora", "")):
                errore(f"{ev['id']}: la foto {foto['file']} ha un'ora non valida")
        controlla_social(ev)
        eventi.append(ev)
    return eventi


def salti(voci):
    return '<nav class="salti">' + "".join(f'<a href="#{ancora}">{e(testo)}</a>' for ancora, testo in voci) + "</nav>"


def piede(sez, prof):
    r = radice(prof)
    return (
        "<footer>"
        f"<p>Quaderno di acquerello · Eventi · testi del {e(data_it(sez['data']))}.</p>"
        "<p>Le altre sezioni: "
        f'<a href="{r}principi/">1. Principi generali</a> · '
        f'<a href="{r}colori/">2. Teoria dei colori</a> · '
        f'<a href="{r}marche/">3. Marche e tubetti</a> · '
        f'<a href="{r}soggetti/">4. Soggetti</a> · '
        f'<a href="{r}alberi/">4.1 Alberi</a>.</p>'
        "</footer>"
    )


def documento(titolo, descrizione, corpo):
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titolo)}</title>
<meta name="description" content="{e(descrizione)}">
<style>{CSS}</style></head>
<body>
{corpo}
</body></html>
"""


def card_evento(ev, oggi, prof, sez):
    st = stato_evento(ev, oggi)
    etichetta = sez["stati"]["in_corso"] if st == "in_corso" else (
        "In arrivo" if st == "in_arrivo" else "Passato")
    href = f"{ev['anno']}/{ev['slug']}/" if prof == 1 else f"{ev['slug']}/"
    fonte = ev["fonte"]
    return (
        f'<article class="voce" id="evento-{e(ev["id"])}">'
        f'<p><span class="stato {st}">{e(etichetta)}</span></p>'
        f"<h3>{e(ev['titolo'])}</h3>"
        f"<p>{e(ev['sottotitolo'])}</p>"
        f"<p>{e(intervallo(ev['data_inizio'], ev['data_fine']).capitalize())}. {e(ev['luogo'])}.</p>"
        f'<p><a href="{e(href)}">Apri la scheda</a>. '
        f'<a href="{e(fonte["url"])}">{e(fonte["etichetta"])}</a>, letto il {e(data_it(fonte["letto"]))}.</p>'
        "</article>"
    )


def gruppo(ancora, chiave, eventi, oggi, prof, sez):
    titolo = sez["stati"][chiave]
    corpo = "".join(card_evento(ev, oggi, prof, sez) for ev in eventi) or f"<p>{e(sez['vuoti_elenco'][chiave])}</p>"
    return f'<section class="blocco" id="{ancora}"><h2>{e(titolo)}</h2>{corpo}</section>'


def pagina_calendario(sez, eventi, oggi):
    in_corso = sorted((ev for ev in eventi if stato_evento(ev, oggi) == "in_corso"), key=lambda ev: ev["data_inizio"])
    in_arrivo = sorted((ev for ev in eventi if stato_evento(ev, oggi) == "in_arrivo"), key=lambda ev: ev["data_inizio"])
    passati = sorted((ev for ev in eventi if stato_evento(ev, oggi) == "passato"), key=lambda ev: ev["data_fine"], reverse=True)
    anni = sorted({ev["anno"] for ev in eventi}, reverse=True)
    archivio = []
    for anno in anni:
        voci = "".join(
            f'<li><a href="{anno}/{e(ev["slug"])}/">{e(ev["titolo"])}</a>, {e(intervallo(ev["data_inizio"], ev["data_fine"]))}.</li>'
            for ev in sorted((ev for ev in eventi if ev["anno"] == anno), key=lambda ev: ev["data_inizio"])
        )
        archivio.append(f"<h3><a href=\"{anno}/\">{e(str(anno))}</a></h3><ul>{voci}</ul>")
    corpo = (
        f"<h1>{e(sez['titolo'])}</h1>"
        f"<p class=\"sotto\">{e(sez['sottotitolo'])}</p>"
        + salti([
            ("in-corso", "In corso"),
            ("in-arrivo", "In arrivo"),
            ("passati", "Passati"),
            ("archivio", "Archivio"),
        ])
        + f'<div class="intro">{paragrafi(sez["introduzione"])}</div>'
        + gruppo("in-corso", "in_corso", in_corso, oggi, 1, sez)
        + gruppo("in-arrivo", "in_arrivo", in_arrivo, oggi, 1, sez)
        + gruppo("passati", "passato", passati, oggi, 1, sez)
        + '<section class="blocco" id="archivio"><h2>Archivio per anno</h2>'
        + f'<div class="nota">{paragrafi(sez["archivio_intro"])}</div>'
        + ("".join(archivio) or "<p>Nessun anno in archivio.</p>")
        + "</section>"
        + piede(sez, 1)
    )
    return documento(sez["titolo"], sez["sottotitolo"], corpo)


def pagina_anno(sez, anno, eventi, oggi):
    elenco = sorted(eventi, key=lambda ev: ev["data_inizio"])
    cards = "".join(card_evento(ev, oggi, 2, sez) for ev in elenco)
    descrizione = f"Archivio {anno} degli eventi del Quaderno di acquerello."
    corpo = (
        f'<p class="filo"><a href="../">Eventi</a></p>'
        f"<h1>Archivio {anno}</h1>"
        f"<p class=\"sotto\">Gli eventi del {anno}, con data, luogo e scheda.</p>"
        + f'<div class="intro">{paragrafi(sez["archivio_intro"])}</div>'
        + f'<section class="blocco" id="elenco"><h2>Eventi del {anno}</h2>{cards}</section>'
        + piede(sez, 2)
    )
    return documento(f"Archivio {anno}", descrizione, corpo)


def figura_foto(foto, prof):
    src = radice(prof - 1) + "immagini/" + foto["file"]
    return (
        '<figure class="foto">'
        f'<img src="{e(src)}" alt="{e(foto["alt"])}">'
        f'<figcaption>{e(foto["didascalia"])}. {e(foto["credito"])}.</figcaption>'
        "</figure>"
    )


def foto_del_momento(ev, momento_id):
    scelte = [f for f in ev.get("foto", []) if f.get("momento") == momento_id]
    return sorted(scelte, key=lambda f: (f.get("ora") or "", f["file"]))


def tabella_programma(ev, prof):
    righe = []
    gruppo_aperto = None
    for m in ev.get("programma", []):
        chiave = (m["giorno"], m["fascia"])
        if chiave != gruppo_aperto:
            gruppo_aperto = chiave
            d = date.fromisoformat(m["giorno"])
            titolo = f"{GIORNI[d.weekday()].capitalize()} {d.day} {MESI[d.month - 1]} {d.year}. {m['fascia'].capitalize()}"
            righe.append(f'<tr><th class="giorno">{e(titolo)}</th></tr>')
        nota = f'<span class="nota-riga">{e(m["nota"])}</span>' if m.get("nota") else ""
        figure = "".join(figura_foto(f, prof) for f in foto_del_momento(ev, m["id"]))
        if figure:
            cella = f'<div class="accanto"><p class="testo">{e(m["voce"])}{nota}</p>{figure}</div>'
        else:
            cella = f'{e(m["voce"])}{nota}'
        righe.append(f'<tr id="m-{e(m["id"])}"><td>{cella}</td></tr>')
    if not righe:
        return "<p>Programma da aggiungere.</p>"
    fonte = ev["fonte"]
    caption = (
        f'Fonte: <a href="{e(fonte["url"])}">{e(fonte["etichetta"])}</a>, '
        f'letto il {e(data_it(fonte["letto"]))}.'
    )
    return (
        '<div class="tab"><table>'
        "<thead><tr><th>Voce del programma</th></tr></thead>"
        f"<tbody>{''.join(righe)}</tbody>"
        f"<caption>{caption}</caption></table></div>"
    )


def blocco_locandina(ev, sez, prof):
    loc = ev.get("locandina")
    if not loc:
        return f'<p class="vuoto">{e(sez["locandina_manca"])}</p>'
    src = radice(prof - 1) + "immagini/" + loc["file"]
    fonte = loc["fonte"]
    didascalia = f'{e(loc["didascalia"])}. ' if loc.get("didascalia") else ""
    return (
        '<figure class="foto">'
        f'<img src="{e(src)}" alt="{e(loc["alt"])}">'
        f'<figcaption>{didascalia}{e(loc["credito"])}. '
        f'<a href="{e(fonte["url"])}">{e(fonte["etichetta"])}</a>.</figcaption>'
        "</figure>"
    )


def blocco_foto(ev, sez, prof):
    tutte = ev.get("foto", [])
    if not tutte:
        return f"<p>{e(sez['nessuna_foto'])}</p>"
    pezzi = [figura_foto(foto, prof) for foto in tutte if not foto.get("momento")]
    ordine = {m["id"]: i for i, m in enumerate(ev.get("programma", []))}
    legate = sorted((f for f in tutte if f.get("momento")),
                    key=lambda f: (ordine.get(f["momento"], len(ordine)), f.get("ora") or "", f["file"]))
    if legate:
        voci = "".join(
            "<li>"
            f'<a href="#m-{e(foto["momento"])}">{e(foto["didascalia"])}</a>. '
            f"{e(foto['credito'])}."
            "</li>"
            for foto in legate
        )
        pezzi.append(
            "<p>Queste fotografie stanno accanto alla voce corrispondente del programma.</p>"
            f"<ul>{voci}</ul>"
        )
    return "".join(pezzi)


def link_esterno(url, etichetta):
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(etichetta)}</a>'


def blocco_social(ev):
    social = ev.get("social")
    if not social:
        return ""
    voci = "".join(f"<li>{link_esterno(voce['url'], voce['etichetta'])}</li>" for voce in social["link"])
    return f'<aside class="social"><h2>{e(social["titolo"])}</h2><ul>{voci}</ul></aside>'


def pagina_scheda(sez, ev, oggi):
    prof = 3
    st = stato_evento(ev, oggi)
    etichetta = {"in_corso": "L'evento è in corso", "in_arrivo": "L'evento è in arrivo", "passato": "L'evento è passato"}[st]
    quando = intervallo(ev["data_inizio"], ev["data_fine"])
    descrizione = f"{ev['titolo']}, {quando}, {ev['luogo']}."
    corpo = (
        f'<p class="filo"><a href="../../">Eventi</a> · <a href="../">Archivio {ev["anno"]}</a></p>'
        f"<h1>{e(ev['titolo'])}</h1>"
        f"<p class=\"sotto\">{e(ev['sottotitolo'])}</p>"
        + salti([
            ("locandina", "Locandina"),
            ("programma", "Programma"),
            ("fotografie", "Fotografie"),
        ])
        + f'<div class="intro">{paragrafi(sez["scheda_intro"])}</div>'
        + f"<p>{e(etichetta)}: {e(quando)}. {e(ev['luogo'])}.</p>"
        + '<section class="blocco" id="locandina"><h2>Locandina</h2>'
        + blocco_locandina(ev, sez, prof)
        + "</section>"
        + '<section class="blocco" id="programma"><h2>Programma</h2>'
        + tabella_programma(ev, prof)
        + "</section>"
        + '<section class="blocco" id="fotografie"><h2>Fotografie</h2>'
        + f'<div class="nota">{paragrafi(sez["foto_intro"])}</div>'
        + blocco_foto(ev, sez, prof)
        + "</section>"
        + blocco_social(ev)
        + piede(sez, prof)
    )
    return documento(ev["titolo"], descrizione, corpo)


def pagina():
    sez = carica_json(QUI / "sezione.json")
    for campo in ("introduzione", "scheda_intro", "archivio_intro", "foto_intro", "locandina_manca", "nessuna_foto"):
        if campo not in sez:
            errore(f"sezione.json: manca {campo}")
    if sez["locandina_manca"] != "locandina da aggiungere":
        errore("il testo della locandina mancante non è quello previsto")
    eventi = carica_eventi()
    if PAGINE.exists():
        shutil.rmtree(PAGINE)
    PAGINE.mkdir(parents=True)
    oggi = oggi_roma()
    CALENDARIO.write_text(pagina_calendario(sez, eventi, oggi), encoding="utf-8", newline="\n")
    for anno in sorted({ev["anno"] for ev in eventi}):
        del_anno = [ev for ev in eventi if ev["anno"] == anno]
        cartella = PAGINE / str(anno)
        cartella.mkdir(parents=True)
        (cartella / "index.html").write_text(pagina_anno(sez, anno, del_anno, oggi), encoding="utf-8", newline="\n")
        for ev in del_anno:
            dest = cartella / ev["slug"]
            dest.mkdir(parents=True)
            (dest / "index.html").write_text(pagina_scheda(sez, ev, oggi), encoding="utf-8", newline="\n")
    print(f"pagina: {CALENDARIO.name}, {len(eventi)} eventi, oggi {oggi.isoformat()} (Europe/Rome)")


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "pagina":
        pagina()
    else:
        errore(f"comando sconosciuto: {sys.argv[1]}")

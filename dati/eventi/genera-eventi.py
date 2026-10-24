#!/usr/bin/env python3
"""Genera la sezione Eventi: calendario, scheda per evento e archivio per anno.

Uso: python genera-eventi.py pagina

Legge sezione.json, domande.json e un file JSON per evento in schede/.
Scrive eventi.html (il calendario) e pagine/<anno>/index.html più
pagine/<anno>/<slug>/index.html. scripts/genera-sito.py copia il calendario
in site/eventi/, inietta barra, chat e suggerimenti, e pubblica le altre pagine
insieme alla cartella immagini/.

Il giorno «oggi», per dire se un evento è in corso, in arrivo o passato, è
quello di Europe/Rome nel momento della generazione.

Controlli: date e giorni della settimana coerenti; ogni racconto ha la firma
e cita momenti del programma; ogni foto è in immagini/ e ha il credito; le
lezioni citano una demo; le interviste usano solo le domande fisse e, se ci
sono, hanno la firma. Nessun testo contiene «da verificare» né il trattino
lungo. I campi senza materiale restano «da completare»: non si inventano.
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
HREF_QUADRANO = re.compile(
    r"^/(?:principi|colori|marche|soggetti|alberi|eventi)/[A-Za-z0-9./_-]*$"
)
ID_OK = re.compile(r"^[a-z0-9-]+$")
FILE_OK = re.compile(r"^[a-z0-9.-]+$")

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
table { width: 100%; border-collapse: collapse; font-size: .92em; }
th, td { border: 1px solid #d8d2c4; padding: 6px 8px; vertical-align: top; text-align: left; }
th { background: #eef4ef; color: #2c4f3a; }
th.giorno { background: #263529; color: #f7f2e7; }
caption { caption-side: bottom; text-align: left; font-size: .85em; color: #555; padding-top: 6px; }
.vuoto { color: #6b5e4c; font-style: italic; }
.manca { color: #6b3418; }
.coperto { color: #1e4638; font-weight: 600; }
.nota-riga { display: block; margin-top: 4px; color: #555; font-size: .92em; }
blockquote.racconto { margin: 10px 0; padding: 8px 14px; border-left: 4px solid #263529; background: #fffdf8; }
blockquote.racconto p { margin: 0; }
.firma { margin: 4px 0 10px; font-size: .95em; }
figure.foto { margin: 12px 0; }
figure.foto img { width: 100%; max-width: 28rem; height: auto; border-radius: 8px; border: 1px solid #dfd5c3; display: block; }
figure.foto figcaption { font-size: .9em; color: #444; margin-top: 6px; }
ol.domande { margin: 8px 0 12px; padding-left: 1.2em; }
ol.domande li { margin: 4px 0; }
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


def vuoto(sez):
    return f'<span class="vuoto">{e(sez["vuoto"])}</span>'


def radice(prof):
    return "../" * prof


def href_nel_sito(percorso, prof):
    if not HREF_QUADRANO.match(percorso.split("#", 1)[0]) and percorso != "/":
        errore(f"collegamento non ammesso: {percorso}")
    if percorso.startswith("/"):
        return radice(prof) + percorso.lstrip("/")
    return percorso


def carica_json(path):
    try:
        dati = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errore(f"{path.name} non è un JSON valido ({exc})")
    controlla_stringhe(dati, path.name)
    return dati


def stato_evento(ev, oggi):
    inizio = date.fromisoformat(ev["data_inizio"])
    fine = date.fromisoformat(ev["data_fine"])
    if inizio <= oggi <= fine:
        return "in_corso"
    if oggi < inizio:
        return "in_arrivo"
    return "passato"


def carica_eventi(domande):
    if not SCHEDE.is_dir():
        errore("manca la cartella schede/")
    eventi = []
    elenco_domande = domande["domande"]
    ids_domande = [d["id"] for d in elenco_domande]
    solo_strada = {d["id"] for d in elenco_domande if d.get("solo") == "per_strada"}
    for path in sorted(SCHEDE.glob("*.json")):
        ev = carica_json(path)
        for campo in ("id", "slug", "anno", "titolo", "sottotitolo", "data_inizio", "data_fine", "luogo", "fonte"):
            if campo not in ev:
                errore(f"{path.name}: manca {campo}")
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
        momenti = {}
        for m in ev.get("programma", []):
            for campo in ("id", "giorno", "fascia", "orario", "voce", "demo"):
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
            if m["demo"] and not m.get("chi"):
                errore(f"{ev['id']}: la demo {m['id']} non ha l'artista")
            momenti[m["id"]] = m
        for mid, lezione in ev.get("lezioni", {}).items():
            if mid not in momenti or not momenti[mid]["demo"]:
                errore(f"{ev['id']}: lezione su un momento che non è una demo ({mid})")
            for campo in ("testo", "fonte", "fonte_etichetta"):
                if not lezione.get(campo):
                    errore(f"{ev['id']}: lezione {mid} senza {campo}")
            if not lezione["fonte"].startswith("https://"):
                errore(f"{ev['id']}: fonte della lezione {mid} non https")
        for col in ev.get("collegamenti", {}):
            if col not in momenti or not momenti[col]["demo"]:
                errore(f"{ev['id']}: collegamenti su una demo inesistente ({col})")
            if not ev["collegamenti"][col]:
                errore(f"{ev['id']}: collegamenti vuoti in {col}; omettere la chiave")
            for c in ev["collegamenti"][col]:
                if not c.get("href") or not c.get("testo"):
                    errore(f"{ev['id']}: collegamento incompleto in {col}")
                href_nel_sito(c["href"], 1)
        for r in ev.get("racconti", []):
            for campo in ("id", "firma", "momenti", "testo", "fonte"):
                if not r.get(campo):
                    errore(f"{ev['id']}: racconto senza {campo}")
            if not ID_OK.match(r["id"]) or r["id"] in visti:
                errore(f"{ev['id']}: id racconto duplicato o non valido")
            visti.add(r["id"])
            if not r["fonte"].get("url", "").startswith("https://") or not r["fonte"].get("etichetta"):
                errore(f"{ev['id']}: fonte del racconto {r['id']} incompleta")
            for mid in r["momenti"]:
                if mid not in momenti:
                    errore(f"{ev['id']}: il racconto {r['id']} cita un momento inesistente")
            for foto in r.get("foto", []):
                for campo in ("file", "credito", "alt"):
                    if not foto.get(campo):
                        errore(f"{ev['id']}: foto del racconto {r['id']} senza {campo}")
                if not FILE_OK.match(foto["file"]) or not (IMMAGINI / foto["file"]).is_file():
                    errore(f"{ev['id']}: foto assente in immagini/{foto.get('file')}")
        for inter in ev.get("interviste", []):
            if not inter.get("firma") or not inter.get("id"):
                errore(f"{ev['id']}: intervista senza firma o senza id")
            if not isinstance(inter.get("nel_programma"), bool):
                errore(f"{ev['id']}: intervista {inter['id']} senza nel_programma vero o falso")
            if inter["id"] in visti or not ID_OK.match(inter["id"]):
                errore(f"{ev['id']}: id intervista duplicato o non valido")
            visti.add(inter["id"])
            per_strada = inter.get("per_strada", False)
            if not isinstance(per_strada, bool):
                errore(f"{ev['id']}: per_strada dell'intervista {inter['id']} non è vero o falso")
            risposte = inter.get("risposte", {})
            for chiave in risposte:
                if chiave not in ids_domande:
                    errore(f"{ev['id']}: risposta «{chiave}» fuori dalle domande fisse")
                if chiave in solo_strada and not per_strada:
                    errore(f"{ev['id']}: «{chiave}» vale solo per chi dipinge per strada")
            if inter.get("momento") and inter["momento"] not in momenti:
                errore(f"{ev['id']}: l'intervista cita un momento inesistente")
        ev["_path"] = path.name
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


def blocco_contributi(sez):
    return (
        '<section class="blocco" id="contributi">'
        "<h2>Contributi</h2>"
        f'<div class="nota">{paragrafi(sez["contributi"])}</div>'
        "</section>"
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
        archivio.append(
            f"<h3><a href=\"{anno}/\">{e(str(anno))}</a></h3><ul>{voci}</ul>"
        )
    corpo = (
        f"<h1>{e(sez['titolo'])}</h1>"
        f"<p class=\"sotto\">{e(sez['sottotitolo'])}</p>"
        + salti([
            ("in-corso", "In corso"),
            ("in-arrivo", "In arrivo"),
            ("passati", "Passati"),
            ("archivio", "Archivio"),
            ("contributi", "Contributi"),
        ])
        + f'<div class="intro">{paragrafi(sez["introduzione"])}</div>'
        + gruppo("in-corso", "in_corso", in_corso, oggi, 1, sez)
        + gruppo("in-arrivo", "in_arrivo", in_arrivo, oggi, 1, sez)
        + gruppo("passati", "passato", passati, oggi, 1, sez)
        + '<section class="blocco" id="archivio"><h2>Archivio per anno</h2>'
        + f'<div class="nota">{paragrafi(sez["archivio_intro"])}</div>'
        + ("".join(archivio) or f"<p>{vuoto(sez)}</p>")
        + "</section>"
        + blocco_contributi(sez)
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
        + salti([("elenco", "Eventi"), ("contributi", "Contributi")])
        + f'<div class="intro">{paragrafi(sez["archivio_intro"])}</div>'
        + f'<section class="blocco" id="elenco"><h2>Eventi del {anno}</h2>{cards}</section>'
        + blocco_contributi(sez)
        + piede(sez, 2)
    )
    return documento(f"Archivio {anno}", descrizione, corpo)


def copertura(momento, racconti, sez):
    suoi = [r for r in racconti if momento["id"] in r["momenti"]]
    if not suoi:
        return f'<span class="manca">{e(sez["manca_racconto"])}</span>. <a href="#contributi">Come si aggiunge</a>'
    link = ", ".join(f'<a href="#r-{e(r["id"])}">{e(r["firma"])}</a>' for r in suoi)
    return f'<span class="coperto">Coperto</span>: {link}'


def tabella_programma(ev, sez):
    righe = []
    gruppo = None
    for m in ev.get("programma", []):
        chiave = (m["giorno"], m["fascia"])
        if chiave != gruppo:
            gruppo = chiave
            d = date.fromisoformat(m["giorno"])
            titolo = f"{GIORNI[d.weekday()].capitalize()} {d.day} {MESI[d.month - 1]} {d.year}. {m['fascia'].capitalize()}"
            righe.append(f'<tr><th class="giorno" colspan="2">{e(titolo)}</th></tr>')
        nota = f'<span class="nota-riga">{e(m["nota"])}</span>' if m.get("nota") else ""
        righe.append(
            f'<tr id="m-{e(m["id"])}"><td>{e(m["voce"])}{nota}</td>'
            f"<td>{copertura(m, ev.get('racconti', []), sez)}</td></tr>"
        )
    if not righe:
        return f"<p>{vuoto(sez)}</p>"
    fonte = ev["fonte"]
    caption = (
        f'Fonte: <a href="{e(fonte["url"])}">{e(fonte["etichetta"])}</a>, '
        f'letto il {e(data_it(fonte["letto"]))}.'
    )
    return (
        '<div class="tab"><table>'
        "<thead><tr><th>Voce del programma</th><th>Racconto</th></tr></thead>"
        f"<tbody>{''.join(righe)}</tbody>"
        f"<caption>{caption}</caption></table></div>"
    )


def cella_lezione(lezione):
    if not lezione:
        return None
    return (
        f"{e(lezione['testo'])}. "
        f'<a href="{e(lezione["fonte"])}">{e(lezione["fonte_etichetta"])}</a>'
    )


def cella_collegamenti(ev, mid, prof, sez):
    lista = ev.get("collegamenti", {}).get(mid)
    if not lista:
        return vuoto(sez)
    parti = []
    for c in lista:
        parti.append(f'<a href="{e(href_nel_sito(c["href"], prof))}">{e(c["testo"])}</a>')
    return "<br>".join(parti)


def schede_demo(ev, sez, prof):
    demo = [m for m in ev.get("programma", []) if m["demo"]]
    if not demo:
        return f"<p>{vuoto(sez)}</p>"
    blocchi = []
    for m in demo:
        d = date.fromisoformat(m["giorno"])
        quando = (
            f"{GIORNI[d.weekday()].capitalize()} {d.day} {MESI[d.month - 1]} {d.year}, "
            f"{m['fascia']}. {m['orario']}."
        )
        lezione = cella_lezione(ev.get("lezioni", {}).get(m["id"])) or vuoto(sez)
        campi = [
            ("Artista", e(m["chi"])),
            ("Quando", e(quando)),
            ("Soggetto", campo_demo(ev, m["id"], "soggetto", sez)),
            ("Tecnica", campo_demo(ev, m["id"], "tecnica", sez)),
            ("Carte", campo_demo(ev, m["id"], "carte", sez)),
            ("Colori", campo_demo(ev, m["id"], "colori", sez)),
            ("Lezione", lezione),
            ("Collegamenti al Quaderno", cella_collegamenti(ev, m["id"], prof, sez)),
        ]
        righe = "".join(f"<tr><th>{e(nome)}</th><td>{valore}</td></tr>" for nome, valore in campi)
        blocchi.append(
            f'<article class="voce" id="demo-{e(m["id"])}">'
            f'<div class="tab"><table>'
            f'<thead><tr><th colspan="2">{e(m["chi"])}</th></tr></thead>'
            f"<tbody>{righe}</tbody>"
            f'<caption><a href="#m-{e(m["id"])}">Voce nel programma</a></caption>'
            "</table></div></article>"
        )
    return "".join(blocchi)


def blocco_racconti(ev, sez, prof):
    if not ev.get("racconti"):
        return f"<p>{vuoto(sez)}. Si può aggiungere un racconto firmato.</p>"
    pezzi = []
    for r in ev["racconti"]:
        momenti = []
        for mid in r["momenti"]:
            voce = next(m["voce"] for m in ev["programma"] if m["id"] == mid)
            momenti.append(f'<a href="#m-{e(mid)}">{e(voce)}</a>')
        foto = []
        for f in r.get("foto", []):
            src = radice(prof - 1) + "immagini/" + f["file"]
            foto.append(
                "<figure class=\"foto\">"
                f'<img src="{e(src)}" alt="{e(f["alt"])}">'
                f"<figcaption>{e(f['credito'])}</figcaption></figure>"
            )
        fonte = r["fonte"]
        pezzi.append(
            f'<article class="voce" id="r-{e(r["id"])}">'
            f"<h3>{e(r['firma'])}</h3>"
            f"<p>Momenti coperti: {', '.join(momenti)}.</p>"
            f'<blockquote class="racconto"><p>{e(r["testo"])}</p></blockquote>'
            f'<p class="firma">{e(r["firma"])}, '
            f'<a href="{e(fonte["url"])}">{e(fonte["etichetta"])}</a>.</p>'
            + "".join(foto)
            + "</article>"
        )
    return "".join(pezzi)


def voce_domanda(domanda, prof):
    testo = e(domanda["testo"])
    if domanda.get("rimando"):
        href = href_nel_sito(domanda["rimando"]["href"], prof)
        testo += f' Rimando: <a href="{e(href)}">{e(domanda["rimando"]["etichetta"])}</a>.'
    if domanda.get("solo") == "per_strada":
        testo += " Solo per chi dipinge per strada durante l'evento."
    return f"<li>{testo}</li>"


def cella_risposta(domanda, inter, sez, prof):
    """La domanda sui materiali, se ha una risposta, resta una citazione di chi parla."""
    if domanda.get("solo") == "per_strada" and not inter.get("per_strada"):
        return "Non si applica"
    testo = (inter.get("risposte") or {}).get(domanda["id"])
    if not testo:
        return vuoto(sez)
    if domanda.get("come_detta"):
        href = href_nel_sito(domanda["rimando"]["href"], prof)
        return (
            f"<q>{e(testo)}</q>"
            f'<span class="nota-riga">Come detto da {e(inter["firma"])}. '
            f'<a href="{e(href)}">{e(domanda["rimando"]["etichetta"])}</a>.</span>'
        )
    return e(testo)


def blocco_interviste(ev, sez, domande, prof):
    intro = f'<div class="nota">{paragrafi(sez["interviste_intro"])}</div>'
    elenco = "<ol class=\"domande\">" + "".join(voce_domanda(d, prof) for d in domande["domande"]) + "</ol>"
    if not ev.get("interviste"):
        return intro + elenco + f"<p>{e(sez['nessuna_intervista'])}</p>"
    testate = "".join(f"<th>{e(d['testo'])}</th>" for d in domande["domande"])
    righe = []
    for inter in ev["interviste"]:
        dove = "Nel programma" if inter["nel_programma"] else "Fuori programma"
        if inter.get("per_strada"):
            dove += '<span class="nota-riga">Dipinge per strada durante l\'evento.</span>'
        if inter.get("nota"):
            dove += f'<span class="nota-riga">{e(inter["nota"])}</span>'
        celle = "".join(f"<td>{cella_risposta(d, inter, sez, prof)}</td>" for d in domande["domande"])
        righe.append(
            f'<tr id="i-{e(inter["id"])}"><th>{e(inter["firma"])}</th><td>{dove}</td>{celle}</tr>'
        )
    tabella = (
        '<div class="tab"><table><thead><tr><th>Firma</th><th>Rispetto al programma</th>'
        f"{testate}</tr></thead><tbody>{''.join(righe)}</tbody></table></div>"
    )
    return intro + elenco + tabella


def frase_copertura(ev):
    totale = len(ev.get("programma", []))
    coperti = sum(1 for m in ev.get("programma", []) if any(m["id"] in r["momenti"] for r in ev.get("racconti", [])))
    if totale == 0:
        return "Il programma è da completare."
    return (
        f"I momenti coperti da almeno un racconto sono {coperti} su {totale}. "
        "Gli altri restano aperti: si può aggiungere un racconto firmato."
    )


def note_lezioni(ev):
    pezzi = []
    for m in ev.get("programma", []):
        lezione = ev.get("lezioni", {}).get(m["id"])
        if not lezione:
            continue
        d = date.fromisoformat(m["giorno"])
        quando = f"{d.day} {MESI[d.month - 1]} {d.year}"
        pezzi.append(
            f"<p>Dalla demo di {e(m['chi'])}, il {e(quando)}, la lezione segnata è: {e(lezione['testo'])}. "
            f'<a href="{e(lezione["fonte"])}">{e(lezione["fonte_etichetta"])}</a>.</p>'
        )
    return "".join(pezzi)


def campo_demo(ev, mid, nome, sez):
    """Soggetto, tecnica, carte e colori: se il dato c'è, porta una fonte https."""
    valore = ev.get("campi_demo", {}).get(mid, {}).get(nome)
    if not valore:
        return vuoto(sez)
    if not isinstance(valore, dict) or not valore.get("testo") or not str(valore.get("fonte", "")).startswith("https://"):
        errore(f"{ev['id']}: il campo {nome} di {mid} richiede testo e fonte https")
    etichetta = valore.get("fonte_etichetta") or "fonte"
    return f'{e(valore["testo"])}. <a href="{e(valore["fonte"])}">{e(etichetta)}</a>'


def pagina_scheda(sez, ev, oggi, domande):
    prof = 3
    st = stato_evento(ev, oggi)
    etichetta = {"in_corso": "L'evento è in corso", "in_arrivo": "L'evento è in arrivo", "passato": "L'evento è passato"}[st]
    fonte = ev["fonte"]
    quando = intervallo(ev["data_inizio"], ev["data_fine"])
    descrizione = f"{ev['titolo']}, {quando}, {ev['luogo']}."
    note = paragrafi(ev.get("note", []))
    lezioni = note_lezioni(ev)
    corpo = (
        f'<p class="filo"><a href="../../">Eventi</a> · <a href="../">Archivio {ev["anno"]}</a></p>'
        f"<h1>{e(ev['titolo'])}</h1>"
        f"<p class=\"sotto\">{e(ev['sottotitolo'])}</p>"
        + salti([
            ("programma", "Programma"),
            ("demo", "Demo"),
            ("io-cero", "Io c'ero"),
            ("interviste", "Interviste"),
            ("contributi", "Contributi"),
        ])
        + f'<div class="intro">{paragrafi(sez["scheda_intro"])}</div>'
        + "<p>"
        + f"{e(etichetta)}: {e(quando)}. {e(ev['luogo'])}.</p>"
        + (f"<div class=\"nota\">{note}</div>" if note else "")
        + "<p>"
        + f'Fonte del programma: <a href="{e(fonte["url"])}">{e(fonte["etichetta"])}</a>, '
        + f"letto il {e(data_it(fonte['letto']))}.</p>"
        + f"<p>{e(frase_copertura(ev))}</p>"
        + '<section class="blocco" id="programma"><h2>Programma</h2>'
        + tabella_programma(ev, sez)
        + "</section>"
        + '<section class="blocco" id="demo"><h2>Demo</h2>'
        + "<p>Per ogni demo restano visibili i campi ancora aperti, così si vede che cosa manca.</p>"
        + (f"<div class=\"nota\">{lezioni}</div>" if lezioni else "")
        + schede_demo(ev, sez, prof)
        + "</section>"
        + '<section class="blocco" id="io-cero"><h2>Racconti: io c\'ero</h2>'
        + "<p>Ogni racconto è firmato. Vale per i momenti indicati, non per tutto l'evento.</p>"
        + blocco_racconti(ev, sez, prof)
        + "</section>"
        + '<section class="blocco" id="interviste"><h2>Interviste</h2>'
        + blocco_interviste(ev, sez, domande, prof)
        + "</section>"
        + blocco_contributi(sez)
        + piede(sez, prof)
    )
    return documento(ev["titolo"], descrizione, corpo)


def pagina():
    sez = carica_json(QUI / "sezione.json")
    domande = carica_json(QUI / "domande.json")
    attese = [
        ("cominciato", "Come hai cominciato con l'acquerello?", None, None),
        ("materiali", "Che materiali usi: carta (marca e grammatura), pennelli e marche di colori, con la tavolozza?", "/marche/", None),
        ("consiglio", "Un consiglio per chi dipinge en plein air?", None, None),
        ("errore", "Un errore da evitare?", None, None),
        ("perche_qui", "Perché sei qui oggi?", None, "per_strada"),
    ]
    trovate = [
        (d["id"], d["testo"], (d.get("rimando") or {}).get("href"), d.get("solo"))
        for d in domande["domande"]
    ]
    if trovate != attese or not domande["domande"][1].get("come_detta"):
        errore("le domande fisse non coincidono con quelle previste")
    eventi = carica_eventi(domande)
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
            (dest / "index.html").write_text(pagina_scheda(sez, ev, oggi, domande), encoding="utf-8", newline="\n")
    print(f"pagina: {CALENDARIO.name}, {len(eventi)} eventi, oggi {oggi.isoformat()} (Europe/Rome)")


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "pagina":
        pagina()
    else:
        errore(f"comando sconosciuto: {sys.argv[1]}")

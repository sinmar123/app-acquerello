#!/usr/bin/env python3
"""Genera la sezione Opere: l'elenco degli autori e una sottosezione per autore.

Uso: python genera-opere.py pagina

Legge sezione.json e un file JSON per autore in autori/. Scrive opere.html
(l'elenco degli autori) e pagine/<id-autore>/index.html (le opere
dell'autore, dalla più recente). scripts/genera-sito.py copia l'elenco in
site/opere/, inietta barra, chat e suggerimenti, e pubblica le pagine degli
autori insieme alla cartella immagini/. Le foto si preparano con
prepara-foto.py.

Ogni autore è una sottosezione: il numero della sezione in sezione.json più
il suo «ordine», per esempio 6.1. La pagina dell'autore si apre con la frase
che la colloca fra le opere di non professionisti e con la sua presentazione.

Il titolo di ogni opera è la data in cui è stata dipinta, in una o più
sedute, con il giorno della settimana e, se nota, l'ora. Sotto il titolo
stanno il numero che l'autore ha dato al foglio, se c'è, la «nota» breve
dell'opera, se c'è, e «data della fotografia» quando la data non viene dal
foglio (data_da «foto» o «nome-file»).

Controlli: ogni autore ha un ordine intero diverso da quello degli altri;
ogni opera ha la foto in immagini/<id-autore>/, il testo alternativo,
l'origine della data e almeno una seduta, in ordine di data; ogni foto della
cartella è usata da un'opera; il giorno della settimana scritto sul foglio,
se trascritto, coincide con la data; l'ora è nel formato 21, 21-22 o 22.03;
una data presa dal foglio ha la trascrizione in «scritta»; una data della
fotografia vale per una sola seduta. Nessun testo contiene «da verificare»
né il trattino lungo.
"""
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

QUI = Path(__file__).resolve().parent
AUTORI = QUI / "autori"
IMMAGINI = QUI / "immagini"
PAGINE = QUI / "pagine"
ELENCO = QUI / "opere.html"
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
        "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
GIORNI = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
TRATTINI = ("—", "–", "―")
ID_OK = re.compile(r"^[a-z0-9-]+$")
FILE_OK = re.compile(r"^[a-z0-9-]+\.jpg$")
NUMERO_OK = re.compile(r"^\d+$")
ORA = r"([01]?\d|2[0-3])(\.[0-5]\d)?"
ORA_OK = re.compile(rf"^{ORA}(-{ORA})?$")
ORIGINI = ("foglio", "foto", "nome-file")

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
.intro { background: #eef4ef; border: 1px solid #cadbce; border-radius: 8px; padding: 10px 14px; margin: 12px 0 18px; }
.intro p { margin: 0 0 8px; }
.intro p:last-child { margin-bottom: 0; }
section.blocco { border-top: 3px solid #3d6b4f; padding-top: 14px; margin-top: 26px; }
.autore { display: flex; align-items: center; gap: 16px; background: #fffdf8; border: 1px solid #dfd5c3; border-radius: 12px;
          padding: 12px 14px; margin: 10px 0; }
.autore p { margin: 4px 0; }
.miniatura { flex: none; display: block; width: 132px; height: 132px; background: #f3eee4; border-radius: 8px; overflow: hidden; }
.miniatura img { width: 100%; height: 100%; object-fit: contain; display: block; }
.galleria { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; margin: 12px 0; }
figure.opera { margin: 0; background: #fffdf8; border: 1px solid #dfd5c3; border-radius: 12px; padding: 10px 10px 12px; }
.cornice { display: block; aspect-ratio: 1 / 1; background: #f3eee4; border-radius: 8px; overflow: hidden; }
.cornice img { width: 100%; height: 100%; object-fit: contain; display: block; }
figure.opera figcaption { margin-top: 8px; }
figure.opera h3 { font-size: 1em; margin: 0; }
figure.opera p { margin: 2px 0 0; font-size: .9em; color: #555; }
footer { margin-top: 28px; border-top: 1px solid #ddd; padding-top: 12px; font-size: .9em; color: #444; }
@media (max-width: 480px) {
  .autore { flex-direction: column; align-items: flex-start; }
}
"""


def e(testo):
    return html.escape(str(testo if testo is not None else ""), quote=True)


def errore(msg):
    raise SystemExit(f"opere: {msg}")


def data_it(iso):
    anno, mese, giorno = iso.split("-")
    return f"{int(giorno)}/{mese}/{anno}"


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


def carica_json(path):
    try:
        dati = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errore(f"{path.name} non è un JSON valido ({exc})")
    controlla_stringhe(dati, path.name)
    return dati


def controlla_opera(autore, op):
    dove = f"{autore['id']}/{op.get('file')}"
    for campo in ("file", "data_da", "sedute", "alt"):
        if not op.get(campo):
            errore(f"{dove}: manca {campo}")
    if not FILE_OK.match(op["file"]) or not (IMMAGINI / autore["id"] / op["file"]).is_file():
        errore(f"{dove}: foto assente in immagini/{autore['id']}/")
    if op["data_da"] not in ORIGINI:
        errore(f"{dove}: data_da deve essere uno fra {', '.join(ORIGINI)}")
    if "numero" in op and not NUMERO_OK.match(str(op["numero"])):
        errore(f"{dove}: numero del foglio non valido")
    if "nota" in op and (not isinstance(op["nota"], str) or not op["nota"].strip()):
        errore(f"{dove}: la nota deve essere un testo breve")
    if op["data_da"] == "foglio" and not op.get("scritta"):
        errore(f"{dove}: una data presa dal foglio vuole la trascrizione in «scritta»")
    if op["data_da"] != "foglio" and len(op["sedute"]) != 1:
        errore(f"{dove}: la data della fotografia vale per una sola seduta")
    precedente = ""
    for s in op["sedute"]:
        try:
            d = date.fromisoformat(s.get("giorno", ""))
        except ValueError:
            errore(f"{dove}: giorno non valido ({s.get('giorno')})")
        if s["giorno"] < precedente:
            errore(f"{dove}: le sedute non sono in ordine di data")
        precedente = s["giorno"]
        if "ora" in s and not ORA_OK.match(str(s["ora"])):
            errore(f"{dove}: ora non valida ({s['ora']})")
        scritto = s.get("giorno_scritto")
        if scritto and GIORNI[d.weekday()] != scritto.lower():
            errore(f"{dove}: il {data_it(s['giorno'])} non è un {scritto}")


def carica_autori():
    if not AUTORI.is_dir():
        errore("manca la cartella autori/")
    autori = []
    ordini = set()
    for path in sorted(AUTORI.glob("*.json")):
        autore = carica_json(path)
        for campo in ("id", "nome", "ordine", "opere"):
            if not autore.get(campo):
                errore(f"{path.name}: manca {campo}")
        if not ID_OK.match(autore["id"]) or path.stem != autore["id"]:
            errore(f"{path.name}: il nome del file deve essere <id>.json, con id in minuscolo e trattini")
        if not isinstance(autore["ordine"], int) or autore["ordine"] < 1 or autore["ordine"] in ordini:
            errore(f"{path.name}: «ordine» deve essere un intero da 1 in su, diverso da quello degli altri autori")
        ordini.add(autore["ordine"])
        visti = set()
        for op in autore["opere"]:
            controlla_opera(autore, op)
            if op["file"] in visti:
                errore(f"{autore['id']}: foto ripetuta ({op['file']})")
            visti.add(op["file"])
        cartella = IMMAGINI / autore["id"]
        avanzano = sorted(p.name for p in cartella.glob("*") if p.name not in visti)
        if avanzano:
            errore(f"{autore['id']}: foto senza opera in immagini/{autore['id']}/: {', '.join(avanzano)}")
        autore["opere"] = sorted(autore["opere"], key=chiave_opera, reverse=True)
        autori.append(autore)
    if not autori:
        errore("nessun autore in autori/")
    # nell'ordine delle sottosezioni: 6.1, 6.2...
    return sorted(autori, key=lambda a: a["ordine"])


def sottosezione(sez, autore):
    return f"{sez['numero']}.{autore['ordine']}"


def chiave_opera(op):
    """Data e ora dell'ultima seduta: le opere si ordinano dalla più recente."""
    s = op["sedute"][-1]
    inizio = str(s.get("ora") or "").split("-")[0]
    if inizio:
        ore, _, minuti = inizio.partition(".")
        inizio = f"{int(ore):02d}.{minuti or '00'}"
    return s["giorno"], inizio, op["file"]


def titolo_opera(op):
    parti = []
    for s in op["sedute"]:
        d = date.fromisoformat(s["giorno"])
        testo = f"{GIORNI[d.weekday()]} {d.day} {MESI[d.month - 1]} {d.year}"
        if s.get("ora"):
            testo += f", ore {s['ora']}"
        parti.append(testo)
    if len(parti) == 1:
        titolo = parti[0]
    else:
        unione = ", e " if op["sedute"][-2].get("ora") else " e "
        titolo = ", ".join(parti[:-1]) + unione + parti[-1]
    return titolo[0].upper() + titolo[1:]


def dettaglio_opera(op, sez):
    pezzi = []
    if op.get("numero"):
        pezzi.append(f"n. {op['numero']}")
    if op.get("nota"):
        pezzi.append(op["nota"])
    if op["data_da"] != "foglio":
        pezzi.append(sez["data_foto"])
    return " · ".join(pezzi)


def quante(autore):
    n = len(autore["opere"])
    anni = sorted(int(s["giorno"][:4]) for op in autore["opere"] for s in op["sedute"])
    periodo = f"nel {anni[0]}" if anni[0] == anni[-1] else f"dal {anni[0]} al {anni[-1]}"
    return f"{n} {'acquerello' if n == 1 else 'acquerelli'}, {periodo}"


def immagine(autore, op, prefisso, lazy=True):
    with Image.open(IMMAGINI / autore["id"] / op["file"]) as im:
        larghezza, altezza = im.size
    src = f"{prefisso}immagini/{autore['id']}/{op['file']}"
    carica = ' loading="lazy" decoding="async"' if lazy else ""
    return (f'<img src="{e(src)}" alt="{e(op["alt"])}" width="{larghezza}" height="{altezza}"{carica}>', src)


def paragrafi(frasi):
    return "".join(f"<p>{e(p)}</p>" for p in frasi)


def piede(sez, prefisso):
    return (
        "<footer>"
        f"<p>Quaderno di acquerello · Opere · testi del {e(data_it(sez['data']))}.</p>"
        f"<p>{e(sez['diritti'])}</p>"
        "<p>Le altre sezioni: "
        f'<a href="{prefisso}principi/">1. Principi generali</a> · '
        f'<a href="{prefisso}colori/">2. Teoria dei colori</a> · '
        f'<a href="{prefisso}marche/">3. Marche e tubetti</a> · '
        f'<a href="{prefisso}soggetti/">4. Soggetti</a> · '
        f'<a href="{prefisso}alberi/">4.1 Alberi</a> · '
        f'<a href="{prefisso}eventi/">5. Eventi</a>.</p>'
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


def pagina_elenco(sez, autori):
    schede = []
    for autore in autori:
        img, _ = immagine(autore, autore["opere"][0], "", lazy=False)
        schede.append(
            f'<article class="autore" id="autore-{e(autore["id"])}">'
            f'<a class="miniatura" href="{e(autore["id"])}/">{img}</a>'
            "<div>"
            f'<h3><a href="{e(autore["id"])}/">{e(sottosezione(sez, autore))} · {e(autore["nome"])}</a></h3>'
            f"<p>{e(quante(autore))}.</p>"
            f'<p><a href="{e(autore["id"])}/">Apri la sottosezione</a>.</p>'
            "</div></article>"
        )
    corpo = (
        f"<h1>{e(sez['titolo'])}</h1>"
        f'<p class="sotto">{e(sez["sottotitolo"])}</p>'
        f'<div class="intro">{paragrafi(sez["introduzione"])}</div>'
        f'<section class="blocco" id="autori"><h2>Autori</h2>{"".join(schede)}</section>'
        + piede(sez, "../")
    )
    return documento(sez["titolo"], sez["sottotitolo"], corpo)


def pagina_autore(sez, autore):
    figure = []
    for op in autore["opere"]:
        img, src = immagine(autore, op, "../")
        dettaglio = dettaglio_opera(op, sez)
        riga = f"<p>{e(dettaglio)}</p>" if dettaglio else ""
        ancora = "o-" + op["file"].removesuffix(".jpg")
        figure.append(
            f'<figure class="opera" id="{e(ancora)}">'
            f'<a class="cornice" href="{e(src)}">{img}</a>'
            f"<figcaption><h3>{e(titolo_opera(op))}</h3>{riga}</figcaption>"
            "</figure>"
        )
    presentazione = [autore["presentazione"]] if autore.get("presentazione") else []
    numero = sottosezione(sez, autore)
    descrizione = f"{autore['nome']}: {quante(autore)}. {sez['titolo']} nel Quaderno di acquerello."
    corpo = (
        f'<p class="filo"><a href="../">{e(sez["numero"])}. {e(sez["titolo"])}</a></p>'
        f"<h1>{e(numero)} · {e(autore['nome'])}</h1>"
        f'<p class="sotto">{e(quante(autore))}, dal più recente.</p>'
        f'<div class="intro">{paragrafi([sez["autore_apertura"]] + presentazione + sez["autore_intro"])}</div>'
        f'<section class="blocco" id="opere"><h2>Gli acquerelli</h2><div class="galleria">{"".join(figure)}</div></section>'
        + piede(sez, "../../")
    )
    return documento(f"{numero} · {autore['nome']} · {sez['titolo']}", descrizione, corpo)


def pagina():
    sez = carica_json(QUI / "sezione.json")
    for campo in ("data", "numero", "titolo", "sottotitolo", "introduzione", "autore_apertura", "autore_intro",
                  "data_foto", "diritti"):
        if not sez.get(campo):
            errore(f"sezione.json: manca {campo}")
    date.fromisoformat(sez["data"])
    autori = carica_autori()
    if PAGINE.exists():
        shutil.rmtree(PAGINE)
    PAGINE.mkdir(parents=True)
    ELENCO.write_text(pagina_elenco(sez, autori), encoding="utf-8", newline="\n")
    for autore in autori:
        cartella = PAGINE / autore["id"]
        cartella.mkdir(parents=True)
        (cartella / "index.html").write_text(pagina_autore(sez, autore), encoding="utf-8", newline="\n")
    totale = sum(len(a["opere"]) for a in autori)
    print(f"pagina: {ELENCO.name}, {len(autori)} autori, {totale} opere")


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "pagina":
        pagina()
    else:
        errore(f"comando sconosciuto: {sys.argv[1]}")

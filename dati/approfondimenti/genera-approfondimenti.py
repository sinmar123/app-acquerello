#!/usr/bin/env python3
"""Genera la sezione Approfondimenti: l'elenco delle questioni e una pagina per questione.

Uso: python genera-approfondimenti.py pagina

Legge sezione.json e un file JSON per questione in temi/. Scrive
approfondimenti.html (l'elenco) e pagine/<id>/index.html (la pagina della
questione). scripts/genera-sito.py copia l'elenco in site/approfondimenti/,
inietta barra, chat e suggerimenti e pubblica le pagine delle questioni in
site/approfondimenti/<id>/.

Ogni questione è una sottosezione: il numero della sezione in sezione.json più
il suo «ordine», per esempio 5.1. La pagina si apre con la sintesi, i cui punti
rimandano ai capitoli, e la premessa. Il campo facoltativo «nota_metodo», un
elenco di paragrafi, aggiunge un riquadro «Nota di metodo» dopo la premessa.
Seguono i capitoli, con le fonti numerate in fondo a ognuno come nei Principi
generali (scripts/rimandi_fonti.py).

Blocchi dei capitoli: «p» (paragrafo), «lista» (con «numerata» per l'elenco
numerato), «tabella» (intestazione e righe, con la colonna delle fonti),
«titoletto» e «nota», che è una frase di metodo senza fonte.

Controlli: ogni paragrafo, voce e riga di tabella ha almeno una fonte; ogni
fonte citata esiste e ogni fonte del file è citata; i punti della sintesi
rimandano a capitoli esistenti; ogni questione ha un ordine intero diverso da
quello delle altre e un id uguale al nome del file. Nessun testo contiene «da
verificare» né il trattino lungo.

Le pagine dei produttori si possono citare fra le fonti, col loro nome; nel
testo le marche non compaiono (CONTRIBUTING.md § 3). CC, 29/10/2026.
"""
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

QUI = Path(__file__).resolve().parent
TEMI = QUI / "temi"
PAGINE = QUI / "pagine"
ELENCO = QUI / "approfondimenti.html"
sys.path.insert(0, str(QUI.parent.parent / "scripts"))
import rimandi_fonti  # noqa: E402

TRATTINI = ("—", "–", "―")
ID_OK = re.compile(r"^[a-z0-9-]+$")
TIPI = ("p", "lista", "tabella", "titoletto", "nota")

CSS = """
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 52px; }
body { margin: 0 auto; max-width: 760px; padding: 0 14px 40px; font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
       font-size: 17px; line-height: 1.5; color: #1f1f1f; background: #fbfaf7; }
h1 { font-size: 1.45em; line-height: 1.25; margin: 18px 0 4px; color: #2c4f3a; }
h2 { font-size: 1.3em; margin: 0 0 6px; color: #2c4f3a; }
h3 { font-size: 1.08em; margin: 18px 0 6px; color: #2c4f3a; }
a { color: #2c6a4a; }
.sotto { color: #444; margin: 0 0 10px; }
.filo { font-size: .92em; margin: 0 0 4px; }
.filo a { font-weight: 600; text-decoration: none; }
nav.salti { position: sticky; top: 0; z-index: 5; display: flex; gap: 6px; overflow-x: auto; padding: 8px 0;
            background: #fbfaf7; border-bottom: 1px solid #e3e0d8; }
nav.salti a { flex: none; text-decoration: none; color: #2c4f3a; border: 1px solid #3d6b4f; border-radius: 16px;
              padding: 3px 12px; font-weight: 600; }
.sintesi { background: #f6f3eb; border: 1px solid #dfd8c8; border-left: 4px solid #8c4a27; border-radius: 8px;
           padding: 10px 14px; margin: 14px 0; }
.sintesi h2, .intro h2, .metodo h2 { font-size: 1.08em; margin: 0 0 6px; }
.sintesi ul { margin: 0; padding-left: 20px; } .sintesi li { margin-bottom: 6px; }
.sintesi a.al-cap { font-size: .85em; white-space: nowrap; text-decoration: none; }
.intro { background: #eef4ef; border: 1px solid #cadbce; border-radius: 8px; padding: 10px 14px; margin: 12px 0; }
.metodo { background: #f1f3f6; border: 1px solid #cdd6df; border-radius: 8px; padding: 10px 14px; margin: 12px 0; }
.intro p, .metodo p { margin: 6px 0; }
section.cap { border-top: 3px solid #3d6b4f; padding-top: 14px; margin-top: 26px; }
.voci { padding-left: 22px; } .voci li { margin-bottom: 6px; }
p.nota { font-style: italic; color: #444; }
.tab { overflow-x: auto; }
table.riass { width: 100%; border-collapse: collapse; font-size: .9em; margin: 10px 0; }
table.riass th, table.riass td { border: 1px solid #d8d2c4; padding: 6px 7px; vertical-align: top; text-align: left; }
table.riass th { background: #eef4ef; color: #2c4f3a; }
table.riass td:first-child { font-weight: 600; width: 22%; }
@media (max-width: 480px) { table.riass { font-size: .84em; } table.riass th, table.riass td { padding: 5px; } }
section.blocco { border-top: 3px solid #3d6b4f; padding-top: 14px; margin-top: 26px; }
.tema { background: #fffdf8; border: 1px solid #dfd5c3; border-radius: 12px; padding: 12px 14px; margin: 10px 0; }
.tema h3 { margin: 0 0 4px; }
.tema p { margin: 4px 0; }
footer { margin-top: 30px; font-size: .85em; color: #555; border-top: 1px solid #e3e0d8; padding-top: 10px; }
footer p { margin: 4px 0; }
""" + rimandi_fonti.CSS


def e(testo):
    return html.escape(str(testo if testo is not None else ""), quote=True)


def errore(msg):
    raise SystemExit(f"approfondimenti: {msg}")


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


def carica_temi():
    if not TEMI.is_dir():
        errore("manca la cartella temi/")
    temi, ordini = [], set()
    for path in sorted(TEMI.glob("*.json")):
        tema = carica_json(path)
        for campo in ("id", "ordine", "data", "titolo", "sottotitolo", "scheda", "sintesi", "premessa", "capitoli", "fonti"):
            if not tema.get(campo):
                errore(f"{path.name}: manca {campo}")
        if not ID_OK.match(tema["id"]) or path.stem != tema["id"]:
            errore(f"{path.name}: il nome del file deve essere <id>.json, con id in minuscolo e trattini")
        if not isinstance(tema["ordine"], int) or tema["ordine"] < 1 or tema["ordine"] in ordini:
            errore(f"{path.name}: «ordine» deve essere un intero da 1 in su, diverso da quello delle altre questioni")
        ordini.add(tema["ordine"])
        date.fromisoformat(tema["data"])
        id_capitoli = [c["id"] for c in tema["capitoli"]]
        if len(set(id_capitoli)) != len(id_capitoli):
            errore(f"{path.name}: due capitoli con lo stesso id")
        for punto in tema["sintesi"]:
            if punto.get("capitolo") not in id_capitoli:
                errore(f"{path.name}: un punto della sintesi rimanda a un capitolo che non c'è ({punto.get('capitolo')})")
        temi.append(tema)
    if not temi:
        errore("nessuna questione in temi/")
    return sorted(temi, key=lambda t: t["ordine"])


def numero_tema(sez, tema):
    return f"{sez['numero']}.{tema['ordine']}"


def piede(sez, prefisso):
    return (
        "<footer>"
        f"<p>Quaderno di acquerello · Approfondimenti · testi del {e(data_it(sez['data']))}.</p>"
        "<p>Le altre sezioni: "
        f'<a href="{prefisso}principi/">1. Principi generali</a> · '
        f'<a href="{prefisso}colori/">2. Teoria dei colori</a> · '
        f'<a href="{prefisso}marche/">3. Marche e tubetti</a> · '
        f'<a href="{prefisso}soggetti/">4. Soggetti</a> · '
        f'<a href="{prefisso}eventi/">6. Eventi</a> · '
        f'<a href="{prefisso}opere/">7. Opere di non professionisti</a>.</p>'
        "</footer>"
    )


def documento(titolo, descrizione, corpo, script=""):
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titolo)}</title>
<meta name="description" content="{e(descrizione)}">
<style>{CSS}</style></head>
<body>
{corpo}
{script}
</body></html>
"""


def blocco(b, c, F, dove):
    """Un blocco di capitolo in html. I testi dei paragrafi e delle voci possono contenere grassetti, corsivi e
    collegamenti, come nei Principi; le celle delle tabelle sono testo semplice."""
    tipo = b.get("tipo")
    if tipo not in TIPI:
        errore(f"blocco di tipo sconosciuto in {dove}")
    if tipo == "p":
        return f'<p>{b["testo"]}{F.rif(b.get("fonti"), dove)}</p>'
    if tipo == "nota":
        return f'<p class="nota">{b["testo"]}</p>'
    if tipo == "titoletto":
        return f'<h3 id="{e(c["id"])}-{e(b["id"])}">{e(b["testo"])}</h3>'
    if tipo == "lista":
        voci = "".join(f'<li>{v["testo"]}{F.rif(v.get("fonti"), f"{dove}, voce {j + 1}")}</li>'
                       for j, v in enumerate(b["voci"]))
        tag = "ol" if b.get("numerata") else "ul"
        return f'<{tag} class="voci">{voci}</{tag}>'
    testa = "".join(f"<th>{e(x)}</th>" for x in b["intestazione"]) + "<th>Fonti</th>"
    righe = []
    for j, r in enumerate(b["righe"]):
        if len(r["celle"]) != len(b["intestazione"]):
            errore(f"{dove}, riga {j + 1}: il numero delle celle non è quello dell'intestazione")
        celle = "".join(f"<td>{e(x)}</td>" for x in r["celle"])
        righe.append(f'<tr>{celle}<td>{F.rif(r.get("fonti"), f"{dove}, riga {j + 1}")}</td></tr>')
    return f'<div class="tab"><table class="riass"><tr>{testa}</tr>{"".join(righe)}</table></div>'


def pagina_tema(sez, tema):
    capitoli, citate = [], set()
    numeri = {c["id"]: c["titolo"].split(".")[0] for c in tema["capitoli"]}
    for c in tema["capitoli"]:
        F = rimandi_fonti.Capitolo(c["id"], tema["fonti"], f"approfondimenti, {tema['id']}")
        corpo = [f'<section class="cap" id="{e(c["id"])}"><h2>{e(c["titolo"])}</h2>']
        for i, b in enumerate(c["blocchi"]):
            corpo.append(blocco(b, c, F, f'{tema["id"]}, {c["id"]}, blocco {i + 1}'))
        corpo.append(F.elenco())
        corpo.append("</section>")
        capitoli.append("\n".join(corpo))
        citate.update(F.ordine)
    mancano = [k for k in tema["fonti"] if k not in citate]
    if mancano:
        errore(f"{tema['id']}: fonti mai citate: {', '.join(mancano)}")
    salti = "".join(f'<a href="#{e(c["id"])}">{e(c["breve"])}</a>' for c in tema["capitoli"])
    sintesi = "".join(f'<li>{p["testo"]} <a class="al-cap" href="#{e(p["capitolo"])}">capitolo {e(numeri[p["capitolo"]])}</a></li>'
                      for p in tema["sintesi"])
    premessa = "".join(f"<p>{p}</p>" for p in tema["premessa"])
    nota_metodo = ""
    if tema.get("nota_metodo"):
        paragrafi = "".join(f"<p>{e(p)}</p>" for p in tema["nota_metodo"])
        nota_metodo = f'<div class="metodo"><h2>Nota di metodo</h2>{paragrafi}</div>'
    numero = numero_tema(sez, tema)
    corpo = (
        f'<p class="filo"><a href="../">{e(sez["numero"])}. {e(sez["titolo"])}</a></p>'
        f'<header class="testa"><h1>{e(numero)} · {e(tema["titolo"])}</h1>'
        f'<p class="sotto">{e(tema["sottotitolo"])}</p></header>'
        f'<nav class="salti">{salti}</nav>'
        f'<div class="sintesi"><h2>In sintesi</h2><ul>{sintesi}</ul></div>'
        f'<div class="intro"><h2>Premessa</h2>{premessa}</div>'
        + nota_metodo
        + "\n".join(capitoli)
        + piede(sez, "../../")
    )
    titolo = f"{numero} · {tema['titolo']} · {sez['titolo']}"
    return documento(titolo, tema["sottotitolo"], corpo, rimandi_fonti.JS), len(citate)


def pagina_elenco(sez, temi):
    schede = []
    for tema in temi:
        schede.append(
            f'<article class="tema" id="tema-{e(tema["id"])}">'
            f'<h3><a href="{e(tema["id"])}/">{e(numero_tema(sez, tema))} · {e(tema["titolo"])}</a></h3>'
            f"<p>{e(tema['scheda'])}.</p>"
            f'<p><a href="{e(tema["id"])}/">{e(sez["leggi"])}</a></p>'
            "</article>"
        )
    corpo = (
        f"<h1>{e(sez['titolo'])}</h1>"
        f'<p class="sotto">{e(sez["sottotitolo"])}</p>'
        f'<div class="intro">{"".join(f"<p>{e(p)}</p>" for p in sez["introduzione"])}</div>'
        f'<section class="blocco" id="questioni"><h2>{e(sez["elenco_titolo"])}</h2>{"".join(schede)}</section>'
        + piede(sez, "../")
    )
    return documento(sez["titolo"], sez["sottotitolo"], corpo)


def pagina():
    sez = carica_json(QUI / "sezione.json")
    for campo in ("data", "numero", "titolo", "sottotitolo", "introduzione", "elenco_titolo", "leggi"):
        if not sez.get(campo):
            errore(f"sezione.json: manca {campo}")
    date.fromisoformat(sez["data"])
    temi = carica_temi()
    if PAGINE.exists():
        shutil.rmtree(PAGINE)
    PAGINE.mkdir(parents=True)
    ELENCO.write_text(pagina_elenco(sez, temi), encoding="utf-8", newline="\n")
    for tema in temi:
        cartella = PAGINE / tema["id"]
        cartella.mkdir(parents=True)
        testo, n_fonti = pagina_tema(sez, tema)
        (cartella / "index.html").write_text(testo, encoding="utf-8", newline="\n")
        print(f"pagina: {tema['id']}, {len(tema['capitoli'])} capitoli, {n_fonti} fonti")
    print(f"pagina: {ELENCO.name}, {len(temi)} question{'e' if len(temi) == 1 else 'i'}")


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "pagina":
        pagina()
    else:
        errore(f"comando sconosciuto: {sys.argv[1]}")

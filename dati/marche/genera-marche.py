#!/usr/bin/env python3
"""Genera la pagina della sezione «Marche e tubetti» del Quaderno di acquerello.

Uso: python genera-marche.py pagina

Legge marche.json e i sei colori proposti da ../colori/tavolozza.json e scrive marche.html accanto a sé.
scripts/genera-sito.py la copia in site/marche/index.html.
Controlli: ogni riga ha un colore della tavolozza, una fonte ufficiale (link) e la data di controllo;
ogni serie copre tutti e sei i colori; i rimandi dei capitoli puntano a serie esistenti; nessun testo
contiene «da verificare». GBOT-app-acquerello, 18/10/2026."""
import html
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = pathlib.Path(__file__).resolve().parent
USCITA = QUI / "marche.html"
TAVOLOZZA = QUI.parent / "colori" / "tavolozza.json"


def e(testo):
    return html.escape(str(testo), quote=True)


def errore(msg):
    raise SystemExit(f"marche: {msg}")


def controlla_testo(t, dove):
    if "da verificare" in t.lower():
        errore(f"testo «da verificare» in {dove}: resta fuori dalla pagina")


def data_it(d):
    return "/".join(reversed(d.split("-")))


def controlla(d, colori):
    ids = [m["id"] for m in d["marche"]]
    if len(set(ids)) != len(ids):
        errore("id di serie ripetuto")
    for m in d["marche"]:
        if not m.get("fonte_generale", "").startswith("http"):
            errore(f"{m['id']}: manca la fonte generale")
        visti = set()
        for i, r in enumerate(m["righe"], 1):
            dove = f"{m['id']}, riga {i}"
            if r.get("colore") not in colori:
                errore(f"{dove}: colore «{r.get('colore')}» non è nella tavolozza")
            visti.add(r["colore"])
            if not str(r.get("fonte", "")).startswith("http"):
                errore(f"{dove}: manca la fonte ufficiale")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(r.get("controllato", ""))):
                errore(f"{dove}: manca la data di controllo")
            if "assente" in r:
                controlla_testo(r["assente"], dove)
                continue
            for k in ("nome_commerciale", "pigmenti", "trasparenza"):
                if not r.get(k):
                    errore(f"{dove}: manca {k}")
            if not (r.get("numero") or r.get("sku")):
                errore(f"{dove}: manca numero o SKU")
            if r["trasparenza"] not in d["trasparenza"]:
                errore(f"{dove}: trasparenza «{r['trasparenza']}» sconosciuta")
            controlla_testo(r.get("nota", ""), dove)
        if visti != set(colori):
            errore(f"{m['id']}: mancano i colori {', '.join(sorted(set(colori) - visti))}")
    for cap in ("stesso_nome", "etichetta"):
        for i, v in enumerate(d[cap], 1):
            controlla_testo(v["testo"], f"{cap}, voce {i}")
            if not v.get("marche"):
                errore(f"{cap}, voce {i}: senza fonte")
            for k in v["marche"]:
                if k not in ids:
                    errore(f"{cap}, voce {i}: serie «{k}» inesistente")
    for p in d["introduzione"] + [d["criterio"], d["nota_trasparenza"]]:
        controlla_testo(p, "apertura")


CSS = """
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 52px; }
body { margin: 0 auto; max-width: 760px; padding: 0 14px 40px; font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
       font-size: 17px; line-height: 1.45; color: #1f1f1f; background: #fbfaf7; }
h1 { font-size: 1.45em; line-height: 1.2; margin: 18px 0 4px; color: #2c4f3a; }
h2 { font-size: 1.3em; margin: 0 0 6px; color: #2c4f3a; }
a { color: #2c6a4a; }
.sotto { color: #444; margin: 0 0 10px; }
nav.salti { position: sticky; top: 0; z-index: 5; display: flex; gap: 6px; overflow-x: auto; padding: 8px 0;
            background: #fbfaf7; border-bottom: 1px solid #e3e0d8; }
nav.salti a { flex: none; text-decoration: none; color: #2c4f3a; border: 1px solid #3d6b4f; border-radius: 16px;
              padding: 3px 12px; font-weight: 600; }
.intro { background: #eef4ef; border: 1px solid #cadbce; border-radius: 8px; padding: 10px 12px; margin: 12px 0; }
.intro p { margin: 4px 0; }
section.cap { border-top: 3px solid #3d6b4f; padding-top: 14px; margin-top: 26px; }
.nota-serie { color: #444; font-size: .92em; margin: 0 0 8px; }
.tab { overflow-x: auto; }
table.tub { width: 100%; border-collapse: collapse; font-size: .86em; }
table.tub th, table.tub td { border: 1px solid #d8d2c4; padding: 5px 6px; vertical-align: top; text-align: left; }
table.tub th { background: #eef4ef; color: #2c4f3a; }
table.tub td.pig { font-weight: 700; white-space: nowrap; }
table.tub .var { display: block; font-size: .85em; color: #6b5e4c; }
table.tub .nota { display: block; font-size: .88em; color: #555; margin-top: 3px; }
table.tub td.assente { color: #555; font-style: italic; }
.fonte { font-size: .85em; white-space: nowrap; } .fonte small { color: #777; }
.gran { display: inline-block; font-size: .78em; background: #e6e1f2; color: #3c3470; border-radius: 8px; padding: 0 6px; margin-left: 4px; }
ul.voci { padding-left: 20px; } ul.voci li { margin-bottom: 8px; }
sup.rif { font-size: .7em; color: #555; } sup.rif a { text-decoration: none; }
.legenda { font-size: .85em; color: #555; background: #f1efe8; border-radius: 8px; padding: 7px 10px; }
ol.fonti { font-size: .85em; color: #444; padding-left: 26px; overflow-wrap: anywhere; } ol.fonti li { margin-bottom: 5px; }
footer { margin-top: 30px; font-size: .8em; color: #666; border-top: 1px solid #e3e0d8; padding-top: 10px; }
"""


def pagina():
    d = json.loads((QUI / "marche.json").read_text(encoding="utf-8"))
    tav = json.loads(TAVOLOZZA.read_text(encoding="utf-8"))["colori"]
    colori = {c["id"]: c for c in tav}
    ordine = [c["id"] for c in tav]
    controlla(d, colori)
    titoli = {m["id"]: f'{m["marca"]} {m["serie"]}' if m["serie"] != m["marca"] and not m["serie"].startswith(m["marca"])
              else m["serie"] for m in d["marche"]}

    def rimandi(chiavi):
        return '<sup class="rif">[' + ", ".join(f'<a href="#{k}">{e(titoli[k])}</a>' for k in chiavi) + "]</sup>"

    sezioni = []
    for m in d["marche"]:
        righe = []
        for cid in ordine:
            for r in [r for r in m["righe"] if r["colore"] == cid]:
                c = colori[cid]
                var = f'<span class="var">{e(r["variante"])}</span>' if r.get("variante") else ""
                col = f'<td>{e(c["nome"])} ({e(c["pigmento"])}){var}</td>'
                fonte = (f'<td class="fonte"><a href="{e(r["fonte"])}" target="_blank" rel="noopener">pagina ufficiale</a>'
                         f'<br><small>controllata il {e(data_it(r["controllato"]))}</small></td>')
                if "assente" in r:
                    righe.append(f'<tr>{col}<td class="assente" colspan="4">{e(r["assente"])}</td>{fonte}</tr>')
                    continue
                gran = '<span class="gran">granulante</span>' if r.get("granulante") else ""
                nota = f'<span class="nota">{e(r["nota"])}</span>' if r.get("nota") else ""
                num = e(r.get("numero") or r.get("sku"))
                righe.append(f'<tr>{col}<td><b>{e(r["nome_commerciale"])}</b>{nota}</td><td>{num}</td>'
                             f'<td class="pig">{e(r["pigmenti"])}</td><td>{e(d["trasparenza"][r["trasparenza"]])}{gran}</td>{fonte}</tr>')
        n_tit = "SKU" if any(r.get("sku") for r in m["righe"]) else "N."
        nota = f'<p class="nota-serie">{e(m["nota"])}</p>' if m.get("nota") else ""
        sezioni.append(
            f'<section class="cap" id="{e(m["id"])}"><h2>{e(titoli[m["id"]])}</h2>{nota}'
            f'<div class="tab"><table class="tub"><tr><th>Colore proposto</th><th>Tubetto</th><th>{n_tit}</th>'
            f'<th>Pigmenti</th><th>Trasparenza</th><th>Fonte</th></tr>{"".join(righe)}</table></div>'
            f'<p class="nota-serie"><a href="{e(m["fonte_generale"])}" target="_blank" '
            f'rel="noopener">Tabella generale della serie</a> sul sito del produttore.</p></section>')
    stesso = "".join(f'<li>{v["testo"]}{rimandi(v["marche"])}</li>' for v in d["stesso_nome"])
    etich = "".join(f'<li>{v["testo"]}{rimandi(v["marche"])}</li>' for v in d["etichetta"])
    salti = ('<a href="#apertura">Apertura</a>' + "".join(f'<a href="#{e(m["id"])}">{e(titoli[m["id"]])}</a>' for m in d["marche"])
             + '<a href="#stesso-nome">Stesso nome</a><a href="#etichetta">L\'etichetta</a><a href="#fonti">Fonti</a>')
    fonti = "".join(f'<li>{e(titoli[m["id"]])}: <a href="{e(m["fonte_generale"])}" target="_blank" rel="noopener">'
                    f'{e(m["fonte_generale"])}</a></li>' for m in d["marche"])
    fonti += (f'<li>Video «Best Brand to Fill Watercolour Pans», per la scelta delle marche: <a href="{e(d["criterio_fonte"])}" '
              f'target="_blank" rel="noopener">{e(d["criterio_fonte"])}</a></li>')
    intro = "".join(f"<p>{e(p)}</p>" for p in d["introduzione"])
    pagina_html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(d['titolo'])}</title>
<style>{CSS}</style>
</head>
<body>
<header class="testa"><h1>{e(d['titolo'])}</h1>
<p class="sotto">{e(d['sottotitolo'])}</p></header>
<nav class="salti">{salti}</nav>
<div class="intro" id="apertura">{intro}
<p>{e(d['criterio'])} <a href="{e(d['criterio_fonte'])}" target="_blank" rel="noopener">Il video su YouTube ↗</a></p></div>
<p class="legenda">{e(d['nota_trasparenza'])} I nomi comuni e i pigmenti dei sei colori proposti sono quelli della sezione
<a href="../colori/#tavolozza">Teoria dei colori</a>.</p>
{chr(10).join(sezioni)}
<section class="cap" id="stesso-nome"><h2>Stesso nome, pigmenti diversi</h2>
<p>Esempi presi dalle tabelle qui sopra; tra parentesi quadre le serie da cui vengono.</p><ul class="voci">{stesso}</ul></section>
<section class="cap" id="etichetta"><h2>Cosa guardare sull'etichetta</h2>
<p>Le voci che le pagine ufficiali usate qui riportano:</p><ul class="voci">{etich}</ul></section>
<section class="cap" id="fonti"><h2>Fonti</h2>
<p>Ogni riga delle tabelle ha il link alla pagina ufficiale del tubetto e la data di controllo. Le tabelle generali:</p>
<ol class="fonti">{fonti}</ol></section>
<footer>Quaderno di acquerello · Marche e tubetti · testi del {e(data_it(d['data']))}.</footer>
</body>
</html>
"""
    USCITA.write_text(pagina_html, encoding="utf-8")
    n = sum(len(m["righe"]) for m in d["marche"])
    print(f"pagina: {USCITA} {USCITA.stat().st_size / 1024:.0f} KB, {len(d['marche'])} serie, {n} righe")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "pagina":
        print(__doc__)
        sys.exit(1)
    pagina()

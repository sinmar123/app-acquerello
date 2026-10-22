#!/usr/bin/env python3
"""Genera la pagina della sezione «Principi generali» del Quaderno di acquerello.

Uso: python genera-principi.py pagina

Legge i testi e le fonti da principi.json e scrive principi.html accanto a sé, una pagina sola con
tutto dentro. scripts/genera-sito.py la copia in site/principi/index.html. Le fonti sono elencate in
fondo a ogni capitolo, numerate da 1 in ogni capitolo (scripts/rimandi_fonti.py).
Controlli: ogni frase ha almeno una fonte, ogni fonte citata esiste, ogni fonte del json è citata,
nessun testo contiene «da verificare». GBOT-app-acquerello, 18/10/2026; fonti per capitolo CC, 21/10/2026.
L'ultimo capitolo, «In studio e all'aperto», viene dalla sezione Studio ed en plein air (22/10/2026): il blocco
«tavolozza_ridotta» legge i sei colori e le 12 miscele M1-M12 da dati/alberi/pit-261014-video-gesti-alberi.json
e si ferma se un colore non coincide con dati/colori/tavolozza.json."""
import html
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = pathlib.Path(__file__).resolve().parent
USCITA = QUI / "principi.html"
FONTE_ALBERI = QUI.parent / "alberi" / "pit-261014-video-gesti-alberi.json"
FONTE_TAVOLOZZA = QUI.parent / "colori" / "tavolozza.json"
sys.path.insert(0, str(QUI.parent.parent / "scripts"))
import rimandi_fonti  # noqa: E402


def e(testo):
    return html.escape(str(testo), quote=True)


def svg_consistenze():
    """Tre campioni indicativi dello stesso blu a tre diluizioni: uno schema, non una misura."""
    campioni = [("tè", "più acqua che pigmento", 0.22), ("latte", "acqua e pigmento in equilibrio", 0.55),
                ("miele", "più pigmento che acqua", 0.92)]
    pezzi = []
    for i, (nome, sotto, alfa) in enumerate(campioni):
        x = 10 + i * 230
        pezzi.append(f'<rect x="{x}" y="10" width="210" height="80" rx="10" fill="#FBF8F0" stroke="#d8d2c4"/>'
                     f'<rect x="{x + 12}" y="22" width="186" height="56" rx="8" fill="#283A9E" fill-opacity="{alfa}"/>'
                     f'<text x="{x + 105}" y="112" text-anchor="middle" class="t1">{e(nome)}</text>'
                     f'<text x="{x + 105}" y="132" text-anchor="middle" class="t2">{e(sotto)}</text>')
    return ('<figure class="schema"><svg viewBox="0 0 700 142" role="img" aria-label="Tè, latte e miele: tre consistenze dello stesso colore">'
            + "".join(pezzi) + '</svg><figcaption>Schema indicativo: lo stesso blu al tè, al latte e al miele. '
            'Non è una misura: le consistenze si provano su carta.</figcaption></figure>')


def svg_carta():
    """Scala dell'umidità della carta, da bagnata ad asciutta, con il lucido che si spegne."""
    stati = [("bagnata", "lucida", "tè o latte", 0.85), ("lucido che sparisce", "il riflesso si spegne", "più denso", 0.45),
             ("umida, opaca", "niente riflesso", "miele", 0.0), ("quasi asciutta", "", "pennello quasi asciutto", 0.0),
             ("asciutta", "", "qualsiasi", 0.0)]
    fondo = ["#cfdbe6", "#dbe3ea", "#e6e9ea", "#efeee9", "#FBF8F0"]
    pezzi = ['<defs><linearGradient id="luce" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             '<stop offset=".5" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>']
    for i, (nome, aspetto, colore, lucido) in enumerate(stati):
        x = 6 + i * 138
        pezzi.append(f'<rect x="{x}" y="8" width="128" height="70" rx="8" fill="{fondo[i]}" stroke="#c9d8cd"/>')
        if lucido:
            pezzi.append(f'<rect x="{x + 8}" y="16" width="112" height="54" rx="6" fill="url(#luce)" fill-opacity="{lucido}"/>')
        pezzi.append(f'<text x="{x + 64}" y="98" text-anchor="middle" class="t1">{e(nome)}</text>')
        if aspetto:
            pezzi.append(f'<text x="{x + 64}" y="116" text-anchor="middle" class="t2">{e(aspetto)}</text>')
        pezzi.append(f'<text x="{x + 64}" y="136" text-anchor="middle" class="t3">{e(colore)}</text>')
    pezzi.append('<path d="M10 152 H684" stroke="#3d6b4f" stroke-width="2" marker-end="url(#freccia)"/>'
                 '<defs><marker id="freccia" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">'
                 '<path d="M0,0 L8,4 L0,8 Z" fill="#3d6b4f"/></marker></defs>'
                 '<text x="347" y="170" text-anchor="middle" class="t2">la carta asciuga: meno acqua sul foglio, colore più denso nel pennello</text>')
    return ('<figure class="schema"><svg viewBox="0 0 700 176" role="img" aria-label="Gli stati della carta, da bagnata ad asciutta">'
            + "".join(pezzi) + '</svg><figcaption>Schema: gli stati della carta dal bagnato all\'asciutto, '
            'col riflesso dell\'acqua che si spegne e il colore adatto sotto ogni stato (in verde). '
            'I dettagli e le fonti sono nel testo.</figcaption></figure>')


SVG = {"consistenze": svg_consistenze, "carta": svg_carta}


def tavolozza_ridotta(b, F, dove):
    """I sei colori della tavolozza ridotta e le 12 miscele M1-M12, dai dati della sezione Alberi (riquadro
    «All'aperto»), con i rimandi al calcolatore della Teoria dei colori."""
    a = json.loads(FONTE_ALBERI.read_text(encoding="utf-8"))["apertura"]
    tav = a["tavolozza"]
    rif = {c["id"]: c for c in json.loads(FONTE_TAVOLOZZA.read_text(encoding="utf-8"))["colori"]}
    for c in tav:
        r = rif.get(c["id"])
        if not r or (r["nome"], r["pigmento"], r.get("trasparenza_tubetto")) != (c["nome"], c["pigmento"], c.get("trasparenza_tubetto")):
            raise SystemExit(f"principi: tavolozza, {c['id']} diverso da dati/colori/tavolozza.json")
    nomi = {c["id"]: c["nome"] for c in tav}

    def riga_tav(c):
        sigla = f' ({e(c["sigla"])})' if c.get("sigla") else ""
        tras = f'; nel tubetto della tavolozza: {e(c["trasparenza_tubetto"])}' if c.get("trasparenza_tubetto") else ""
        nota = f' ({e(c["nota"])})' if c.get("nota") else ""
        return f'<li><b>{e(c["nome"])}</b>{sigla}: pigmento <b>{e(c["pigmento"])}</b>{tras}{nota}</li>'

    sei_colori = (f'<div class="sei-colori"><h4>I sei colori della tavolozza ridotta{F.rif(b["fonti_colori"], f"{dove}, sei colori")}</h4>'
                  f'<ul class="tav">{"".join(riga_tav(c) for c in tav)}</ul>'
                  '<p class="rimando">Teoria e calcolatore: <a href="../colori/">Teoria dei colori</a> · '
                  '<a href="../colori/#calcolatore">Calcolatore di miscele</a>. '
                  'I tubetti marca per marca: <a href="../marche/">Marche e tubetti</a>.</p></div>')

    def riquadro(r, classe):
        voci = "".join(f'<li><b>{e(k)}</b>: {e(v)}</li>' for k, v in r["voci"])
        rim = r.get("rimando")
        if rim and rim["href"].startswith("../principi/#"):
            # Nella pagina dei Principi il rimando ai Principi generali diventa un rimando interno ai capitoli 1 e 2.
            rim = {"testo": rim["testo"], "link": "capitoli 1 e 2", "href": rim["href"][len("../principi/"):]}
        rimando = f'<p class="rimando">{e(rim["testo"])} <a href="{e(rim["href"])}">{e(rim["link"])}</a>.</p>' if rim else ""
        return (f'<div class="riquadro {classe}"><h5>{e(r["titolo"])}</h5><p>{e(r["testo"])}</p><ul>{voci}</ul>'
                f'<p>{e(r["chiusura"])}</p>{rimando}</div>')

    def link(mix, testo):
        q = ",".join(f"{i}:{n}" for i, n in mix)
        return f'<a class="calc" href="../colori/?mix={e(q)}#mescola">{e(testo)}</a>'

    righe = []
    for x in a["miscele"]:
        if x.get("mix"):
            lk = link(x["mix"], "prova nel calcolatore")
        else:
            lk = " · ".join(link([m], f"{nomi[m[0]].lower()} nel calcolatore") for m in x.get("mix_separati", []))
        nota = f' {e(x["nota"])}' if x.get("nota") else ""
        righe.append(f'<tr id="{e(x["m"])}"><td class="m">{e(x["m"])}</td><td><b>{e(x["nome"])}</b><br>{e(x["ricetta"])}'
                     f'<br><span class="cons">Consistenza: <b>{e(x["consistenza"])}</b></span>'
                     f'<br><span class="pigm">Pigmenti: {e(x["pigmenti"])}.{nota}</span><br>{lk}</td></tr>')
    return (f'{sei_colori}<div id="miscele"><h4>Le 12 miscele (M1-M12){F.rif(b["fonti_miscele"], f"{dove}, miscele")}</h4>'
            f'{riquadro(a["dosi"], "dosi")}{riquadro(a["prove"], "prove")}<p class="nota-calc">{e(a["calcolatore_nota"])}</p>'
            f'<div class="tab"><table class="mix">{"".join(righe)}</table></div></div>')

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
ul.voci { padding-left: 20px; } ul.voci li { margin-bottom: 6px; }
.pill { display: inline-block; font-size: .78em; font-weight: 700; border-radius: 10px; padding: 0 8px; margin-right: 4px; color: #fff; }
.pill.bagnata { background: #2f6f9f; } .pill.umida { background: #6b8fa8; } .pill.asciutta { background: #a07a4a; }
figure { margin: 12px 0; } figcaption { font-size: .85em; color: #555; margin-top: 4px; }
.schema svg { width: 100%; display: block; }
.schema .t1 { font-size: 15px; font-weight: 700; fill: #2c4f3a; } .schema .t2 { font-size: 12px; fill: #555; }
.schema .t3 { font-size: 12px; font-weight: 600; fill: #2c6a4a; }
.tab { overflow-x: auto; }
table.riass { width: 100%; min-width: 520px; border-collapse: collapse; font-size: .88em; }
table.riass th, table.riass td { border: 1px solid #d8d2c4; padding: 5px 6px; vertical-align: top; text-align: left; }
table.riass th { background: #eef4ef; color: #2c4f3a; }
.intro p.nota-fonti { font-size: .88em; color: #555; }
h3 { font-size: 1.1em; margin: 18px 0 6px; color: #2c4f3a; }
h4 { font-size: 1em; margin: 8px 0 6px; color: #2c4f3a; }
h5 { font-size: .95em; margin: 4px 0 6px; color: #2c4f3a; }
.sei-colori, .riquadro { background: #f6f3eb; border: 1px solid #dfd8c8; border-radius: 8px; padding: 11px 14px; margin: 12px 0; font-size: .95em; }
.sei-colori ul, .riquadro ul { margin: 6px 0; padding-left: 20px; }
.sei-colori li, .riquadro li { margin-bottom: 4px; }
.sei-colori p, .riquadro p { margin: 4px 0; }
.rimando { font-size: .9em; color: #444; margin: 6px 0 0; }
.nota-calc { font-size: .9em; color: #555; font-style: italic; margin: 10px 0; }
table.mix { width: 100%; border-collapse: collapse; font-size: .94em; background: #fffdf9; border: 1px solid #dfd8c8; margin-top: 10px; }
table.mix td { border-top: 1px solid #dfd8c8; padding: 8px 10px; vertical-align: top; }
table.mix td.m { font-weight: 700; color: #2c4f3a; white-space: nowrap; width: 3.2em; background: #f7f3ea; text-align: center; }
.cons, .pigm { font-size: .9em; color: #444; }
a.calc { display: inline-block; margin-top: 3px; font-size: .86em; color: #2c4f3a; text-decoration: none;
         border: 1px solid #9ab5a3; border-radius: 10px; padding: 1px 9px; background: #eef4ef; }
a.calc:hover { background: #dfece2; }
footer { margin-top: 30px; font-size: .8em; color: #666; border-top: 1px solid #e3e0d8; padding-top: 10px; }
""" + rimandi_fonti.CSS


def controlla_testo(t, dove):
    if "da verificare" in t.lower():
        raise SystemExit(f"principi: testo «da verificare» in {dove}: fuori dalla pagina finché non ha una fonte")


def pagina():
    d = json.loads((QUI / "principi.json").read_text(encoding="utf-8"))
    salti = "".join(f'<a href="#{c["id"]}">{e(c["breve"])}</a>' for c in d["capitoli"])
    sezioni, citate = [], set()
    for c in d["capitoli"]:
        F = rimandi_fonti.Capitolo(c["id"], d["fonti"], "principi")
        corpo = [f'<section class="cap" id="{c["id"]}"><h2>{e(c["titolo"])}</h2>']
        for i, b in enumerate(c["blocchi"]):
            dove = f'{c["id"]}, blocco {i + 1}'
            if b["tipo"] == "p":
                controlla_testo(b["testo"], dove)
                corpo.append(f'<p>{b["testo"]}{F.rif(b["fonti"], dove)}</p>')
            elif b["tipo"] == "lista":
                voci = []
                for j, v in enumerate(b["voci"]):
                    controlla_testo(v["testo"], f"{dove}, voce {j + 1}")
                    voci.append(f'<li>{v["testo"]}{F.rif(v["fonti"], f"{dove}, voce {j + 1}")}</li>')
                corpo.append('<ul class="voci">' + "".join(voci) + "</ul>")
            elif b["tipo"] == "svg":
                corpo.append(SVG[b["nome"]]())
            elif b["tipo"] == "titoletto":
                controlla_testo(b["testo"], dove)
                corpo.append(f'<h3 id="{e(b["id"])}">{e(b["testo"])}</h3>')
            elif b["tipo"] == "tavolozza_ridotta":
                corpo.append(tavolozza_ridotta(b, F, dove))
            elif b["tipo"] == "tabella":
                testa = "".join(f"<th>{e(x)}</th>" for x in b["intestazione"]) + "<th>Fonti</th>"
                righe = []
                for j, r in enumerate(b["righe"]):
                    for x in r["celle"]:
                        controlla_testo(x, f"{dove}, riga {j + 1}")
                    celle = "".join(f"<td>{e(x)}</td>" for x in r["celle"])
                    righe.append(f'<tr>{celle}<td>{F.rif(r["fonti"], f"{dove}, riga {j + 1}")}</td></tr>')
                corpo.append(f'<div class="tab"><table class="riass"><tr>{testa}</tr>{"".join(righe)}</table></div>')
            else:
                raise SystemExit(f"principi: blocco di tipo sconosciuto in {dove}")
        corpo.append(F.elenco())
        corpo.append("</section>")
        sezioni.append("\n".join(corpo))
        citate.update(F.ordine)
    mancano = [k for k in d["fonti"] if k not in citate]
    if mancano:
        raise SystemExit(f"principi: fonti mai citate: {', '.join(mancano)}")
    for p in d["introduzione"]:
        controlla_testo(p, "introduzione")
    intro = "".join(f"<p>{p}</p>" for p in d["introduzione"]) + f'<p class="nota-fonti">{e(d["nota_fonti"])}</p>'
    data = "/".join(reversed(d["data"].split("-")))
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
<div class="intro">{intro}</div>
{chr(10).join(sezioni)}
<footer>Quaderno di acquerello · Principi generali · testi del {e(data)}.</footer>
{rimandi_fonti.JS}
</body>
</html>
"""
    USCITA.write_text(pagina_html, encoding="utf-8")
    print(f"pagina: {USCITA} {USCITA.stat().st_size / 1024:.0f} KB, {len(citate)} fonti")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "pagina":
        print(__doc__)
        sys.exit(1)
    pagina()

#!/usr/bin/env python3
"""Genera la pagina della sezione «Principi generali» del Quaderno di acquerello.

Uso: python genera-principi.py pagina

Legge i testi e le fonti da principi.json e scrive principi.html accanto a sé, una pagina sola con
tutto dentro. scripts/genera-sito.py la copia in site/principi/index.html.
Controlli: ogni frase ha almeno una fonte, ogni fonte citata esiste, ogni fonte del json è citata,
nessun testo contiene «da verificare». GBOT-app-acquerello, 18/10/2026."""
import html
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = pathlib.Path(__file__).resolve().parent
USCITA = QUI / "principi.html"


def e(testo):
    return html.escape(str(testo), quote=True)


class Fonti:
    """Numera le fonti nell'ordine in cui compaiono nella pagina."""

    def __init__(self, fonti):
        self.fonti = fonti
        self.ordine = []

    def rif(self, chiavi, dove):
        if not chiavi:
            raise SystemExit(f"principi: frase senza fonte in {dove}")
        nums = []
        for k in chiavi:
            if k not in self.fonti:
                raise SystemExit(f"principi: fonte «{k}» non definita ({dove})")
            if k not in self.ordine:
                self.ordine.append(k)
            nums.append(self.ordine.index(k) + 1)
        link = ", ".join(f'<a href="#f{n}">{n}</a>' for n in sorted(set(nums)))
        return f'<sup class="rif">[{link}]</sup>'

    def elenco(self):
        mancano = [k for k in self.fonti if k not in self.ordine]
        if mancano:
            raise SystemExit(f"principi: fonti mai citate: {', '.join(mancano)}")
        voci = []
        for n, k in enumerate(self.ordine, 1):
            f = self.fonti[k]
            testo = e(f["testo"])
            if f.get("url"):
                esterno = f["url"].startswith("http")
                attr = ' target="_blank" rel="noopener"' if esterno else ""
                testo += f' <a href="{e(f["url"])}"{attr}>{"apri" if esterno else "nel Quaderno"}</a>'
            voci.append(f'<li id="f{n}">{testo}</li>')
        return '<ol class="fonti">' + "".join(voci) + "</ol>"


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
            'Non è una misura: le consistenze si provano sul foglietto.</figcaption></figure>')


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
sup.rif { font-size: .68em; color: #555; white-space: nowrap; } sup.rif a { text-decoration: none; }
.pill { display: inline-block; font-size: .78em; font-weight: 700; border-radius: 10px; padding: 0 8px; margin-right: 4px; color: #fff; }
.pill.bagnata { background: #2f6f9f; } .pill.umida { background: #6b8fa8; } .pill.asciutta { background: #a07a4a; }
figure { margin: 12px 0; } figcaption { font-size: .85em; color: #555; margin-top: 4px; }
.schema svg { width: 100%; display: block; }
.schema .t1 { font-size: 15px; font-weight: 700; fill: #2c4f3a; } .schema .t2 { font-size: 12px; fill: #555; }
.schema .t3 { font-size: 12px; font-weight: 600; fill: #2c6a4a; }
table.riass { width: 100%; border-collapse: collapse; font-size: .88em; }
table.riass th, table.riass td { border: 1px solid #d8d2c4; padding: 5px 6px; vertical-align: top; text-align: left; }
table.riass th { background: #eef4ef; color: #2c4f3a; }
.fonti-tit { margin-top: 30px; }
ol.fonti { font-size: .85em; color: #444; padding-left: 26px; } ol.fonti li { margin-bottom: 5px; }
ol.fonti li:target { background: #fff3cd; }
.nota-fonti { font-size: .85em; color: #555; background: #f1efe8; border-radius: 8px; padding: 7px 10px; }
footer { margin-top: 30px; font-size: .8em; color: #666; border-top: 1px solid #e3e0d8; padding-top: 10px; }
"""


def controlla_testo(t, dove):
    if "da verificare" in t.lower():
        raise SystemExit(f"principi: testo «da verificare» in {dove}: fuori dalla pagina finché non ha una fonte")


def pagina():
    d = json.loads((QUI / "principi.json").read_text(encoding="utf-8"))
    F = Fonti(d["fonti"])
    salti = "".join(f'<a href="#{c["id"]}">{e(c["breve"])}</a>' for c in d["capitoli"])
    sezioni = []
    for c in d["capitoli"]:
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
            elif b["tipo"] == "tabella":
                testa = "".join(f"<th>{e(x)}</th>" for x in b["intestazione"]) + "<th>Fonti</th>"
                righe = []
                for j, r in enumerate(b["righe"]):
                    for x in r["celle"]:
                        controlla_testo(x, f"{dove}, riga {j + 1}")
                    celle = "".join(f"<td>{e(x)}</td>" for x in r["celle"])
                    righe.append(f'<tr>{celle}<td>{F.rif(r["fonti"], f"{dove}, riga {j + 1}")}</td></tr>')
                corpo.append(f'<table class="riass"><tr>{testa}</tr>{"".join(righe)}</table>')
            else:
                raise SystemExit(f"principi: blocco di tipo sconosciuto in {dove}")
        corpo.append("</section>")
        sezioni.append("\n".join(corpo))
    for p in d["introduzione"]:
        controlla_testo(p, "introduzione")
    intro = "".join(f"<p>{p}</p>" for p in d["introduzione"])
    data = "/".join(reversed(d["data"].split("-")))
    pagina_html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(d['titolo'])}</title>
<style>{CSS}</style>
</head>
<body>
<header class="testa"><h1>{e(d['titolo'])}</h1>
<p class="sotto">{e(d['sottotitolo'])}</p></header>
<nav class="salti">{salti}</nav>
<div class="intro">{intro}</div>
{chr(10).join(sezioni)}
<h2 class="fonti-tit" id="fonti">Fonti</h2>
<p class="nota-fonti">{e(d['nota_fonti'])}</p>
{F.elenco()}
<footer>Quaderno di acquerello · Principi generali · testi del {e(data)}.</footer>
</body>
</html>
"""
    USCITA.write_text(pagina_html, encoding="utf-8")
    print(f"pagina: {USCITA} {USCITA.stat().st_size / 1024:.0f} KB, {len(F.ordine)} fonti")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "pagina":
        print(__doc__)
        sys.exit(1)
    pagina()

#!/usr/bin/env python3
"""Genera la pagina della sezione «Repertorio dei soggetti pittorici» da soggetti.json."""
import html
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(QUI, "soggetti.json")
# I nomi degli esempi di un modulo pubblicato si leggono dai dati del modulo: così la sezione
# Soggetti non può dare a un esempio un nome diverso da quello della sua pagina.
MODULI = {"alberi": (os.path.join(QUI, "..", "alberi", "pit-261014-video-gesti-alberi.json"), "../alberi/")}
PAGINA = os.path.join(QUI, "soggetti.html")

e = lambda t: html.escape(str(t or ""))

CSS = """
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 52px; }
body { margin: 0 auto; max-width: 820px; padding: 0 14px 40px; font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
       font-size: 17px; line-height: 1.5; color: #1f1f1f; background: #fbfaf7; }
h1 { font-size: 1.45em; line-height: 1.25; margin: 18px 0 6px; color: #2c4f3a; }
h2 { font-size: 1.22em; margin: 0; color: #1f1c17; }
.sotto { color: #444; margin: 0 0 14px; }
.intro-box { background: #eef4ef; border: 1px solid #cadbce; border-radius: 8px; padding: 12px 14px; margin: 12px 0 20px; }
.intro-box p { margin: 0 0 8px; }
.intro-box p:last-child { margin-bottom: 0; }
.grid-soggetti { display: grid; grid-template-columns: 1fr; gap: 18px; }
.sogg-card { background: #fffdf8; border: 1px solid #dfd5c3; border-radius: 12px; padding: 16px 18px 18px;
             box-shadow: 0 2px 8px rgba(31,28,23,.05); }
.sogg-card.attivo { border-left: 5px solid #263529; background: #fffdf9; }
.sogg-card.prog { border-left: 5px solid #b5a68e; background: #faf7f0; opacity: .94; }
.sogg-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin-bottom: 6px; }
.sogg-tit-wrap { display: flex; align-items: flex-start; gap: 10px; }
.sig { display: inline-flex; align-items: center; justify-content: center; min-width: 34px; height: 34px;
       border-radius: 8px; background: #263529; color: #f7f2e7; font-weight: 700; font-size: .92rem; margin-top: 2px; }
.sogg-card.prog .sig { background: #7a6f5d; }
.stato-badge { display: inline-block; border-radius: 999px; padding: 3px 10px; font-size: .78rem; font-weight: 700; }
.stato-badge.attivo { background: #e3f1e8; color: #1e4638; border: 1px solid #a9cfb7; }
.stato-badge.prog { background: #efe8d8; color: #5a4d3b; border: 1px solid #d5c8b0; }
.sogg-sub { margin: 2px 0 8px; font-size: .9em; color: #6b5e4c; font-weight: 500; }
.sogg-desc { margin: 8px 0 12px; font-size: .93em; color: #363027; }
.sottovoci { background: #f6f3eb; border: 1px solid #e2dac9; border-radius: 8px; padding: 10px 14px; margin: 10px 0 14px; }
.sottovoci h3 { margin: 0 0 6px; font-size: .95em; color: #2c4f3a; }
.sottovoci ul { margin: 0; padding-left: 18px; columns: 2; column-gap: 1.8em; font-size: .9em; }
.sottovoci li { break-inside: avoid; margin-bottom: 4px; }
.sottovoci a { color: #2c4f3a; text-decoration: none; font-weight: 600; }
.sottovoci a:hover { text-decoration: underline; }
@media (max-width: 620px) { .sottovoci ul { columns: 1; } }
.pills { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.pill { background: #efe6d5; color: #4f3d27; border: 1px solid #d8ccb8; border-radius: 999px; padding: 2px 10px; font-size: .78rem; font-weight: 600; }
.btn { display: inline-block; background: #263529; color: #f7f2e7; padding: 8px 14px; border-radius: 8px;
       font-size: .9rem; font-weight: 600; text-decoration: none; }
.btn:hover { background: #1c281f; }
footer { margin-top: 28px; border-top: 1px solid #ddd; padding-top: 12px; font-size: .9em; color: #444; }
"""


def sottovoci_da(modulo):
    percorso, href = MODULI[modulo]
    voci = []
    for t in json.load(open(percorso, encoding="utf-8"))["alberi"]:
        sigla, nome = t["voce"].split(" ", 1)
        voci.append({"sigla": sigla, "titolo": nome, "href": f"{href}#{sigla}"})
    return voci


def pagina():
    d = json.load(open(FONTE, encoding="utf-8"))
    intro_p = "".join(f"<p>{e(p)}</p>" for p in d["introduzione"])

    cards = []
    for s in d["soggetti"]:
        attivo = s["stato"] == "pubblicato"
        cls = "attivo" if attivo else "prog"
        badges = "".join(f'<span class="pill">{e(b)}</span>' for b in s.get("badge", []))
        blocco_sottovoci = ""
        if s.get("sottovoci_da"):
            s["sottovoci"] = sottovoci_da(s["sottovoci_da"])
        if s.get("sottovoci"):
            voci = "".join(
                f'<li><a href="{e(v["href"])}"><b>{e(v["sigla"])}</b> · {e(v["titolo"])}</a></li>'
                for v in s["sottovoci"]
            )
            blocco_sottovoci = (
                f'<div class="sottovoci"><h3>Gli esempi del modulo:</h3><ul>{voci}</ul></div>'
            )
        pulsante = (
            f'<a class="btn" href="{e(s["href"])}">Apri il modulo →</a>'
            if s.get("href")
            else ""
        )
        cards.append(
            f'<article class="sogg-card {cls}" id="{e(s["codice"])}">'
            f'<div class="sogg-head">'
            f'<div class="sogg-tit-wrap">'
            f'<span class="sig">{e(s["codice"])}</span>'
            f'<div><h2>{e(s["titolo"])}</h2><p class="sogg-sub">{e(s["sottotitolo"])}</p></div>'
            f'</div>'
            f'<span class="stato-badge {cls}">{e(s["etichetta_stato"])}</span>'
            f'</div>'
            f'<p class="sogg-desc">{e(s["descrizione"])}</p>'
            f'{blocco_sottovoci}'
            f'<div class="pills">{badges}</div>'
            f'{pulsante}'
            f'</article>'
        )

    html_out = f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(d["titolo"])}</title>
<style>{CSS}</style></head>
<body>
<header>
  <h1>{e(d["titolo"])}</h1>
  <p class="sotto">{e(d["sottotitolo"])}</p>
</header>
<div class="intro-box">{intro_p}</div>
<div class="grid-soggetti">{"".join(cards)}</div>
<footer>
  <p>Il lavoro in studio e all'aperto e il prontuario delle 12 miscele sono nella sezione <a href="../studio-plein-air/">2. Studio ed en plein air</a>. Le altre sezioni: <a href="../principi/">1. Principi generali</a> · <a href="../colori/">3. Teoria dei colori</a> · <a href="../marche/">4. Marche e tubetti</a>.</p>
</footer>
</body></html>"""

    open(PAGINA, "w", encoding="utf-8").write(html_out)
    print(f"pagina: {PAGINA} {os.path.getsize(PAGINA) // 1024} KB")


if __name__ == "__main__":
    pagina()

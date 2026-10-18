#!/usr/bin/env python3
"""Genera la pagina della sezione «Teoria dei colori» del Quaderno di acquerello.

Uso: python genera-teoria-colori.py pagina

Legge i testi (teoria-colori.json), la tavolozza (tavolozza.json), la tabella delle tinte Munsell
(munsell-tinte.json) e il codice del calcolatore (spettri-spectraljs.js, calcolatore.js, interfaccia.js)
e scrive teoria-colori.html accanto a sé, una pagina sola con tutto dentro: niente collegamenti
a file o librerie esterne. scripts/genera-sito.py la copia in site/colori/index.html.
GBOT-app-acquerello, 18/10/2026."""
import html
import json
import math
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = pathlib.Path(__file__).resolve().parent
USCITA = QUI / "teoria-colori.html"


def leggi_json(nome):
    return json.loads((QUI / nome).read_text(encoding="utf-8"))


def leggi_testo(nome):
    return (QUI / nome).read_text(encoding="utf-8")


def e(testo):
    return html.escape(str(testo), quote=True)


def grigio_da_lstar(l):
    """sRGB di un grigio con chiarezza CIELAB L* (D65)."""
    fy = (l + 16) / 116
    y = fy ** 3 if fy ** 3 > 216 / 24389 else (116 * fy - 16) / (24389 / 27)
    c = 1.055 * y ** (1 / 2.4) - 0.055 if y > 0.0031308 else 12.92 * y
    v = max(0, min(255, round(c * 255)))
    return f"#{v:02X}{v:02X}{v:02X}"


def scala_valori():
    # L* dei grigi N1-N9 della renotation di Munsell (illuminante C), arrotondati
    lstar = {1: 10.4, 2: 20.2, 3: 30.4, 4: 40.7, 5: 51.0, 6: 61.1, 7: 70.9, 8: 80.5, 9: 90.2}
    celle = []
    for v in range(1, 10):
        col = grigio_da_lstar(lstar[v])
        testo = "#fff" if v < 6 else "#1f1f1f"
        celle.append(f'<div class="val" style="background:{col};color:{testo}">N{v}</div>')
    return ('<figure class="scala"><div class="valori">' + "".join(celle) + "</div>"
            "<figcaption>Scala dei valori da N1 a N9: passi che l'occhio vede uguali (a schermo è indicativa).</figcaption></figure>")


def ruota_tinte(tinte):
    """Ruota delle 40 tinte Munsell a valore 6 e croma 6, come SVG."""
    n = len(tinte)
    cx = cy = 130
    r1, r2 = 62, 112
    pezzi = []
    for i, t in enumerate(tinte):
        a0 = (i - 0.5) / n * 2 * math.pi - math.pi / 2
        a1 = (i + 0.5) / n * 2 * math.pi - math.pi / 2
        p = [(cx + r2 * math.cos(a0), cy + r2 * math.sin(a0)), (cx + r2 * math.cos(a1), cy + r2 * math.sin(a1)),
             (cx + r1 * math.cos(a1), cy + r1 * math.sin(a1)), (cx + r1 * math.cos(a0), cy + r1 * math.sin(a0))]
        d = (f"M{p[0][0]:.1f},{p[0][1]:.1f} A{r2},{r2} 0 0 1 {p[1][0]:.1f},{p[1][1]:.1f} "
             f"L{p[2][0]:.1f},{p[2][1]:.1f} A{r1},{r1} 0 0 0 {p[3][0]:.1f},{p[3][1]:.1f} Z")
        pezzi.append(f'<path d="{d}" fill="{t["srgb_6_6"]}"><title>{e(t["tinta"])} 6/6</title></path>')
        if t["tinta"].startswith("5") and not t["tinta"].startswith("5."):
            am = i / n * 2 * math.pi - math.pi / 2
            x, y = cx + 124 * math.cos(am), cy + 124 * math.sin(am)
            pezzi.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="middle">{e(t["tinta"][1:])}</text>')
    pezzi.append(f'<text x="{cx}" y="{cy - 6}" text-anchor="middle" class="centro">40 tinte</text>')
    pezzi.append(f'<text x="{cx}" y="{cy + 12}" text-anchor="middle" class="centro">valore 6, croma 6</text>')
    return ('<figure class="ruota"><svg viewBox="-6 -6 272 272" role="img" aria-label="Ruota delle 40 tinte Munsell">'
            + "".join(pezzi) + "</svg><figcaption>Le 40 tinte di Munsell allo stesso valore (6) e croma (6), "
            "dalla renotation del 1943; i colori a schermo sono indicativi. Partendo dall'alto, in senso orario: "
            "R, YR, Y, GY, G, BG, B, PB, P, RP.</figcaption></figure>")


def elenco_fonti(chiavi, fonti):
    voci = []
    for k in chiavi:
        f = fonti[k]
        if f["url"]:
            voci.append(f'<a href="{e(f["url"])}" target="_blank" rel="noopener">{f["testo"]}</a>')
        else:
            voci.append(f["testo"])
    return '<p class="fonti-cap">Fonti: ' + "; ".join(voci) + ".</p>"


def schede_tavolozza(tav):
    carte = []
    for c in tav["colori"]:
        carte.append(f"""<div class="tubo">
  <div class="tubo-camp" style="background:{e(c['srgb'])}"><span>provvisorio</span></div>
  <div class="tubo-txt">
    <b>{e(c['nome'])}</b><br>
    <span class="cot">Cotman n. {e(c['numero'])} {e(c['nome_cotman'])}</span><br>
    Pigmento <b>{e(c['pigmento'])}</b> · {e(c['trasparenza'])}<br>
    <span class="nota-tubo">{e(c['note'])}</span>
  </div>
</div>""")
    return '<div class="tubi">' + "\n".join(carte) + "</div>"


CALCOLATORE_HTML = """
<div class="strum" id="mescola">
  <h3>Mescola</h3>
  <p class="aiuto">Scegli due o tre tubetti e le parti di ognuno (da 1 a 10).</p>
  <div class="righe-mix">
    <div class="riga-mix"><select id="mc1"></select><input id="mp1" type="number" min="1" max="10" value="1"> parti</div>
    <div class="riga-mix"><select id="mc2"></select><input id="mp2" type="number" min="1" max="10" value="1"> parti</div>
    <div class="riga-mix"><select id="mc3"></select><input id="mp3" type="number" min="1" max="10" value="1"> parti</div>
  </div>
  <div class="esito-mix">
    <div class="camp-grande" id="mcamp"></div>
    <div class="esito-txt" id="mtxt"></div>
  </div>
  <div class="striscia-tit">Striscia di diluizione, dal miele al tè (velo sul bianco della carta) · <a href="../principi/#consistenze">le tre consistenze</a></div>
  <div class="striscia" id="mstriscia"></div>
</div>

<div class="strum" id="trova">
  <h3>Trova la miscela</h3>
  <p class="aiuto">Scegli il colore che vuoi ottenere: il calcolatore prova tutte le combinazioni di uno, due o tre tubetti con parti da 1 a 10 e mostra le 5 più vicine, misurando la distanza nello spazio OKLab.</p>
  <div class="riga-trova">
    <label>Colore obiettivo <input id="tobj" type="color" value="#6b8e23"></label>
    <label class="spunta"><input id="tdil" type="checkbox" checked> considera anche la diluizione</label>
    <button id="tvai" type="button">Cerca</button>
  </div>
  <div id="tris"></div>
</div>
"""


CSS = """
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 52px; }
body { margin: 0 auto; max-width: 760px; padding: 0 14px 40px; font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
       font-size: 17px; line-height: 1.45; color: #1f1f1f; background: #fbfaf7; }
h1 { font-size: 1.45em; line-height: 1.2; margin: 18px 0 4px; color: #2c4f3a; }
h2 { font-size: 1.3em; margin: 0 0 6px; color: #2c4f3a; }
h3 { font-size: 1.05em; margin: 14px 0 6px; color: #2c4f3a; }
a { color: #2c6a4a; }
.sotto { color: #444; margin: 0 0 10px; }
nav.salti { position: sticky; top: 0; z-index: 5; display: flex; gap: 6px; overflow-x: auto; padding: 8px 0;
            background: #fbfaf7; border-bottom: 1px solid #e3e0d8; }
nav.salti a { flex: none; text-decoration: none; color: #2c4f3a; border: 1px solid #3d6b4f; border-radius: 16px;
              padding: 3px 12px; font-weight: 600; }
section.cap { border-top: 3px solid #3d6b4f; padding-top: 14px; margin-top: 26px; }
.fonti-cap { font-size: .85em; color: #555; background: #f1efe8; border-radius: 8px; padding: 7px 10px; }
figure { margin: 12px 0; } figcaption { font-size: .85em; color: #555; margin-top: 4px; }
.valori { display: grid; grid-template-columns: repeat(9, 1fr); border-radius: 6px; overflow: hidden; border: 1px solid #d8d2c4; }
.val { padding: 14px 0; text-align: center; font-size: .8em; font-weight: 600; }
.ruota svg { width: 100%; max-width: 320px; display: block; margin: 0 auto; }
.ruota text { font-size: 11px; font-weight: 700; fill: #2c4f3a; } .ruota text.centro { font-size: 10px; font-weight: 600; fill: #555; }
.avviso { background: #fff8ea; border-left: 4px solid #c87a28; border-radius: 6px; padding: 8px 10px; margin: 10px 0; font-size: .92em; color: #4a3010; }
.avviso ul { margin: 4px 0 0; padding-left: 20px; } .avviso li { margin-bottom: 3px; }
.tubi { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 10px 0; }
@media (max-width: 560px) { .tubi { grid-template-columns: 1fr; } }
.tubo { display: flex; gap: 10px; background: #fff; border: 1px solid #c9d8cd; border-radius: 10px; padding: 8px; }
.tubo-camp { flex: none; width: 64px; border-radius: 6px; border: 1px solid rgba(0,0,0,.15); display: flex; align-items: flex-end; justify-content: center; }
.tubo-camp span { font-size: .62em; background: rgba(255,255,255,.85); border-radius: 4px; padding: 0 3px; margin-bottom: 3px; color: #4a3010; }
.tubo-txt { font-size: .88em; line-height: 1.35; } .cot { color: #555; } .nota-tubo { color: #6b5e4c; font-size: .95em; }
.strum { background: #eef4ef; border: 2px solid #3d6b4f; border-radius: 12px; padding: 10px 14px 14px; margin: 16px 0; }
.strum h3 { margin-top: 2px; } .aiuto { font-size: .9em; color: #354a3d; margin: 0 0 8px; }
.riga-mix { display: flex; align-items: center; gap: 8px; margin: 5px 0; font-size: .92em; }
.riga-mix select { flex: 1; min-width: 0; font-size: 1em; padding: 4px; }
.riga-mix input { width: 4em; font-size: 1em; padding: 4px; }
.esito-mix { display: flex; gap: 12px; align-items: stretch; margin: 10px 0; }
.camp-grande { flex: none; width: 110px; min-height: 90px; border-radius: 8px; border: 1px solid rgba(0,0,0,.2); }
.esito-txt { font-size: .9em; } .esito-txt .ric { font-weight: 700; color: #1f3c2b; }
.striscia-tit { font-size: .85em; font-weight: 600; color: #354a3d; margin-top: 4px; }
.striscia { display: grid; grid-template-columns: repeat(6, 1fr); gap: 0; border-radius: 6px; overflow: hidden; border: 1px solid #d8d2c4; margin-top: 4px; }
.passo { min-height: 54px; display: flex; align-items: flex-end; justify-content: center; }
.passo span { font-size: .7em; background: rgba(255,255,255,.85); border-radius: 4px; padding: 0 4px; margin-bottom: 3px; color: #333; }
.riga-trova { display: flex; flex-wrap: wrap; gap: 10px 16px; align-items: center; font-size: .92em; }
.riga-trova input[type=color] { width: 54px; height: 34px; vertical-align: middle; border: 1px solid #999; padding: 0; background: none; }
.riga-trova button, .usa { background: #2c4f3a; color: #fff; border: 0; border-radius: 8px; padding: 6px 14px; font-weight: 600; font-size: .95em; cursor: pointer; }
.usa { padding: 3px 10px; font-size: .8em; margin-top: 4px; }
.prop { display: flex; gap: 10px; align-items: center; background: #fff; border: 1px solid #c9d8cd; border-radius: 10px; padding: 8px; margin: 8px 0; }
.coppia { flex: none; display: flex; border-radius: 6px; overflow: hidden; border: 1px solid rgba(0,0,0,.2); }
.coppia div { width: 44px; height: 54px; }
.prop-txt { font-size: .88em; line-height: 1.35; } .prop-txt b.ric { color: #1f3c2b; }
.vicino { font-weight: 600; } .vicino.si { color: #2c6a4a; } .vicino.quasi { color: #8a6a10; } .vicino.no { color: #a33; }
code { background: #f1efe8; border-radius: 4px; padding: 0 4px; font-size: .9em; }
footer { margin-top: 30px; font-size: .8em; color: #666; border-top: 1px solid #e3e0d8; padding-top: 10px; }
"""


def pagina():
    testi = leggi_json("teoria-colori.json")
    tav = leggi_json("tavolozza.json")
    mun = leggi_json("munsell-tinte.json")
    fonti = testi["fonti"]

    salti = "".join(f'<a href="#{c["id"]}">{e(c["breve"])}</a>' for c in testi["capitoli"])
    sezioni = []
    for c in testi["capitoli"]:
        corpo = [f'<section class="cap" id="{c["id"]}"><h2>{e(c["titolo"])}</h2>']
        corpo += [f"<p>{p}</p>" for p in c["paragrafi"]]
        if c["id"] == "munsell":
            corpo.append(scala_valori())
            corpo.append(ruota_tinte(mun["tinte"]))
        if c["id"] == "tavolozza":
            corpo.append(schede_tavolozza(tav))
        if c["id"] == "calcolatore":
            corpo.append('<div class="avviso"><b>Prima di usarlo.</b><ul>' + "".join(f"<li>{x}</li>" for x in c["limiti"]) + "</ul></div>")
            corpo.append(CALCOLATORE_HTML)
            corpo.append(f'<p class="aiuto">{c["taratura"]}</p>')
        corpo.append(elenco_fonti(c["fonti"], fonti))
        corpo.append("</section>")
        sezioni.append("\n".join(corpo))

    dati_js = ("var TAVOLOZZA = " + json.dumps(tav, ensure_ascii=False) + ";\n"
               "var MUNSELL = " + json.dumps(mun, ensure_ascii=False) + ";\n")
    script = "\n".join([leggi_testo("spettri-spectraljs.js"), leggi_testo("calcolatore.js"), dati_js, leggi_testo("interfaccia.js")])
    script = script.replace("</script", "<\\/script")

    pagina_html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(testi['titolo'])}</title>
<style>{CSS}</style>
</head>
<body>
<header class="testa"><h1>{e(testi['titolo'])}</h1>
<p class="sotto">{e(testi['sottotitolo'])}</p></header>
<nav class="salti">{salti}</nav>
{chr(10).join(sezioni)}
<footer>Quaderno di acquerello · Teoria dei colori · testi del {e('/'.join(reversed(testi['data'].split('-'))))}. Il calcolatore usa le tabelle spettrali di
<a href="https://github.com/rvanwijnen/spectral.js" target="_blank" rel="noopener">spectral.js</a> di Ronald van Wijnen (licenza MIT, testo della licenza nel codice della pagina); il resto del codice è scritto per il Quaderno.</footer>
<script>
{script}
</script>
</body>
</html>
"""
    USCITA.write_text(pagina_html, encoding="utf-8")
    print(f"pagina: {USCITA} {USCITA.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "pagina":
        print(__doc__)
        sys.exit(1)
    pagina()

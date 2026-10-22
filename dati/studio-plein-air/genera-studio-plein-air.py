#!/usr/bin/env python3
"""Genera la pagina della sezione «Pittura in studio ed en plein air» da studio-plein-air.json e dai dati delle miscele."""
import html
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(QUI, "studio-plein-air.json")
FONTE_ALBERI = os.path.join(QUI, "..", "alberi", "pit-261014-video-gesti-alberi.json")
FONTE_TAVOLOZZA = os.path.join(QUI, "..", "colori", "tavolozza.json")
PAGINA = os.path.join(QUI, "studio-plein-air.html")

e = lambda t: html.escape(str(t or ""))


def parte_colori(a):
    tav = a["tavolozza"]
    if os.path.exists(FONTE_TAVOLOZZA):
        rif = {c["id"]: c for c in json.load(open(FONTE_TAVOLOZZA, encoding="utf-8"))["colori"]}
        for c in tav:
            r = rif.get(c["id"])
            if not r or (r["nome"], r["pigmento"], r.get("trasparenza_tubetto")) != (
                c["nome"],
                c["pigmento"],
                c.get("trasparenza_tubetto"),
            ):
                raise SystemExit(f"tavolozza: {c['id']} diverso da dati/colori/tavolozza.json")
    nomi = {c["id"]: c["nome"] for c in tav}

    def riga_tav(c):
        sigla = f' ({e(c["sigla"])})' if c.get("sigla") else ""
        tras = f'; nel tubetto della tavolozza: {e(c["trasparenza_tubetto"])}' if c.get("trasparenza_tubetto") else ""
        nota = f' ({e(c["nota"])})' if c.get("nota") else ""
        return f'<li><b>{e(c["nome"])}</b>{sigla}: pigmento <b>{e(c["pigmento"])}</b>{tras}{nota}</li>'

    righe_tav = "".join(riga_tav(c) for c in tav)
    sei_colori = (
        f'<div class="sei-colori"><h4>I sei colori della tavolozza ridotta</h4>'
        f'<ul class="tav">{righe_tav}</ul>'
        f'<p class="rimando">Teoria e calcolatore: '
        f'<a href="../colori/">Teoria dei colori</a> · <a href="../colori/#calcolatore">Calcolatore di miscele</a>. '
        f'I tubetti marca per marca: <a href="../marche/">Marche e tubetti</a>.</p></div>'
    )

    def riquadro(r, classe):
        voci = "".join(f'<li><b>{e(k)}</b>: {e(v)}</li>' for k, v in r["voci"])
        rim = r.get("rimando")
        rimando = (
            f'<p class="rimando">{e(rim["testo"])} <a href="{e(rim["href"])}">{e(rim["link"])}</a>.</p>'
            if rim
            else ""
        )
        return (
            f'<div class="riquadro {classe}"><h4>{e(r["titolo"])}</h4><p>{e(r["testo"])}</p><ul>{voci}</ul>'
            f'<p>{e(r["chiusura"])}</p>{rimando}</div>'
        )

    riquadri = (
        riquadro(a["dosi"], "dosi")
        + riquadro(a["prove"], "prove")
        + f'<p class="nota-calc">{e(a["calcolatore_nota"])}</p>'
    )

    def link(mix, testo):
        q = ",".join(f"{i}:{n}" for i, n in mix)
        return f'<a class="calc" href="../colori/?mix={e(q)}#mescola">{e(testo)}</a>'

    righe = []
    for x in a["miscele"]:
        if x.get("mix"):
            lk = link(x["mix"], "prova nel calcolatore")
        else:
            lk = " · ".join(
                link([m], f"{nomi[m[0]].lower()} nel calcolatore") for m in x.get("mix_separati", [])
            )
        nota = f' {e(x["nota"])}' if x.get("nota") else ""
        righe.append(
            f'<tr id="{e(x["m"])}"><td class="m">{e(x["m"])}</td><td><b>{e(x["nome"])}</b><br>{e(x["ricetta"])}'
            f'<br><span class="cons">Consistenza: <b>{e(x["consistenza"])}</b></span>'
            f'<br><span class="pigm">Pigmenti: {e(x["pigmenti"])}.{nota}</span><br>{lk}</td></tr>'
        )
    return "".join(righe), sei_colori, riquadri


CSS = """
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 52px; }
body { margin: 0 auto; max-width: 820px; padding: 0 14px 40px; font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
       font-size: 17px; line-height: 1.5; color: #1f1f1f; background: #fbfaf7; }
h1 { font-size: 1.45em; line-height: 1.25; margin: 18px 0 6px; color: #2c4f3a; }
h2 { font-size: 1.25em; margin: 22px 0 8px; color: #2c4f3a; }
h3 { font-size: 1.08em; margin: 16px 0 6px; color: #2c4f3a; }
h4 { font-size: 1em; margin: 8px 0 6px; color: #2c4f3a; }
.sotto { color: #444; margin: 0 0 14px; }
nav.salti { position: sticky; top: 0; z-index: 5; display: flex; gap: 6px; overflow-x: auto; padding: 8px 0;
            background: #fbfaf7; border-bottom: 1px solid #e3e0d8; margin-bottom: 14px; }
nav.salti a { flex: none; text-decoration: none; color: #2c4f3a; border: 1px solid #3d6b4f; border-radius: 16px;
              padding: 3px 12px; font-weight: 600; font-size: .9em; }
.intro-box { background: #eef4ef; border: 1px solid #cadbce; border-radius: 8px; padding: 12px 14px; margin: 12px 0 18px; }
.intro-box p { margin: 0 0 8px; }
.intro-box p:last-child { margin-bottom: 0; }
.tab-wrap { overflow-x: auto; margin: 12px 0 20px; }
table.confronto { width: 100%; border-collapse: collapse; background: #fffdf9; border: 1px solid #dfd8c8; font-size: .93em; }
table.confronto th, table.confronto td { border: 1px solid #dfd8c8; padding: 9px 11px; vertical-align: top; text-align: left; }
table.confronto th { background: #efe8d8; color: #263529; font-weight: 700; }
table.confronto td.asp { font-weight: 700; color: #2c4f3a; width: 22%; background: #f7f3ea; }
section.cap { background: #fffdf9; border: 1px solid #e3ded3; border-radius: 10px; padding: 14px 16px; margin: 16px 0; }
section.cap h2 { margin-top: 0; }
section.cap p { margin: 0 0 10px; }
section.cap p:last-child { margin-bottom: 0; }
.sei-colori, .riquadro { background: #f6f3eb; border: 1px solid #dfd8c8; border-radius: 8px; padding: 11px 14px; margin: 12px 0; font-size: .95em; }
.sei-colori ul, .riquadro ul { margin: 6px 0; padding-left: 20px; }
.sei-colori li, .riquadro li { margin-bottom: 4px; }
.rimando { font-size: .9em; color: #444; margin: 6px 0 0; }
.nota-calc { font-size: .9em; color: #555; font-style: italic; margin: 10px 0; }
table.mix { width: 100%; border-collapse: collapse; font-size: .94em; background: #fffdf9; border: 1px solid #dfd8c8; margin-top: 10px; }
table.mix td { border-top: 1px solid #dfd8c8; padding: 8px 10px; vertical-align: top; }
table.mix td.m { font-weight: 700; color: #2c4f3a; white-space: nowrap; width: 3.2em; background: #f7f3ea; text-align: center; }
.cons, .pigm { font-size: .9em; color: #444; }
a.calc { display: inline-block; margin-top: 3px; font-size: .86em; color: #2c4f3a; text-decoration: none;
         border: 1px solid #9ab5a3; border-radius: 10px; padding: 1px 9px; background: #eef4ef; }
a.calc:hover { background: #dfece2; }
footer { margin-top: 28px; border-top: 1px solid #ddd; padding-top: 12px; font-size: .9em; color: #444; }
"""


def pagina():
    d = json.load(open(FONTE, encoding="utf-8"))
    d_alb = json.load(open(FONTE_ALBERI, encoding="utf-8"))
    miscele_html, sei_colori_html, riquadri_html = parte_colori(d_alb["apertura"])

    intro_p = "".join(f"<p>{e(p)}</p>" for p in d["introduzione"])
    righe_conf = "".join(
        f'<tr><td class="asp">{e(r["aspetto"])}</td>'
        f'<td>{e(r["studio"])}</td>'
        f'<td>{e(r["plein_air"])}</td></tr>'
        for r in d["confronto"]
    )

    cap_html = []
    for c in d["capitoli"]:
        pars = "".join(f"<p>{e(p)}</p>" for p in c["paragrafi"])
        extra = ""
        if c["id"] == "tavolozza-plein-air":
            extra = (
                f'{sei_colori_html}'
                f'<div id="miscele"><h3>Le 12 miscele (M1-M12)</h3>'
                f'{riquadri_html}'
                f'<table class="mix">{miscele_html}</table></div>'
            )
        cap_html.append(f'<section class="cap" id="{e(c["id"])}"><h2>{e(c["titolo"])}</h2>{pars}{extra}</section>')

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
<nav class="salti">
  <a href="#confronto">Studio e aperto</a>
  <a href="#tavolozza-studio">Tavolozza estesa</a>
  <a href="#tavolozza-plein-air">Sei colori</a>
  <a href="#miscele">12 miscele</a>
</nav>
<div class="intro-box">{intro_p}</div>

<section class="cap" id="confronto">
  <h2>Studio e aperto a confronto</h2>
  <div class="tab-wrap">
    <table class="confronto">
      <thead>
        <tr>
          <th>Aspetto</th>
          <th>🎨 In studio</th>
          <th>🎒 All'aperto (en plein air)</th>
        </tr>
      </thead>
      <tbody>{righe_conf}</tbody>
    </table>
  </div>
</section>

{"".join(cap_html)}

<footer>
  <p>Le altre sezioni: <a href="../principi/">1. Principi generali</a> · <a href="../colori/">3. Teoria dei colori</a> · <a href="../marche/">4. Marche e tubetti</a> · <a href="../soggetti/">5. Soggetti</a>.</p>
</footer>
</body></html>"""

    open(PAGINA, "w", encoding="utf-8").write(html_out)
    print(f"pagina: {PAGINA} {os.path.getsize(PAGINA) // 1024} KB")


if __name__ == "__main__":
    pagina()

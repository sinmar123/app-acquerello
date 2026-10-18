#!/usr/bin/env python3
"""Genera il sito statico delle guide di acquerello in site/ dai sorgenti delle sezioni in dati/<sezione>/.

Dal 16/10/2026 il repository basta a se stesso: GitHub è la copia principale e i sorgenti delle pagine
non si copiano più da pit/acquerello-* del workspace, dove restano lo studio e i pdf."""
import base64
import io
import pathlib
import subprocess
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

APP_DIR = pathlib.Path(__file__).resolve().parent.parent
SITE_DIR = APP_DIR / "site"
DATI_DIR = APP_DIR / "dati"

SEZIONI = [
    {
        "slug": "principi",
        "numero": "1",
        "titolo": "Principi generali: acqua, colore e carta",
        "sottotitolo": "Da leggere prima degli esercizi: le tre consistenze, gli stati della carta e come abbinarli",
        "descrizione": (
            "Tè, latte e miele; carta asciutta, umida, bagnata e i momenti di mezzo, riconoscibili dal lucido dell'acqua; "
            "come abbinare il pennello alla carta, fioriture comprese; bordi netti e morbidi, asciugatura, "
            "carta hot press, cold press e rough. Ogni frase con la sua fonte, dai corsi e dai video al minuto giusto."
        ),
        "badge": ["8 capitoli", "tè · latte · miele", "stati della carta", "ogni frase con la fonte"],
        "script_genera": DATI_DIR / "principi" / "genera-principi.py",
        "html_generato": DATI_DIR / "principi" / "principi.html",
    },
    {
        "slug": "alberi",
        "numero": "2",
        "titolo": "Alberi ad acquerello: i gesti nei video",
        "sottotitolo": "Sette esercizi su foglietti A5 partendo da 6 colori di base e 12 miscele",
        "descrizione": (
            "Abeti fitti, abeti vecchi, faggi, siepi d'autunno, latifoglie brinate, arbusti in controluce "
            "e riflessi nell'acqua: 35 passi con 39 estratti video al secondo esatto del gesto, "
            "traduzione in italiano del parlato e infografica riepilogativa in 4 fasi."
        ),
        "badge": ["7 esercizi A5", "6 colori · 12 miscele", "39 estratti video", "7 infografiche in 4 fasi"],
        "script_genera": DATI_DIR / "alberi" / "pit-261013-video-gesti.py",
        "html_generato": DATI_DIR / "alberi" / "pit-261014-video-gesti-alberi.html",
    },
    {
        "slug": "colori",
        "numero": "3",
        "titolo": "Teoria dei colori per l'acquerello",
        "sottotitolo": "Munsell, luce e pigmento, acqua e carta, la tavolozza Cotman e un calcolatore di miscele",
        "descrizione": (
            "Tinta, valore e croma secondo Munsell; perché i pigmenti non si mescolano come le luci; "
            "diluizione tè, latte, miele e velature; le schede dei sei tubetti Cotman; un calcolatore "
            "che mescola i tubetti in parti intere e cerca la miscela per un colore scelto, tutto nel browser."
        ),
        "badge": ["5 capitoli", "6 tubetti Cotman", "calcolatore di miscele", "stime da verificare sul foglietto"],
        "script_genera": DATI_DIR / "colori" / "genera-teoria-colori.py",
        "html_generato": DATI_DIR / "colori" / "teoria-colori.html",
    },
]


def miniatura_data_uri(percorso: pathlib.Path, larghezza: int = 720, qualita: int = 80) -> str:
    if not percorso.exists():
        return ""
    im = Image.open(percorso).convert("RGB")
    if im.width > larghezza:
        im = im.resize((larghezza, int(im.height * larghezza / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=qualita, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


def inietta_link_indice(html: str) -> str:
    barra = (
        '<div style="background:#efe6d5;border-bottom:1px solid #d8ccb8;padding:6px 14px;'
        'font-size:.86rem;text-align:center">'
        '<a href="../" style="color:#6b4226;text-decoration:none;font-weight:600">'
        '← Tutte le guide di acquerello</a></div>\n'
    )
    if 'href="../"' in html:
        return html
    return html.replace("<body>", "<body>\n" + barra, 1)


def genera_home(sezioni_pronte: list[dict]) -> str:
    cards = []
    for s in sezioni_pronte:
        badges = "".join(f'<span class="pill">{b}</span>' for b in s.get("badge", []))
        cards.append(
            f"""<article class="card">
  <a class="card-link" href="./{s['slug']}/">
    <div class="card-body">
      <div class="card-head">
        <span class="sig">{s['numero']}</span>
        <div>
          <h2>{s['titolo']}</h2>
          <p class="card-sub">{s['sottotitolo']}</p>
        </div>
      </div>
      <p class="card-desc">{s['descrizione']}</p>
      <div class="pills">{badges}</div>
      <span class="btn">Apri la sezione →</span>
    </div>
  </a>
</article>"""
        )

    cards_html = "\n".join(cards)
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Quaderno di acquerello - Guide pratiche ed esercizi</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#faf6ee;color:#1f1c17;line-height:1.5}}
.testa{{padding:28px 18px 22px;background:#263529;color:#f7f2e7;text-align:center}}
.testa h1{{margin:0 0 6px;font-size:1.45rem;letter-spacing:.01em}}
.testa p{{margin:0 auto;max-width:640px;font-size:.95rem;color:#d8dfd5}}
main{{max-width:820px;margin:0 auto;padding:22px 14px 48px}}
.intro-note{{background:#fffdf8;border:1px solid #dfd5c3;border-left:4px solid #263529;border-radius:8px;padding:12px 15px;margin-bottom:20px;font-size:.92rem;color:#3d352b}}
.grid{{display:grid;grid-template-columns:1fr;gap:18px}}
.card{{background:#fffdf8;border:1px solid #dfd5c3;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(31,28,23,.06);transition:transform .15s ease,box-shadow .15s ease}}
.card:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(31,28,23,.12)}}
.card-link{{display:block;color:inherit;text-decoration:none}}
.card-body{{padding:16px 18px 18px}}
.card-head{{display:flex;align-items:flex-start;gap:12px;margin-bottom:8px}}
.sig{{display:inline-flex;align-items:center;justify-content:center;min-width:32px;height:32px;border-radius:8px;background:#263529;color:#f7f2e7;font-weight:700;font-size:.95rem;margin-top:2px}}
.card-head h2{{margin:0;font-size:1.18rem;color:#1f1c17}}
.card-sub{{margin:2px 0 0;font-size:.9rem;color:#6b5e4c;font-weight:500}}
.card-desc{{margin:10px 0 12px;font-size:.92rem;color:#363027}}
.pills{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}}
.pill{{background:#efe6d5;color:#4f3d27;border:1px solid #d8ccb8;border-radius:999px;padding:3px 10px;font-size:.78rem;font-weight:600}}
.btn{{display:inline-block;background:#263529;color:#f7f2e7;padding:8px 14px;border-radius:8px;font-size:.88rem;font-weight:600}}
footer{{text-align:center;padding:18px;font-size:.8rem;color:#7a6f5d;border-top:1px solid #e5dccb;margin-top:28px}}
</style>
</head>
<body>
<header class="testa">
  <h1>Quaderno di acquerello</h1>
  <p>Guide pratiche per studiare i gesti, le miscele e i passaggi su foglietti di prova</p>
</header>
<main>
  <div class="intro-note">
    Raccolta in crescita di quaderni operativi per esercitarsi ad acquerello: ogni sezione affronta un tema con tavolozza ridotta, estratti video mirati al singolo gesto e schede riepilogative passo per passo.
  </div>
  <div class="grid">
    {cards_html}
  </div>
</main>
<footer>Quaderno di studio ad acquerello · Aggiornato al 18 ottobre 2026</footer>
</body>
</html>
"""


def main():
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    sezioni_pronte = []

    for s in SEZIONI:
        script = s["script_genera"]
        html_src = s["html_generato"]
        if script.exists():
            print(f"[{s['slug']}] Rigenerazione pagina da {script.name}...")
            subprocess.run([sys.executable, str(script), "pagina"], check=True)
        if not html_src.exists():
            raise FileNotFoundError(f"File HTML sorgente non trovato: {html_src}")

        dest_dir = SITE_DIR / s["slug"]
        dest_dir.mkdir(parents=True, exist_ok=True)
        html_text = html_src.read_text(encoding="utf-8")
        html_con_barra = inietta_link_indice(html_text)
        dest_html = dest_dir / "index.html"
        dest_html.write_text(html_con_barra, encoding="utf-8")
        print(f"[{s['slug']}] Scritto {dest_html.relative_to(APP_DIR)} ({dest_html.stat().st_size // 1024} KB)")

        sezioni_pronte.append(dict(s))

    index_html = SITE_DIR / "index.html"
    index_html.write_text(genera_home(sezioni_pronte), encoding="utf-8")
    print(f"[home] Scritto {index_html.relative_to(APP_DIR)} ({index_html.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

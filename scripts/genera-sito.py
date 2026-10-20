#!/usr/bin/env python3
"""Genera il sito statico delle guide di acquerello in site/ dai sorgenti delle sezioni in dati/<sezione>/.

Il repository è autonomo: contiene tutti i file di dati, le infografiche e gli script necessari a generare le pagine."""
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
        "nome_form": "Principi",
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
        "nome_form": "Alberi",
        "titolo": "Alberi ad acquerello: esempi, modalità e gesti nei video",
        "sottotitolo": "Sei esempi di alberi e arbusti con 24 modalità nei video, un'infografica per ciascun video e colori liberi in studio o 6 all'aperto",
        "descrizione": (
            "Abeti e conifere in gruppo, abeti alti e radi contro il cielo, chiome tonde d'autunno, siepi e cespugli, "
            "alberi invernali con fusti chiari e brina, rami sottili e foglie brinate in primo piano: per ciascun esempio "
            "i video propongono diverse modalità di sviluppo, ognuna spiegata da un'infografica in 3 fasi e da 31 estratti video al secondo esatto."
        ),
        "badge": ["6 esempi di alberi", "24 modalità e infografiche", "31 estratti video", "colori liberi in studio · 6 all'aperto"],
        "script_genera": DATI_DIR / "alberi" / "pit-261013-video-gesti.py",
        "html_generato": DATI_DIR / "alberi" / "pit-261014-video-gesti-alberi.html",
    },
    {
        "slug": "colori",
        "numero": "3",
        "nome_form": "Teoria dei colori",
        "titolo": "Teoria dei colori per l'acquerello",
        "sottotitolo": "Munsell, luce e pigmento, velature, i sei colori di base e un calcolatore di miscele",
        "descrizione": (
            "Tinta, valore e croma secondo Munsell; perché i pigmenti non si mescolano come le luci; "
            "mescolare o velare; le schede dei sei colori della tavolozza ridotta, col nome comune e il pigmento; un calcolatore "
            "che mescola i tubetti in parti intere e cerca la miscela per un colore scelto, tutto nel browser."
        ),
        "badge": ["5 capitoli", "6 colori di base", "calcolatore di miscele", "stime da verificare sul foglietto"],
        "script_genera": DATI_DIR / "colori" / "genera-teoria-colori.py",
        "html_generato": DATI_DIR / "colori" / "teoria-colori.html",
    },
    {
        "slug": "marche",
        "numero": "4",
        "nome_form": "Confronto marche",
        "titolo": "Marche e tubetti",
        "sottotitolo": "I sei colori di base nelle serie in commercio: nome del tubetto, numero, pigmento e trasparenza",
        "descrizione": (
            "Per ognuno dei sei colori della tavolozza ridotta, il tubetto corrispondente in sei serie: Winsor &amp; Newton Cotman e Professional, "
            "Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu. Dati solo dalle pagine ufficiali, con il link "
            "e la data di controllo su ogni riga; e perché lo stesso nome nasconde pigmenti diversi."
        ),
        "badge": ["6 serie", "6 colori di base", "fonte ufficiale su ogni riga", "stesso nome, pigmenti diversi"],
        "script_genera": DATI_DIR / "marche" / "genera-marche.py",
        "html_generato": DATI_DIR / "marche" / "marche.html",
    },
]

OPZIONI_SEZIONE = [
    "Generale / Nuovo argomento",
    "Principi",
    "Alberi",
    "Teoria dei colori",
    "Confronto marche",
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


def blocco_casella_suggerimenti(sezione_predefinita: str, pagina_path: str) -> str:
    opts = []
    for opz in OPZIONI_SEZIONE:
        sel = " selected" if opz == sezione_predefinita else ""
        opts.append(f'<option value="{opz}"{sel}>{opz}</option>')
    options_html = "".join(opts)

    return f"""
<style>
.sugg-wrap{{max-width:820px;margin:28px auto 18px;padding:0 14px;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.sugg-box{{background:#fffdf8;border:1px solid #d8ccb8;border-left:4px solid #2f5e4e;border-radius:10px;padding:18px 20px;box-shadow:0 2px 8px rgba(31,28,23,.05);color:#1f1c17}}
.sugg-box h2{{margin:0 0 6px;font-size:1.15rem;color:#263529}}
.sugg-sub{{margin:0 0 14px;font-size:.9rem;color:#4a4236;line-height:1.45}}
.sugg-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}}
@media(max-width:600px){{.sugg-grid{{grid-template-columns:1fr}}}}
.sugg-field{{display:flex;flex-direction:column;gap:4px;margin-bottom:12px}}
.sugg-field label{{font-size:.83rem;font-weight:600;color:#3d352b}}
.sugg-field input,.sugg-field select,.sugg-field textarea{{font:inherit;font-size:.92rem;padding:8px 10px;border:1px solid #c9bba3;border-radius:6px;background:#ffffff;color:#1f1c17}}
.sugg-field textarea{{min-height:92px;resize:vertical}}
.sugg-avviso{{background:#f5efe2;border:1px solid #dfd3be;border-radius:7px;padding:10px 12px;margin:10px 0 14px;font-size:.82rem;color:#3d352b;line-height:1.45}}
.sugg-avviso a{{color:#2f5e4e;font-weight:600}}
.sugg-actions{{display:flex;flex-wrap:wrap;align-items:center;gap:12px}}
.sugg-btn{{background:#263529;color:#f7f2e7;border:0;border-radius:7px;padding:9px 16px;font:inherit;font-size:.9rem;font-weight:600;cursor:pointer}}
.sugg-btn:hover{{background:#1c281f}}
.sugg-btn:disabled{{opacity:.6;cursor:wait}}
.sugg-link-gh{{font-size:.82rem;color:#5c5142;text-decoration:none}}
.sugg-link-gh:hover{{text-decoration:underline}}
.sugg-esito{{margin-top:12px;padding:10px 12px;border-radius:7px;font-size:.88rem;display:none}}
.sugg-esito.ok{{display:block;background:#e6f4ea;border:1px solid #a8dab5;color:#135225}}
.sugg-esito.err{{display:block;background:#fce8e6;border:1px solid #f5c2c0;color:#7a1c18}}
.sugg-hp{{position:absolute;left:-9999px;opacity:0;pointer-events:none;height:0;overflow:hidden}}
</style>
<section id="suggerimenti" class="sugg-wrap" aria-label="Invia un suggerimento">
  <div class="sugg-box">
    <h2>💬 Suggerisci una modifica, una correzione o un video</h2>
    <p class="sugg-sub">
      Hai trovato un refuso, conosci un bel passaggio in un video su YouTube (magari indicando il minuto esatto) o vuoi proporre un'aggiunta?
      Scrivilo qui sotto senza bisogno di conoscere GitHub o il codice: se la proposta è valida la inseriamo nel quaderno.
    </p>
    <form id="form-suggerimento" data-pagina="{pagina_path}">
      <div class="sugg-hp" aria-hidden="true">
        <label>Non compilare questo campo <input type="text" name="miele" tabindex="-1" autocomplete="off"></label>
      </div>
      <div class="sugg-grid">
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-sezione">Sezione</label>
          <select id="sugg-sezione" name="sezione">
            {options_html}
          </select>
        </div>
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-firma">Il tuo nome o soprannome (facoltativo)</label>
          <input id="sugg-firma" name="firma" type="text" maxlength="60" placeholder="Lascia vuoto per restare anonimo">
        </div>
      </div>
      <div class="sugg-field" style="margin-top:12px">
        <label for="sugg-titolo">Titolo breve *</label>
        <input id="sugg-titolo" name="titolo" type="text" required minlength="4" maxlength="120" placeholder="Es. Nuovo video sul pino marittimo / Correzione su un pigmento">
      </div>
      <div class="sugg-field">
        <label for="sugg-testo">Il tuo suggerimento *</label>
        <textarea id="sugg-testo" name="testo" required minlength="10" maxlength="3500" placeholder="Descrivi la proposta o la correzione. Se segnali un video YouTube, incolla il link e indica da che minuto a che minuto si vede il passaggio utile."></textarea>
      </div>
      <div class="sugg-avviso">
        <strong>Avviso sulla pubblicazione:</strong> non serve registrarsi né avere un account.
        Premendo <em>Invia suggerimento</em>, il testo che hai scritto e l'eventuale nome o soprannome
        <strong>saranno pubblicati pubblicamente</strong> nella bacheca aperta delle
        <a href="https://github.com/sinmar123/app-acquerello/issues" target="_blank" rel="noopener">segnalazioni del progetto su GitHub</a>
        (sotto licenza aperta CC BY 4.0) per essere valutati e integrati nel sito.
        <strong>Non inserire indirizzi email, numeri di telefono o altri dati personali riservati.</strong>
      </div>
      <div class="sugg-actions">
        <button type="submit" class="sugg-btn" id="sugg-submit">Invia suggerimento</button>
        <a class="sugg-link-gh" href="https://github.com/sinmar123/app-acquerello/issues" target="_blank" rel="noopener">Vedi le segnalazioni già pubblicate →</a>
      </div>
      <div id="sugg-esito" class="sugg-esito" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
<script>
(function(){{
  var form = document.getElementById("form-suggerimento");
  if (!form) return;
  var btn = document.getElementById("sugg-submit");
  var esito = document.getElementById("sugg-esito");
  form.addEventListener("submit", async function(ev) {{
    ev.preventDefault();
    esito.className = "sugg-esito";
    esito.style.display = "none";
    var dati = {{
      sezione: form.sezione.value,
      firma: form.firma.value.trim(),
      titolo: form.titolo.value.trim(),
      testo: form.testo.value.trim(),
      miele: form.miele.value,
      pagina: form.getAttribute("data-pagina") || window.location.pathname
    }};
    btn.disabled = true;
    btn.textContent = "Invio in corso...";
    try {{
      var r = await fetch("/api/suggerimento", {{
        method: "POST",
        headers: {{"Content-Type": "application/json"}},
        body: JSON.stringify(dati)
      }});
      var risp = await r.json();
      if (r.ok && risp.ok) {{
        esito.className = "sugg-esito ok";
        esito.innerHTML = 'Grazie! La tua segnalazione (<strong>#' + risp.numero + '</strong>) è stata pubblicata: <a href="' + risp.url + '" target="_blank" rel="noopener">aprila su GitHub</a>.';
        form.titolo.value = "";
        form.testo.value = "";
      }} else {{
        throw new Error((risp && risp.errore) || "Errore durante l'invio.");
      }}
    }} catch (err) {{
      esito.className = "sugg-esito err";
      var ghUrl = "https://github.com/sinmar123/app-acquerello/issues/new?title=" +
        encodeURIComponent("[Suggerimento · " + dati.sezione + "] " + dati.titolo) +
        "&body=" + encodeURIComponent(dati.testo);
      esito.innerHTML = (err.message || "Impossibile inviare direttamente.") +
        ' Puoi comunque <a href="' + ghUrl + '" target="_blank" rel="noopener">inviare la segnalazione su GitHub da questo link precompilato</a>.';
    }} finally {{
      btn.disabled = false;
      btn.textContent = "Invia suggerimento";
    }}
  }});
}})();
</script>
"""


def inietta_elementi_comuni(html: str, sezione_predefinita: str, pagina_path: str) -> str:
    barra = (
        '<div style="background:#efe6d5;border-bottom:1px solid #d8ccb8;padding:6px 14px;'
        'font-size:.86rem;display:flex;justify-content:center;gap:18px;flex-wrap:wrap">'
        '<a href="../" style="color:#6b4226;text-decoration:none;font-weight:600">'
        '← Tutte le guide di acquerello</a>'
        '<a href="#suggerimenti" style="color:#2f5e4e;text-decoration:none;font-weight:600">'
        '💬 Suggerisci una modifica o un video</a></div>\n'
    )
    if 'href="../"' not in html:
        html = html.replace("<body>", "<body>\n" + barra, 1)

    blocco = blocco_casella_suggerimenti(sezione_predefinita, pagina_path)
    if 'id="suggerimenti"' not in html:
        if "<footer" in html:
            html = html.replace("<footer", blocco + "\n<footer", 1)
        else:
            html = html.replace("</body>", blocco + "\n</body>", 1)
    return html


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
    blocco_sugg = blocco_casella_suggerimenti("Generale / Nuovo argomento", "/")
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quaderno di acquerello - Guide pratiche ed esercizi</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#faf6ee;color:#1f1c17;line-height:1.5}}
.testa{{padding:28px 18px 22px;background:#263529;color:#f7f2e7;text-align:center}}
.testa h1{{margin:0 0 6px;font-size:1.45rem;letter-spacing:.01em}}
.testa p{{margin:0 auto;max-width:640px;font-size:.95rem;color:#d8dfd5}}
main{{max-width:820px;margin:0 auto;padding:22px 14px 12px}}
.intro-note{{background:#fffdf8;border:1px solid #dfd5c3;border-left:4px solid #263529;border-radius:8px;padding:12px 15px;margin-bottom:20px;font-size:.92rem;color:#3d352b}}
.intro-note a{{color:#2f5e4e;font-weight:600}}
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
footer{{text-align:center;padding:18px;font-size:.82rem;color:#7a6f5d;border-top:1px solid #e5dccb;margin-top:24px}}
footer a{{color:#5a4d3b}}
</style>
</head>
<body>
<header class="testa">
  <h1>Quaderno di acquerello</h1>
  <p>Guide pratiche per studiare i gesti, le miscele e i passaggi su foglietti di prova</p>
</header>
<main>
  <div class="intro-note">
    Raccolta aperta e in crescita di quaderni operativi per esercitarsi ad acquerello: ogni sezione affronta un tema con proposte di colore libere per lo studio e tavolozza ridotta da 6 colori per l'aperto, estratti video mirati al singolo gesto e infografiche passo per passo.
    In fondo a ogni pagina puoi <a href="#suggerimenti">inviare un suggerimento o segnalare un video</a>.
  </div>
  <div class="grid">
    {cards_html}
  </div>
</main>
{blocco_sugg}
<footer>
  Quaderno di studio ad acquerello · Progetto aperto su <a href="https://github.com/sinmar123/app-acquerello" target="_blank" rel="noopener">GitHub</a>
  (testi e schede <a href="https://creativecommons.org/licenses/by/4.0/deed.it" target="_blank" rel="noopener">CC BY 4.0</a>, codice MIT)
</footer>
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
        html_completo = inietta_elementi_comuni(
            html_text,
            s.get("nome_form", "Generale / Nuovo argomento"),
            f"/{s['slug']}/",
        )
        dest_html = dest_dir / "index.html"
        dest_html.write_text(html_completo, encoding="utf-8")
        print(f"[{s['slug']}] Scritto {dest_html.relative_to(APP_DIR)} ({dest_html.stat().st_size // 1024} KB)")

        sezioni_pronte.append(dict(s))

    index_html = SITE_DIR / "index.html"
    index_html.write_text(genera_home(sezioni_pronte), encoding="utf-8")
    print(f"[home] Scritto {index_html.relative_to(APP_DIR)} ({index_html.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

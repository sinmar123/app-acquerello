# Prova vera della pagina dei gesti in Chrome, da un indirizzo web locale (14/10/2026).
# Per ogni pezzo chiesto clicca «Guarda il gesto», misura dove il video parte e dove si ferma
# (window.statoGesto della pagina) e salva tre schermate in formato telefono: l'apertura, il primo
# albero e il primo pezzo chiesto.
#
#   python -m http.server 8765 --bind 127.0.0.1 --directory dati/alberi      (dalla radice del repository, in un'altra finestra)
#   uv run --with playwright python dati/alberi/pit-261014-prova-pagina.py http://127.0.0.1:8765/pit-261014-video-gesti-alberi.html CARTELLA A1-1 A1-2 ...
#
# Usa il Chrome installato (channel="chrome"), senza scaricare browser. Un pezzo è «ok» se parte
# entro 1 s dall'inizio della tabella e si ferma entro 1 s dalla fine. Aperta come file, la pagina
# non fa partire i video: la prova va fatta sempre dall'indirizzo web.
import json, sys, time
from playwright.sync_api import sync_playwright

url, cartella, pezzi = sys.argv[1], sys.argv[2], sys.argv[3:]
esiti = []
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True, args=["--autoplay-policy=no-user-gesture-required"])
    pg = b.new_page(viewport={"width": 412, "height": 900}, device_scale_factor=2)
    errori = []
    pg.on("pageerror", lambda e: errori.append(str(e)))
    pg.goto(url, wait_until="load")
    pg.screenshot(path=f"{cartella}/telefono-apertura.png")
    pg.locator("#A1").scroll_into_view_if_needed()
    pg.screenshot(path=f"{cartella}/telefono-A1.png")
    for sigla in pezzi:
        v = pg.locator(f'.video[data-passo="{sigla}"]')
        inizio, fine = float(v.get_attribute("data-inizio")), float(v.get_attribute("data-fine"))
        v.locator("button.guarda").click()
        t0 = time.time()
        primo, ultimo, fermo = None, None, None
        while time.time() - t0 < (fine - inizio) + 25:
            s = pg.evaluate("window.statoGesto && window.statoGesto()")
            if s and s["passo"] == sigla:
                if s["stato"] == 1 and primo is None:
                    primo = s["tempo"]
                ultimo = s
                if primo is not None and s["stato"] in (0, 2) and s["tempo"] >= fine - 1.5:
                    time.sleep(1.2)
                    fermo = pg.evaluate("window.statoGesto()")
                    break
            time.sleep(0.25)
        if sigla == pezzi[0]:
            v.screenshot(path=f"{cartella}/telefono-pezzo-{sigla}.png")
        esiti.append({"pezzo": sigla, "inizio": inizio, "fine": fine,
                      "primo_tempo_in_riproduzione": None if primo is None else round(primo, 2),
                      "fermo_a": None if fermo is None else round(fermo["tempo"], 2),
                      "stato_finale": (fermo or ultimo or {}).get("stato"),
                      "ok": primo is not None and fermo is not None and abs(primo - inizio) <= 1.0
                            and fermo["stato"] in (0, 2) and abs(fermo["tempo"] - fine) <= 1.0})
    b.close()
print(json.dumps({"errori_js": errori, "esiti": esiti}, ensure_ascii=False, indent=1))

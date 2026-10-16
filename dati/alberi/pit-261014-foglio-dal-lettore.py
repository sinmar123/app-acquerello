# Foglio di controllo ricavato dal lettore di YouTube dentro la pagina dei gesti (14/10/2026).
# Allarga la finestra di un pezzo, lo fa scorrere in Chrome e fotografa lo schermo del video una
# volta al secondo, in un foglio a griglia come quelli di «controllo» di pit-261013-video-gesti.py.
# Serve quando il flusso diretto (yt-dlp e ffmpeg) è troppo lento: sul W520, il 14/10, alcuni video
# non davano un fotogramma in mezz'ora, mentre nel lettore scorrevano senza intoppi.
#
#   python -m http.server 8765 --bind 127.0.0.1 --directory dati/alberi      (dalla radice del repository, in un'altra finestra)
#   uv run --with playwright --with pillow python dati/alberi/pit-261014-foglio-dal-lettore.py http://127.0.0.1:8765/pit-261014-video-gesti-alberi.html A1-1 82 110 foglio.jpg
#
# PEZZO è la sigla di un pezzo già nella pagina (ne usa il video); DA e A sono i secondi della
# finestra da guardare, anche fuori dal pezzo. Il foglio va scritto fuori dal workspace.
import io, sys, time
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

url, pezzo, da, a, uscita = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
quadri = []
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True, args=["--autoplay-policy=no-user-gesture-required"])
    pg = b.new_page(viewport={"width": 800, "height": 900})
    pg.goto(url, wait_until="load")
    v = pg.locator(f'.video[data-passo="{pezzo}"]')
    v.evaluate(f"(el) => {{ el.dataset.inizio = '{da}'; el.dataset.fine = '{a}'; }}")
    v.locator("button.guarda").click()
    schermo = v.locator(".schermo")
    visti = set()
    t0 = time.time()
    while time.time() - t0 < (a - da) + 30:
        s = pg.evaluate("window.statoGesto && window.statoGesto()")
        if s and s["stato"] == 1:
            sec = int(s["tempo"])
            if sec not in visti and da <= sec < a:
                visti.add(sec)
                quadri.append((sec, Image.open(io.BytesIO(schermo.screenshot())).convert("RGB")))
        if s and s["stato"] in (0, 2) and s["tempo"] >= a - 1:
            break
        time.sleep(0.1)
    b.close()

col, lato = 6, 300
quadri.sort()
ims = [(t, im.resize((lato, int(im.height * lato / im.width)))) for t, im in quadri]
h = max(im.height for _, im in ims)
righe = (len(ims) + col - 1) // col
out = Image.new("RGB", (lato * col, 40 + righe * (h + 4)), "white")
dr = ImageDraw.Draw(out)
font = ImageFont.truetype("arialbd.ttf", 22)
dr.text((8, 8), f"{pezzo} · dal lettore della pagina, {da // 60:02d}:{da % 60:02d}-{a // 60:02d}:{a % 60:02d}, un fotogramma al secondo", fill="black", font=font)
for i, (t, im) in enumerate(ims):
    x, y = (i % col) * lato, 40 + (i // col) * (h + 4)
    out.paste(im, (x, y))
    dr.rectangle([x, y, x + 74, y + 26], fill="black")
    dr.text((x + 5, y + 1), f"{t // 60:02d}:{t % 60:02d}", fill="yellow", font=font)
out.save(uscita, quality=85)
print(uscita, len(ims), "fotogrammi:", [t for t, _ in ims])

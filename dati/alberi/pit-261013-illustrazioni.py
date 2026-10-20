# Illustrazioni e immagini di riferimento per gli alberi ad acquerello: Nano Banana 2.1 (gemini-nano-banana-2.1).
#   python pit-261013-illustrazioni.py [A1 A3 ...]               (illustrazioni dei gesti, solo da testo)
#   python pit-261013-illustrazioni.py --riferimenti [A1 A3 ...] (7 immagini iniziali della pagina, da ritaglio + testo)
# SUFFISSO=-v2 nell'ambiente per non sovrascrivere. Salva PNG in illustrazioni/ e registra i token usati.
# Genera le illustrazioni nella sottocartella illustrazioni/ usando l'API Gemini (variabile GEMINI_API_KEY).
import base64, io, json, os, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageOps

MODELLO = "gemini-nano-banana-2.1"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELLO}:generateContent"
QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(QUI, "illustrazioni")
_WKS = QUI
for _ in range(5):
    _WKS = os.path.dirname(_WKS)
FOTO = os.path.join(_WKS, "pit", "acquerello-corso-avanzato-2026-27", "schizzi+foto")
REG = os.path.join(os.environ.get("TEMP", "."), "pit-alberi", "tutorial", "illustra-registro.jsonl")
CODA = " Natural daylight, realistic photo, clean desk. No text, no letters, no watermark, no logos."
PROMPT = {
 "A1-spina-di-pesce": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper with a pale yellow-green wash already dry. A hand holds a round watercolor brush and is painting a small fir tree: a thin vertical trunk line, and short herringbone strokes made with the belly of the brush, angled downward and getting longer toward the bottom, in dark green. Fresh paint looks slightly glossy.",
 "A2-piani-staccati": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper. A tall slender fir tree is painted against a pale blue sky wash: a long thin pale cream trunk, and short separate tiers of dark green branches made with quick oblique strokes from top to bottom, with clear gaps of blue sky showing between the tiers, ragged edges, pointed top. A round brush rests next to the painting.",
 "A3-rosso-sul-bagnato": "Overhead close-up photograph of a loose watercolor landscape sketch in progress on white cold-press watercolor paper. An autumn beech tree is painted as an irregular crown of three or four rounded foliage clumps, ragged edges, in warm orange and copper, still wet and shiny, with a few thin branches and a short trunk visible below. The tip of a round watercolor brush is dropping dark red-brown paint into the lower part of the wet crown, where it spreads softly and blooms into the orange (wet-in-wet).",
 "A4-base-scura": "Overhead close-up photograph of a loose watercolor landscape sketch in progress on white cold-press watercolor paper. A low garden hedge seen from the front, painted flat like in a landscape painting (no box, no perspective): a long soft cushion of copper-red and orange foliage with an irregular leafy top edge. A round watercolor brush is adding dense dark red-brown dabs in a narrow band along the bottom of the hedge, while the top stays lighter and warmer. A pale grey-lilac strip of frosty lawn is painted below it.",
 "A5-sale": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper. A damp, matte lilac-grey watercolor wash with soft pale golden areas at the top; fingers sprinkle a few grains of coarse table salt onto the damp wash, and small pale star-shaped speckles are appearing where the salt grains sit, like frost.",
 "A6-mascherante": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper. Several oval leaves on thin twigs are painted in very dark green-black over a pale blue wash. A hand rubs a small beige crepe rubber eraser over dried masking fluid, peeling it off and revealing thin bright white lines along the edges of the dark leaves, like frost.",
 "A7-tavola-inclinata": "Photograph of a watercolor painting in progress, the board tilted almost vertically on a table. Autumn trees in orange and olive green are painted along a shoreline in the upper part; below the shoreline, on wet paper, their reflections run down in soft vertical streaks, the colors bleeding gently downward into a pale blue water area.",
}

CODA_RIF = (" Generate a clean, high-definition outdoor nature photograph that stays VERY close to this reference image "
            "in composition, tree shapes, branch structure, lighting, and color palette, while removing the printed-paper "
            "halftone texture, any stray foreground twigs at the very bottom edge, any text/logos, and replacing any "
            "building/castle walls with natural trees and hillside.")

RIFERIMENTI = {
 "A1-abeti-fitti": {
  "file": "pit-261013-riferimento-dettaglio-abeti-sinistra.jpg",
  "box": [440, 260, 3740, 2960],
  "prompt": "Recreate this exact landscape scene as a crisp, clean outdoor photograph staying very close to the reference: on the left and center, the dense group of tall conical fir/spruce trees with varied peak heights, sunlit olive-green herringbone branches, and narrow glimpses of pale trunks in the gaps; behind them, the same sunlit golden-ochre rocky mountain peak against the clear blue sky; on the right, the warm copper-orange autumn beech foliage next to the firs (replace the small piece of castle wall on the far right edge with natural trees and bushes); at the bottom, the warm golden-brown lakeshore bank.",
 },
 "A2-abeti-alti": {
  "file": "pit-261013-riferimento-dettaglio-abeti-destra.jpg",
  "box": [1150, 300, 3860, 2880],
  "prompt": "Recreate this exact landscape scene as a crisp, clean outdoor photograph staying very close to the reference: in the center-right, the two tall, slender, sparse old fir/pine trees rising high against the clear pale-blue sky, keeping their distinct separated horizontal branch tiers with blue sky showing through and the thin pale trunk visible in the gaps; to their left, lower conifers and warm autumn trees; in the lower-right foreground, the shaded blue-violet frosty deciduous trees and pale cream birch trunks; in the background, the blue-grey mountain ridges and golden sunlit slope on the left (replace the yellow building on the far lower-left edge with natural hillside and autumn bushes).",
 },
 "A3-faggi-autunno": {
  "file": "pit-261013-riferimento-dettaglio-abeti-sinistra.jpg",
  "box": [1500, 750, 3740, 2960],
  "prompt": "Recreate this exact landscape scene as a crisp, clean outdoor photograph staying very close to the reference: in the center, the rounded billowy autumn beech crowns with golden-orange sunlit tops, rich copper-red middle foliage, dark red-brown lower hollows, and fine pale twigs showing inside the crown mass; on the left, the tall dark-green fir trees meeting the warm orange beech foliage; behind, the sunlit golden-ochre rocky mountain slope; on the right edge, replace the small piece of building wall with natural green and copper foliage.",
 },
 "A4-siepi-rame": {
  "file": "pit-261013-riferimento-dettaglio-abeti-destra.jpg",
  "box": [0, 1850, 2250, 2880],
  "prompt": "Recreate this exact landscape scene as a crisp, clean outdoor photograph staying very close to the reference: on the terraced bank above the water, the low, wide flat-topped copper-orange and rust-red hedges with dark red-brown shadow along their base, the rounded dark green bush dome in the middle gap, the autumn bushes and dark conifers on the right, and the frosty pale grey-lilac and sunlit grass strip sloping down toward the water in the foreground. Behind the hedges on the upper left, replace the yellow building facade with natural autumn trees and sunlit golden hillside.",
 },
 "A5-latifoglie-brinate": {
  "file": "pit-261013-riferimento-dettaglio-abeti-destra.jpg",
  "box": [1800, 800, 3860, 2920],
  "prompt": "Recreate this exact landscape scene as a crisp, clean outdoor photograph staying very close to the reference: on the right and center, the bare frosty deciduous trees on the shaded slope with slender pale cream trunks and Y-shaped branches standing out against the deep dark blue-violet shaded undergrowth below, and the delicate misty cloud of fine bare twigs above (warm golden-orange at the sunlit top, cool grey-lilac frost below); on the left, the tall sparse fir trees with separated branch tiers; in the background, the blue-violet mountain ridge.",
 },
 "A6-arbusti-brinati": {
  "file": "pit-261013-riferimento-stampa-intera.jpg",
  "box": [300, 1780, 3550, 2810],
  "prompt": "Recreate this exact foreground scene as a crisp, clean outdoor photograph staying very close to the reference: in the foreground, the backlit winter shrubs with thin dark intersecting twigs rising from the bottom and small oval dark leaves in silhouette, each leaf and twig sharply rimmed with a thin glowing white-blue line of morning frost. In the soft-focus background behind the shrubs, keep the calm lake water with vertical green, copper-orange, and blue tree reflections (replace the yellow building reflection in the middle water with natural tree and hillside reflections).",
 },
 "A7-riflessi-acqua": {
  "file": "pit-261013-riferimento-stampa-intera.jpg",
  "box": [100, 1480, 3880, 2810],
  "prompt": "Recreate this exact lakeshore reflection scene as a crisp, clean outdoor photograph staying very close to the reference: along the upper part, the lakeshore with dense green firs on the left, copper-orange autumn trees and low copper hedges with frosty lawn in the center, and shaded blue-violet frosty bushes on the right (replace the castle building in the upper center with natural autumn trees and golden hillside). Across the lower two-thirds, the calm lake water mirroring the green firs, warm copper foliage, and blue-violet shaded bank in soft vertical streaks fading into pale blue sky reflection at the bottom, with dark shadow right under the shoreline and fine pale horizontal ripples.",
 },
}

def _chiama_api(parti_input, ratio, dest, etichetta_reg):
    corpo = {"contents": [{"parts": parti_input}],
             "generationConfig": {"responseModalities": ["TEXT", "IMAGE"], "imageConfig": {"aspectRatio": ratio}}}
    req = urllib.request.Request(URL, data=json.dumps(corpo).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    for tentativo in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                risposta = json.load(r)
            break
        except urllib.error.HTTPError as e:
            testo = e.read().decode("utf-8", "replace")[:400]
            if e.code in (429, 500, 503) and tentativo < 2:
                time.sleep(20 * (tentativo + 1)); continue
            return etichetta_reg, f"HTTP {e.code}: {testo}"
    uso = risposta.get("usageMetadata", {})
    parti = (risposta.get("candidates") or [{}])[0].get("content", {}).get("parts", [])
    for p in parti:
        if "inlineData" in p:
            im = Image.open(io.BytesIO(base64.b64decode(p["inlineData"]["data"]))).convert("RGB")
            os.makedirs(OUT, exist_ok=True)
            im.save(dest, "PNG")
            os.makedirs(os.path.dirname(REG), exist_ok=True)
            with open(REG, "a", encoding="utf-8") as f:
                f.write(json.dumps({"nome": etichetta_reg, "modello": risposta.get("modelVersion", MODELLO), "uso": uso,
                                    "quando": time.strftime("%Y-%m-%d %H:%M:%S")}, ensure_ascii=False) + "\n")
            return etichetta_reg, f"ok {im.size} -> {dest}"
    return etichetta_reg, "nessuna immagine: " + json.dumps(risposta)[:400]

def genera(nome, suffisso=""):
    dest = os.path.join(OUT, f"pit-261013-illustrazione-{nome}{suffisso}.png")
    return _chiama_api([{"text": PROMPT[nome] + CODA}], "4:3", dest, nome + suffisso)

def genera_riferimento(nome, suffisso=""):
    cfg = RIFERIMENTI[nome]
    if cfg.get("solo_testo"):
        parti_in = [{"text": cfg["prompt"] + CODA_RIF}]
    else:
        im_src = ImageOps.exif_transpose(Image.open(os.path.join(FOTO, cfg["file"]))).convert("RGB")
        if cfg.get("box"):
            im_src = im_src.crop(tuple(cfg["box"]))
        im_src.thumbnail((1024, 1024))
        buf = io.BytesIO()
        im_src.save(buf, "JPEG", quality=85)
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        parti_in = [
            {"inlineData": {"mimeType": "image/jpeg", "data": b64}},
            {"text": cfg["prompt"] + CODA_RIF},
        ]
    dest = os.path.join(OUT, f"pit-261015-riferimento-{nome}{suffisso}.png")
    return _chiama_api(parti_in, "16:9", dest, f"rif-{nome}{suffisso}")

if __name__ == "__main__":
    args = sys.argv[1:]
    suffisso = os.environ.get("SUFFISSO", "")
    if args and args[0] == "--riferimenti":
        filtro = args[1:]
        nomi = [n for n in RIFERIMENTI if not filtro or n.split("-")[0] in filtro]
        with ThreadPoolExecutor(max_workers=4) as ex:
            for nome, esito in ex.map(lambda n: genera_riferimento(n, suffisso), nomi):
                print(nome, esito, flush=True)
    else:
        nomi = [n for n in PROMPT if not args or n.split("-")[0] in args]
        with ThreadPoolExecutor(max_workers=4) as ex:
            for nome, esito in ex.map(lambda n: genera(n, suffisso), nomi):
                print(nome, esito, flush=True)

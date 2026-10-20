# Illustrazioni dei gesti per gli alberi ad acquerello: Nano Banana 2.1 (gemini-nano-banana-2.1).
#   python pit-261013-illustrazioni.py [A1 A3 ...]
# SUFFISSO=-v2 nell'ambiente per non sovrascrivere. Salva PNG in illustrazioni/ e registra i token usati.
# Genera le illustrazioni nella sottocartella illustrazioni/ usando l'API Gemini (variabile GEMINI_API_KEY).
import base64, io, json, os, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

MODELLO = "gemini-nano-banana-2.1"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELLO}:generateContent"
QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(QUI, "illustrazioni")
REG = os.path.join(os.environ.get("TEMP", "."), "pit-alberi", "tutorial", "illustra-registro.jsonl")
CODA = " Natural daylight, realistic photo, clean desk. No text, no letters, no watermark, no logos."
PROMPT = {
 "A1-spina-di-pesce": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper with a pale yellow-green wash already dry. A hand holds a round watercolor brush and is painting a small fir tree: a thin vertical trunk line, and short herringbone strokes made with the belly of the brush, angled downward and getting longer toward the bottom, in dark green. Fresh paint looks slightly glossy.",
 "A2-piani-staccati": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper. A tall slender fir tree is painted against a pale blue sky wash: a long thin pale cream trunk, and short separate tiers of dark green branches made with quick oblique strokes from top to bottom, with clear gaps of blue sky showing between the tiers, ragged edges, pointed top. A round brush rests next to the painting.",
 "A3-rosso-sul-bagnato": "Overhead close-up photograph of a loose watercolor landscape sketch in progress on white cold-press watercolor paper. An autumn beech tree is painted as an irregular crown of three or four rounded foliage clumps, ragged edges, in warm orange and copper, still wet and shiny, with a few thin branches and a short trunk visible below. The tip of a round watercolor brush is dropping dark red-brown paint into the lower part of the wet crown, where it spreads softly and blooms into the orange (wet-in-wet).",
 "A4-base-scura": "Overhead close-up photograph of a loose watercolor landscape sketch in progress on white cold-press watercolor paper. A low garden hedge seen from the front, painted flat like in a landscape painting (no box, no perspective): a long soft cushion of copper-red and orange foliage with an irregular leafy top edge. A round watercolor brush is adding dense dark red-brown dabs in a narrow band along the bottom of the hedge, while the top stays lighter and warmer. A pale grey-lilac strip of frosty lawn is painted below it.",
 "A5-sale": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper. A damp, matte lilac-grey watercolor wash with soft pale golden areas at the top; fingers sprinkle a few grains of coarse table salt onto the damp wash, and small pale star-shaped speckles are appearing where the salt grains sit, like frost.",
 "A6-mascherante": "Overhead close-up photograph of a watercolor painting in progress on white cold-press watercolor paper. Several oval leaves on thin twigs are painted in very dark green-black over a pale blue wash. A hand rubs a small beige crepe rubber eraser over dried masking fluid, peeling it off and revealing thin bright white lines along the edges of the dark leaves, like frost.",
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

if __name__ == "__main__":
    args = sys.argv[1:]
    suffisso = os.environ.get("SUFFISSO", "")
    nomi = [n for n in PROMPT if not args or n.split("-")[0] in args]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for nome, esito in ex.map(lambda n: genera(n, suffisso), nomi):
            print(nome, esito, flush=True)

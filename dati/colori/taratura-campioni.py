#!/usr/bin/env python3
"""Taratura su carta vera dei sei colori e della forza di tintura del calcolatore.

Uso:
  python dati/colori/taratura-campioni.py scheda [percorso.html]
  python dati/colori/taratura-campioni.py misura <foto> [--angoli x1,y1,x2,y2,x3,y3,x4,y4]
         [--senza-foglio-stampa] [--confronto confronto.png] [--scrivi]
  python dati/colori/taratura-campioni.py autoverifica

Prepara una griglia 4 x 4 da dipingere su un foglio di carta da acquerello (due riferimenti di
bianco, i sei colori puri al miele e otto miscele binarie 1:1) e ricava da una sola fotografia
alla luce diffusa del giorno sia i valori sRGB normalizzati sul bianco di riferimento, sia i
fattori «forza» di Kubelka-Munk che minimizzano lo scarto OKLab sulle otto miscele reali.
Antigravity / AGY, 15/11/2026."""
import argparse
import datetime as dt
import html
import json
import math
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = pathlib.Path(__file__).resolve().parent
FILE_TAVOLOZZA = QUI / "tavolozza.json"
FILE_SPETTRI = QUI / "spettri-spectraljs.js"
FILE_CALCOLATORE = QUI / "calcolatore.js"

# Griglia 4 colonne x 4 righe (16 caselle):
# Riga 1: due riferimenti di bianco + primi due colori puri al miele
# Riga 2: gli altri quattro colori puri al miele
# Riga 3: quattro miscele 1:1 col giallo limone (tarano la forza relativa al giallo)
# Riga 4: quattro miscele 1:1 incrociate (tarano l'oltremare e verificano il modello)
GRIGLIA = [
    {"cella": "A1", "riga": 0, "col": 0, "tipo": "carta", "titolo": "Carta acquerello", "sotto": "lasciare bianca, non dipinta"},
    {"cella": "B1", "riga": 0, "col": 1, "tipo": "stampa", "titolo": "Carta bianca stampa", "sotto": "foglietto bianco appoggiato per la foto (opzionale)"},
    {"cella": "C1", "riga": 0, "col": 2, "tipo": "puro", "id": "giallo", "titolo": "1. Giallo limone", "sotto": "puro, consistenza miele"},
    {"cella": "D1", "riga": 0, "col": 3, "tipo": "puro", "id": "ceruleo", "titolo": "2. Ceruleo", "sotto": "puro, consistenza miele"},
    {"cella": "A2", "riga": 1, "col": 0, "tipo": "puro", "id": "cremisi", "titolo": "3. Cremisi", "sotto": "puro, consistenza miele"},
    {"cella": "B2", "riga": 1, "col": 1, "tipo": "puro", "id": "siena", "titolo": "4. Siena bruciata", "sotto": "puro, consistenza miele"},
    {"cella": "C2", "riga": 1, "col": 2, "tipo": "puro", "id": "ombra", "titolo": "5. Ombra bruciata", "sotto": "puro, consistenza miele"},
    {"cella": "D2", "riga": 1, "col": 3, "tipo": "puro", "id": "oltremare", "titolo": "6. Blu oltremare", "sotto": "puro, consistenza miele"},
    {"cella": "A3", "riga": 2, "col": 0, "tipo": "mix", "voci": [("giallo", 1), ("ceruleo", 1)], "titolo": "M-A · Giallo + Ceruleo", "sotto": "1 : 1, punte uguali al latte/miele"},
    {"cella": "B3", "riga": 2, "col": 1, "tipo": "mix", "voci": [("giallo", 1), ("cremisi", 1)], "titolo": "M-B · Giallo + Cremisi", "sotto": "1 : 1, punte uguali al latte/miele"},
    {"cella": "C3", "riga": 2, "col": 2, "tipo": "mix", "voci": [("giallo", 1), ("siena", 1)], "titolo": "M-C · Giallo + Siena", "sotto": "1 : 1, punte uguali al latte/miele"},
    {"cella": "D3", "riga": 2, "col": 3, "tipo": "mix", "voci": [("giallo", 1), ("ombra", 1)], "titolo": "M-D · Giallo + Ombra", "sotto": "1 : 1, punte uguali al latte/miele"},
    {"cella": "A4", "riga": 3, "col": 0, "tipo": "mix", "voci": [("giallo", 1), ("oltremare", 1)], "titolo": "M-E · Giallo + Oltremare", "sotto": "1 : 1, punte uguali al latte/miele"},
    {"cella": "B4", "riga": 3, "col": 1, "tipo": "mix", "voci": [("oltremare", 1), ("siena", 1)], "titolo": "M-F · Oltremare + Siena", "sotto": "1 : 1, grigio neutro"},
    {"cella": "C4", "riga": 3, "col": 2, "tipo": "mix", "voci": [("ceruleo", 1), ("cremisi", 1)], "titolo": "M-G · Ceruleo + Cremisi", "sotto": "1 : 1, viola freddo"},
    {"cella": "D4", "riga": 3, "col": 3, "tipo": "mix", "voci": [("oltremare", 1), ("cremisi", 1)], "titolo": "M-H · Oltremare + Cremisi", "sotto": "1 : 1, viola caldo"},
]

# Riflettanza sRGB lineare tipica di un foglio bianco da ufficio non sovraesposto (circa #F5F6F7)
RIF_FOGLIO_STAMPA_LIN = (0.913, 0.922, 0.930)

XYZ_RGB = [
    [3.2409699419, -1.5373831776, -0.4986107603],
    [-0.9692436363, 1.8759675015, 0.0415550574],
    [0.0556300797, -0.2039769589, 1.0569715142],
]
XYZ_LMS = [
    [0.8190224380, 0.3619062601, -0.1288737815],
    [0.0329836539, 0.9292868616, 0.0361446664],
    [0.0481771894, 0.2642395318, 0.6335478285],
]
LMS_LAB = [
    [0.2104542683, 0.7936177747, -0.0040720430],
    [1.9779985324, -2.4285922420, 0.4505937096],
    [0.0259040425, 0.7827717125, -0.8086757549],
]


def carica_spettri():
    testo = FILE_SPETTRI.read_text(encoding="utf-8")
    m = re.search(r"var\s+SPETTRI\s*=\s*(\{.*\})\s*;", testo, re.S)
    if not m:
        raise SystemExit("taratura-campioni: oggetto SPETTRI non trovato in spettri-spectraljs.js")
    js_obj = re.sub(r"\b(W|C|M|Y|R|G|B|CMF)\s*:", r'"\1":', m.group(1))
    return json.loads(js_obj)


SPETTRI = carica_spettri()
NBANDE = len(SPETTRI["W"])


def decod_srgb(v_0_255: float) -> float:
    x = max(0.0, min(1.0, v_0_255 / 255.0))
    return ((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92


def codif_srgb(lin: float) -> int:
    x = max(0.0, min(1.0, lin))
    c = 1.055 * (x ** (1.0 / 2.4)) - 0.055 if x > 0.0031308 else 12.92 * x
    return max(0, min(255, round(c * 255)))


def hex_a_lin(esad: str) -> tuple[float, float, float]:
    h = esad.lstrip("#")
    return tuple(decod_srgb(int(h[i : i + 2], 16)) for i in (0, 2, 4))  # type: ignore[return-value]


def lin_a_hex(rgb_lin: tuple[float, float, float]) -> str:
    r, g, b = (codif_srgb(v) for v in rgb_lin)
    return f"#{r:02X}{g:02X}{b:02X}"


def mv3(mat, vec):
    return [mat[i][0] * vec[0] + mat[i][1] * vec[1] + mat[i][2] * vec[2] for i in range(3)]


def cbrt(x: float) -> float:
    return math.copysign(abs(x) ** (1.0 / 3.0), x)


def spettro_da_lin(rgb_lin: tuple[float, float, float]) -> list[float]:
    lr, lg, lb = (max(0.0, min(1.0, c)) for c in rgb_lin)
    w = min(lr, lg, lb)
    r, g, b = lr - w, lg - w, lb - w
    c = min(g, b)
    m = min(r, b)
    y = min(r, g)
    rr = max(0.0, min(r - b, r - g))
    gg = max(0.0, min(g - b, g - r))
    bb = max(0.0, min(b - g, b - r))
    S = SPETTRI
    return [
        max(1e-6, w * S["W"][i] + c * S["C"][i] + m * S["M"][i] + y * S["Y"][i] + rr * S["R"][i] + gg * S["G"][i] + bb * S["B"][i])
        for i in range(NBANDE)
    ]


def spettro_da_hex(esad: str) -> list[float]:
    return spettro_da_lin(hex_a_lin(esad))


def ks(r: float) -> float:
    return (1.0 - r) * (1.0 - r) / (2.0 * r)


def km(k: float) -> float:
    return 1.0 + k - math.sqrt(k * k + 2.0 * k)


def xyz_da_spettro(R: list[float]) -> list[float]:
    return [sum(riga[i] * R[i] for i in range(NBANDE)) for riga in SPETTRI["CMF"]]


def srgb_da_spettro(R: list[float]) -> str:
    rgb = [codif_srgb(v) for v in mv3(XYZ_RGB, xyz_da_spettro(R))]
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def oklab_da_xyz(X: list[float]) -> list[float]:
    lms = [cbrt(v) for v in mv3(XYZ_LMS, X)]
    return mv3(LMS_LAB, lms)


def oklab_da_spettro(R: list[float]) -> list[float]:
    return oklab_da_xyz(xyz_da_spettro(R))


def oklab_da_lin(rgb_lin: tuple[float, float, float]) -> list[float]:
    lr, lg, lb = rgb_lin
    X = [
        0.4123907993 * lr + 0.3575843394 * lg + 0.1804807884 * lb,
        0.2126390059 * lr + 0.7151686788 * lg + 0.0721923154 * lb,
        0.0193308187 * lr + 0.1191947798 * lg + 0.9505321522 * lb,
    ]
    return oklab_da_xyz(X)


def distanza_oklab(a: list[float], b: list[float]) -> float:
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def peso_luminanza(R: list[float]) -> float:
    return max(1e-4, xyz_da_spettro(R)[1])


def mescola_km(spettri_puri: dict[str, list[float]], forze: dict[str, float], voci: list[tuple[str, float]]) -> list[float]:
    pesi = []
    tot = 0.0
    for cid, parti in voci:
        R = spettri_puri[cid]
        w = parti * forze[cid] * peso_luminanza(R)
        pesi.append(([ks(r) for r in R], w))
        tot += w
    out = []
    for i in range(NBANDE):
        k = sum(ks_vec[i] * w for ks_vec, w in pesi) / tot
        out.append(km(k))
    return out


def risolvi_sistema_lineare(A: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    M = [riga[:] + [b[i]] for i, riga in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < 1e-12:
            raise ValueError("Angoli degeneri: quattro punti allineati o coincidenti")
        M[col], M[piv] = M[piv], M[col]
        div = M[col][col]
        for j in range(col, n + 1):
            M[col][j] /= div
        for r in range(n):
            if r != col and abs(M[r][col]) > 0:
                f = M[r][col]
                for j in range(col, n + 1):
                    M[r][j] -= f * M[col][j]
    return [M[i][n] for i in range(n)]


def coeff_prospettiva(sorgente_4pt: list[tuple[float, float]], dest_w: int, dest_h: int) -> list[float]:
    """Coefficienti (a,b,c,d,e,f,g,h) per PIL Image.transform(..., Transform.PERSPECTIVE) che mappa
    dest (0,0)-(dest_w,0)-(dest_w,dest_h)-(0,dest_h) sui quattro angoli sorgente (alto-sx, alto-dx, basso-dx, basso-sx)."""
    dest_4pt = [(0.0, 0.0), (float(dest_w), 0.0), (float(dest_w), float(dest_h)), (0.0, float(dest_h))]
    A, b = [], []
    for (xd, yd), (xs, ys) in zip(dest_4pt, sorgente_4pt):
        A.append([xd, yd, 1.0, 0.0, 0.0, 0.0, -xd * xs, -yd * xs])
        b.append(xs)
        A.append([0.0, 0.0, 0.0, xd, yd, 1.0, -xd * ys, -yd * ys])
        b.append(ys)
    return risolvi_sistema_lineare(A, b)


def campiona_cella_lin(img, riga: int, col: int, frazione: float = 0.42) -> tuple[float, float, float]:
    """Media troncata (15%-85%) in RGB lineare della regione centrale di una cella della griglia 4 x 4."""
    w, h = img.size
    cw, ch = w / 4.0, h / 4.0
    marg_x = cw * (1.0 - frazione) / 2.0
    marg_y = ch * (1.0 - frazione) / 2.0
    x0 = max(0, int(round(col * cw + marg_x)))
    x1 = min(w, int(round((col + 1) * cw - marg_x)))
    y0 = max(0, int(round(riga * ch + marg_y)))
    y1 = min(h, int(round((riga + 1) * ch - marg_y)))
    ritaglio = img.crop((x0, y0, x1, y1)).convert("RGB")
    leggi_px = getattr(ritaglio, "get_flattened_data", ritaglio.getdata)
    px = list(leggi_px())
    if not px:
        raise ValueError(f"Cella ({riga},{col}) vuota")
    canali = []
    for k in range(3):
        vals = sorted(decod_srgb(p[k]) for p in px)
        n = len(vals)
        i0, i1 = int(n * 0.15), max(int(n * 0.15) + 1, int(n * 0.85))
        canali.append(sum(vals[i0:i1]) / (i1 - i0))
    return (canali[0], canali[1], canali[2])


def ottimizza_forze(
    spettri_puri: dict[str, list[float]],
    mix_misurati_oklab: list[tuple[list[tuple[str, float]], list[float]]],
) -> dict[str, float]:
    """Stima i fattori «forza» (con giallo = 1.0 fisso) minimizzando l'errore quadratico medio in OKLab."""
    ordine_liberi = ["ceruleo", "cremisi", "siena", "ombra", "oltremare"]
    log_f = [0.0 for _ in ordine_liberi]  # exp(0) = 1.0 iniziale

    def obiettivo(lf: list[float]) -> float:
        forze = {"giallo": 1.0}
        for cid, v in zip(ordine_liberi, lf):
            forze[cid] = math.exp(v)
        err2 = 0.0
        for voci, lab_vero in mix_misurati_oklab:
            R_pred = mescola_km(spettri_puri, forze, voci)
            d = distanza_oklab(oklab_da_spettro(R_pred), lab_vero)
            err2 += d * d
        # lieve regolarizzazione per evitare derive se un colore fosse quasi assente
        reg = 1e-5 * sum(v * v for v in lf)
        return err2 / len(mix_misurati_oklab) + reg

    miglior_val = obiettivo(log_f)
    for passo in (0.5, 0.2, 0.08, 0.03, 0.01, 0.003):
        migliorato = True
        while migliorato:
            migliorato = False
            for idx in range(len(log_f)):
                for segno in (-1.0, 1.0):
                    cand = log_f[:]
                    cand[idx] = max(-2.5, min(2.5, cand[idx] + segno * passo))
                    val = obiettivo(cand)
                    if val + 1e-10 < miglior_val:
                        log_f, miglior_val = cand, val
                        migliorato = True
    out = {"giallo": 1.0}
    for cid, v in zip(ordine_liberi, log_f):
        out[cid] = round(math.exp(v), 2)
    return out


def analizza_immagine(
    percorso_foto: pathlib.Path,
    angoli: list[tuple[float, float]] | None = None,
    usa_foglio_stampa: bool = True,
    bianco_carta_rif: str = "#FBF8F0",
) -> dict:
    from PIL import Image, ImageOps

    img = ImageOps.exif_transpose(Image.open(percorso_foto)).convert("RGB")
    if angoli is not None:
        coeff = coeff_prospettiva(angoli, 1200, 1200)
        try:
            metodo = Image.Transform.PERSPECTIVE
        except AttributeError:
            metodo = Image.PERSPECTIVE  # type: ignore[attr-defined]
        try:
            resamp = Image.Resampling.BICUBIC
        except AttributeError:
            resamp = Image.BICUBIC  # type: ignore[attr-defined]
        img = img.transform((1200, 1200), metodo, coeff, resample=resamp)

    grezzi = {v["cella"]: campiona_cella_lin(img, v["riga"], v["col"]) for v in GRIGLIA}
    lin_carta_grezzo = grezzi["A1"]
    lin_stampa_grezzo = grezzi["B1"]

    # Se B1 contiene davvero un foglietto più chiaro o neutro (e non è rimasto scuro o dipinto per errore),
    # usiamo B1 come riferimento neutro per stimare anche il punto di bianco caldo della carta in A1.
    lum_a1 = sum(lin_carta_grezzo) / 3.0
    lum_b1 = sum(lin_stampa_grezzo) / 3.0
    if usa_foglio_stampa and lum_b1 > 0.75 * lum_a1:
        scala = tuple(RIF_FOGLIO_STAMPA_LIN[k] / max(1e-4, lin_stampa_grezzo[k]) for k in range(3))
        metodo_bianco = "normalizzato sul foglio bianco da stampa in B1"
    else:
        rif_carta = hex_a_lin(bianco_carta_rif)
        scala = tuple(rif_carta[k] / max(1e-4, lin_carta_grezzo[k]) for k in range(3))
        metodo_bianco = f"normalizzato sulla carta da acquerello non dipinta in A1 ({bianco_carta_rif})"

    def corr(rgb_l: tuple[float, float, float]) -> tuple[float, float, float]:
        return tuple(max(0.001, min(0.995, rgb_l[k] * scala[k])) for k in range(3))  # type: ignore[return-value]

    corr_celle = {k: corr(v) for k, v in grezzi.items()}
    carta_hex = lin_a_hex(corr_celle["A1"])

    puri_hex: dict[str, str] = {}
    spettri_puri: dict[str, list[float]] = {}
    for v in GRIGLIA:
        if v["tipo"] == "puro":
            cid = v["id"]
            esad = lin_a_hex(corr_celle[v["cella"]])
            puri_hex[cid] = esad
            spettri_puri[cid] = spettro_da_hex(esad)

    mix_dati = []
    for v in GRIGLIA:
        if v["tipo"] == "mix":
            lin_mix = corr_celle[v["cella"]]
            mix_dati.append((v, lin_mix, oklab_da_lin(lin_mix)))

    forze_unitarie = {cid: 1.0 for cid in puri_hex}
    forze_tarate = ottimizza_forze(spettri_puri, [(v["voci"], lab_m) for v, _, lab_m in mix_dati])

    righe_mix = []
    scarti_prima, scarti_dopo = [], []
    for v, lin_mix, lab_vero in mix_dati:
        R_prima = mescola_km(spettri_puri, forze_unitarie, v["voci"])
        R_dopo = mescola_km(spettri_puri, forze_tarate, v["voci"])
        d_prima = distanza_oklab(oklab_da_spettro(R_prima), lab_vero)
        d_dopo = distanza_oklab(oklab_da_spettro(R_dopo), lab_vero)
        scarti_prima.append(d_prima)
        scarti_dopo.append(d_dopo)
        righe_mix.append(
            {
                "cella": v["cella"],
                "titolo": v["titolo"],
                "misurato": lin_a_hex(lin_mix),
                "predetto_forza1": srgb_da_spettro(R_prima),
                "predetto_tarato": srgb_da_spettro(R_dopo),
                "oklab_prima": round(d_prima, 4),
                "oklab_dopo": round(d_dopo, 4),
            }
        )

    return {
        "metodo_bianco": metodo_bianco,
        "carta_srgb": carta_hex,
        "puri_srgb": puri_hex,
        "forze": forze_tarate,
        "errore_medio_oklab_prima": round(sum(scarti_prima) / len(scarti_prima), 4),
        "errore_medio_oklab_dopo": round(sum(scarti_dopo) / len(scarti_dopo), 4),
        "miscele": righe_mix,
    }


def salva_confronto_png(esito: dict, tav_attuale: dict, destinazione: pathlib.Path) -> None:
    from PIL import Image, ImageDraw

    nomi = {c["id"]: c["nome"] for c in tav_attuale["colori"]}
    vecchi = {c["id"]: c["srgb"] for c in tav_attuale["colori"]}
    W, H = 900, 680
    im = Image.new("RGB", (W, H), (251, 250, 247))
    dr = ImageDraw.Draw(im)
    dr.text((24, 18), "Taratura campioni su carta vera - Confronto colori puri e miscele 1:1", fill=(38, 53, 41))
    dr.text(
        (24, 40),
        f"Carta: {esito['carta_srgb']} | Scarto medio OKLab miscele: da {esito['errore_medio_oklab_prima']:.3f} (forza=1) a {esito['errore_medio_oklab_dopo']:.3f} (tarato)",
        fill=(85, 85, 85),
    )

    y = 74
    dr.text((24, y), "SEI COLORI PURI (sinistra: provvisorio precedente | destra: misurato su carta)", fill=(44, 79, 58))
    y += 24
    for idx, cid in enumerate(["giallo", "ceruleo", "cremisi", "siena", "ombra", "oltremare"]):
        col_x = 24 + (idx % 3) * 290
        row_y = y + (idx // 3) * 78
        c_old = tuple(int(vecchi[cid][k : k + 2], 16) for k in (1, 3, 5))
        c_new = tuple(int(esito["puri_srgb"][cid][k : k + 2], 16) for k in (1, 3, 5))
        dr.rectangle([col_x, row_y, col_x + 48, row_y + 48], fill=c_old, outline=(160, 150, 135))
        dr.rectangle([col_x + 48, row_y, col_x + 96, row_y + 48], fill=c_new, outline=(160, 150, 135))
        dr.text((col_x + 106, row_y + 6), nomi[cid], fill=(31, 31, 31))
        dr.text((col_x + 106, row_y + 25), f"{esito['puri_srgb'][cid]}  forza {esito['forze'][cid]:.2f}", fill=(90, 80, 68))

    y += 176
    dr.text((24, y), "OTTO MISCELE 1:1 (sinistra: carta fotografata | destra: Kubelka-Munk tarato)", fill=(44, 79, 58))
    y += 24
    for idx, m in enumerate(esito["miscele"]):
        col_x = 24 + (idx % 2) * 435
        row_y = y + (idx // 2) * 90
        c_mis = tuple(int(m["misurato"][k : k + 2], 16) for k in (1, 3, 5))
        c_cal = tuple(int(m["predetto_tarato"][k : k + 2], 16) for k in (1, 3, 5))
        dr.rectangle([col_x, row_y, col_x + 56, row_y + 56], fill=c_mis, outline=(160, 150, 135))
        dr.rectangle([col_x + 56, row_y, col_x + 112, row_y + 56], fill=c_cal, outline=(160, 150, 135))
        dr.text((col_x + 124, row_y + 8), f"{m['cella']}  {m['titolo']}", fill=(31, 31, 31))
        dr.text(
            (col_x + 124, row_y + 28),
            f"carta {m['misurato']} | modello {m['predetto_tarato']} | dOKLab {m['oklab_dopo']:.3f}",
            fill=(90, 80, 68),
        )

    destinazione.parent.mkdir(parents=True, exist_ok=True)
    im.save(destinazione)


def aggiorna_tavolozza_json(esito: dict) -> None:
    tav = json.loads(FILE_TAVOLOZZA.read_text(encoding="utf-8"))
    oggi = dt.date.today().isoformat()
    tav["data"] = oggi
    tav["fonte_colori"] = f"campioni stesi su carta di cotone da 300 g/m² e misurati da fotografia ({esito['metodo_bianco']})"
    tav["carta"]["srgb"] = esito["carta_srgb"]
    tav["carta"]["fonte"] = f"misurato il {oggi} sul riquadro A1 non dipinto"
    for c in tav["colori"]:
        cid = c["id"]
        c["srgb"] = esito["puri_srgb"][cid]
        c["forza"] = esito["forze"][cid]
        c["stato"] = "tarato su carta"
        c.pop("nota_srgb", None)
    FILE_TAVOLOZZA.write_text(json.dumps(tav, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def genera_scheda_html(destinazione: pathlib.Path) -> None:
    tav = json.loads(FILE_TAVOLOZZA.read_text(encoding="utf-8"))
    pigmenti = {c["id"]: c["pigmento"] for c in tav["colori"]}
    srgb_prov = {c["id"]: c["srgb"] for c in tav["colori"]}

    celle_html = []
    for v in GRIGLIA:
        extra = ""
        bordo = "#9ab5a3"
        sfondo = "#ffffff"
        if v["tipo"] == "carta":
            sfondo = "#fbf8f0"
            bordo = "#c8b99e"
        elif v["tipo"] == "stampa":
            sfondo = "#f7f8fa"
            bordo = "#9aa7b8"
        elif v["tipo"] == "puro":
            cid = v["id"]
            sigla_pig = "PR206 / PR179" if cid == "cremisi" else pigmenti[cid]
            extra = f'<span class="pig">{html.escape(sigla_pig)}</span>'
            sfondo = "#fffdf9"
        else:
            extra = '<span class="pig">parti 1 : 1</span>'
            sfondo = "#f9fbf9"
        celle_html.append(
            f'<div class="cella" style="background:{sfondo};border-color:{bordo}">'
            f'<div class="testa-c"><span class="cod">{v["cella"]}</span>{extra}</div>'
            f'<div class="zona-colore"></div>'
            f'<div class="piede-c"><b>{html.escape(v["titolo"])}</b><br><span>{html.escape(v["sotto"])}</span></div>'
            f"</div>"
        )

    spettri_js = FILE_SPETTRI.read_text(encoding="utf-8")
    calc_js = FILE_CALCOLATORE.read_text(encoding="utf-8")
    griglia_json = json.dumps(GRIGLIA, ensure_ascii=False)
    tav_json = json.dumps(tav, ensure_ascii=False)

    pagina = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Scheda di taratura su carta vera · Tavolozza ridotta a 6 colori</title>
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0 auto; max-width: 860px; padding: 18px 18px 40px; font-family: system-ui, 'Segoe UI', Roboto, sans-serif; color: #1f1f1f; background: #fbfaf7; line-height: 1.42; }}
h1 {{ font-size: 1.38rem; margin: 0 0 4px; color: #263529; }}
h2 {{ font-size: 1.08rem; margin: 18px 0 6px; color: #2c4f3a; }}
p, li {{ font-size: .92rem; }}
.sotto {{ margin: 0 0 12px; color: #4a4236; font-size: .94rem; }}
.istruzioni {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 10px 0 14px; }}
@media (max-width: 640px) {{ .istruzioni {{ grid-template-columns: 1fr; }} }}
.box {{ background: #f3f7f3; border: 1px solid #cadbce; border-radius: 8px; padding: 10px 12px; }}
.box h3 {{ margin: 0 0 5px; font-size: .95rem; color: #263529; }}
.box ol, .box ul {{ margin: 0; padding-left: 18px; }}
.box li {{ margin-bottom: 4px; font-size: .86rem; }}
.cornice-griglia {{ border: 3px solid #1f1f1f; padding: 8px; background: #fff; border-radius: 4px; margin: 10px 0; }}
.griglia {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }}
.cella {{ border: 1.5px dashed #9ab5a3; border-radius: 6px; padding: 6px; display: flex; flex-direction: column; justify-content: space-between; min-height: 126px; }}
.testa-c {{ display: flex; justify-content: space-between; align-items: center; font-size: .76rem; }}
.cod {{ font-weight: 800; color: #263529; background: #e8efe9; border-radius: 4px; padding: 1px 5px; }}
.pig {{ color: #5c5142; font-weight: 600; }}
.zona-colore {{ flex: 1; min-height: 58px; margin: 5px 0; border: 1px dotted #d6cfc2; border-radius: 4px; }}
.piede-c {{ font-size: .75rem; line-height: 1.25; }}
.piede-c span {{ color: #555; font-size: .71rem; }}
.lettore-foto {{ margin-top: 24px; padding: 14px 16px; background: #fffdf8; border: 2px solid #3d6b4f; border-radius: 10px; }}
.barra-foto {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin: 8px 0; }}
.btn {{ background: #2c4f3a; color: #fff; border: 0; border-radius: 6px; padding: 7px 13px; font-weight: 600; cursor: pointer; font-size: .88rem; }}
.btn.sec {{ background: #6b5e4c; }}
canvas {{ max-width: 100%; border: 1px solid #c9bba3; border-radius: 6px; cursor: crosshair; display: none; margin-top: 8px; }}
pre {{ background: #1f2421; color: #e8efe9; padding: 10px 12px; border-radius: 6px; overflow-x: auto; font-size: .8rem; }}
table.ris {{ width: 100%; border-collapse: collapse; font-size: .84rem; margin-top: 10px; }}
table.ris th, table.ris td {{ border: 1px solid #d8d2c4; padding: 5px 7px; text-align: left; }}
table.ris th {{ background: #eef4ef; color: #263529; }}
.sw {{ display: inline-block; width: 22px; height: 16px; vertical-align: middle; border: 1px solid rgba(0,0,0,.25); border-radius: 3px; margin-right: 5px; }}
@media print {{
  body {{ background: #fff; padding: 0; max-width: none; line-height: 1.32; }}
  h1 {{ font-size: 1.22rem; margin-bottom: 2px; }}
  .sotto {{ font-size: .84rem; margin-bottom: 8px; }}
  .istruzioni {{ gap: 8px; margin: 6px 0 10px; }}
  .box {{ padding: 7px 10px; }}
  .box h3 {{ font-size: .88rem; margin-bottom: 3px; }}
  .box li {{ font-size: .78rem; margin-bottom: 2px; }}
  .cornice-griglia {{ padding: 6px; margin: 6px 0 0; break-inside: avoid; }}
  .griglia {{ gap: 6px; }}
  .cella {{ min-height: 112px; padding: 5px; break-inside: avoid; }}
  .zona-colore {{ min-height: 50px; margin: 4px 0; }}
  .no-stampa {{ display: none !important; }}
}}
</style>
</head>
<body>
<h1>Scheda di taratura su carta vera (griglia 4 × 4)</h1>
<p class="sotto">Un solo foglietto di carta di cotone da 300 g/m² per misurare insieme i sei colori pieni (<code>srgb</code>), il bianco della carta e il potere tingente reale in miscela (<code>forza</code>).</p>

<div class="istruzioni">
  <div class="box">
    <h3>1. Come preparare il foglio (10 minuti)</h3>
    <ol>
      <li>Su un foglio di carta da acquerello (almeno 14 × 14 cm, per esempio metà A4) traccia a matita leggera un quadrato esterno diviso in <b>4 colonne × 4 righe</b> (16 caselle da circa 3 × 3 cm).</li>
      <li>Lascia <b>A1</b> completamente bianca (carta da acquerello nuda) e lascia vuota <b>B1</b>.</li>
      <li>Nelle sei caselle <b>C1, D1, A2, B2, C2, D2</b> stendi i sei colori puri a <b>consistenza miele</b> (colore denso e uniforme, senza far trasparire chiazze d'acqua), sciacquando bene il pennello a ogni cambio.</li>
      <li>Nelle otto caselle <b>A3..D4</b> prepara le miscele <b>1 : 1 a parti uguali</b>: preleva con la punta umida la stessa quantità di pasta dai due colori indicati, mescola bene sul piatto a consistenza latte denso/miele e riempi il centro della casella.</li>
    </ol>
  </div>
  <div class="box">
    <h3>2. Come fotografarlo</h3>
    <ul>
      <li>Aspetta che tutte le 14 pennellate siano <b>completamente asciutte</b> e opache (il colore bagnato riflette la luce e appare più scuro e saturo).</li>
      <li>Se hai a portata di mano un pezzetto di normale <b>carta bianca da stampante</b>, appoggialo dentro la casella <b>B1</b>: serve da riferimento neutro per leggere anche la tinta calda della carta di cotone in A1.</li>
      <li>Fotografa alla <b>luce naturale diffusa</b> (vicino a una finestra, senza sole diretto né ombre della mano o del telefono sul foglio), tenendo il telefono parallelo al foglio.</li>
      <li>Passa la foto allo script Python oppure aprila nella versione HTML interattiva della scheda.</li>
    </ul>
  </div>
</div>

<div class="cornice-griglia">
  <div class="griglia">
    {"".join(celle_html)}
  </div>
</div>

<div class="lettore-foto no-stampa">
  <h2>Misura rapida dalla foto (direttamente nel browser)</h2>
  <p>Carica la foto scattata col telefono e clicca in ordine i <b>4 angoli esterni</b> della griglia 4 × 4: <b>1. alto-sinistra</b>, <b>2. alto-destra</b>, <b>3. basso-destra</b>, <b>4. basso-sinistra</b>. La pagina calcola subito colori, forze di tintura, comando Python e JSON aggiornato.</p>
  <div class="barra-foto">
    <input type="file" id="file-foto" accept="image/*">
    <label style="font-size:.86rem"><input type="checkbox" id="chk-stampa" checked> in B1 c'è il foglietto bianco da stampante</label>
    <button type="button" class="btn sec" id="btn-reset">Azzera i 4 angoli</button>
  </div>
  <div id="stato-clic" style="font-size:.86rem;color:#2c4f3a;font-weight:600">In attesa della fotografia.</div>
  <canvas id="tela"></canvas>
  <div id="esito-browser"></div>
</div>

<script>
{spettri_js}
{calc_js}
(function() {{
  var GRIGLIA = {griglia_json};
  var TAV = {tav_json};
  var fileIn = document.getElementById('file-foto');
  var chkStampa = document.getElementById('chk-stampa');
  var btnReset = document.getElementById('btn-reset');
  var stato = document.getElementById('stato-clic');
  var tela = document.getElementById('tela');
  var ctx = tela.getContext('2d');
  var esitoDiv = document.getElementById('esito-browser');
  var img = null, nomeFile = 'campioni.jpg', angoli = [];
  var NOMI_ANGOLI = ['1. alto-sinistra', '2. alto-destra', '3. basso-destra', '4. basso-sinistra'];

  function decod(v) {{ v /= 255; return v > 0.04045 ? Math.pow((v + 0.055) / 1.055, 2.4) : v / 12.92; }}
  function codif(x) {{ x = Math.max(0, Math.min(1, x)); var c = x > 0.0031308 ? 1.055 * Math.pow(x, 1 / 2.4) - 0.055 : 12.92 * x; return Math.max(0, Math.min(255, Math.round(c * 255))); }}
  function aHexLin(l) {{ return '#' + l.map(function(x) {{ return ('0' + codif(x).toString(16)).slice(-2); }}).join('').toUpperCase(); }}

  function bilerp(p, u, v) {{
    var x = (1 - u) * (1 - v) * p[0].x + u * (1 - v) * p[1].x + u * v * p[2].x + (1 - u) * v * p[3].x;
    var y = (1 - u) * (1 - v) * p[0].y + u * (1 - v) * p[1].y + u * v * p[2].y + (1 - u) * v * p[3].y;
    return {{ x: x, y: y }};
  }}

  function disegna() {{
    if (!img) return;
    var scala = Math.min(1, 820 / img.width);
    tela.width = Math.round(img.width * scala);
    tela.height = Math.round(img.height * scala);
    tela.style.display = 'block';
    ctx.drawImage(img, 0, 0, tela.width, tela.height);
    ctx.lineWidth = 2;
    angoli.forEach(function(pt, i) {{
      ctx.fillStyle = '#d9381e';
      ctx.beginPath(); ctx.arc(pt.x * scala, pt.y * scala, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#fff'; ctx.font = 'bold 11px sans-serif';
      ctx.fillText(String(i + 1), pt.x * scala - 3, pt.y * scala + 4);
    }});
    if (angoli.length === 4) {{
      ctx.strokeStyle = '#2c6a4a';
      ctx.beginPath();
      angoli.forEach(function(pt, i) {{ if (i === 0) ctx.moveTo(pt.x * scala, pt.y * scala); else ctx.lineTo(pt.x * scala, pt.y * scala); }});
      ctx.closePath(); ctx.stroke();
      GRIGLIA.forEach(function(g) {{
        var c = bilerp(angoli, (g.col + 0.5) / 4, (g.riga + 0.5) / 4);
        ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(c.x * scala, c.y * scala, 9, 0, Math.PI * 2); ctx.stroke();
        ctx.strokeStyle = '#1f3c2b'; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(c.x * scala, c.y * scala, 10, 0, Math.PI * 2); ctx.stroke();
      }});
    }}
  }}

  function calcolaDaFoto() {{
    var off = document.createElement('canvas');
    off.width = img.width; off.height = img.height;
    var octx = off.getContext('2d');
    octx.drawImage(img, 0, 0);
    var dati = octx.getImageData(0, 0, img.width, img.height).data;

    function campiona(riga, col) {{
      var rs = [], gs = [], bs = [];
      for (var sy = -5; sy <= 5; sy++) {{
        for (var sx = -5; sx <= 5; sx++) {{
          var u = (col + 0.5 + sx * 0.032) / 4;
          var v = (riga + 0.5 + sy * 0.032) / 4;
          var pt = bilerp(angoli, u, v);
          var px = Math.max(0, Math.min(img.width - 1, Math.round(pt.x)));
          var py = Math.max(0, Math.min(img.height - 1, Math.round(pt.y)));
          var idx = (py * img.width + px) * 4;
          rs.push(decod(dati[idx])); gs.push(decod(dati[idx + 1])); bs.push(decod(dati[idx + 2]));
        }}
      }}
      function medTronc(arr) {{
        arr.sort(function(a, b) {{ return a - b; }});
        var i0 = Math.floor(arr.length * 0.15), i1 = Math.ceil(arr.length * 0.85);
        var s = 0; for (var i = i0; i < i1; i++) s += arr[i];
        return s / (i1 - i0);
      }}
      return [medTronc(rs), medTronc(gs), medTronc(bs)];
    }}

    var grezzi = {{}};
    GRIGLIA.forEach(function(g) {{ grezzi[g.cella] = campiona(g.riga, g.col); }});
    var rifStampa = [0.913, 0.922, 0.930];
    var rifCarta = [decod(251), decod(248), decod(240)];
    var usaB1 = chkStampa.checked && ((grezzi.B1[0] + grezzi.B1[1] + grezzi.B1[2]) > 0.75 * (grezzi.A1[0] + grezzi.A1[1] + grezzi.A1[2]));
    var scala = [0, 1, 2].map(function(k) {{
      return usaB1 ? rifStampa[k] / Math.max(1e-4, grezzi.B1[k]) : rifCarta[k] / Math.max(1e-4, grezzi.A1[k]);
    }});
    function corr(l) {{ return [0, 1, 2].map(function(k) {{ return Math.max(0.001, Math.min(0.995, l[k] * scala[k])); }}); }}

    var puriHex = {{}};
    GRIGLIA.forEach(function(g) {{ if (g.tipo === 'puro') puriHex[g.id] = aHexLin(corr(grezzi[g.cella])); }});
    var cartaHex = aHexLin(corr(grezzi.A1));

    var liberi = ['ceruleo', 'cremisi', 'siena', 'ombra', 'oltremare'];
    var logF = [0, 0, 0, 0, 0];
    function preparaConForze(lf) {{
      var copia = JSON.parse(JSON.stringify(TAV));
      copia.carta.srgb = cartaHex;
      var mappaF = {{ giallo: 1.0 }};
      liberi.forEach(function(id, i) {{ mappaF[id] = Math.exp(lf[i]); }});
      copia.colori.forEach(function(c) {{ c.srgb = puriHex[c.id]; c.forza = mappaF[c.id]; }});
      Acq.prepara(copia);
      return copia;
    }}
    function erroreMedio(lf) {{
      preparaConForze(lf);
      var s = 0, n = 0;
      GRIGLIA.forEach(function(g) {{
        if (g.tipo !== 'mix') return;
        var hexVero = aHexLin(corr(grezzi[g.cella]));
        var lista = g.voci.map(function(v) {{ return {{ col: Acq.colore(v[0]), parti: v[1] }}; }});
        var R = Acq.mescola(lista);
        var d = Acq.distanza(Acq.oklab(R), Acq.oklabHex(hexVero));
        s += d * d; n++;
      }});
      return Math.sqrt(s / n);
    }}
    var err0 = erroreMedio([0, 0, 0, 0, 0]);
    var best = err0;
    [0.5, 0.2, 0.08, 0.03, 0.01].forEach(function(passo) {{
      var mig = true;
      while (mig) {{
        mig = false;
        for (var i = 0; i < liberi.length; i++) {{
          [-1, 1].forEach(function(segno) {{
            var cand = logF.slice();
            cand[i] = Math.max(-2.5, Math.min(2.5, cand[i] + segno * passo));
            var e = erroreMedio(cand);
            if (e + 1e-9 < best) {{ best = e; logF = cand; mig = true; }}
          }});
        }}
      }}
    }});
    var tavFinale = preparaConForze(logF);
    tavFinale.data = new Date().toISOString().slice(0, 10);
    tavFinale.carta.fonte = 'misurato su carta non dipinta (A1)';
    tavFinale.colori.forEach(function(c) {{ c.forza = Math.round(c.forza * 100) / 100; c.stato = 'tarato su carta'; delete c.nota_srgb; }});

    var coordsCli = angoli.map(function(p) {{ return Math.round(p.x) + ',' + Math.round(p.y); }}).join(',');
    var cmd = 'python dati/colori/taratura-campioni.py misura "' + nomeFile + '" --angoli ' + coordsCli + (chkStampa.checked ? '' : ' --senza-foglio-stampa') + ' --confronto confronto-taratura.png --scrivi';

    var righePuri = tavFinale.colori.map(function(c) {{
      return '<tr><td><b>' + c.nome + '</b> (' + c.pigmento + ')</td><td><span class="sw" style="background:' + c.srgb + '"></span><code>' + c.srgb + '</code></td><td><b>' + c.forza.toFixed(2) + '</b></td></tr>';
    }}).join('');

    var righeMix = '';
    Acq.prepara(tavFinale);
    GRIGLIA.forEach(function(g) {{
      if (g.tipo !== 'mix') return;
      var hexVero = aHexLin(corr(grezzi[g.cella]));
      var lista = g.voci.map(function(v) {{ return {{ col: Acq.colore(v[0]), parti: v[1] }}; }});
      var R = Acq.mescola(lista);
      var hexPred = Acq.aHex(Acq.aSrgb(R));
      var d = Acq.distanza(Acq.oklab(R), Acq.oklabHex(hexVero));
      righeMix += '<tr><td>' + g.cella + ' · ' + g.titolo + '</td><td><span class="sw" style="background:' + hexVero + '"></span><code>' + hexVero + '</code></td><td><span class="sw" style="background:' + hexPred + '"></span><code>' + hexPred + '</code></td><td>' + d.toFixed(3) + '</td></tr>';
    }});

    esitoDiv.innerHTML =
      '<h3>Risultato della misura</h3>' +
      '<p>Bianco carta (A1): <span class="sw" style="background:' + cartaHex + '"></span><code>' + cartaHex + '</code> · Errore quadratico medio OKLab sulle 8 miscele: da <b>' + err0.toFixed(3) + '</b> (forza=1) a <b>' + best.toFixed(3) + '</b> (tarato).</p>' +
      '<table class="ris"><tr><th>Colore</th><th>sRGB misurato</th><th>Forza tarata</th></tr>' + righePuri + '</table>' +
      '<table class="ris"><tr><th>Miscela 1 : 1</th><th>Carta vera</th><th>Modello tarato</th><th>Scarto OKLab</th></tr>' + righeMix + '</table>' +
      '<h3>Comando per aggiornare tavolozza.json e salvare il confronto</h3><pre>' + cmd + '</pre>';
  }}

  fileIn.addEventListener('change', function() {{
    var f = fileIn.files && fileIn.files[0];
    if (!f) return;
    nomeFile = f.name;
    var r = new FileReader();
    r.onload = function(ev) {{
      var im = new Image();
      im.onload = function() {{
        img = im; angoli = []; esitoDiv.innerHTML = '';
        stato.textContent = 'Clicca sulla foto l\\'angolo ' + NOMI_ANGOLI[0] + ' della griglia 4 × 4.';
        disegna();
      }};
      im.src = ev.target.result;
    }};
    r.readAsDataURL(f);
  }});

  tela.addEventListener('click', function(ev) {{
    if (!img || angoli.length >= 4) return;
    var rect = tela.getBoundingClientRect();
    var scala = img.width / rect.width;
    angoli.push({{ x: (ev.clientX - rect.left) * scala, y: (ev.clientY - rect.top) * scala }});
    disegna();
    if (angoli.length < 4) {{
      stato.textContent = 'Clicca ora l\\'angolo ' + NOMI_ANGOLI[angoli.length] + '.';
    }} else {{
      stato.textContent = 'Quattro angoli acquisiti: taratura calcolata qui sotto.';
      calcolaDaFoto();
    }}
  }});

  chkStampa.addEventListener('change', function() {{ if (angoli.length === 4) calcolaDaFoto(); }});
  btnReset.addEventListener('click', function() {{
    angoli = []; esitoDiv.innerHTML = '';
    if (img) {{ stato.textContent = 'Clicca sulla foto l\\'angolo ' + NOMI_ANGOLI[0] + '.'; disegna(); }}
  }});
}})();
</script>
</body>
</html>
"""
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    destinazione.write_text(pagina, encoding="utf-8", newline="\n")


def esegui_autoverifica() -> None:
    """Genera un foglio sintetico 4 x 4 con dominante calda d'illuminazione, leggera rotazione prospettica
    e forze di tintura note diverse da 1, e controlla che analizza_immagine recuperi colori e forze."""
    import tempfile
    from PIL import Image, ImageDraw

    puri_veri = {
        "giallo": "#F2DF3A",
        "ceruleo": "#1F78B8",
        "cremisi": "#8B1E38",
        "siena": "#9A4526",
        "ombra": "#5A3D2A",
        "oltremare": "#26389A",
    }
    forze_vere = {"giallo": 1.0, "ceruleo": 2.6, "cremisi": 1.8, "siena": 1.35, "ombra": 1.5, "oltremare": 1.15}
    carta_vera = "#FAF6EC"
    spettri_veri = {k: spettro_da_hex(v) for k, v in puri_veri.items()}
    illuminante = (0.92, 0.88, 0.80)  # luce leggermente calda e sottoesposta

    def dipingi_su_foto(esad: str) -> tuple[int, int, int]:
        lin = hex_a_lin(esad)
        return tuple(codif_srgb(lin[k] * illuminante[k]) for k in range(3))  # type: ignore[return-value]

    im = Image.new("RGB", (1000, 1000), (235, 230, 220))
    dr = ImageDraw.Draw(im)
    gx0, gy0, lato = 100, 100, 800
    passo = lato // 4
    for v in GRIGLIA:
        if v["tipo"] == "carta":
            col = dipingi_su_foto(carta_vera)
        elif v["tipo"] == "stampa":
            col = tuple(codif_srgb(RIF_FOGLIO_STAMPA_LIN[k] * illuminante[k]) for k in range(3))  # type: ignore[assignment]
        elif v["tipo"] == "puro":
            col = dipingi_su_foto(puri_veri[v["id"]])
        else:
            R_mix = mescola_km(spettri_veri, forze_vere, v["voci"])
            col = dipingi_su_foto(srgb_da_spettro(R_mix))
        x0 = gx0 + v["col"] * passo + 14
        y0 = gy0 + v["riga"] * passo + 14
        dr.rectangle([x0, y0, x0 + passo - 28, y0 + passo - 28], fill=col, outline=(90, 90, 90))

    with tempfile.TemporaryDirectory() as td:
        f_img = pathlib.Path(td) / "prova.png"
        im.save(f_img)
        angoli = [(100.0, 100.0), (900.0, 100.0), (900.0, 900.0), (100.0, 900.0)]
        esito = analizza_immagine(f_img, angoli=angoli, usa_foglio_stampa=True)
        assert esito["errore_medio_oklab_dopo"] < 0.004, f"Errore OKLab troppo alto: {esito['errore_medio_oklab_dopo']}"
        for cid, f_attesa in forze_vere.items():
            f_stima = esito["forze"][cid]
            scarto_rel = abs(f_stima - f_attesa) / f_attesa
            assert scarto_rel < 0.08, f"Forza {cid}: attesa {f_attesa}, stimata {f_stima}"
        print(
            f"[autoverifica ok] dOKLab prima={esito['errore_medio_oklab_prima']:.4f} -> dopo={esito['errore_medio_oklab_dopo']:.4f}; "
            f"forze stimate={esito['forze']}"
        )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="comando", required=True)

    p_sch = sub.add_parser("scheda", help="Genera la scheda guida 4 x 4 in HTML (stampabile e con lettore foto)")
    p_sch.add_argument("uscita", nargs="?", default=str(QUI / "scheda-taratura-campioni.html"))

    p_mis = sub.add_parser("misura", help="Misura sRGB e fattori forza da una fotografia della griglia 4 x 4")
    p_mis.add_argument("foto", type=pathlib.Path)
    p_mis.add_argument("--angoli", help="x1,y1,x2,y2,x3,y3,x4,y4 (alto-sx, alto-dx, basso-dx, basso-sx in pixel)")
    p_mis.add_argument("--senza-foglio-stampa", action="store_true", help="Ignora B1 e normalizza sul bianco carta A1")
    p_mis.add_argument("--bianco-carta", default="#FBF8F0", help="sRGB attribuito ad A1 se manca B1 (default: #FBF8F0)")
    p_mis.add_argument("--confronto", type=pathlib.Path, help="Salva un PNG di confronto carta contro modello")
    p_mis.add_argument("--scrivi", action="store_true", help="Aggiorna direttamente dati/colori/tavolozza.json")

    sub.add_parser("autoverifica", help="Verifica numerica su un foglio sintetico con illuminante caldo e forze note")

    args = ap.parse_args()
    if args.comando == "autoverifica":
        esegui_autoverifica()
        return
    if args.comando == "scheda":
        out = pathlib.Path(args.uscita)
        genera_scheda_html(out)
        print(f"Scheda scritta in {out} ({out.stat().st_size // 1024} KB)")
        return

    angoli = None
    if args.angoli:
        vals = [float(x) for x in args.angoli.split(",")]
        if len(vals) != 8:
            raise SystemExit("taratura-campioni: --angoli richiede 8 numeri separati da virgola (x1,y1,...,x4,y4)")
        angoli = [(vals[i], vals[i + 1]) for i in range(0, 8, 2)]

    esito = analizza_immagine(
        args.foto,
        angoli=angoli,
        usa_foglio_stampa=not args.senza_foglio_stampa,
        bianco_carta_rif=args.bianco_carta,
    )
    tav_attuale = json.loads(FILE_TAVOLOZZA.read_text(encoding="utf-8"))
    print(f"Metodo bianco: {esito['metodo_bianco']}")
    print(f"Carta (A1):    {esito['carta_srgb']}")
    print("\nSei colori puri e fattori forza:")
    for c in tav_attuale["colori"]:
        cid = c["id"]
        print(f"  - {c['nome']:24s} ({c['pigmento']:11s}): {c['srgb']} -> {esito['puri_srgb'][cid]}   forza: {esito['forze'][cid]:.2f}")
    print(
        f"\nScarto medio OKLab sulle 8 miscele 1:1: "
        f"da {esito['errore_medio_oklab_prima']:.4f} (forza=1) a {esito['errore_medio_oklab_dopo']:.4f} (tarato)"
    )
    for m in esito["miscele"]:
        print(f"  {m['cella']} {m['titolo']:26s}  carta={m['misurato']}  modello={m['predetto_tarato']}  dOKLab={m['oklab_dopo']:.4f}")

    if args.confronto:
        salva_confronto_png(esito, tav_attuale, args.confronto)
        print(f"\nConfronto visivo salvato in {args.confronto}")
    if args.scrivi:
        aggiorna_tavolozza_json(esito)
        print(f"Aggiornato {FILE_TAVOLOZZA}")


if __name__ == "__main__":
    main()

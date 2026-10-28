#!/usr/bin/env python3
"""Prepara le fotografie delle opere per la sezione Opere.

Uso: python prepara-foto.py <cartella-di-origine> <id-autore>

Per ogni jpg o png della cartella di origine scrive immagini/<id-autore>/<nome>.jpg:
raddrizzata secondo l'orientamento della foto, lato lungo 1600 pixel, senza dati
EXIF e quindi senza la posizione GPS. Il nome viene da quello del file di origine,
in minuscolo e con il trattino al posto del trattino basso.

Per ogni foto stampa una riga JSON con la data e l'ora dello scatto, lette dai dati
EXIF, o, per le immagini di WhatsApp (IMG-AAAAMMGG-WA...), la data del nome del
file. Servono a compilare autori/<id-autore>.json quando il foglio non porta la data:
la data scritta a mano sul foglio, se c'è, si legge sulla foto e vale di più.
"""
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8")

QUI = Path(__file__).resolve().parent
LATO_LUNGO = 1600
ID_OK = re.compile(r"^[a-z0-9-]+$")
WHATSAPP = re.compile(r"^IMG-(\d{4})(\d{2})(\d{2})-WA\d+$", re.I)


def errore(msg):
    raise SystemExit(f"prepara-foto: {msg}")


def nome_pulito(stem):
    nome = re.sub(r"[^a-z0-9-]", "-", stem.lower().replace("_", "-"))
    return re.sub(r"-{2,}", "-", nome).strip("-")


def data_scatto(im, stem):
    """Data e ora dai dati EXIF (DateTimeOriginal, se no DateTime), altrimenti dal nome WhatsApp."""
    exif = im.getexif()
    valore = exif.get_ifd(0x8769).get(36867) or exif.get(306)
    if valore:
        m = re.match(r"^(\d{4}):(\d{2}):(\d{2}) (\d{2}):(\d{2})", str(valore))
        if m:
            return f"{m[1]}-{m[2]}-{m[3]}", f"{m[4]}.{m[5]}", "foto"
    m = WHATSAPP.match(stem)
    if m:
        return f"{m[1]}-{m[2]}-{m[3]}", None, "nome-file"
    return None, None, None


def main():
    if len(sys.argv) != 3:
        errore("uso: python prepara-foto.py <cartella-di-origine> <id-autore>")
    origine, autore = Path(sys.argv[1]), sys.argv[2]
    if not origine.is_dir():
        errore(f"cartella di origine assente: {origine}")
    if not ID_OK.match(autore):
        errore(f"id dell'autore non valido: {autore}")
    dest = QUI / "immagini" / autore
    dest.mkdir(parents=True, exist_ok=True)
    foto = sorted(p for p in origine.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"})
    if not foto:
        errore(f"nessuna foto in {origine}")
    for p in foto:
        with Image.open(p) as im:
            giorno, ora, data_da = data_scatto(im, p.stem)
            dritta = ImageOps.exif_transpose(im).convert("RGB")
        dritta.thumbnail((LATO_LUNGO, LATO_LUNGO), Image.LANCZOS)
        nome = nome_pulito(p.stem) + ".jpg"
        # senza il parametro exif Pillow non scrive i dati EXIF: niente GPS, modello o orientamento
        dritta.save(dest / nome, "JPEG", quality=85, optimize=True, progressive=True)
        riga = {"file": nome, "larghezza": dritta.width, "altezza": dritta.height,
                "giorno": giorno, "ora": ora, "data_da": data_da}
        print(json.dumps(riga, ensure_ascii=False))


if __name__ == "__main__":
    main()

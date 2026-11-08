#!/usr/bin/env python3
"""Genera S6 da testi, segmenti verificati e schemi SVG autonomi. Uso: pagina."""
import csv
import html
import importlib.util
import json
from pathlib import Path
import re
import sys

from infografiche import disegna

QUI = Path(__file__).resolve().parent
PAGINA = QUI / "urbano.html"
e = lambda s: html.escape(str(s), quote=True)

# Stessi comandi e stessa informativa degli Alberi, senza duplicare il lettore.
spec = importlib.util.spec_from_file_location("lettore_alberi", QUI.parent / "alberi" / "pit-261013-video-gesti.py")
lettore = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lettore)
sec, mmss = lettore.sec, lettore.mmss


def leggi():
    dati = json.loads((QUI / "urbano.json").read_text(encoding="utf-8"))
    with (QUI / "segmenti.csv").open(encoding="utf-8", newline="") as f:
        righe = list(csv.DictReader(f, delimiter=";"))
    seg = {r["passo"]: r for r in righe}
    if len(seg) != len(righe):
        raise ValueError("Segmenti duplicati")
    for vid, v in dati["video"].items():
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid) or not isinstance(v["durata_s"], int):
            raise ValueError("Identificativo o durata del video non validi")
        for campo in ("titolo", "autore", "canale", "consultato_il", "limite"):
            if not v.get(campo):
                raise ValueError(f"Video {vid}: manca {campo}")
    usati, id_visti = [], set()
    for esempio in dati["esempi"]:
        sigla, _ = esempio["voce"].split(" ", 1)
        for ident in [sigla] + [m["id"] for m in esempio["modalita"]]:
            if ident in id_visti:
                raise ValueError(f"Identificativo duplicato: {ident}")
            id_visti.add(ident)
        for m in esempio["modalita"]:
            if len(m["fasi"]) != 3 or not m["segmenti"]:
                raise ValueError("Ogni studio richiede tre fasi e almeno un segmento")
            for campo in ("titolo", "tipo", "osservazione", "proposta", "procedimento", "controllo"):
                if not m.get(campo):
                    raise ValueError(f"Studio {m['id']}: manca {campo}")
            for fase in m["fasi"]:
                if fase["carta"] not in {"bagnata", "umida", "asciutta"}:
                    raise ValueError("Stato della carta non valido")
            usati.extend(m["segmenti"])
    if set(usati) != set(seg) or len(usati) != len(set(usati)) or set(seg) & id_visti:
        raise ValueError("Segmenti mancanti, inutilizzati o identificativi duplicati")
    for r in righe:
        if not re.fullmatch(r"\d{2}:\d{2}", r["inizio"]) or not re.fullmatch(r"\d{2}:\d{2}", r["fine"]):
            raise ValueError("Tempi non nel formato mm:ss")
        if r["video"] not in dati["video"] or not 0 <= sec(r["inizio"]) < sec(r["fine"]) <= dati["video"][r["video"]]["durata_s"]:
            raise ValueError("Segmento fuori dalla durata del video")
        if r["incorporabile"] not in {"sì", "no"} or not r["verificato_il"] or not r["osservazione"]:
            raise ValueError("Segmento senza verifica o non incorporabile")
    if {r["video"] for r in righe} != set(dati["video"]):
        raise ValueError("Catalogo video non coerente con i segmenti")
    testo = json.dumps(dati, ensure_ascii=False) + json.dumps(righe, ensure_ascii=False)
    if "da verificare" in testo.lower() or "\u2014" in testo or "\ufffd" in testo:
        raise ValueError("Testo provvisorio o carattere non ammesso")
    return dati, seg


def video(r, v):
    s, f = sec(r["inizio"]), sec(r["fine"])
    link = f'https://www.youtube.com/watch?v={r["video"]}&t={s}s'
    if r["incorporabile"] == "no":
        return (f'<div class="video-esterno" id="{e(r["passo"])}" data-id="{e(r["video"])}" data-inizio="{s}" data-fine="{f}">'
                f'<p class="pv-tit">{e(r["etichetta"])}</p><p class="pv-dati">Da {e(r["inizio"])} a {e(r["fine"])} ({f-s} s). {e(v["autore"])}.</p>'
                '<p>Questo video si guarda su YouTube. Il link apre il minuto indicato; la riproduzione non si ferma da sola alla fine del passaggio.</p>'
                f'<a class="apri-youtube" href="{e(link)}" target="_blank" rel="noopener">Apri il passaggio su YouTube ↗</a>'
                f'<p class="nel-video">{e(r["osservazione"])}</p></div>')
    return (f'<div class="video" id="{e(r["passo"])}" data-passo="{e(r["passo"])}" data-id="{e(r["video"])}" data-inizio="{s}" data-fine="{f}">'
            f'<div class="prima-del-video"><p class="pv-tit">{e(r["etichetta"])}</p>'
            f'<p class="pv-dati">{f-s} s, da {e(r["inizio"])} a {e(r["fine"])}. {e(v["autore"])}, canale {e(v["canale"])}.</p>'
            '<p class="pv-avviso">Il video si carica solo al clic. YouTube (Google) riceverà alcuni dati della visita. '
            '<a href="../informativa/">Informativa del sito</a> · '
            f'<a href="{lettore.PRIVACY_GOOGLE}" target="_blank" rel="noopener">Privacy di Google</a> · '
            f'<a href="{lettore.TERMINI_YOUTUBE}" target="_blank" rel="noopener">Termini di YouTube</a></p>'
            f'<button class="guarda" type="button" aria-label="Guarda il video: {e(r["etichetta"])}"><span class="tri">▶</span><span class="lab">Guarda il video</span></button></div>'
            '<div class="schermo"></div><div class="comandi">'
            '<button type="button" class="dacapo">↺ Da capo</button>'
            '<button type="button" class="lento" aria-pressed="false">Lento</button>'
            '<button type="button" class="ripeti" aria-pressed="false">Ripeti</button>'
            f'<a class="yt" href="{e(link)}" target="_blank" rel="noopener">YouTube ↗</a></div>'
            f'<p class="dove-video">da {e(r["inizio"])} a {e(r["fine"])} nel video di {e(v["canale"])}</p>'
            f'<p class="nel-video">{e(r["osservazione"])}</p></div>')


def pagina():
    d, tab = leggi()
    a = d["apertura"]
    indice, sezioni = [], []
    for esempio in d["esempi"]:
        sigla, nome = esempio["voce"].split(" ", 1)
        indice.append(f'<a href="#{e(sigla)}">{e(esempio["breve"])}</a>')
        schede = []
        for m in esempio["modalita"]:
            fasi = []
            for n, fase in enumerate(m["fasi"], 1):
                svg = disegna(m["schema"], n, f'{m["id"]}-{n}', fase["titolo"])
                fasi.append(f'<div class="fase-card"><div class="fase-testa"><span class="fase-num">{n}</span><span class="fase-tit">{e(fase["titolo"])}</span></div>'
                            f'<div class="fase-svg">{svg}</div><div class="fase-meta">Carta: <span class="pill {e(fase["carta"])}">{e(fase["carta"])}</span>'
                            f'<span class="fase-pen">{e(fase["attrezzo"])}</span></div><p class="fase-txt">{e(fase["testo"])}</p></div>')
            players = "".join(video(tab[s], d["video"][tab[s]["video"]]) for s in m["segmenti"])
            schede.append(f'<article class="modalita-card" id="{e(m["id"])}"><div class="mod-head"><h3>{e(m["titolo"])}</h3>'
                          f'<span class="mod-autore">{e(m["tipo"])}</span></div>'
                          f'<p class="osservazione"><b>Nel video:</b> {e(m["osservazione"])}</p>'
                          f'<p class="mod-proposta"><b>Prova proposta:</b> {e(m["proposta"])}</p>'
                          '<div class="mod-info"><div class="mod-info-tit">La prova in tre fasi</div>'
                          f'<div class="fasi-grid tre">{"".join(fasi)}</div></div>'
                          f'<details class="procedimento"><summary>Procedimento della prova</summary><p>{e(m["procedimento"])}</p></details>'
                          f'<div class="info-check ok"><b>Che cosa osservare nella prova:</b> {e(m["controllo"])}</div>'
                          f'<h4>I passaggi di riferimento</h4>{players}</article>')
        sezioni.append(f'<section class="albero" id="{e(sigla)}"><h2><span class="sig">{e(sigla)}</span> {e(nome)}</h2>'
                       f'<p class="dove">{e(esempio["descrizione"])}</p><div class="modalita-lista">{"".join(schede)}</div></section>')
    fonti = []
    for vid, v in d["video"].items():
        fonti.append(f'<li><b>{e(v["autore"])}</b>, <a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">{e(v["titolo"])}</a>. '
                     f'{e(v["canale"])}, {mmss(v["durata_s"])}. {e(v["limite"])}</li>')
    corpo = (f'<header class="testa"><h1>{e(a["titolo"])}</h1></header>'
             f'<nav class="salti" aria-label="Esempi del modulo"><a href="../soggetti/">← Tutti i soggetti</a>{"".join(indice)}</nav>'
             '<div id="avviso" hidden></div><section class="intro"><div class="sommario"><h2>Sommario</h2>'
             f'<p>{e(a["sommario"])}</p></div><div class="guida" id="premessa"><h2>Premessa</h2>'
             + "".join(f'<p>{e(p)}</p>' for p in a["premessa"]) + '</div>'
             '<div class="uso-video" id="come-leggere"><h2>Come usare schemi e video</h2>'
             '<p>Le infografiche sono schemi disegnati, non immagini del video. Gli esercizi sono proposte da provare, non risultati già ottenuti.</p>'
             '<p>Gli stati della carta nelle fasi riguardano la prova proposta. La tinta degli schemi non identifica un pigmento.</p>'
             '<p><b>Guarda il video</b> apre il lettore ufficiale e lo ferma al termine dell’estratto. <b>Da capo</b> lo riavvia; '
             '<b>Lento</b> imposta metà velocità; <b>Ripeti</b> attiva la ripetizione. <b>YouTube ↗</b> apre il punto nella pagina originale.</p>'
             '<p>I tre passaggi della demo Iocco/Zangarelli si aprono su YouTube, che non consente qui il lettore incorporato. Il collegamento mantiene il minuto d’inizio.</p>'
             '<p>Per acqua, bordi e asciugatura: <a href="../principi/#carta-umidita">gli stati della carta nei Principi</a>. '
             'Per lavorare con pochi colori: <a href="../principi/#tavolozza-plein-air">la tavolozza ridotta</a>, non obbligatoria.</p></div>'
             '<details id="metodo"><summary>Fonti e limiti della consultazione</summary>'
             + "".join(f'<p>{e(p)}</p>' for p in a["metodo"]) + '</details></section>'
             + "".join(sezioni) + '<footer id="fonti"><h2>I tre video</h2><ul class="crediti">' + "".join(fonti) + '</ul>'
             '<p>Consultati l’8 novembre 2026. I video restano dei rispettivi autori. Cinque passaggi usano il lettore ufficiale di YouTube. '
             'I passaggi della demo italiana si aprono invece nella pagina originale. Le fotografie del corso e i fotogrammi di studio non vengono pubblicati.</p></footer>')
    css = lettore.CSS + "\n.video-esterno{margin:10px 0;padding:12px;background:#f7f5ef;border:1px solid #d8d3c6;border-radius:10px;font-size:.93em}.video-esterno p{margin:0 0 8px}.apri-youtube{display:block;background:#a33328;color:white;border-radius:8px;padding:10px 12px;font-weight:600;text-decoration:none}.osservazione{font-size:.93em;background:#f5f2ea;border-left:3px solid #ad9261;padding:8px 11px}.modalita-card h4{color:#2c4f3a;margin:18px 0 9px}.intro h2{font-size:1.05em;margin:0 0 7px}.fasi-grid .fase-txt{flex:1}.mod-autore{border-radius:6px}#metodo p{font-size:.9em}footer li{margin-bottom:12px}\n"
    testo = (f'<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
             f'<meta name="referrer" content="strict-origin-when-cross-origin"><title>{e(a["titolo"])}</title><style>{css}</style></head>'
             f'<body>{corpo}<script>{lettore.JS}</script></body></html>')
    PAGINA.write_text(testo, encoding="utf-8", newline="\n")
    print(f"pagina: {PAGINA}; {len(d['esempi'])} esempi, {sum(len(x['modalita']) for x in d['esempi'])} studi, {len(tab)} estratti")


if __name__ == "__main__":
    if sys.argv[1:] != ["pagina"]:
        raise SystemExit("Uso: genera-urbano.py pagina")
    pagina()

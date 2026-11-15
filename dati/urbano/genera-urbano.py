#!/usr/bin/env python3
"""Genera il modulo S6 · Paesaggio urbano da urbano.json, segmenti.csv e infografiche.py. Uso: pagina."""
import csv
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

QUI = Path(__file__).resolve().parent
if str(QUI) not in sys.path:
    sys.path.insert(0, str(QUI))

from infografiche import INFOGRAFICHE, rendi_coda_esempio, rendi_infografica_modalita

PAGINA = QUI / "urbano.html"

# Stesso lettore a clic, stessi stili e stesse pillole del modulo S1 · Alberi.
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
        raise ValueError("Segmenti duplicati in segmenti.csv")

    for vid, v in dati["video"].items():
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid) or not isinstance(v.get("durata_s"), int):
            raise ValueError(f"Identificativo o durata non validi per il video {vid}")
        for campo in ("titolo", "autore", "canale", "consultato_il", "nota_fonte"):
            if not v.get(campo):
                raise ValueError(f"Video {vid}: manca il campo {campo}")

    usati, id_visti, mod_ids = [], set(), set()
    for esempio in dati["esempi"]:
        sigla, _ = esempio["voce"].split(" ", 1)
        for campo in ("breve", "descrizione", "colori_studio", "colori_aperto", "pennelli", "esercizio", "controllo", "attenzione"):
            if not esempio.get(campo):
                raise ValueError(f"Esempio {sigla}: manca il campo {campo}")
        if sigla in id_visti:
            raise ValueError(f"Identificativo duplicato: {sigla}")
        id_visti.add(sigla)

        for m in esempio["modalita"]:
            mid = m["id"]
            if mid in id_visti:
                raise ValueError(f"Identificativo duplicato: {mid}")
            id_visti.add(mid)
            mod_ids.add(mid)
            if mid not in INFOGRAFICHE or len(INFOGRAFICHE[mid].get("fasi", [])) != 3:
                raise ValueError(f"Modalità {mid}: infografica in 3 fasi mancante o incompleta")
            if not m.get("segmenti"):
                raise ValueError(f"Modalità {mid}: nessun segmento associato")
            for campo in ("titolo", "autore", "proposta", "colori_video", "pennelli_video", "procedimento"):
                if not m.get(campo):
                    raise ValueError(f"Modalità {mid}: manca il campo {campo}")
            usati.extend(m["segmenti"])

    if mod_ids != set(INFOGRAFICHE):
        raise ValueError(f"Disallineamento tra modalità JSON ({sorted(mod_ids)}) e INFOGRAFICHE ({sorted(INFOGRAFICHE)})")
    if set(usati) != set(seg) or len(usati) != len(set(usati)) or (set(seg) & id_visti):
        raise ValueError("Segmenti mancanti, inutilizzati o con identificativi duplicati")

    for r in righe:
        if not re.fullmatch(r"\d{2}:\d{2}", r["inizio"]) or not re.fullmatch(r"\d{2}:\d{2}", r["fine"]):
            raise ValueError(f"Segmento {r['passo']}: tempi non nel formato mm:ss")
        if r["video"] not in dati["video"]:
            raise ValueError(f"Segmento {r['passo']}: video {r['video']} non presente in urbano.json")
        i0, i1 = sec(r["inizio"]), sec(r["fine"])
        if not (0 <= i0 < i1 <= dati["video"][r["video"]]["durata_s"]):
            raise ValueError(f"Segmento {r['passo']}: intervallo {r['inizio']}-{r['fine']} fuori dalla durata del video")
        if r["incorporabile"] != "sì":
            raise ValueError(f"Segmento {r['passo']}: il video deve essere incorporabile (incorporabile=sì)")
        for campo in ("verificato_il", "etichetta", "nel_video", "sintesi"):
            if not r.get(campo):
                raise ValueError(f"Segmento {r['passo']}: manca il campo {campo}")

    if {r["video"] for r in righe} != set(dati["video"]):
        raise ValueError("Catalogo video in urbano.json non coerente con segmenti.csv")

    testo = json.dumps(dati, ensure_ascii=False) + json.dumps(righe, ensure_ascii=False)
    if "da verificare" in testo.lower() or "\u2014" in testo or "\u2013" in testo or "\ufffd" in testo:
        raise ValueError("Testo provvisorio o carattere non ammesso (trattino lungo/medio o U+FFFD)")
    return dati, seg


def con_collegamenti(p, e):
    """Trasforma in link le espressioni elencate in p['link']."""
    testo = e(p["testo"])
    for lk in p.get("link", []):
        parola = e(lk["parola"])
        if parola not in testo:
            raise ValueError(f"Premessa: «{lk['parola']}» non compare nel paragrafo")
        testo = testo.replace(parola, f'<a href="{e(lk["href"])}">{parola}</a>', 1)
    return f"<p>{testo}</p>"


def scatola_video(r, v, e):
    i0, i1 = sec(r["inizio"]), sec(r["fine"])
    yt = f'https://www.youtube.com/watch?v={r["video"]}&t={i0}s'
    da_video = f'dal video «{e(v["titolo"])}» di {e(v["canale"])}'
    sintesi = r.get("sintesi", "")
    riga_sintesi = (
        f'<p class="traduzione muto">{e(sintesi)}</p>'
        if sintesi.startswith("(")
        else f'<details class="sintesi-video"><summary>Dal video, in sintesi</summary><p class="traduzione">{e(sintesi)}</p></details>'
    ) if sintesi else ""
    nel_video = f'<p class="nel-video">{e(r["nel_video"])}</p>' if r.get("nel_video") else ""

    return (
        f'<div class="video" id="{e(r["passo"])}" data-passo="{e(r["passo"])}" data-id="{e(r["video"])}" data-inizio="{i0}" data-fine="{i1}">'
        f'<div class="prima-del-video">'
        f'<p class="pv-tit">{e(r["etichetta"])}</p>'
        f'<p class="pv-dati">{i1 - i0} s, da {mmss(i0)} a {mmss(i1)}, {da_video}</p>'
        f'<p class="pv-avviso">Il video è ospitato su YouTube: aprendolo, YouTube (Google) riceverà alcuni dati della tua visita. '
        f'<a href="../informativa/">Informativa del sito</a> · '
        f'<a href="{lettore.PRIVACY_GOOGLE}" target="_blank" rel="noopener">Privacy di Google</a> · '
        f'<a href="{lettore.TERMINI_YOUTUBE}" target="_blank" rel="noopener">Termini di YouTube</a></p>'
        f'<button class="guarda" type="button" aria-label="Guarda il video: {e(r["etichetta"])}"><span class="tri">▶</span><span class="lab">Guarda il video</span></button>'
        f'</div>'
        f'<div class="schermo"></div>'
        f'<div class="comandi">'
        f'<button type="button" class="dacapo">↺ Da capo</button>'
        f'<button type="button" class="lento" aria-pressed="false">Lento</button>'
        f'<button type="button" class="ripeti" aria-pressed="false">Ripeti</button>'
        f'<a class="yt" href="{e(yt)}" target="_blank" rel="noopener">YouTube ↗</a>'
        f'</div>'
        f'<p class="dove-video">da {mmss(i0)} a {mmss(i1)} nel video di {e(v["canale"])}</p>'
        f'{riga_sintesi}{nel_video}'
        f'</div>'
    )


def pagina():
    c = lettore.comune()
    e, pill = c.e, c.pillola
    d, tab = leggi()
    a = d["apertura"]

    sezioni, indice, elenco = [], [], []
    video_usati = []
    tot_modalita = 0

    for t in d["esempi"]:
        sigla, nome = t["voce"].split(" ", 1)
        n_mod = len(t["modalita"])
        tot_modalita += n_mod
        indice.append(f'<a href="#{e(sigla)}">{e(t["breve"])}</a>')
        elenco.append(f'<li><a href="#{e(sigla)}">{e(nome)}</a> <span class="cnt-mod">({n_mod} modalità)</span></li>')

        blocco_colori = (
            f'<p class="colori studio"><b>🎨 <a href="../principi/#tavolozza-studio" style="color:inherit">Colori in studio</a> (proposta libera):</b> {e(t["colori_studio"])}</p>'
            f'<p class="colori aperto"><b>🎒 All\'aperto (con la <a href="../principi/#tavolozza-plein-air">tavolozza ridotta</a>):</b> {e(t["colori_aperto"])}</p>'
        )
        pennelli = f'<p class="pennelli"><b>🖌 Pennelli e attrezzi:</b> {e(t["pennelli"])}</p>'
        testo_es = e(t["esercizio"]).replace(
            "liquido per mascherare",
            '<a href="../approfondimenti/bianco/#riserve" style="color:#2c6a4a;font-weight:600">liquido per mascherare</a>',
            1,
        )
        esercizio = f'<div class="esercizio"><b>📄 Come esercitarsi:</b> {testo_es}</div>'

        schede_mod = []
        for m in t["modalita"]:
            mid = m["id"]
            info_svg = rendi_infografica_modalita(mid, e, pill)
            players_list = []
            for s_id in m["segmenti"]:
                r = tab[s_id]
                vid = r["video"]
                if vid not in video_usati:
                    video_usati.append(vid)
                players_list.append(scatola_video(r, d["video"][vid], e))
            players = "".join(players_list)
            procedimento = (
                f'<details class="procedimento"><summary>Descrizione estesa del metodo</summary>'
                f'<p>{e(m["procedimento"])}</p></details>'
            )
            schede_mod.append(
                f'<article class="modalita-card" id="{e(mid)}">'
                f'<div class="mod-head">'
                f'<h3>{e(m["titolo"])}</h3>'
                f'<span class="mod-autore">Video: {e(m["autore"])}</span>'
                f'</div>'
                f'<p class="mod-proposta"><b>Il metodo:</b> {e(m["proposta"])}</p>'
                f'<div class="mod-meta">'
                f'<p><b>🎨 Colori usati nel video:</b> {e(m["colori_video"])}</p>'
                f'<p><b>🖌 Pennelli e attrezzi nel video:</b> {e(m["pennelli_video"])}</p>'
                f'</div>'
                f'{info_svg}{procedimento}'
                f'<div class="mod-videos">{players}</div>'
                f'</article>'
            )

        blocco_coda = rendi_coda_esempio(t, e)
        sezioni.append(
            f'<section class="albero" id="{e(sigla)}">'
            f'<h2><span class="sig">{e(sigla)}</span> {e(nome)}</h2>'
            f'<p class="dove">{e(t["descrizione"])}</p>'
            f'{blocco_colori}{pennelli}{esercizio}'
            f'<div class="modalita-lista">{"".join(schede_mod)}</div>'
            f'{blocco_coda}'
            f'</section>'
        )

    premessa = "".join(con_collegamenti(p, e) for p in a["premessa"])
    sommario = e(a["sommario"].format(modalita=tot_modalita, video=len(video_usati)))
    metodo_p = "".join(f"<p>{e(p)}</p>" for p in a.get("metodo", []))
    crediti = "".join(
        f'<li><b>{e(d["video"][vid]["autore"])}</b>, '
        f'<a href="https://www.youtube.com/watch?v={e(vid)}" target="_blank" rel="noopener">«{e(d["video"][vid]["titolo"])}»</a>, '
        f'canale {e(d["video"][vid]["canale"])} ({mmss(d["video"][vid]["durata_s"])}). {e(d["video"][vid]["nota_fonte"])}</li>'
        for vid in video_usati
    )

    corpo = f"""<header class="testa"><h1>{e(a["titolo"])}</h1></header>
<nav class="salti" aria-label="Esempi del modulo"><a href="../soggetti/">← Tutti i soggetti</a>{"".join(indice)}</nav>
<div id="avviso" hidden></div>
<section class="intro">
<div class="sommario" id="sommario">
<h3>Sommario</h3>
<p>{sommario}</p>
</div>
<div class="indice" id="indice">
<h3>Indice</h3>
<ol class="indice-voci">
<li><a href="#premessa">Premessa</a></li>
<li><a href="#come-leggere">Come leggere le infografiche e usare i video</a></li>
<li>I tre esempi del paesaggio urbano ({tot_modalita} modalità nei video)<ol class="alberi">{"".join(elenco)}</ol></li>
</ol>
</div>
<div class="guida" id="premessa">
<h3>Premessa</h3>
{premessa}
</div>
<div class="uso-video" id="come-leggere">
<h3>Come leggere le infografiche e usare i video</h3>
<p class="legenda"><b>Stato della carta nelle fasi dell'infografica:</b> {pill('bagnata')} lucida d'acqua, il colore corre · {pill('umida')} opaca, i bordi si fondono · {pill('asciutta')} il tratto resta netto. <a href="../principi/#carta-umidita">Gli stati della carta, momenti di mezzo compresi, nei Principi generali</a>.</p>
<ul class="come">
<li>Al posto di ogni video c'è un riquadro del sito: finché non si preme <b>▶ Guarda il video</b>, la pagina non carica nulla da YouTube o da Google. Il pulsante apre il lettore ufficiale, fa partire il video nel punto giusto e lo ferma da solo alla fine del passaggio. Che cosa succede ai dati della visita è spiegato nell'<a href="../informativa/">informativa del sito</a>.</li>
<li><b>Da capo</b> fa ripartire l'estratto, <b>Lento</b> lo porta a metà velocità per studiare il movimento del pennello, <b>Ripeti</b> lo ripete in continuo mentre si prova sulla carta.</li>
<li><b>YouTube ↗</b> apre lo stesso punto nell'app o nel sito di YouTube.</li>
<li>I riquadri apribili <b>Dal video, in sintesi</b> riassumono in italiano quello che l'autore o l'autrice spiega o mostra in quel passaggio: sono sintesi preparate con l'aiuto dell'intelligenza artificiale, non trascrizioni, e la fonte resta il video.</li>
</ul>
</div>
<details id="metodo">
<summary>Nota di metodo sui video e sulle infografiche</summary>
{metodo_p}
</details>
</section>
{"".join(sezioni)}
<footer id="fonti"><h2>I video</h2><p>I video restano dei loro autori: la pagina li mostra col lettore ufficiale di YouTube, senza copiarli. Grazie a:</p>
<ul class="crediti">{crediti}</ul>
<p>Le {tot_modalita} infografiche in 3 fasi sono disegnate per questa guida, una per ogni modalità.</p></footer>"""

    css = lettore.CSS + "\n.fasi-grid .fase-txt { flex: 1; }\n#metodo p { margin: 6px 0 0; font-size: .9em; }\nfooter ul.crediti li { margin-bottom: 8px; }\n"
    testo = (
        f'<!doctype html>\n<html lang="it"><head><meta charset="utf-8">\n'
        f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<meta name="referrer" content="strict-origin-when-cross-origin">\n'
        f'<title>{e(a["titolo"])}</title>\n<style>{css}</style></head>\n'
        f'<body>{corpo}<script>{lettore.JS}</script></body></html>\n'
    )
    PAGINA.write_text(testo, encoding="utf-8", newline="\n")
    print(f"pagina: {PAGINA}; {len(d['esempi'])} esempi, {tot_modalita} modalità, {len(tab)} estratti")


if __name__ == "__main__":
    if sys.argv[1:] != ["pagina"]:
        raise SystemExit("Uso: genera-urbano.py pagina")
    pagina()

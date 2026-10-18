# Pagina coi pezzi dei video veri per i gesti degli alberi ad acquerello.
#
# Dal 16/10/2026 lo script sta nel repository app-acquerello (dati/alberi/), che è la copia principale:
# per «pagina» bastano i file di questa cartella. Gli altri comandi usano yt-dlp, YouTube e le schede
# dei video, che restano nel workspace di Sandro (pit/acquerello-alberi/schede/): girano dal W520.
#
# Dal 14/10/2026 la pagina è un tutorial sugli alberi, senza il corso: niente stampa della prima prova
# né ritagli, nessun passo attribuito a Irene, e i quattro passi che venivano dalla sua demo hanno un
# video. Il contenuto sta in pit-261014-video-gesti-alberi.json, ricavato dalla versione breve del 13/10,
# che resta per i pdf. La pagina del 13/10, legata alla prima prova, sta in old/ e non si rigenera più.
# Prova della pagina in Chrome: pit-261014-prova-pagina.py; fotogrammi dal lettore della pagina, se il
# flusso diretto è troppo lento: pit-261014-foglio-dal-lettore.py.
#
#   python pit-261013-video-gesti.py info
#       legge con yt-dlp -J i video dei passi della versione breve (durata, canale, capitoli e
#       playable_in_embed, cioè se l'autore permette di incorporarlo) e crea o aggiorna la tabella
#       dei segmenti, senza toccare inizio, fine e note già scritti.
#   python pit-261013-video-gesti.py fogli [A1-3 ...]
#       per ogni passo con video, un fotogramma ogni 3 s da 12 s prima a 33 s dopo il minuto della
#       scheda, in un foglio a griglia; i fotogrammi si leggono dal flusso, il video non si scarica.
#       «A1-3@13:10-14:40/5» chiede una finestra a scelta; «A1-4=pD2RifxNeRM@02:10-03:00/3» la chiede
#       su un altro video, per esempio una fonte della versione completa.
#   python pit-261013-video-gesti.py mandati
#       per i subagenti che propongono inizio e fine: passo, passaggi della scheda, capitoli e
#       sottotitoli automatici attorno al minuto, un file per segmento.
#   python pit-261013-video-gesti.py controllo [A1-3 ...]
#       foglio di controllo del segmento scelto, un fotogramma al secondo da inizio a fine.
#   python pit-261013-video-gesti.py pagina
#       genera la pagina html dal json della pagina e dalla tabella dei segmenti.
#
# Ingresso: pit-261014-video-gesti-alberi.json (testi e video dei passi), le selezioni dei video
#           (canale e titolo), le schede, la tabella dei segmenti.
# Uscita:   pit-261013-video-gesti-segmenti.csv (un pezzo per riga: video, inizio, fine, incorporabile,
#           etichetta e riga «nel video» per la pagina, nota sulla scelta; «A5-6b» è il secondo pezzo
#           del passo A5-6) e pit-261014-video-gesti-alberi.html.
# La tabella si scrive a mano: inizio e fine li decide il modello di sessione, sui fogli di controllo.
# I file di lavoro stanno in %TEMP%\pit-alberi\video-gesti\ (fuori dal workspace): si rigenerano.
import concurrent.futures, csv, glob, json, os, subprocess, sys

QUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(QUI, "pit-261014-video-gesti-alberi.json")
TABELLA = os.path.join(QUI, "pit-261013-video-gesti-segmenti.csv")
PAGINA = os.path.join(QUI, "pit-261014-video-gesti-alberi.html")
LAVORO = os.path.join(os.environ.get("TEMP", "."), "pit-alberi", "video-gesti")
YTDLP = os.path.expanduser("~/.local/bin/yt-dlp.exe")
COLONNE = ["passo", "albero", "video", "canale", "minuto_scheda", "inizio", "fine", "durata_s",
           "incorporabile", "etichetta", "nel_video", "traduzione", "quadri", "nota"]

selezione = {}
for _f in sorted(glob.glob(os.path.join(QUI, "pit-*-alberi-selezione-video*.csv"))):
    selezione.update({r["id"]: r for r in csv.DictReader(open(_f, encoding="utf-8"), delimiter=";")})

def sec(m):
    p = [int(x) for x in str(m).strip().split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1] if len(p) == 2 else p[0]

def mmss(s):
    return f"{s // 60:02d}:{s % 60:02d}"

def passi_con_video(d):
    # Sigla del passo: albero e numero d'ordine del passo nella versione breve (A1-3 = terzo passo di A1).
    for t in d["alberi"]:
        s, nome = t["voce"].split(" ", 1)
        for n, p in enumerate(t["passi"], 1):
            if p.get("video"):
                yield f"{s}-{n}", nome, p

def principale(sigla):
    # «A5-6b» è il secondo pezzo del passo A5-6, per i passi che contengono due gesti.
    return sigla.rstrip("abcdefgh")

def leggi_tabella():
    if not os.path.exists(TABELLA):
        return {}
    return {r["passo"]: r for r in csv.DictReader(open(TABELLA, encoding="utf-8"), delimiter=";")}

def scrivi_tabella(righe):
    with open(TABELLA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLONNE, delimiter=";")
        w.writeheader()
        w.writerows(righe)

def info_video(vid):
    os.makedirs(os.path.join(LAVORO, "info"), exist_ok=True)
    out = os.path.join(LAVORO, "info", f"{vid}.json")
    if not os.path.exists(out):
        r = subprocess.run([YTDLP, "-J", "--no-warnings", "--skip-download", f"https://www.youtube.com/watch?v={vid}"],
                           capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0:
            return {"id": vid, "errore": r.stderr[-400:]}
        j = json.loads(r.stdout)
        tenuti = {k: j.get(k) for k in ("id", "title", "channel", "uploader", "duration", "playable_in_embed",
                                         "availability", "age_limit", "live_status", "chapters")}
        tenuti["sottotitoli_auto"] = sorted(k for k in (j.get("automatic_captions") or {}) if k in ("en", "it", "en-orig", "it-orig"))
        tenuti["sottotitoli"] = sorted((j.get("subtitles") or {}).keys())
        json.dump(tenuti, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return json.load(open(out, encoding="utf-8"))

def info():
    d = json.load(open(FONTE, encoding="utf-8"))
    vecchie = leggi_tabella()
    passi = list(passi_con_video(d))
    extra = {s: r for s, r in vecchie.items() if s != principale(s)}
    ids = sorted({(vecchie.get(s) or {}).get("video") or p["video"]["id"] for s, _, p in passi} | {r["video"] for r in extra.values()})
    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        dati = dict(zip(ids, ex.map(info_video, ids)))
    righe = []
    for s, nome, p in passi:
        r = vecchie.get(s) or {"passo": s, "video": p["video"]["id"], "minuto_scheda": p["video"]["minuto"],
                               "inizio": "", "fine": "", "nota": ""}
        for r in [r] + [extra[x] for x in sorted(extra) if principale(x) == s]:
            r["albero"] = nome
            j = dati.get(r["video"], {})
            r["canale"] = j.get("channel") or selezione.get(r["video"], {}).get("canale", "")
            r["incorporabile"] = {True: "sì", False: "no"}.get(j.get("playable_in_embed"), "da verificare")
            r["durata_s"] = str(sec(r["fine"]) - sec(r["inizio"])) if r.get("inizio") and r.get("fine") else ""
            righe.append({k: r.get(k, "") for k in COLONNE})
    scrivi_tabella(righe)
    for vid in ids:
        j = dati[vid]
        print(vid, "ERRORE " + j["errore"] if "errore" in j else
              f"embed={j.get('playable_in_embed')} durata={j.get('duration')} disp={j.get('availability')} "
              f"eta={j.get('age_limit')} capitoli={len(j.get('chapters') or [])} sub_auto={j.get('sottotitoli_auto')} "
              f"| {j.get('channel')} | {(j.get('title') or '')[:60]}")
    print(len(righe), "passi con video nella tabella", TABELLA)

FORMATI = ("bv*[height<=480][ext=mp4]/bv*[height<=480]", "18/best[height<=480]", "bv*[height<=720]")

def flusso(vid, tentativo=0):
    for formato in FORMATI[tentativo:] + FORMATI[:tentativo]:
        r = subprocess.run([YTDLP, "-g", "--no-warnings", "-f", formato, f"https://www.youtube.com/watch?v={vid}"],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip().splitlines()[0]
    raise RuntimeError(f"nessun flusso per {vid}: {r.stderr[-300:]}")

def finestra(vid, t0, durata, passo, cartella, lato=400):
    # Legge dal flusso solo la finestra richiesta e ne tiene un fotogramma ogni «passo» secondi.
    os.makedirs(cartella, exist_ok=True)
    for f in glob.glob(os.path.join(cartella, "f*.jpg")):
        os.remove(f)
    for tentativo in range(len(FORMATI)):
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t0), "-i", flusso(vid, tentativo),
                            "-t", str(durata), "-vf", f"fps=1/{passo},scale={lato}:-2", "-q:v", "3",
                            os.path.join(cartella, "f%02d.jpg")], capture_output=True, text=True)
        uscite = sorted(glob.glob(os.path.join(cartella, "f*.jpg")))
        if r.returncode == 0 and uscite:
            return [(t0 + i * passo, u) for i, u in enumerate(uscite)]
    raise RuntimeError(f"ffmpeg {vid} {t0}: {r.stderr[-300:]}")

def testo_passo(d, sigla):
    s, n = principale(sigla).split("-")
    t = next(t for t in d["alberi"] if t["voce"].split()[0] == s)
    return t["passi"][int(n) - 1]["testo"]

def foglio(sigla, vid, t0, durata, passo, testo, nome, col=4, lato=400, titolo=None):
    from PIL import Image, ImageDraw, ImageFont
    quadri = finestra(vid, t0, durata, passo, os.path.join(LAVORO, "quadri", nome), lato)
    font, piccolo = ImageFont.truetype("arialbd.ttf", 24), ImageFont.truetype("arial.ttf", 19)
    ims = [(t, Image.open(u).convert("RGB")) for t, u in quadri]
    h = max(im.height for _, im in ims)
    righe = (len(ims) + col - 1) // col
    out = Image.new("RGB", (lato * col, 64 + righe * (h + 4)), "white")
    dr = ImageDraw.Draw(out)
    dr.text((8, 6), titolo or f"{sigla} · {vid} · {mmss(t0)}-{mmss(t0 + durata)}, uno ogni {passo} s", fill="black", font=font)
    dr.text((8, 36), testo[:150], fill=(60, 60, 60), font=piccolo)
    for i, (t, im) in enumerate(ims):
        x, y = (i % col) * lato, 64 + (i // col) * (h + 4)
        out.paste(im, (x, y))
        dr.rectangle([x, y, x + 86, y + 30], fill="black")
        dr.text((x + 6, y + 2), mmss(t), fill="yellow", font=font)
    percorso = os.path.join(LAVORO, "fogli", f"foglio-{nome}.jpg")
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    out.save(percorso, quality=85)
    return percorso

def fogli(args):
    # Senza argomenti: tutti i segmenti distinti, da 12 s prima a 33 s dopo il minuto della scheda.
    # Un argomento «A1-3@13:10-14:40/5» chiede invece una finestra a scelta, con un fotogramma ogni 5 s;
    # «A1-4=8O_avJO4cHY@04:20-05:50/5» la chiede su un altro video, per esempio una fonte della versione completa.
    d = json.load(open(FONTE, encoding="utf-8"))
    tab = leggi_tabella()
    lavori, visti = [], set()
    for a in (args or list(tab)):
        sigla, _, spec = a.partition("@")
        sigla, _, altro = sigla.partition("=")
        r = tab[sigla]
        vid = altro or r["video"]
        if spec:
            fin, _, passo = spec.partition("/")
            da, _, a_ = fin.partition("-")
            t0, durata, passo = sec(da), sec(a_) - sec(da), int(passo or 3)
            nome = f"{sigla}{'-' + altro if altro else ''}-{da.replace(':', '')}-{a_.replace(':', '')}"
        else:
            if (r["video"], r["minuto_scheda"]) in visti:
                continue
            visti.add((r["video"], r["minuto_scheda"]))
            t0, durata, passo, nome = max(0, sec(r["minuto_scheda"]) - 12), 48, 3, sigla
        lavori.append((sigla, vid, t0, durata, passo, testo_passo(d, sigla), nome))
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for p in ex.map(lambda x: foglio(*x), lavori):
            print(p, flush=True)

def controllo(args):
    # Foglio di controllo del segmento scelto: un fotogramma al secondo da 1 s prima dell'inizio a 1 s dopo la fine.
    d = json.load(open(FONTE, encoding="utf-8"))
    tab = leggi_tabella()
    lavori, visti = [], set()
    for sigla in (args or list(tab)):
        r = tab[sigla]
        if not r["inizio"] or not r["fine"] or (r["video"], r["inizio"], r["fine"]) in visti:
            continue
        visti.add((r["video"], r["inizio"], r["fine"]))
        t0, t1 = max(0, sec(r["inizio"]) - 1), sec(r["fine"]) + 1
        titolo = f"{sigla} · {r['video']} · segmento {r['inizio']}-{r['fine']}, un fotogramma al secondo da {mmss(t0)}"
        lavori.append((sigla, r["video"], t0, t1 - t0, 1, testo_passo(d, sigla), f"controllo-{sigla}", 6, 300, titolo))
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for p in ex.map(lambda x: foglio(*x), lavori):
            print(p, flush=True)

def sottotitoli(vid):
    # Sottotitoli automatici nella lingua del video, solo come aiuto per collocare il gesto.
    import re, time
    cartella = os.path.join(LAVORO, "sub")
    os.makedirs(cartella, exist_ok=True)
    lingua = "it-orig" if selezione.get(vid, {}).get("lingua") == "italiano" else "en-orig"
    vtt = glob.glob(os.path.join(cartella, f"{vid}.*.vtt"))
    if not vtt:
        for lingue in (lingua, "en,it"):
            subprocess.run([YTDLP, "--skip-download", "--write-auto-subs", "--sub-langs", lingue, "--sub-format", "vtt",
                            "--no-warnings", "-o", os.path.join(cartella, "%(id)s"),
                            f"https://www.youtube.com/watch?v={vid}"], capture_output=True, text=True)
            vtt = glob.glob(os.path.join(cartella, f"{vid}.*.vtt"))
            if vtt:
                break
            time.sleep(2)
    if not vtt:
        return []
    righe, ultime = [], []
    for blocco in open(vtt[0], encoding="utf-8").read().split("\n\n"):
        m = re.search(r"(\d+):(\d+):(\d+)\.\d+ -->", blocco)
        if not m:
            continue
        t = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
        for l in blocco.splitlines()[1:]:
            l = re.sub(r"<[^>]+>", "", l).strip()
            if l and l not in ultime:
                righe.append((t, l))
                ultime = (ultime + [l])[-3:]
    return righe

def mandati():
    # Un file per segmento distinto con quello che serve a chi guarda i fotogrammi: il passo, i
    # passaggi della scheda vicini al minuto, i capitoli e i sottotitoli attorno al minuto.
    d = json.load(open(FONTE, encoding="utf-8"))
    tab = leggi_tabella()
    os.makedirs(os.path.join(LAVORO, "mandati"), exist_ok=True)
    schede = {}
    for f in glob.glob(os.path.join(cartella_schede(), "*.json")):
        j = json.load(open(f, encoding="utf-8"))
        schede[j["video"]["id"]] = j
    if not schede:
        print("ATTENZIONE: nessuna scheda dei video in", cartella_schede())
    ids = sorted({r["video"] for r in tab.values()})
    sub = {vid: sottotitoli(vid) for vid in ids}
    gruppi = {}
    for sigla, r in tab.items():
        gruppi.setdefault((r["video"], r["minuto_scheda"]), []).append(sigla)
    for (vid, minuto), sigle in gruppi.items():
        t0 = sec(minuto)
        alberi = {t["voce"].split()[0]: t for t in d["alberi"]}
        j = info_video(vid)
        sc = schede.get(vid, {})
        v = sc.get("video", {})
        r = [f"# Segmento {', '.join(sigle)}", "",
             f"Video `{vid}`: «{v.get('titolo', j.get('title'))}», {v.get('canale', j.get('channel'))}, "
             f"durata {mmss(int(j.get('duration') or 0))}, lingua {v.get('lingua', '?')}.",
             f"Minuto indicato dalla scheda: **{minuto}**. Foglio dei fotogrammi: `{os.path.join(LAVORO, 'fogli', 'foglio-' + sigle[0] + '.jpg')}`", ""]
        for s in sigle:
            a, n = s.split("-")
            t = alberi[a]
            r += [f"## Passo {s} ({t['voce']})", "", f"Testo del passo: «{t['passi'][int(n) - 1]['testo']}»",
                  f"Stato della carta nel passo: {t['passi'][int(n) - 1].get('carta')}. L'albero: {t['descrizione']}", ""]
        r += ["## Passaggi della scheda vicini al minuto", ""]
        for p in sc.get("scheda", {}).get("passaggi", []):
            if abs(sec(p["minuto"]) - t0) <= 150:
                r.append(f"- {p['minuto']} · {p.get('fase')} · carta {p.get('carta')} · {p.get('pennello')} · {p.get('colore')} · gesto: {p.get('gesto')}")
        for p in sc.get("scheda", {}).get("tecniche", []):
            if p.get("minuto") and abs(sec(p["minuto"]) - t0) <= 150:
                r.append(f"- tecnica a {p['minuto']} · {p.get('nome')}: {p.get('come')}")
        r += ["", "## Capitoli del video", ""]
        r += [f"- {mmss(int(c['start_time']))} {c['title']}" for c in (j.get("chapters") or [])] or ["- nessuno"]
        r += ["", f"## Sottotitoli automatici da {mmss(max(0, t0 - 30))} a {mmss(t0 + 90)}", ""]
        estratto = [f"{mmss(t)} {l}" for t, l in sub[vid] if t0 - 30 <= t <= t0 + 90]
        r += estratto or ["(nessun sottotitolo: video senza parlato o sottotitoli non disponibili)"]
        open(os.path.join(LAVORO, "mandati", f"{sigle[0]}.md"), "w", encoding="utf-8").write("\n".join(r) + "\n")
        print(sigle, vid, minuto, len(estratto), "righe di sottotitoli")

def cartella_schede():
    # Le schede dei video stanno con lo studio, nel workspace: <workspace>/pit/acquerello-alberi/schede/.
    # Il repository è in <workspace>/software/applicazioni-github/app-acquerello/, cinque livelli sotto.
    if os.path.isdir(os.path.join(QUI, "schede")):
        return os.path.join(QUI, "schede")
    wks = QUI
    for _ in range(5):
        wks = os.path.dirname(wks)
    return os.path.join(wks, "pit", "acquerello-alberi", "schede")

def comune():
    # Testo protetto per l'html, immagini in jpeg e pillole della carta. Fino al 16/10/2026 venivano dallo
    # script del tutorial completo, pit-261013-impagina-tutorial.py, che resta nel workspace per i pdf:
    # qui sono ricopiate uguali, perché la pagina si generi coi soli file del repository. Le immagini
    # della pagina stanno tutte in illustrazioni/.
    import base64, html, io, types
    from PIL import Image, ImageOps

    e = lambda t: html.escape(str(t or ""))

    def jpeg(im, lato=1400, q=84):
        im = im.convert("RGB")
        im.thumbnail((lato, lato))
        b = io.BytesIO()
        im.save(b, "JPEG", quality=q)
        return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

    def apri(nome):
        return ImageOps.exif_transpose(Image.open(os.path.join(QUI, "illustrazioni", nome)))

    def pillola(carta):
        c = (carta or "").strip().lower()
        return f'<span class="pill {e(c)}">{e(c)}</span>' if c in ("bagnata", "umida", "asciutta") else ""

    return types.SimpleNamespace(e=e, jpeg=jpeg, apri=apri, pillola=pillola)

def tempi_striscia(r, i0, i1):
    if r and r.get("quadri"):
        return [sec(x) for x in r["quadri"].split(",") if x.strip()]
    d = max(4, i1 - i0)
    return [i0 + 1, i0 + d // 3, i0 + (2 * d) // 3, max(i0 + 3, i1 - 1)]

def strisce(url="http://127.0.0.1:8765/pit-261014-video-gesti-alberi.html"):
    import io, time
    from PIL import Image
    from playwright.sync_api import sync_playwright
    cartella = os.path.join(LAVORO, "strisce")
    os.makedirs(cartella, exist_ok=True)
    tab = leggi_tabella()
    da_fare = []
    visti = set()
    for sigla, r in tab.items():
        if not r.get("inizio") or not r.get("fine"):
            continue
        vid, i0, i1 = r["video"], sec(r["inizio"]), sec(r["fine"])
        ts = tempi_striscia(r, i0, i1)
        mancanti = []
        for t in ts:
            if (vid, t) in visti:
                continue
            visti.add((vid, t))
            fp = os.path.join(cartella, f"{vid}-t{t}.jpg")
            if not (os.path.exists(fp) and os.path.getsize(fp) > 1000):
                mancanti.append((t, fp))
        if mancanti:
            da_fare.append((sigla, vid, mancanti))
    if not da_fare:
        print("Tutte le strisce sono già presenti in", cartella)
        return
    css_pulito = (".ytp-chrome-top, .ytp-chrome-bottom, .ytp-bezel, .ytp-bezel-text-wrapper, "
                  ".ytp-caption-window-container, .ytp-gradient-top, .ytp-gradient-bottom, "
                  ".ytp-watermark, .ytp-ce-element, .ytp-pause-overlay, .ytp-spinner { display: none !important; }")
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=True, args=["--autoplay-policy=no-user-gesture-required"])
        pg = b.new_page(viewport={"width": 1200, "height": 900})
        pg.goto(url, wait_until="load")
        for sigla, vid, mancanti in da_fare:
            v = pg.locator(f'.video[data-passo="{sigla}"]')
            schermo = v.locator(".schermo")
            for t, out in mancanti:
                v.evaluate(f"(el) => {{ el.dataset.inizio = '{t}'; el.dataset.fine = '{t + 5}'; }}")
                if v.locator("button.guarda").is_visible():
                    v.locator("button.guarda").click()
                else:
                    v.locator("button.dacapo").click()
                t0 = time.time()
                while time.time() - t0 < 12:
                    s = pg.evaluate("window.statoGesto && window.statoGesto()")
                    if s and s["stato"] == 1 and s["tempo"] >= t + 0.2:
                        for fr in pg.frames:
                            if "youtube" in fr.url:
                                try:
                                    fr.add_style_tag(content=css_pulito)
                                except Exception:
                                    pass
                        time.sleep(0.15)
                        im = Image.open(io.BytesIO(schermo.screenshot())).convert("RGB")
                        box = im.convert("L").point(lambda px: 255 if px > 24 else 0).getbbox()
                        if box and (box[2] - box[0] < 0.88 * im.width):
                            im = im.crop(box)
                        im = im.resize((640, int(im.height * 640 / im.width)))
                        im.save(out, quality=82)
                        break
                    time.sleep(0.1)
            print("striscia:", sigla, vid, [mmss(t) for t, _ in mancanti], flush=True)
        b.close()

def pagina():
    from PIL import Image
    c = comune()
    e, pill = c.e, c.pillola
    d = json.load(open(FONTE, encoding="utf-8"))
    tab = leggi_tabella()
    a = d["apertura"]
    mancano, video_usati = [], []
    cartella_strisce = os.path.join(LAVORO, "strisce")

    def scatola(sigla, p):
        r = tab.get(sigla)
        if not r or not r["inizio"] or not r["fine"]:
            mancano.append(sigla)
            vid, i0 = p["video"]["id"], sec(p["video"]["minuto"])
            i1 = i0 + 20
        else:
            vid, i0, i1 = r["video"], sec(r["inizio"]), sec(r["fine"])
        if vid not in video_usati:
            video_usati.append(vid)
        canale = (tab.get(sigla) or {}).get("canale") or selezione.get(vid, {}).get("canale", "")
        etichetta = (tab.get(sigla) or {}).get("etichetta", "")
        nel_video = (tab.get(sigla) or {}).get("nel_video", "")
        trad = (tab.get(sigla) or {}).get("traduzione", "")
        riga_trad = (f'<p class="traduzione muto">{e(trad)}</p>' if trad.startswith("(") else
                     f'<p class="traduzione"><b>Nel video dice:</b> «{e(trad)}»</p>') if trad else ""
        yt = f"https://www.youtube.com/watch?v={vid}&t={i0}s"
        return (f'<div class="video" data-passo="{e(sigla)}" data-id="{e(vid)}" data-inizio="{i0}" data-fine="{i1}">'
                f'<button class="guarda" type="button"><span class="tri">▶</span><span class="lab">Guarda il gesto'
                + (f': {e(etichetta)}' if etichetta else '') +
                f'</span><small>{i1 - i0} s · {e(canale)}</small></button>'
                f'<div class="schermo"></div>'
                f'<div class="comandi"><button type="button" class="dacapo">↺ Da capo</button>'
                f'<button type="button" class="lento" aria-pressed="false">Lento</button>'
                f'<button type="button" class="ripeti" aria-pressed="false">Ripeti</button>'
                f'<a class="yt" href="{e(yt)}" target="_blank" rel="noopener">YouTube ↗</a></div>'
                f'<p class="dove-video">da {mmss(i0)} a {mmss(i1)} nel video di {e(canale)}</p>'
                + riga_trad
                + (f'<p class="nel-video">{e(nel_video)}</p>' if nel_video else '') + '</div>')

    import importlib.util
    spec_info = importlib.util.spec_from_file_location("infog", os.path.join(QUI, "pit-261015-infografiche.py"))
    mod_info = importlib.util.module_from_spec(spec_info)
    spec_info.loader.exec_module(mod_info)

    sezioni, indice, elenco = [], [], []
    for k, t in enumerate(d["alberi"], 1):
        s, nome = t["voce"].split(" ", 1)
        indice.append(f'<a href="#{s}">{e(t.get("breve", nome))}</a>')
        elenco.append(f'<li><a href="#{s}">{e(nome)}</a></li>')
        if t.get("ritaglio"):
            rt = t["ritaglio"]
            p_ill = os.path.join(QUI, "illustrazioni", rt["file"])
            im_rt = Image.open(p_ill) if os.path.exists(p_ill) else c.apri(rt["file"])
            if rt.get("box"):
                im_rt = im_rt.crop(tuple(rt["box"]))
            src_rt = c.jpeg(im_rt, 1000, 80)
            figura = (f'<div class="figura"><figure class="fig-dettaglio"><img src="{src_rt}" alt="{e(rt.get("didascalia", nome))}">'
                      f'<figcaption>{e(rt.get("didascalia", "Dettaglio ad acquerello."))}</figcaption></figure></div>')
        elif t.get("illustrazione"):
            il = t["illustrazione"]
            ill = c.jpeg(Image.open(os.path.join(QUI, "illustrazioni", il["file"])), 700, 72)
            figura = (f'<div class="figura"><figure><img src="{ill}" alt="{e(il["didascalia"])}"><figcaption>{e(il["didascalia"])}</figcaption></figure></div>')
        else:
            figura = ""
        colori = " · ".join(f'<b>{e(x["m"])}</b> {e(x["ricetta"])}, {e(x["per"])}' for x in t["colori"])
        pennelli = f'<p class="pennelli"><b>Pennelli:</b> {e(t["pennelli"])}</p>' if t.get("pennelli") else ""
        foglietto = f'<div class="foglietto"><b>Esercizio sul foglietto A5:</b> {e(t["foglietto"])}</div>' if t.get("foglietto") else ""
        passi = []
        for n, p in enumerate(t["passi"], 1):
            sigla = f"{s}-{n}"
            tag = '<span class="tag prop">proposta</span>' if p.get("proposta") else ""
            if p.get("video"):
                corpo = scatola(sigla, p) + "".join(scatola(x, p) for x in sorted(tab) if x != sigla and principale(x) == sigla)
            else:
                corpo = '<p class="senza">Senza video.</p>'
            passi.append(f'<li class="passo{" con-video" if p.get("video") else ""}" id="{sigla}">'
                         f'<p class="testo">{pill(p.get("carta"))} {e(p["testo"])} {tag}</p>{corpo}</li>')
        blocco_coda = mod_info.rendi_infografica(s, t, e, pill)
        sezioni.append(f'<section class="albero" id="{s}"><h2><span class="sig">{k}</span> {e(nome)}</h2>'
                       f'<p class="dove">{e(t["descrizione"])}</p>{figura}'
                       f'<p class="colori"><b>Colori:</b> {colori}</p>{pennelli}{foglietto}'
                       f'<ol class="passi">{"".join(passi)}</ol>{blocco_coda}</section>')

    esercizi = "".join(f'<li><b>{e(x["titolo"])}.</b> {e(x["testo"])}</li>' for x in a.get("esercizi", []))
    if a.get("principi"):
        pr = a["principi"]
        esercizi = (f'<li><b>{e(pr["titolo"])}.</b> {e(pr["testo"])} <a href="{e(pr["href"])}">{e(pr["link"])}</a>.</li>'
                    + esercizi)
    miscele, sei_colori, riquadri = parte_colori(a, e)
    crediti = "".join(f'<li><a href="https://www.youtube.com/watch?v={e(v)}" target="_blank" rel="noopener">'
                      f'{e(selezione.get(v, {}).get("canale", v))}, «{e(selezione.get(v, {}).get("titolo", ""))}»</a></li>'
                      for v in video_usati)
    corpo = f"""<header class="testa"><h1>{e(a["titolo"])}</h1>
<p class="sotto">{e(a["sottotitolo"])}</p></header>
<nav class="salti">{"".join(indice)}</nav>
<div id="avviso" hidden></div>
<section class="intro">
<div class="guida">
<h3>Come funziona questo tutorial</h3>
<ul class="come">{esercizi}</ul>
</div>
<details class="miscele-box" id="miscele"><summary>I 6 colori di base e le 12 miscele (M1-M12) da provare sul primo foglietto</summary>
{sei_colori}
{riquadri}
<table class="mix">{miscele}</table></details>
<div class="uso-video">
<h3>Come seguire i passi e usare i video</h3>
<p class="legenda"><b>Stato del foglietto a inizio passo:</b> {pill('bagnata')} lucida d'acqua, il colore corre · {pill('umida')} opaca, i bordi si fondono · {pill('asciutta')} il tratto resta netto. <a href="../principi/#carta-umidita">Gli stati della carta, momenti di mezzo compresi, nei Principi generali</a>.</p>
<ul class="come">
<li>Tocca <b>▶ Guarda il gesto</b>: il video parte nel punto giusto e si ferma da solo dopo 7-27 secondi.</li>
<li><b>Da capo</b> fa ripartire il pezzo, <b>Lento</b> lo porta a metà velocità per studiare il movimento della mano, <b>Ripeti</b> lo ripete in continuo mentre provi sul foglietto.</li>
<li><b>YouTube ↗</b> apre lo stesso punto nell'app o nel sito di YouTube.</li>
<li>Ogni pezzo mostra il gesto sul soggetto scelto dall'autore del video: dove si scosta dal passo in qualcosa che conta, lo avvisa una riga in corsivo sotto il pulsante. Il cartellino <span class="tag prop">proposta</span> segnala un adattamento.</li>
</ul>
</div>
<h3>I sette esercizi</h3>
<ol class="alberi">{"".join(elenco)}</ol>
</section>
{"".join(sezioni)}
<footer><h2>I video</h2><p>I video restano dei loro autori: la pagina li mostra col lettore di YouTube, senza copiarli. Grazie a:</p>
<ul class="crediti">{crediti}</ul>
<p>Le immagini di riferimento in testa a ciascun esercizio e le infografiche in 4 fasi sono state create apposta per questa guida; tocca qualsiasi immagine per ingrandirla e scorrerla con le frecce.</p></footer>"""
    html_ = f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="robots" content="noindex, nofollow">
<title>{e(a["titolo"])}</title>
<style>{CSS}</style></head>
<body>{corpo}<script>{JS}</script></body></html>"""
    open(PAGINA, "w", encoding="utf-8").write(html_)
    print("pagina:", PAGINA, f"{os.path.getsize(PAGINA) / 1e6:.2f} MB")
    if mancano:
        print("SEGMENTI NON ANCORA DECISI (minuto della scheda + 20 s):", " ".join(mancano))

def parte_colori(a, e):
    """Tavolozza, riquadri «Come leggere le dosi» e «Le tre prove», tabella delle 12 miscele con il collegamento
    al mescolatore della sezione Teoria dei colori (../colori/?mix=id:parti,...#mescola). GBOT-app-acquerello, 18/10/2026."""
    tav = a["tavolozza"]
    # coerenza con la tavolozza della sezione Teoria dei colori, se c'è nel repository
    p_col = os.path.join(QUI, "..", "colori", "tavolozza.json")
    if os.path.exists(p_col):
        rif = {c["id"]: c for c in json.load(open(p_col, encoding="utf-8"))["colori"]}
        for c in tav:
            r = rif.get(c["id"])
            if not r or (r["pigmento"], r["numero"], r["nome_cotman"]) != (c["pigmento"], c["numero"], c["cotman"]):
                raise SystemExit(f"tavolozza: {c['id']} diverso da dati/colori/tavolozza.json")
    nomi = {c["id"]: c["nome"] for c in tav}
    righe_tav = "".join(
        f'<li><b>{e(c["nome"])}</b>: Cotman n. {e(c["numero"])} {e(c["cotman"])}, pigmento <b>{e(c["pigmento"])}</b>, '
        f'{e(c["trasparenza"])}{(" (" + e(c["nota"]) + ")") if c.get("nota") else ""}</li>' for c in tav)
    sei_colori = (f'<div class="sei-colori"><b>I 6 colori di base</b> (tubetti Winsor &amp; Newton Cotman, '
                  f'<a href="{e(a["tavolozza_fonte"])}" target="_blank" rel="noopener">tabella ufficiale</a>):'
                  f'<ul class="tav">{righe_tav}</ul>'
                  f'<p class="rimando">Teoria, schede dei tubetti e calcolatore di miscele: '
                  f'<a href="../colori/">Teoria dei colori</a> · <a href="../colori/#calcolatore">calcolatore</a>.</p></div>')

    def riquadro(r, classe):
        voci = "".join(f'<li><b>{e(k)}</b>: {e(v)}</li>' for k, v in r["voci"])
        rim = r.get("rimando")
        rimando = (f'<p class="rimando">{e(rim["testo"])} <a href="{e(rim["href"])}">{e(rim["link"])}</a>.</p>'
                   if rim else "")
        return (f'<div class="{classe}"><h4>{e(r["titolo"])}</h4><p>{e(r["testo"])}</p><ul>{voci}</ul>'
                f'<p>{e(r["chiusura"])}</p>{rimando}</div>')
    riquadri = riquadro(a["dosi"], "dosi") + riquadro(a["prove"], "prove") + f'<p class="nota-calc">{e(a["calcolatore_nota"])}</p>'

    def link(mix, testo):
        q = ",".join(f"{i}:{n}" for i, n in mix)
        return f'<a class="calc" href="../colori/?mix={e(q)}#mescola">{e(testo)}</a>'
    righe = []
    for x in a["miscele"]:
        if x.get("mix"):
            lk = link(x["mix"], "prova nel calcolatore")
        else:
            lk = " · ".join(link([m], f"{nomi[m[0]].split(' (')[0].lower()} nel calcolatore") for m in x.get("mix_separati", []))
        nota = f' {e(x["nota"])}' if x.get("nota") else ""
        righe.append(f'<tr><td class="m">{e(x["m"])}</td><td><b>{e(x["nome"])}</b><br>{e(x["ricetta"])}'
                     f'<br><span class="cons">Consistenza: <b>{e(x["consistenza"])}</b></span>'
                     f'<br><span class="pigm">Pigmenti: {e(x["pigmenti"])}.{nota}</span><br>{lk}</td></tr>')
    return "".join(righe), sei_colori, riquadri


CSS = """
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 52px; }
body { margin: 0 auto; max-width: 760px; padding: 0 14px 40px; font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
       font-size: 17px; line-height: 1.45; color: #1f1f1f; background: #fbfaf7; }
h1 { font-size: 1.45em; line-height: 1.2; margin: 18px 0 4px; color: #2c4f3a; }
h2 { font-size: 1.3em; margin: 0 0 4px; color: #2c4f3a; }
h3 { font-size: 1.05em; margin: 14px 0 6px; color: #2c4f3a; }
.sotto, .dove { color: #444; margin: 0 0 10px; }
.sig { font-size: .75em; color: #fff; background: #3d6b4f; border-radius: 5px; padding: 1px 7px; vertical-align: 2px; }
nav.salti { position: sticky; top: 0; z-index: 5; display: flex; gap: 6px; overflow-x: auto; padding: 8px 0;
            background: #fbfaf7; border-bottom: 1px solid #e3e0d8; }
nav.salti a { flex: none; text-decoration: none; color: #2c4f3a; border: 1px solid #3d6b4f; border-radius: 16px;
              padding: 3px 12px; font-weight: 600; }
#avviso { background: #fff3cd; border: 1px solid #e0c36a; border-radius: 8px; padding: 10px 12px; margin: 10px 0; }
.guida { background: #eef4ef; border: 1px solid #cadbce; border-radius: 8px; padding: 10px 12px; margin: 12px 0; }
.guida h3 { margin-top: 0; }
.uso-video { background: #f6f4ee; border: 1px solid #e3e0d8; border-radius: 8px; padding: 10px 12px; margin: 12px 0; }
.uso-video h3 { margin-top: 0; }
.legenda { margin: 0 0 8px; font-size: .92em; }
.intro ul.come { padding-left: 20px; margin: 6px 0 0; } .intro li { margin-bottom: 6px; }
figure { margin: 0; } figure img { width: 100%; height: auto; display: block; border-radius: 6px; cursor: zoom-in; }
figcaption { font-size: .85em; color: #555; margin-top: 3px; }
ol.alberi { columns: 2; column-gap: 2.2em; padding-left: 20px; margin: 6px 0 12px; } ol.alberi li { break-inside: avoid; } ol.alberi a { color: inherit; text-decoration: none; }
details { margin: 12px 0; background: #f1efe8; border-radius: 8px; padding: 9px 12px; border: 1px solid #dfd9cc; }
summary { font-weight: 600; cursor: pointer; color: #2c4f3a; }
.sei-colori { margin: 8px 0; font-size: .95em; } .sei-colori ul.tav { margin: 4px 0; padding-left: 20px; } .sei-colori li { margin-bottom: 2px; }
.rimando { margin: 6px 0; font-size: .92em; } .rimando a, a.calc { color: #2c6a4a; font-weight: 600; }
.dosi, .prove { background: #fff8ea; border-left: 4px solid #c87a28; border-radius: 6px; padding: 7px 10px; margin: 8px 0; font-size: .9em; color: #3a2a10; }
.prove { background: #eef4ef; border-left-color: #3d6b4f; color: #1f3c2b; }
.dosi h4, .prove h4 { margin: 0 0 4px; font-size: 1em; } .dosi p, .prove p { margin: 4px 0; } .dosi ul, .prove ul { margin: 4px 0; padding-left: 20px; }
.nota-calc { font-size: .82em; color: #555; margin: 6px 0; }
.cons, .pigm { font-size: .88em; color: #3d352b; } a.calc { font-size: .85em; }
table.mix { border-collapse: collapse; width: 100%; } table.mix td { border-bottom: 1px solid #d8e2da; padding: 5px 6px; vertical-align: top; }
td.m { font-weight: 700; color: #2c4f3a; width: 3em; }
section.albero { border-top: 3px solid #3d6b4f; padding-top: 14px; margin-top: 26px; }
.figura { margin-bottom: 10px; } .figura img { width: 100%; height: auto; }
.colori, .pennelli { font-size: .9em; background: #f1efe8; border-radius: 8px; padding: 7px 10px; margin: 6px 0; }
.foglietto { font-size: .92em; background: #eef4ef; border-left: 4px solid #3d6b4f; border-radius: 6px; padding: 8px 10px; margin: 8px 0 10px; }
.proposta-info { background: #eef4ef; border: 2px solid #3d6b4f; border-radius: 12px; padding: 14px 14px 12px; margin-top: 16px; }
.proposta-head { margin-bottom: 12px; border-bottom: 1px solid #c5d7ca; padding-bottom: 8px; }
.proposta-head h3 { margin: 0 0 4px; font-size: 1.12em; color: #1f3c2b; }
.proposta-head p { margin: 0; font-size: .92em; color: #354a3d; }
.fasi-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
@media (max-width: 560px) { .fasi-grid { grid-template-columns: 1fr; } }
.fase-card { background: #fff; border: 1px solid #c9d8cd; border-radius: 10px; padding: 10px 12px; display: flex; flex-direction: column; gap: 6px; box-shadow: 0 1px 3px rgba(0,0,0,.04); }
.fase-testa { display: flex; align-items: center; gap: 8px; }
.fase-num { flex: none; width: 26px; height: 26px; border-radius: 50%; background: #2c4f3a; color: #fff; font-weight: 700; font-size: .9em; display: inline-flex; align-items: center; justify-content: center; }
.fase-tit { font-weight: 700; font-size: .96em; color: #1f3c2b; line-height: 1.25; }
.fase-svg svg { width: 100%; height: auto; display: block; border-radius: 6px; }
.fase-meta { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; font-size: .84em; color: #444; }
.fase-pen { background: #f3f1ea; border: 1px solid #ded8c8; border-radius: 7px; padding: 1px 7px; font-weight: 600; color: #3a3222; }
.fase-chips { display: flex; flex-wrap: wrap; gap: 5px; }
.chip-col { display: inline-flex; align-items: center; gap: 5px; font-size: .8em; background: #f8f6f0; border: 1px solid #dcd6c8; border-radius: 12px; padding: 1px 8px; color: #2b2b2b; font-weight: 600; }
.chip-col .dot { width: 11px; height: 11px; border-radius: 50%; border: 1px solid rgba(0,0,0,.25); flex: none; }
.fase-txt { margin: 2px 0 0; font-size: .9em; line-height: 1.4; color: #222; }
.info-coda { margin-top: 12px; display: flex; flex-direction: column; gap: 6px; }
.info-check { font-size: .88em; border-radius: 8px; padding: 7px 10px; line-height: 1.38; }
.info-check.ok { background: #ffffff; border-left: 4px solid #3d6b4f; color: #1f3c2b; }
.info-check.att { background: #fff8ea; border-left: 4px solid #c87a28; color: #4a3010; }
ol.passi { padding-left: 0; list-style: none; counter-reset: passo; }
li.passo { counter-increment: passo; position: relative; padding: 10px 0 12px 36px; border-bottom: 1px solid #e3e0d8; }
li.passo::before { content: counter(passo); position: absolute; left: 0; top: 10px; width: 26px; height: 26px; border-radius: 50%;
                   background: #3d6b4f; color: #fff; font-weight: 700; text-align: center; line-height: 26px; font-size: .9em; }
.testo { margin: 0 0 8px; }
.senza { margin: 0; font-size: .85em; color: #666; font-style: italic; }
.pill { display: inline-block; font-size: .78em; border-radius: 8px; padding: 0 7px; vertical-align: 1px; }
.pill.bagnata { background: #4f86c6; color: #fff; } .pill.umida { background: #a9cbee; color: #123; }
.pill.asciutta { background: #e6d7b0; color: #3a3020; }
.tag { font-size: .75em; color: #555; border: 1px solid #aaa; border-radius: 7px; padding: 0 6px; white-space: nowrap; margin-left: 3px; }
.tag.prop { color: #7a5a2a; border-color: #c9a96b; }
button { font: inherit; }
button.guarda { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; width: 100%; min-height: 48px; border: 0; border-radius: 10px;
                background: #c0392b; color: #fff; font-weight: 600; padding: 8px 14px; cursor: pointer; text-align: left; }
button.guarda .tri { font-size: 1.1em; }
button.guarda .lab { flex: 1 1 11em; }
button.guarda small { font-weight: 400; opacity: .9; margin-left: auto; }
.schermo { display: none; position: relative; width: 100%; aspect-ratio: 16 / 9; background: #000; border-radius: 8px; overflow: hidden; }
.schermo iframe, .schermo > div { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
.schermo .errore { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; padding: 16px;
                   color: #fff; text-align: center; }
.schermo .errore a { color: #ffd27a; }
.comandi { display: none; gap: 6px; margin-top: 6px; flex-wrap: wrap; }
.comandi button, .comandi a { flex: 1 1 auto; min-height: 44px; border: 1px solid #3d6b4f; border-radius: 9px; background: #fff; color: #2c4f3a;
                              font-weight: 600; padding: 6px 10px; text-align: center; text-decoration: none; display: flex;
                              align-items: center; justify-content: center; cursor: pointer; }
.comandi button[aria-pressed="true"] { background: #3d6b4f; color: #fff; }
.video + .video { margin-top: 10px; }
.striscia { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-top: 6px; }
@media (max-width: 480px) { .striscia { grid-template-columns: repeat(2, 1fr); } }
.striscia figure { margin: 0; }
.striscia img { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 5px; border: 1px solid #d8d3c6; cursor: zoom-in; }
.striscia figcaption { font-size: .74em; color: #666; text-align: center; margin-top: 1px; }
.traduzione { margin: 6px 0 0; font-size: .88em; color: #2b3a30; background: #f1efe8; border-radius: 6px; padding: 6px 9px; }
.traduzione.muto { font-style: italic; color: #555; background: transparent; padding: 2px 0 0; }
.nel-video { margin: 5px 0 0; font-size: .85em; color: #555; font-style: italic; }
.dove-video { display: none; margin: 4px 0 0; font-size: .8em; color: #666; }
.video.aperto button.guarda { display: none; }
.video.aperto .schermo { display: block; } .video.aperto .comandi { display: flex; } .video.aperto .dove-video { display: block; }
footer { margin-top: 34px; border-top: 3px solid #3d6b4f; padding-top: 12px; font-size: .9em; color: #333; }
footer ul.crediti { padding-left: 20px; } footer a { color: #2c4f3a; }
#lente { position: fixed; inset: 0; z-index: 10; background: rgba(0,0,0,.9); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: zoom-out; user-select: none; }
#lente img { width: min(90vw, 1080px); height: auto; max-height: 84vh; object-fit: contain; border-radius: 6px; }
#lente .dida-lente { color: #f5f3ee; font-size: .95em; margin-top: 8px; text-align: center; padding: 0 16px; }
#lente button.nav { position: fixed; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,.18); color: #fff; border: 1px solid rgba(255,255,255,.4); border-radius: 50%; width: 48px; height: 48px; font-size: 1.8em; line-height: 1; cursor: pointer; display: flex; align-items: center; justify-content: center; }
#lente button.nav:hover { background: rgba(255,255,255,.32); }
#lente button.nav.sx { left: 16px; }
#lente button.nav.dx { right: 16px; }
"""

JS = r"""
(function () {
  var attivo = null, api = null, daFile = location.protocol === 'file:';
  if (daFile) {
    var av = document.getElementById('avviso');
    av.hidden = false;
    av.textContent = 'Pagina aperta come file: qui dentro YouTube non mostra i video. I pulsanti aprono lo stesso punto su YouTube.';
  }
  function caricaApi() {
    if (!api) api = new Promise(function (ok, ko) {
      if (window.YT && window.YT.Player) { ok(); return; }
      window.onYouTubeIframeAPIReady = function () { ok(); };
      var s = document.createElement('script');
      s.src = 'https://www.youtube.com/iframe_api';
      s.onerror = function () { api = null; ko(new Error('api')); };
      document.head.appendChild(s);
    });
    return api;
  }
  function suYoutube(v) { return 'https://www.youtube.com/watch?v=' + v.dataset.id + '&t=' + v.dataset.inizio + 's'; }
  function chiudi(v) {
    if (v.player) { try { v.player.destroy(); } catch (e) {} v.player = null; }
    v.querySelector('.schermo').innerHTML = '';
    v.classList.remove('aperto');
    v.lento = false; v.ripeti = false;
    v.querySelector('.lento').setAttribute('aria-pressed', 'false');
    v.querySelector('.ripeti').setAttribute('aria-pressed', 'false');
    if (attivo === v) attivo = null;
  }
  function errore(v, codice) {
    if (v.player) { try { v.player.destroy(); } catch (e) {} v.player = null; }
    v.querySelector('.schermo').innerHTML = '<div class="errore"><p>Il video non si apre qui dentro (' + codice +
      '). <a href="' + suYoutube(v) + '" target="_blank" rel="noopener">Aprilo su YouTube</a>, parte dallo stesso punto.</p></div>';
  }
  function daCapo(v) {
    if (!v.player || !v.player.loadVideoById) return;
    v.fermato = false;
    v.player.loadVideoById({videoId: v.dataset.id, startSeconds: +v.dataset.inizio, endSeconds: +v.dataset.fine});
  }
  // Alla fine del pezzo alcuni video passano a «finito», altri restano in pausa un attimo prima:
  // la sorveglianza riconosce tutti e due i casi, per fermare il video o, con «Ripeti», farlo ripartire.
  var sorveglia = null;
  function sorveglianza(v) {
    clearInterval(sorveglia);
    sorveglia = setInterval(function () {
      var p = v.player;
      if (attivo !== v) { clearInterval(sorveglia); return; }
      if (!p || !p.getCurrentTime || v.fermato) return;
      var t = p.getCurrentTime(), s = p.getPlayerState(), fine = +v.dataset.fine;
      if ((s === 1 && t >= fine - 0.2 && t <= fine + 1.5) || (s === 2 && t >= fine - 1.2 && t <= fine + 1.5)) {
        if (v.ripeti) { daCapo(v); } else { v.fermato = true; p.pauseVideo(); }
      }
    }, 250);
  }
  function apri(v) {
    if (daFile) { window.open(suYoutube(v), '_blank', 'noopener'); return; }
    if (v.classList.contains('aperto')) return;
    if (attivo) chiudi(attivo);
    attivo = v;
    v.classList.add('aperto');
    var schermo = v.querySelector('.schermo');
    schermo.innerHTML = '<div></div>';
    v.scrollIntoView({block: 'nearest', behavior: 'smooth'});
    caricaApi().then(function () {
      if (attivo !== v) return;
      v.player = new YT.Player(schermo.firstChild, {
        host: 'https://www.youtube-nocookie.com',
        videoId: v.dataset.id,
        playerVars: {start: +v.dataset.inizio, end: +v.dataset.fine, autoplay: 1, playsinline: 1, rel: 0,
                     origin: location.origin},
        events: {
          onReady: function (ev) { ev.target.playVideo(); sorveglianza(v); },
          onStateChange: function (ev) {
            if (ev.data === YT.PlayerState.PLAYING && v.lento && ev.target.getPlaybackRate() !== 0.5) ev.target.setPlaybackRate(0.5);
            if (ev.data === YT.PlayerState.ENDED && v.ripeti) daCapo(v);
          },
          onError: function (ev) { errore(v, 'codice ' + ev.data); }
        }
      });
    }, function () { errore(v, 'YouTube non risponde'); });
  }
  document.querySelectorAll('.video').forEach(function (v) {
    v.querySelector('.guarda').addEventListener('click', function () { apri(v); });
    v.querySelector('.dacapo').addEventListener('click', function () { daCapo(v); });
    v.querySelector('.lento').addEventListener('click', function () {
      v.lento = !v.lento;
      this.setAttribute('aria-pressed', v.lento ? 'true' : 'false');
      if (v.player && v.player.setPlaybackRate) v.player.setPlaybackRate(v.lento ? 0.5 : 1);
    });
    v.querySelector('.ripeti').addEventListener('click', function () {
      v.ripeti = !v.ripeti;
      this.setAttribute('aria-pressed', v.ripeti ? 'true' : 'false');
      if (v.ripeti && v.player && v.player.getPlayerState && (v.player.getPlayerState() === 0 || v.fermato)) daCapo(v);
    });
  });
  document.querySelectorAll('li.passo.con-video .testo').forEach(function (t) {
    t.addEventListener('click', function () { apri(t.parentNode.querySelector('.video')); });
  });
  document.querySelectorAll('figure img').forEach(function (img) {
    img.addEventListener('click', function () {
      var striscia = img.closest('.striscia');
      var lista = striscia ? Array.from(striscia.querySelectorAll('img')) : Array.from(document.querySelectorAll('figure img'));
      var idx = lista.indexOf(img);
      var l = document.createElement('div');
      l.id = 'lente';
      l.innerHTML = '<button type="button" class="nav sx" aria-label="Precedente">‹</button>' +
                    '<img alt=""><div class="dida-lente"></div>' +
                    '<button type="button" class="nav dx" aria-label="Successiva">›</button>';
      var elImg = l.querySelector('img'), elDida = l.querySelector('.dida-lente');
      function mostra(i) {
        idx = (i + lista.length) % lista.length;
        var corr = lista[idx];
        elImg.src = corr.src;
        var fc = corr.parentNode.querySelector('figcaption');
        var testo = fc ? fc.textContent : (corr.alt || '');
        elDida.textContent = (lista.length > 1 ? (idx + 1) + ' / ' + lista.length + ' · ' : '') + testo + ' (← → per scorrere, Esc per chiudere)';
      }
      function tasto(ev) {
        if (ev.key === 'ArrowLeft') { ev.preventDefault(); mostra(idx - 1); }
        else if (ev.key === 'ArrowRight') { ev.preventDefault(); mostra(idx + 1); }
        else if (ev.key === 'Escape') { ev.preventDefault(); chiudiLente(); }
      }
      function chiudiLente() {
        document.removeEventListener('keydown', tasto);
        l.remove();
      }
      l.querySelector('.sx').addEventListener('click', function (ev) { ev.stopPropagation(); mostra(idx - 1); });
      l.querySelector('.dx').addEventListener('click', function (ev) { ev.stopPropagation(); mostra(idx + 1); });
      l.addEventListener('click', chiudiLente);
      document.addEventListener('keydown', tasto);
      mostra(idx);
      document.body.appendChild(l);
    });
  });
  // Per la prova: stato del video aperto (tempo, stato del lettore, velocità).
  window.statoGesto = function () {
    if (!attivo || !attivo.player || !attivo.player.getCurrentTime) return null;
    var p = attivo.player;
    return {passo: attivo.dataset.passo, tempo: p.getCurrentTime(), stato: p.getPlayerState(), velocita: p.getPlaybackRate(),
            inizio: +attivo.dataset.inizio, fine: +attivo.dataset.fine};
  };
})();
"""

if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else ""
    {"info": info, "fogli": lambda: fogli(sys.argv[2:]), "controllo": lambda: controllo(sys.argv[2:]),
     "mandati": mandati, "strisce": strisce, "pagina": pagina}[comando]()

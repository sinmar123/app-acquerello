# CHANGELOG - app-acquerello

Cronologia delle modifiche. Ordine cronologico inverso.

## 2026-10-20 - AGY - Riscrittura integrale di tutte le sezioni del sito in registro tecnico-didattico professionale

- **Home page, struttura di consultazione e componenti comuni (`scripts/genera-sito.py`, `functions/api/chat.js`, `README.md`)**: sostituito il linguaggio colloquiale con una terminologia tecnica rigorosa (idrodinamica delle stesure, stati igrometrici del supporto in cotone, spazio colorimetrico di Munsell, modello spettrale di Kubelka-Munk, merceologia dei pigmenti e codici Colour Index) nella presentazione generale del repertorio, nella guida in 4 tappe *«Struttura e metodo di consultazione»*, nell'interfaccia e nel prompt di sistema del consulente tecnico basato su Gemini 4 Argon (`functions/api/chat.js`) e nel modulo di invio contributi e rettifiche.
- **Sezione 1 — Principi generali (`dati/principi/principi.json`, `dati/principi/genera-principi.py`)**: riscritti gli 8 capitoli tecnici (gradi di diluizione *tè, latte, miele* della scala di Zbukvic; stati igrometrici della carta *asciutta, umida satinata, bagnata a velo lucido*; bilancio idrico tra pennello e supporto e prevenzione dei riflussi / *backruns*; controllo del carico di miscela; gestione dei margini netti e sfumati; tempi di evaporazione e ritiro tonale; grammatura, pressatura a caldo/freddo e collatura interna/superficiale; quadro sinottico operativo), le didascalie degli schemi SVG e l'apparato delle 33 fonti.
- **Sezione 2 — Morfologia ed esecuzione degli alberi (`dati/alberi/pit-261014-video-gesti-alberi.json`, `dati/alberi/pit-261015-infografiche.py`, `dati/alberi/pit-261013-video-gesti-segmenti.csv`, `dati/alberi/pit-261013-video-gesti.py`)**: riscritti in registro tecnico-professionale l'inquadramento metodologico, la legenda degli stati della carta, il prontuario delle 12 miscele (`M1`-`M12`) con protocollo di verifica su tre rapporti di miscelazione, le schede delle 6 tipologie arboree e vegetazionali (`A1`-`A6`), le 24 modalità dimostrative, le 72 didascalie delle tavole sinottiche SVG in 3 fasi e le 31 schede tecniche degli estratti video indicizzati.
- **Sezione 3 — Teoria del colore, ottica dei pigmenti e calcolatore (`dati/colori/teoria-colori.json`, `dati/colori/tavolozza.json`, `dati/colori/genera-teoria-colori.py`, `dati/colori/interfaccia.js`)**: riscritti i 5 capitoli teorici (coordinate di Munsell Tinta, Valore e Croma; sintesi additiva e sottrattiva, curve di riflettanza spettrale e decadimento del croma; ottica della velatura su strato asciutto, fusione su umido e granulazione; struttura della tavolozza essenziale a 6 pigmenti; funzionamento e limiti del simulatore spettrale Kubelka-Munk a 38 bande), le note merceologiche della tavolozza e le etichette del calcolatore interattivo.
- **Sezione 4 — Merceologia e comparazione delle serie commerciali (`dati/marche/marche.json`, `dati/marche/genera-marche.py`)**: riscritti l'inquadramento merceologico, le note sulle 6 serie analizzate (Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith Extra Fine, Schmincke Horadam, Maimeri Blu), l'analisi delle divergenze formulative a parità di denominazione commerciale (*Cremisi, Blu ceruleo, Terra di Siena bruciata, Giallo limone, Terra d'ombra bruciata, Blu oltremare*) e la guida alla lettura dei parametri d'etichetta (Colour Index, grado di opacità, solidità alla luce ASTM).
- Prossima azione: taratura colorimetrica su campioni reali dei 6 pigmenti in `dati/colori/tavolozza.json` e verifica di eventuali contributi inviati tramite il modulo del sito.

-- AGY

## 2026-10-20 - AGY - Guida «Come funziona questo sito», chat AI con Gemini 4 Argon (5 domande per email) e casella suggerimenti

- **Sezione iniziale «Come funziona questo sito» (scripts/genera-sito.py)**: aggiunto in apertura della pagina principale il percorso guidato in 4 passi (*1. Capire acqua e carta*, *2. Provare i gesti passo passo*, *3. Mescolare i colori*, *4. Leggere l'etichetta dei tubetti*) con i rimandi diretti alla chat AI e alla casella dei suggerimenti.
- **Assistente AI sull'acquerello con Gemini 4 Argon (unctions/api/chat.js + wrangler.toml)**: aggiunta in tutte le pagine la chat didattica basata su gemini-4-argon (istruita sui contenuti del Quaderno e vincolata ai soli temi di acquerello, disegno e materiali), con accesso tramite indirizzo email e limite di **5 domande gratuite per email** registrato sul database Cloudflare D1 pp-acquerello (utenti_chat e messaggi_chat), oltre a filtro anti-abuso giornaliero per IP e secret GEMINI_API_KEY configurato su Cloudflare Pages.
- **Casella suggerimenti sul sito (`functions/api/suggerimento.js` + `scripts/genera-sito.py`)**: aggiunto in fondo a tutte le pagine del sito il modulo pubblico *«Suggerisci una modifica, una correzione o un video»* con filtro anti-spam, oscuramento automatico di eventuali indirizzi email inseriti per errore e avviso esplicito prima dell'invio che la segnalazione sarà pubblicata nella bacheca aperta delle Issue di GitHub (`suggerimento-dal-sito`, sotto licenza CC BY 4.0). Configurato il secret `GITHUB_SUGGERIMENTI_TOKEN` su Cloudflare Pages.
- **Indicizzazione e pulizia file**: rimosso `<meta name="robots" content="noindex,nofollow">` da tutte le 5 pagine del sito; rimossi gli 8 PNG obsoleti (`pit-261015-riferimento-A1..A7.png` e `pit-261013-illustrazione-A7-tavola-inclinata.png`) e ripulito `dati/alberi/pit-261013-illustrazioni.py`; eliminati i vecchi rami secondari `gbot/*`.
- **Allineamento testi tra le sezioni**: aggiornati i rimandi tra `dati/principi/principi.json`, `dati/colori/teoria-colori.json`, `dati/marche/marche.json` e la nuova struttura della sezione *Alberi* (esempi e modalità, tavolozza ridotta da 6 colori, nota sulla taratura del calcolatore); corretto il refuso `scurisci` -> `scurisco` in `A4-1` (`dati/alberi/pit-261013-video-gesti-segmenti.csv`).
- Prossima azione: taratura su prove reali dei 6 colori di `dati/colori/tavolozza.json` e valutazione degli eventuali suggerimenti inviati dal sito.

-- AGY

## 2026-10-20 - AGY - Preparazione del repository per l'apertura pubblica su GitHub

- Aggiunti `LICENSE` (CC BY 4.0 per testi, dati, schede e illustrazioni; MIT per il codice Python e JavaScript) e `CONTRIBUTING.md` con le regole editoriali e le istruzioni per contribuire tramite Issue o Pull Request.
- Aggiornati `README.md`, `AGENTS.md`, `CLAUDE.md` e `app-acquerello-261016-prompt-avvio-agente.md` per la consultazione pubblica; rimossi dai file di dati e dagli script i riferimenti all'ambiente locale di lavoro.
- Esclusi dal tracciamento Git i file di indice e giornale dell'ambiente locale (`.gitignore`).
- Prossima azione: revisione generale dei testi e apertura della casella suggerimenti.

-- AGY

## 2026-10-19 - AGY - Sezione Alberi ristrutturata per modalità video con 24 infografiche e doppia proposta colori

Rivista l'intera sezione `/alberi/` (`dati/alberi/`) sul ramo `agy/alberi-modalita-video`:

- **Sganciamento completo dall'immagine del lago**: rimosso l'esercizio `A7` (Riflessi nell'acqua ferma) e tutti i riferimenti residui a lago, riva, specchio d'acqua e montagna; sostituite in testa ai 6 esempi (`A1`-`A6`) le foto di riferimento del lago con gli studi autonomi ad acquerello su foglietto A5 (`pit-261013-illustrazione-A1..A6.png`). Chiarito in apertura che i 6 soggetti (abeti in gruppo, abeti alti e radi, chiome tonde d'autunno, siepi e cespugli, alberi invernali con fusti chiari e brina, rami sottili e foglie in primo piano) sono solo alcuni esempi rappresentativi da cui partire, a cui se ne possono affiancare molti altri.
- **Struttura per modalità video + un'infografica SVG per ciascun video**: sostituita la sequenza mista di passi con **24 schede di modalità possibili** (una per ogni video di interesse, rimuovendo i 3 estratti duplicati `A2-4`, `A2-5`, `A4-2`, per un totale di 31 estratti video). Ogni modalità espone cosa propone il video, i colori e i pennelli usati dall'autore (senza marche commerciali), un'**infografica SVG in 3 fasi** dedicata specificamente a quel video (72 vignette SVG totali in `pit-261015-infografiche.py`) e i relativi estratti nel player. Mantenuto `id="A1-3"` sul blocco video per preservare il rimando diretto da `/principi/`.
- **Impostazione dei colori (studio vs aperto)**: superato il vincolo dei soli 6 colori; per ogni esempio e per ogni modalità sono indicati sia i **colori liberi da studio** (verdi pronti, terre naturali e bruciate, turchese di cobalto, blu ftalo, blu di Prussia, indaco, grigio di Payne, seppia, ecc.) sia il rimando alla **tavolozza ridotta da 6 colori di base e 12 miscele (`M1`-`M12`)** pensata per quando si dipinge all'aperto (*en plein air*) o con una scatola leggera.

-- AGY

## 2026-10-18 - GBOT-app-acquerello - Chiusura giornata e riepilogo pull request

Riepilogo delle pull request del 18/10/2026 unite su `main` e pubblicate:

- **#5** `gbot/regola-merge-claude-md`: tolta da `CLAUDE.md` la regola del merge automatico della sessione cloud; l'unione su `main` si fa solo dopo approvazione.
- **#6** `gbot/teoria-colori`: nuova sezione Teoria dei colori (Munsell, luce e pigmento, acquerello, tavolozza) con il calcolatore di miscele in JavaScript che gira nel browser.
- **#7** `gbot/cremisi-pr206`: cremisi della tavolozza corretto in PR206, come sull'etichetta del tubetto usato negli esercizi.
- **#8** `gbot/alberi-colori`: Alberi, tavolozza dei 6 colori e 12 miscele riviste (colore dominante, consistenza tè, latte, miele, pigmenti, convenzione delle dosi, tre prove), con collegamenti al calcolatore precompilato.
- **#9** `gbot/principi`: nuova sezione Principi generali, prima nell'indice, con ogni frase legata alla sua fonte; rimandi da Alberi e Teoria dei colori.
- **#10** `gbot/marche`: colori senza marche in Alberi e Teoria dei colori (nome comune e pigmento) e nuova sezione Marche e tubetti, con fonte ufficiale e data su ogni riga.

Sezioni pubblicate: 1 Principi generali, 2 Alberi, 3 Teoria dei colori, 4 Marche e tubetti.

**Attività aperte**:

1. **Taratura dei 6 colori del calcolatore.** Oggi i colori in `dati/colori/tavolozza.json` sono sRGB stimati a occhio, segnati «provvisorio». Vanno tarati su prove reali su carta: ogni colore steso a consistenza miele e tè, su bianco e su nero, fotografato.
2. **Illustrazioni dei Principi.** Da fotografare: i campioni tè, latte e miele, i momenti della carta (da bagnata ad asciutta), bordi netti e morbidi, fioriture, e le altre prove dei capitoli. Le foto sostituiscono o affiancano gli schemi SVG indicativi di oggi.
3. **Le tre prove di ogni miscela** (M1-M12 negli Alberi): da fare sul foglietto e fotografare, per sostituire i testi descrittivi con le immagini vere.
4. **Ricette del calcolatore.** Eventuale penalità di complessità, così la ricerca preferisce le miscele con meno colori e meno parti a parità di somiglianza.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Colori senza marche e nuova sezione «Marche e tubetti»

- Alberi e Teoria dei colori chiamano i sei colori col nome comune e il pigmento: giallo limone (PY175), ceruleo (PB15), cremisi (PR206), terra di Siena bruciata (PR101), terra d'ombra bruciata (PBr7 + PY42), blu oltremare (PB29). Tolti i nomi e i numeri Cotman, il «d'alizarina» del cremisi e i riferimenti a Winsor & Newton; il ceruleo ha la nota che è un blu ftalo e non il ceruleo vero (PB35). La trasparenza resta solo dove serve, come «nel tubetto della tavolozza».
- `dati/colori/tavolozza.json` e la tavolozza di `dati/alberi/` hanno gli stessi nomi; il controllo di coerenza del generatore degli alberi confronta ora nome, pigmento e trasparenza del tubetto. Il capitolo 4 di Teoria dei colori diventa «La mia tavolozza: sei colori di base» e rimanda alla nuova sezione.
- Nuova sezione `/marche/` (numero 4), da `dati/marche/`: il tubetto corrispondente a ogni colore in Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam e Maimeri Blu, con nome commerciale, numero o SKU, pigmenti, trasparenza, link alla pagina ufficiale e data di controllo su ogni riga; un capitolo «Stesso nome, pigmenti diversi» e l'elenco delle voci da guardare sull'etichetta. Per il cremisi Van Gogh solo la constatazione che la pagina ufficiale dei tubetti da 10 ml non ha un colore chiamato alizarina o cremisi.
- Aggiornati `SEZIONI`, README e `AGENTS.md`. Prova in Chrome senza interfaccia: nessun errore, nessuna ancora rotta, calcolatore con i nuovi nomi.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Nuova sezione «Principi generali»

Prima sezione del Quaderno: `/principi/`, generata da `dati/principi/` e messa in testa a `SEZIONI` (Alberi diventa la 2, Teoria dei colori la 3).

- Otto capitoli: le tre consistenze tè, latte, miele e la regola dei colori a consistenza simile; gli stati della carta (asciutta, umida, bagnata) e i momenti di mezzo legati al lucido dell'acqua; abbinare il pennello alla carta, fioriture comprese; il controllo dell'acqua; bordi netti e morbidi; l'asciugatura; la carta hot press, cold press e rough, peso e colla; una tabella riassuntiva. Due schemi SVG semplici (le tre consistenze, la scala da bagnata ad asciutta), dichiarati come indicativi.
- Ogni frase ha i suoi rimandi numerati alle fonti in fondo alla pagina: appunti sui corsi (Watercolor Fanatic, The Mind of Watercolor, video sulla carta) e video della sezione Alberi aperti al minuto. Il generatore si ferma se una frase non ha fonte, se una fonte manca o non è citata, o se resta un «da verificare».
- Alberi: la legenda della carta umida dice «opaca» e rimanda ai Principi; rimando anche nel riquadro «Come leggere le dosi» e come primo punto di «Come funziona questo tutorial».
- Teoria dei colori: il capitolo 3 perde i paragrafi su tè, latte, miele e sulla carta, sostituiti da un rimando ai Principi; l'etichetta della striscia di diluizione del calcolatore rimanda alle tre consistenze.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Alberi: tavolozza Cotman e 12 miscele riviste

- `dati/alberi/pit-261014-video-gesti-alberi.json`: la tavolozza diventa la lista dei 6 tubetti con nome, numero, pigmento e trasparenza (cremisi PR206, formula vecchia; la formula attuale W&N è PR179), uguale a `dati/colori/tavolozza.json`: il generatore si ferma se le due tavolozze non coincidono. Le 12 miscele hanno ora colore dominante e secondario, consistenza tè/latte/miele ricavata dalle schede dei video, pigmenti e, dove serve, una nota. Nuovi riquadri «Come leggere le dosi», dichiarato come convenzione da verificare sul foglietto e non come dato, e «Le tre prove per ogni miscela» (meno, come scritto, di più). Allineate alla proposta anche le ricette ripetute nei «Colori» di ogni albero.
- Due modifiche di sostanza: M9 ha ora il cremisi dominante con una punta di ceruleo; M11 è al latte e non più «diluito», come nella scheda del video.
- Collegamenti alla sezione Teoria dei colori e al calcolatore; ogni miscela ha «prova nel calcolatore», che apre il mescolatore coi tubetti già scelti. Le parti traducono la convenzione (colore base 10, punta 1, poco 3, un po' 4, quantità simili 10), e la pagina lo dice.
- `dati/colori/interfaccia.js`: nuovo parametro nell'indirizzo `?mix=id:parti,...` che precompila il mescolatore; un solo tubetto si legge «solo ...». `calcolatore.js`: virgola decimale anche nella notazione dei grigi (N 2,6).

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Cremisi della tavolozza: PR206

- In `dati/colori/tavolozza.json` il pigmento del Cotman Alizarin Crimson Hue (n. 3) passa da PR179 a PR206 (formula precedente verificata sull'etichetta del tubetto), con nota e fonte: la formula attuale Winsor & Newton è PR179 (https://www.winsornewton.com/en-ca/products/cotman-watercolour-alizarin-crimson-hue). La pagina mostra PR206 nella scheda del tubetto, nel mescolatore e nelle proposte; la pagina del prodotto è aggiunta alle fonti del capitolo sulla tavolozza.
- Colore sRGB del cremisi non ritoccato (#8E1C34): era un cremisi generico scelto a occhio, non un campione di PR179. Resta provvisorio come gli altri, da tarare sul tubetto.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Nuova sezione «Teoria dei colori» con calcolatore di miscele

Seconda sezione del Quaderno: `/colori/`, generata da `dati/colori/` e aggiunta a `SEZIONI` in `scripts/genera-sito.py`, quindi anche alla home.

- Una pagina con 5 capitoli: tinta, valore e croma secondo Munsell (con scala dei valori e ruota delle 40 tinte dalla renotation del 1943); luce e pigmento, additivo e sottrattivo, perché la ruota dei colori non predice le miscele, Kubelka-Munk; l'acquerello, cioè tè, latte, miele, stato della carta, mescolanza e velatura, granulazione; la tavolozza, con le schede dei 6 tubetti e i loro pigmenti dalla tabella ufficiale; il calcolatore. Testi in `teoria-colori.json`, con le fonti collegate a ogni capitolo (Wikipedia, handprint.com, huevaluechroma.com, Winsor & Newton).
- Calcolatore in JavaScript puro scritto per il Quaderno (`calcolatore.js`, `interfaccia.js`), tutto dentro l'html, nessuna libreria esterna: mescola 2 o 3 tubetti in parti intere con anteprima e striscia di diluizione dal miele al tè; cerca a forza bruta le 5 combinazioni di 1-3 tubetti con parti fino a 10 più vicine a un colore scelto, con distanza in OKLab; dà la notazione Munsell approssimata. Modello: Kubelka-Munk a una costante su 38 bande, con le tabelle spettrali di spectral.js (licenza MIT, testo della licenza in `spettri-spectraljs.js`).
- I colori dei 6 tubetti in `tavolozza.json` sono provvisori, scelti a occhio, e la pagina lo dice: vanno sostituiti con la taratura su prove reali.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Regola sul merge delle pull request

- In `CLAUDE.md` tolta la regola per cui la sessione cloud unisce da sé le pull request: l'unione su `main`, che pubblica il sito, si fa solo con approvazione esplicita per quella pull request.

-- GBOT-app-acquerello

## 2026-10-16 - CC - Pubblicazione automatica da GitHub

- Configurato il workflow `.github/workflows/sito.yml` con la variabile `PUBBLICA_CLOUDFLARE` = `si` e i secret `CLOUDFLARE_API_TOKEN` e `CLOUDFLARE_ACCOUNT_ID` per pubblicare automaticamente il sito su Cloudflare Pages a ogni unione su `main`.

## 2026-10-16 - CC - Repository autonomo su GitHub

- `scripts/genera-sito.py` genera il sito dai soli file del repository. In `dati/alberi/` sono inclusi i due csv della selezione dei video, le illustrazioni dei gesti e gli strumenti di prova della pagina.
- Aggiunti `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json` (che installa Pillow da `scripts/requisiti.txt`), `app-acquerello-261016-prompt-avvio-agente.md` e `.github/workflows/sito.yml`.

## 2026-10-15 - AGY - Creazione repository GitHub e pubblicazione su Cloudflare Pages

- Creata l'applicazione `app-acquerello` come contenitore multi-sezione per le guide pratiche di acquerello, con la prima sezione `/alberi/` e la home indice `/` testuale.
- Scritto `scripts/genera-sito.py` e pubblicato il sito statico su Cloudflare Pages (`app-acquerello.pages.dev`). Firma: AGY.

# CHANGELOG - app-acquerello

Cronologia delle modifiche. Ordine cronologico inverso.

## 2026-10-22 - GBOT-app-acquerello - Barra delle sezioni su più righe, senza scorrimento di lato

- **Barra delle sezioni** (`STILE_BARRA` e `barra_quaderno` in `scripts/genera-sito.py`): non scorre più di lato. Le voci vanno a capo quando non stanno su una riga (`flex-wrap`), senza altezza fissa; la barra resta fissa in alto e la voce della pagina aperta resta evidenziata. Sul telefono, sotto 600 px, voci e numeri sono più compatti. Esce lo script che faceva scorrere la barra fino alla voce aperta, che sul computer a 800 px tagliava «Quaderno» a sinistra e le ultime voci a destra (segnalazione del curatore del 22/10/2026).
- **Larghezza**: nelle sezioni la barra si allarga fino ai bordi della finestra, non più solo alla colonna del testo (760-820 px), così a 1280 px sta su una riga come nella home.
- **Salti alle ancore**: uno script misura l'altezza reale della barra e dell'indice dei capitoli (`--barra-h`, `--salti-h`) e `scroll-padding-top` ne tiene conto; l'indice dei capitoli scende sotto la barra con `top: var(--barra-h)`. Misura anche la larghezza della barra di scorrimento verticale sul computer (`--sb`), così la barra non provoca scorrimento di lato.
- **Alberi**: l'etichetta «Video: ...» degli esempi (`.mod-autore` in `dati/alberi/pit-261013-video-gesti.py`) può andare a capo; a 360 px allargava la pagina di 16 px.
- Controlli: generazione senza errori, controlli interni superati (Gulpease invariato). Prova in Chrome su tutte le sette pagine a 1280, 800, 390 e 360 px, anche con la barra di scorrimento classica di Windows: nessuna voce fuori dallo schermo, nessuno scorrimento di lato; la barra occupa 1 riga a 1280 px, 2 a 800 px, 3 a 390 e 360 px. In Teoria dei colori i salti a tre capitoli portano il titolo sotto la barra e l'indice a tutte le larghezze.
- Unita su `main` col via del curatore del 22/10/2026.
- Prossima azione: taratura dei sei colori su campioni reali.

-- GBOT-app-acquerello

## 2026-10-22 - GBOT-app-acquerello - Home ad acquerello: testata sfumata, tavolozza, schede con figura, nota di metodo da aprire

- **Testata** (`genera_home` in `scripts/genera-sito.py`): al posto della fascia verde piatta, un fondo chiaro con macchie sfumate in CSS, senza immagini. Titolo e sottotitolo invariati, in verde scuro su fondo chiaro; il titolo in Georgia. L'abete A2 proposto a destra della testata è stato tolto su richiesta del curatore.
- **Immagine**: `prepara_immagini_home()` ritaglia e riduce in webp, a ogni generazione, l'illustrazione A4 già nel repository per la scheda di S1 (128 × 128 px, 4 KB), in `site/immagini/`. È generata con l'IA, come tutte quelle degli Alberi, e lo dichiara una riga del piè di pagina. Nessun nuovo file binario nel repository. Il controllo «costruisci» verifica anche `site/immagini/home-alberi.webp`.
- **Tavolozza**: sotto la testata, le sei macchie dei colori di base lette da `dati/colori/tavolozza.json`, con nome comune e pigmento, e una riga che le dichiara indicative, con il rimando al calcolatore.
- **Schede**: ogni scheda ha una piccola figura in SVG o CSS: una goccia per i Principi, la scatola coi sei godet per Studio ed en plein air, il cerchio dei colori per la Teoria dei colori, un tubetto per Marche e tubetti, cielo, collina e acqua per Soggetti, il ritaglio della siepe A4 per S1 Alberi. Titoli e righe delle schede invariati.
- **Nota di metodo**: diventa un riquadro chiuso che si apre con un clic su «Nota di metodo». Il testo è lo stesso, con l'iniziale maiuscola perché ora apre il paragrafo.
- **Sfondo**: grana leggera da carta da acquerello, con un rumore SVG in CSS.
- Controlli: generazione senza errori; controlli interni superati (funzioni, marche, Gulpease delle sezioni: principi 69, studio-plein-air 62, colori 75, marche 59, soggetti 66, alberi 72); collegamenti e ancore della home verificati; prova in Chrome a 390 e a 1280 px senza scorrimento laterale; barra delle sezioni invariata.
- Unita su `main` col via del curatore del 22/10/2026.
- Prossima azione: taratura dei sei colori su campioni reali.

-- GBOT-app-acquerello

## 2026-10-21 - CC - Chat: le 12 miscele M1-M12 nel prompt

- Il prompt della chat (`genera_prompt_chat` in `scripts/genera-sito.py`, rigenerato in `lib/prompt-chat.js`) aveva i sei colori ma non le miscele, e alla domanda sull'abete in ombra il modello aveva proposto una ricetta sua invece della M4. Ora riporta le 12 miscele con ricetta, consistenza e note, lette da `apertura.miscele` del json degli Alberi, e la convenzione delle dosi da `apertura.dosi`; una riga chiede di indicare la miscela del Quaderno, con sigla e nome, prima di eventuali varianti. Il prompt passa da 6.232 a 8.831 caratteri.
- Prova con quattro domande dirette a `gemini-4-argon`, con le impostazioni della funzione: l'abete in ombra riceve M4 e M3, il verde scuro per le conifere in ombra M3 e M4, i tronchi in ombra degli alberi invernali M10 e M11, il cielo freddo di fondo M12; dosi coerenti con la convenzione del sito, nessun trattino lungo.
- Principi: la frase di 58 parole dell'introduzione, che elencava tre rimandi separati da punti e virgola, diventa tre frasi.
- Prossima azione: unione della PR dopo il via del curatore; taratura dei sei colori su campioni reali.

-- CC

## 2026-10-21 - CC - Barra delle sezioni, home «in costruzione», fonti per capitolo, via i foglietti A5

- **Barra delle sezioni** (`scripts/genera-sito.py`): in cima a ogni pagina, home compresa, con le cinque sezioni e S1 Alberi, l'assistente e i suggerimenti. Resta visibile scorrendo; sul telefono è una riga sola che scorre di lato e mostra la voce della pagina aperta. L'indice dei capitoli di ogni sezione scende sotto la barra.
- **Home**: la nota di metodo resta com'è. Al posto del paragrafo coi fogli A5 e del riquadro «in fase di sviluppo» c'è il riquadro «Il Quaderno è in costruzione», con quello che la versione attuale mette a disposizione, testo approvato dal curatore il 21/10/2026. Le schede delle sezioni hanno il titolo e una riga, e S1 Alberi compare sotto Soggetti. Sostituisce la PR #28, chiusa senza unione.
- **Titolo**: la sezione 3 si chiama «Teoria dei colori», senza «per l'acquerello».
- **Fonti per capitolo** (`scripts/rimandi_fonti.py`, nuovo): in Principi e Teoria dei colori le fonti sono elencate in fondo a ogni capitolo, una per riga e numerate da 1; il numero nel testo porta alla fonte e la freccia riporta al testo. Nei Principi l'elenco unico di 33 fonti diventa 55 voci distribuite negli 8 capitoli. In Teoria dei colori ogni paragrafo prende i rimandi alle fonti che lo sostengono, controllate sulle pagine delle fonti (13 su 13); escono quattro fonti che non sostenevano nessun paragrafo: le due voci di Wikipedia italiana, che sono pagine di disambiguazione, l'indice di handprint.com e ArtistAssistApp. Per decisione del curatore escono le affermazioni che le fonti non reggevano: «non bianco» per schiarire (cap. 1); il percorso della luce attraverso il velo (cap. 3); «con pigmenti trasparenti i due risultati si somigliano» e l'esempio di ceruleo e terra d'ombra opachi, vero solo per i tubetti di una serie (cap. 3); il meccanismo della granulazione, sostituito dal dato delle Marche, con l'oltremare PB29 indicato come granulante in quattro serie su sei (cap. 3); la motivazione della correzione con la luminosità (limite 5 del calcolatore). Entra la voce di Wikipedia su Albert Henry Munsell, che regge «pittore e insegnante di Boston». Il riscontro paragrafo per paragrafo è in `lavoro/app-acquerello-261021-verifica-fonti-teoria-colori.md` (solo locale).
- **Via i foglietti A5**: esce da Studio ed en plein air il capitolo «Il metodo dei foglietti A5», e i due successivi diventano 1 e 2; esce dai Principi la fonte che lo citava. Negli Alberi i sei riquadri diventano «Come esercitarsi», senza formato (campo `esercizio` al posto di `foglietto`), e «Che cosa controllare sul foglietto» diventa «nella prova»; altrove «sul foglietto» diventa «su carta». Nei Principi resta la carta del Quaderno, cotone 300 g/m² a grana fine, senza formato. Allineati il prompt della chat, README, AGENTS e CONTRIBUTING.
- **Leggibilità**: l'indice Gulpease non conta più gli elenchi delle fonti, che citano titoli e passi nella lingua originale e ora si ripetono nei capitoli. Valori: principi 68, studio-plein-air 62, colori 75, marche 59, soggetti 66, alberi 72.
- Controlli: generazione senza errori; i 443 collegamenti interni del sito generato portano a una pagina e a un'ancora esistenti; nessun «foglietto» nei sorgenti e nelle pagine; prova in Chrome a larghezza di telefono e di computer.
- Prossima azione: unione della PR dopo il via del curatore; taratura dei sei colori su campioni reali.

-- CC

## 2026-10-21 - CC - Chat: risposte senza trattino lungo

- Le istruzioni della chat (`scripts/genera-sito.py`, rigenerate in `lib/prompt-chat.js`) chiedono di non usare il trattino lungo e di fare gli incisi con virgole, due punti o parentesi, come vuole `CONTRIBUTING.md` § 3 per i testi del sito. La domanda di prova sul sito pubblicato aveva ricevuto una risposta col trattino lungo; con le istruzioni nuove, tre domande inviate direttamente a Gemini ne hanno ricevute zero.
- Prossima azione: taratura dei sei colori su campioni reali.

-- CC

## 2026-10-21 - CC - Sistemata generale dopo la contro-analisi: testi del 20/10 mattina in registro da manuale tecnico, chat senza email, funzioni del server protette

Contro-analisi dello stato di `main` al commit 41b4640: prima lettura di Claude Code, tre revisori esterni indipendenti (Grok, Codex e Gemini) e arbitrato di Fable, 59 rilievi. Le correzioni seguono le decisioni del curatore del 21/10/2026.

- **Testi delle guide**: Principi, Teoria dei colori, Marche e Alberi ripartono dai testi di b981b4d, già controllati sulle fonti, perché la riscrittura del 20/10 (#16) aveva cambiato in una sessantina di punti dati, citazioni e cautele. Vi sono riportate le modifiche valide venute dopo: lezioni di Robert Joyner sul canale attuale, dichiarate come video affini; rimandi alle sezioni Studio ed en plein air e Soggetti; A2 «Conifere alte e rade», perché fra i video c'è un pino silvestre. Su tutte le guide il registro è quello di un manuale tecnico, scelto dal curatore (regole in `CONTRIBUTING.md` § 3); l'indice Gulpease delle pagine va da 59 a 72.
- **Alberi**: pennelli, stati della carta e colori corretti sulle schede dei video in A2-M2, A3-M2, A3-M3, A3-M4, A3-M5, A4-M1, A4-M4, A5-M1, A5-M2, A5-M4, A5-M5 e A6-M2, e negli estratti A3-4 (terra di Siena naturale) e A4-1 (rosso inglese). Le frasi degli autori sono presentate come sintesi («Dal video, in sintesi:»), non come citazioni. Le sei illustrazioni sono dichiarate generate con l'IA, in didascalia e nel piè di pagina; diventano file jpg caricati solo quando servono, e la pagina passa da 1,3 MB a 220 KB.
- **Studio ed en plein air e Soggetti**: il foglietto si ricava dal foglio di 30 × 40 cm tagliato in quattro (15 × 20 cm) o da quello di 56 × 76 cm tagliato in sedici (14 × 19 cm), non da un ottavo del 56 × 76; la tavolozza ridotta coincide con i sei codici di `dati/colori/tavolozza.json`; tolte le spiegazioni senza fonte. I nomi degli esempi di S1 sono letti dal json degli Alberi.
- **Teoria dei colori e Marche**: i colori del calcolatore tornano a essere dichiarati provvisori; corrette la spiegazione della miscela sottrattiva, quella delle «parti» del simulatore, che il modello pesa con la luminanza, e la descrizione del ceruleo; «Carica nel simulatore» riporta il grado di diluizione. Il cremisi della serie Van Gogh è Madder Lake Deep 331 (PR264), controllato il 21/10/2026 sulla pagina ufficiale.
- **Chat** (`functions/api/chat.js`): senza email, con 5 domande a settimana per connessione e 10 al giorno in tutto, contate su D1 in modo atomico con un'impronta dell'IP a sale segreto; nessuna domanda né risposta conservata; la cronologia rimandata dal browser è firmata (HMAC) e limitata a due scambi; se il modello non risponde, la domanda non si conta. I contatori della chat e dei suggerimenti stanno nella stessa tabella e le due funzioni li cancellano con la stessa regola, entro 14 giorni dalla creazione. Il prompt di sistema è generato dai dati in `lib/prompt-chat.js` e il controllo «costruisci» verifica che sia allineato. Informativa riscritta in base al codice.
- **Suggerimenti** (`functions/api/suggerimento.js`): sezioni prese dal menu del sito, corpo limitato a 8000 byte e validato, indirizzi della pagina ridotti a quelli del sito, menzioni `@utente` neutralizzate, 5 invii al giorno per connessione e 30 in tutto.
- **Generatore e pubblicazione**: titoli delle sezioni ripristinati e presi da un'unica lista di `scripts/genera-sito.py`; la generazione si ferma se il menu e le pagine non coincidono con le funzioni, se un nome di marca compare fuori da Marche o se una pagina scende sotto 52 di Gulpease; home con i cinque riquadri delle sezioni; la tabella riassuntiva dei Principi scorre nel suo riquadro e non allarga più la pagina sul telefono; meta description, anteprime per i social, favicon, `robots.txt` e `sitemap.xml`; wrangler fissato alla 4.151.3; `npm run deploy` passa da `scripts/pubblica-locale.py`, che pubblica solo da `main` pulito e allineato a `origin/main`.
- **Documenti**: README, AGENTS e CONTRIBUTING allineati al nuovo stato; LICENSE dichiara le illustrazioni generate con l'IA e mette sotto MIT anche `functions/` e `lib/`.
- **Rilettura integrale** del testo risultante, con quattro revisori a contesto pulito e mandato anti-ridondanza: tolti i doppioni (elenco delle sezioni ripetuto nella home, moduli futuri detti tre volte, regole ripetute in Principi, Studio, Teoria dei colori, Marche e nell'introduzione degli Alberi) e i rimandi a un «corso» mai definito; l'informativa dice anche che cosa arriva a Google oltre alla domanda, che cosa diventa pubblico con un suggerimento e che anche la casella dei suggerimenti registra un'impronta dell'IP; stati della carta, pennelli e colori allineati fra descrizione, infografica ed estratto in A2-M1, A3-M3, A4-M4, A5-M1 e A5-M5; etichetta degli estratti neutra rispetto a chi parla nel video.
- **Decisioni del curatore sui punti aperti**: negli Alberi, dove la sintesi del parlato e la descrizione del gesto dicevano quasi la stessa cosa (22 estratti su 31), resta solo la sintesi, e tre regole ripetute nelle fasi delle infografiche restano nella descrizione e nei riquadri «Da evitare» e «Che cosa controllare»; la pagina passa da 14.249 a 13.586 parole. L'informativa indica come titolare Alessandro Sanvitale; da `CONTRIBUTING.md` § 4 è tolta la clausola sull'uso dei contributi in servizi in abbonamento, e resta la sola licenza del progetto; la chat ha un tetto complessivo di 10 domande al giorno; la chiave Gemini su Cloudflare è quella del progetto a pagamento.
- Prossima azione: taratura dei sei colori su campioni reali; Turnstile di Cloudflare sui due moduli solo se arrivano invii abusivi.

-- CC

## 2026-10-21 - AGY - Nota di metodo iniziale, correzione dei link alle fonti nella sezione 1 «Principi tecnici» e nuove sezioni «Studio ed en plein air» e «Soggetti»

- **Verifica e correzione dei link alle fonti di `dati/principi/principi.json` (`/principi/`)**: sostituito nelle 6 fonti del corso *Watercolor Fanatic* (`wf4`, `wf5`, `wf6`, `wf7`, `wf8`, `wf-fiori`, pari alle voci `[1]`, `[2]`, `[3]`, `[5]`, `[6]` e `[29]` dell'apparato) il vecchio handle `https://www.youtube.com/@WatercolorFanatic` (che restituiva errore 404 dopo il cambio di denominazione del canale dell'autore Robert Joyner in `@crafted_by_robert`) con i collegamenti diretti verificati ai video e al canale attivo di **Robert Joyner | Loose Art** (`jWJvOV24ftY`, `62t3oGplSIE`, `as4p09ekLrY`, `vK9F0fFtDqU`, `U-cV9mfPde8`, `@crafted_by_robert`); aggiornata la fonte `mow` con il collegamento diretto al video specifico di *The Mind of Watercolor* (`xSp2qNBvMSo`) e la fonte `alberi-foglietti` con il rimando a `../studio-plein-air/#protocollo-a5`. Verificati via API oEmbed tutti i collegamenti YouTube della sezione.
- **Nuova sezione 2 — «Pittura in studio ed en plein air: metodo, dotazione e tavolozze» (`dati/studio-plein-air/`, `/studio-plein-air/`)**: scorporata in una sezione autonoma la trattazione del metodo di lavoro in studio e all'aperto, con quadro sinottico comparativo (cinetica di asciugatura, configurazione della tavolozza, dotazione di pennelli e accessori, finalità didattica), protocollo di sperimentazione su campioni in formato A5, descrizione dei pigmenti di comodità della tavolozza estesa da studio e prontuario completo dei 6 pigmenti e delle 12 miscele (`M1`-`M12`) per l'esecuzione *en plein air*.
- **Nuova sezione 5 — «Repertorio dei soggetti pittorici» (`dati/soggetti/`, `/soggetti/`)**: creata la sezione dedicata ai singoli temi pittorici del corso in progressiva estensione: **S1 · Alberi, conifere e masse arbustive** (modulo attivo, collegato a `/alberi/` e alle 6 tipologie `A1`-`A6`, primo argomento affrontato nel corso), seguito dai moduli in preparazione **S2 · Cieli, velature atmosferiche e formazioni nuvolose**, **S3 · Morfologia botanica, corolle e fiori**, **S4 · Specchi d'acqua, increspature e riflessi**, **S5 · Masse rocciose, rilievi montuosi e terreni** e **S6 · Architetture, murature storiche e scorci urbani**.
- **Riorganizzazione dell'indice generale e del modulo Alberi (`scripts/genera-sito.py`, `dati/alberi/`, `functions/api/chat.js`, `README.md`)**: riordinate le 5 sezioni in Home page (*1. Principi tecnici*, *2. Studio ed en plein air*, *3. Colorimetria*, *4. Merceologia*, *5. Soggetti pittorici* con accesso rapido anche a `S1 · Alberi`), aggiunta in apertura la nota di metodo sull'impiego dell'IA come strumento di spoglio e di ordinamento al servizio dello studio manuale dell'acquerello per indicizzare e confrontare le dimostrazioni video su YouTube, snellita l'introduzione di `/alberi/` con rinvio a `/studio-plein-air/` e `/soggetti/` e allineato il prompt di sistema di Gemini 4 Argon.
- Prossima azione: taratura colorimetrica su campioni reali dei 6 pigmenti in `dati/colori/tavolozza.json` e redazione dei successivi moduli della sezione *Soggetti pittorici* (a partire da cieli/nuvole o fiori).

-- AGY

## 2026-10-20 - AGY - Riscrittura integrale di tutte le sezioni del sito in registro tecnico-didattico professionale

- **Home page, struttura di consultazione e componenti comuni (`scripts/genera-sito.py`, `functions/api/chat.js`, `README.md`)**: sostituito il linguaggio colloquiale con una terminologia tecnica rigorosa (idrodinamica delle stesure, stati igrometrici del supporto in cotone, spazio colorimetrico di Munsell, modello spettrale di Kubelka-Munk, merceologia dei pigmenti e codici Colour Index) nella presentazione generale del repertorio, nella guida in 4 tappe *«Struttura e metodo di consultazione»*, nell'interfaccia e nel prompt di sistema del consulente tecnico basato su Gemini 4 Argon (`functions/api/chat.js`) e nel modulo di invio contributi e rettifiche. Esplicitato in apertura, nella sezione *Alberi* e nel prospetto dei moduli in programma che il repertorio è **in fase di sviluppo** e che la monografia sugli alberi inaugura la serie in quanto primo soggetto affrontato nel corso, a cui seguiranno progressivamente i moduli su cieli e formazioni nuvolose, fiori ed elementi botanici, specchi d'acqua, rocce e architetture.
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

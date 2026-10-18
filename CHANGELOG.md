# CHANGELOG - app-acquerello

Cronologia delle modifiche. Ordine cronologico inverso.

## 2026-10-18 - GBOT-app-acquerello - Cremisi della tavolozza: PR206

- Sandro ha controllato l'etichetta: il suo Cotman Alizarin Crimson Hue (n. 3) è PR206, la formula vecchia. In `dati/colori/tavolozza.json` il pigmento passa da PR179 a PR206, con nota e fonte: la formula attuale Winsor & Newton è PR179 (https://www.winsornewton.com/en-ca/products/cotman-watercolour-alizarin-crimson-hue). La pagina mostra PR206 nella scheda del tubetto, nel mescolatore e nelle proposte; la pagina del prodotto è aggiunta alle fonti del capitolo sulla tavolozza.
- Colore sRGB del cremisi non ritoccato (#8E1C34): era un cremisi generico scelto a occhio, non un campione di PR179. Resta provvisorio come gli altri, da tarare sul tubetto.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Nuova sezione «Teoria dei colori» con calcolatore di miscele

Su richiesta di Sandro, seconda sezione del Quaderno: `/colori/`, generata da `dati/colori/` e aggiunta a `SEZIONI` in `scripts/genera-sito.py`, quindi anche alla home.

- Una pagina con 5 capitoli: tinta, valore e croma secondo Munsell (con scala dei valori e ruota delle 40 tinte dalla renotation del 1943); luce e pigmento, additivo e sottrattivo, perché la ruota dei colori non predice le miscele, Kubelka-Munk; l'acquerello, cioè tè, latte, miele, stato della carta, mescolanza e velatura, granulazione; la tavolozza, con le schede dei 6 tubetti Winsor & Newton Cotman e i loro pigmenti dalla tabella ufficiale; il calcolatore. Testi in `teoria-colori.json`, con le fonti collegate a ogni capitolo (Wikipedia, handprint.com, huevaluechroma.com, Winsor & Newton).
- Calcolatore in JavaScript puro scritto per il Quaderno (`calcolatore.js`, `interfaccia.js`), tutto dentro l'html, nessuna libreria esterna: mescola 2 o 3 tubetti in parti intere con anteprima e striscia di diluizione dal miele al tè; cerca a forza bruta le 5 combinazioni di 1-3 tubetti con parti fino a 10 più vicine a un colore scelto, con distanza in OKLab; dà la notazione Munsell approssimata. Modello: Kubelka-Munk a una costante su 38 bande, con le tabelle spettrali di spectral.js (licenza MIT, testo della licenza in `spettri-spectraljs.js`). Niente Mixbox né codice di ArtistAssistApp, che è solo collegata.
- I colori dei 6 tubetti in `tavolozza.json` sono provvisori, scelti a occhio, e la pagina lo dice: vanno sostituiti con la taratura sulle prove di Sandro. In pagina anche i limiti del calcolatore.
- Prove nel browser senza interfaccia: giallo limone + oltremare 1:1 dà un verde (7,5GY 6,2/6,1), oltremare + Siena bruciata 1:1 un grigio scuro (7Y 2,9/1,1), oltremare + cremisi un viola; nessun errore nella console e nessuna richiesta esterna.
- Aggiornati README, `AGENTS.md` e la data della home.

Prossima azione: Sandro guarda la pagina e conferma il cremisi (PR179 o PR206); poi si tarano i 6 tubetti sulle sue prove. La proposta sui testi delle 12 miscele della sezione Alberi è a parte, da approvare prima di scriverla nel json.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Niente merge automatico della sessione cloud

- In `CLAUDE.md` tolta la regola per cui la sessione cloud unisce da sé le pull request: su decisione di Sandro, l'unione su `main`, che pubblica il sito, si fa solo con il suo ok esplicito per quella pull request. Chiude così la prossima azione lasciata aperta il 2026-10-16.

-- GBOT-app-acquerello

## 2026-10-16 - CC - Pubblicazione automatica da GitHub

- Token Cloudflare «github-actions-app-acquerello», col solo permesso Cloudflare Pages: Edit sull'account del progetto, creato da Claude su Chrome e passato a GitHub dagli appunti senza mai mostrarlo. Prima di salvarlo è stato verificato: attivo, e in grado di leggere il progetto Pages `app-acquerello`.
- Nel repository: secret `CLOUDFLARE_API_TOKEN` e `CLOUDFLARE_ACCOUNT_ID`, variabile `PUBBLICA_CLOUDFLARE` = `si`.
- Prova: workflow avviato a mano su `main`, «costruisci» e «pubblica» verdi, pubblicazione `ac921423` in produzione; home e pagina degli alberi rispondono 200 coi titoli giusti.
- Da ora unire su `main` vuol dire pubblicare: aggiornati README, `AGENTS.md`, `CLAUDE.md` e `_index`.

Prossima azione: alla prima sessione cloud, se claude.ai/code non vede il repository privato, aggiungerlo all'app Claude su GitHub; Sandro conferma o toglie da `CLAUDE.md` la regola per cui la sessione cloud unisce da sé le pull request.

## 2026-10-16 - CC - GitHub copia principale, come per le NTC

Su richiesta di Sandro il repository basta a se stesso, e ci possono lavorare anche le sessioni cloud.

- `scripts/genera-sito.py` genera il sito dai soli file del repository, senza più copiare da `pit/acquerello-alberi/`. In `dati/alberi/` sono entrati i due csv della selezione dei video, le 7 illustrazioni dei gesti (`pit-261013-illustrazione-A*.png`) e i due strumenti di prova della pagina. Il generatore `pit-261013-video-gesti.py` contiene ora i quattro aiuti che prendeva dallo script del tutorial, rimasto nel workspace per i pdf, e cerca nel workspace le schede dei video solo per il comando `mandati`; `pit-261013-illustrazioni.py` prende dal workspace le foto del corso.
- Verifica: home e pagina degli alberi generate col flusso nuovo sono identiche byte per byte a quelle pubblicate (md5 `7fd52a42…` e `c181bde4…`), sia nel workspace sia in una copia isolata fuori dal workspace coi soli file del repository.
- Per gli agenti: `AGENTS.md`, `CLAUDE.md` con le regole della sessione cloud sul modello delle NTC, `.claude/settings.json` che installa Pillow da `scripts/requisiti.txt`, prompt di avvio `app-acquerello-261016-prompt-avvio-agente.md`.
- `.github/workflows/sito.yml`: controllo «costruisci» su ogni pull request e su `main`; job «pubblica» su Cloudflare Pages, fermo finché non ci sono la variabile `PUBBLICA_CLOUDFLARE` e la chiave Cloudflare.
- `npm run deploy` allinea prima la copia locale con `git pull --ff-only`.
- Nel workspace, da `pit/acquerello-alberi/` sono usciti i file passati qui; restano lo studio, le schede, i tutorial e le tavole in pdf, con le loro copie della selezione dei video e delle illustrazioni.

Prossima azione: con la chiave Cloudflare di Sandro, impostare i secret e la variabile per la pubblicazione automatica.

## 2026-10-15 - AGY - Creazione repository GitHub e pubblicazione su Cloudflare Pages

- Creata l'applicazione `software/applicazioni-github/app-acquerello/` come contenitore multi-sezione per le guide pratiche di acquerello, con la prima sezione `/alberi/` («Alberi ad acquerello: i gesti nei video», generata da `pit/acquerello-alberi/` con le 7 immagini panoramiche di Nano Banana 2.1 al posto dei ritagli della stampa del corso, senza catture di schermo tratte dai video YouTube) e la home indice `/` testuale.
- Scritto `scripts/genera-sito.py`, che sincronizza in `dati/alberi/` i sorgenti riproducibili (JSON, CSV dei segmenti, script Python e le 7 illustrazioni `pit-261015-riferimento-*.png`) e compila `site/index.html` (3 KB) e `site/alberi/index.html` (1.673 KB).
- Creato il repository privato GitHub `sinmar123/app-acquerello` e pubblicato il sito statico su Cloudflare Pages (`app-acquerello.pages.dev`). Firma: AGY.

Prossima azione: aggiungere le prossime sezioni di acquerello in `SEZIONI` man mano che vengono preparate in `pit/`.

# CHANGELOG - app-acquerello

Cronologia delle modifiche. Ordine cronologico inverso.

## 2026-10-16 - CC - Pubblicazione automatica da GitHub

- Token Cloudflare «github-actions-app-acquerello», col solo permesso Cloudflare Pages: Edit sull'account del progetto, creato da Claude su Chrome e passato a GitHub dagli appunti senza mai mostrarlo. Prima di salvarlo è stato verificato: attivo, e in grado di leggere il progetto Pages `app-acquerello`.
- Nel repository: secret `CLOUDFLARE_API_TOKEN` e `CLOUDFLARE_ACCOUNT_ID`, variabile `PUBBLICA_CLOUDFLARE` = `si`.
- Prova: workflow avviato a mano su `main`, «costruisci» e «pubblica» verdi, pubblicazione `ac921423` in produzione; home e pagina degli alberi rispondono 200 coi titoli giusti.
- Da ora unire su `main` vuol dire pubblicare: aggiornati README, `AGENTS.md`, `CLAUDE.md` e `_index`.

Prossima azione: nessuna.

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

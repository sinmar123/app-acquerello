# CHANGELOG - app-acquerello

Cronologia delle modifiche. Ordine cronologico inverso.

## 2026-10-15 - AGY - Creazione repository GitHub e pubblicazione su Cloudflare Pages

- Creata l'applicazione `software/applicazioni-github/app-acquerello/` come contenitore multi-sezione per le guide pratiche di acquerello, con la prima sezione `/alberi/` («Alberi ad acquerello: i gesti nei video», generata da `pit/acquerello-alberi/` con le 7 immagini panoramiche di Nano Banana 2.1 al posto dei ritagli della stampa del corso, senza catture di schermo tratte dai video YouTube) e la home indice `/` testuale.
- Scritto `scripts/genera-sito.py`, che sincronizza in `dati/alberi/` i sorgenti riproducibili (JSON, CSV dei segmenti, script Python e le 7 illustrazioni `pit-261015-riferimento-*.png`) e compila `site/index.html` (3 KB) e `site/alberi/index.html` (1.673 KB).
- Creato il repository privato GitHub `sinmar123/app-acquerello` e pubblicato il sito statico su Cloudflare Pages (`app-acquerello.pages.dev`). Firma: AGY.

Prossima azione: aggiungere le prossime sezioni di acquerello in `SEZIONI` man mano che vengono preparate in `pit/`.

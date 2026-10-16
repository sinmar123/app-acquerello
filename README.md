---
title: app-acquerello
tags: [software, app, github, cloudflare, acquerello, pit]
progetto: app-acquerello
stato: attivo
tipo: applicazione web statica su Cloudflare Pages
creazione: 2026-10-15
giornale: "[[app-acquerello-giornale]]"
ultimo-aggiornamento: 2026-10-15
---

# app-acquerello

Sito statico a sezioni del **Quaderno di acquerello** (guide pratiche, miscele, gesti nei video ed esercizi su foglietti di prova), pubblicato su **Cloudflare Pages** e versionato sul repository privato GitHub `sinmar123/app-acquerello`.

I contenuti e il materiale di studio vivono nelle sottocartelle sorelle della famiglia `pit/` (a partire da `pit/acquerello-alberi/`). Questo repository raccoglie in `dati/<sezione>/` i sorgenti riproducibili (JSON, CSV dei segmenti, generatori Python, tavole illustrate generate con Nano Banana 2.1) e compila in `site/` l'indice generale e le singole sezioni pronte per la pubblicazione.

## Sezioni attive

| Percorso | Sezione | Sorgente nel workspace |
|----------|---------|------------------------|
| `/` (`site/index.html`) | Indice generale del Quaderno di acquerello | `scripts/genera-sito.py` |
| `/alberi/` (`site/alberi/index.html`) | **1. Alberi ad acquerello: i gesti nei video** (7 esercizi A5, 6 colori, 12 miscele, 35 passi, 39 estratti video, 7 infografiche in 4 fasi) | `pit/acquerello-alberi/` |

## Generare il sito (W520)

```bat
python software\applicazioni-github\app-acquerello\scripts\genera-sito.py
```

Lo script:
1. sincronizza i sorgenti e le illustrazioni Nano Banana 2.1 di ciascuna sezione in `dati/<sezione>/` (tracciati su GitHub);
2. rigenera l'HTML di ogni sezione e lo copia in `site/<sezione>/index.html` con la barra di ritorno all'indice generale;
3. genera la home `site/index.html`.

La cartella compilata `site/` è in `.gitignore` (si rigenera sempre da `dati/` con `scripts/genera-sito.py`).

## Pubblicare su Cloudflare Pages

Prima creazione del progetto Pages (una tantum):

```bat
npx --yes wrangler pages project create app-acquerello --production-branch main
```

Pubblicazione ordinaria (dalla cartella `software/applicazioni-github/app-acquerello`):

```bat
npm run deploy
```

Indirizzo Cloudflare Pages: `https://app-acquerello.pages.dev` (sezione alberi: `https://app-acquerello.pages.dev/alberi/`).

## Aggiungere una nuova sezione in futuro

1. Creare la cartella sorella in `pit/acquerello-<tema>/` con il suo generatore e i suoi dati.
2. Aggiungere il dizionario della nuova sezione nella lista `SEZIONI` di `scripts/genera-sito.py`.
3. Lanciare `npm run deploy`, poi fare commit e push sul repository GitHub.

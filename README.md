---
title: app-acquerello
tags: [software, app, github, cloudflare, acquerello, pit]
progetto: app-acquerello
stato: attivo
tipo: applicazione web statica su Cloudflare Pages
creazione: 2026-10-15
giornale: "[[app-acquerello-giornale]]"
ultimo-aggiornamento: 2026-10-18
---

# app-acquerello

Sito statico a sezioni del **Quaderno di acquerello** (guide pratiche, miscele, gesti nei video ed esercizi su foglietti di prova), pubblicato su **Cloudflare Pages** e versionato sul repository privato GitHub `sinmar123/app-acquerello`.

Dal 16/10/2026 **GitHub è la copia principale**, come per il repository delle NTC: il repository contiene tutto quello che serve a generare le pagine, e ci lavorano anche le sessioni cloud. I sorgenti di ogni sezione stanno in `dati/<sezione>/`. Lo studio da cui la sezione nasce (schede dei video fatte con Gemini, tutorial e tavole in pdf) resta nel workspace, nella cartella sorella della famiglia `pit/`: per gli alberi `pit/acquerello-alberi/`.

## Sezioni attive

| Percorso | Sezione | Sorgenti | Studio nel workspace |
|----------|---------|----------|----------------------|
| `/` (`site/index.html`) | Indice generale del Quaderno di acquerello | `scripts/genera-sito.py` | - |
| `/principi/` (`site/principi/index.html`) | **1. Principi generali: acqua, colore e carta** (tè, latte, miele; stati della carta e momenti di mezzo; pennello e carta; bordi, asciugatura, tipi di carta; ogni frase con la fonte, video aperti al minuto) | `dati/principi/` | `pit/documentazione/`, `pit/acquerello-alberi/schede/` |
| `/alberi/` (`site/alberi/index.html`) | **2. Alberi ad acquerello: i gesti nei video** (7 esercizi A5, 6 colori, 12 miscele, 35 passi, 39 estratti video, 7 infografiche in 4 fasi) | `dati/alberi/` | `pit/acquerello-alberi/` |
| `/colori/` (`site/colori/index.html`) | **3. Teoria dei colori per l'acquerello** (Munsell, luce e pigmento, velature, schede dei 6 colori di base col nome comune e il pigmento, calcolatore di miscele in JavaScript che gira nel browser) | `dati/colori/` | `pit/documentazione/` |
| `/marche/` (`site/marche/index.html`) | **4. Marche e tubetti** (i 6 colori di base in sei serie: Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu; dati solo da pagine ufficiali, con link e data su ogni riga; stesso nome, pigmenti diversi) | `dati/marche/` | - |

## Lavorare con un agente

Frase da dare a un agente, in cloud o sul W520:

```text
Leggi ed esegui app-acquerello-261016-prompt-avvio-agente.md del repository https://github.com/sinmar123/app-acquerello
```

Il repository è privato: lo apre solo un agente collegato all'account GitHub di Sandro. Le regole stanno in `AGENTS.md` e, per Claude Code, in `CLAUDE.md`: si lavora su un ramo e si chiude con una pull request.

Un agente che lavora sulla copia del workspace parte da `git pull` e chiude con una pull request, o con commit e push: la copia locale non è più la principale.

## Generare il sito

Dalla radice del repository:

```bat
python scripts/genera-sito.py
```

Lo script:
1. rigenera la pagina di ogni sezione col suo generatore in `dati/<sezione>/` (per gli alberi `pit-261013-video-gesti.py pagina`);
2. la copia in `site/<sezione>/index.html` con la barra di ritorno all'indice generale;
3. genera la home `site/index.html`.

Serve solo Pillow (`scripts/requisiti.txt`). `site/` e le pagine html generate dentro `dati/` sono in `.gitignore`.

## Controllo e pubblicazione

Su GitHub il controllo «costruisci» (`.github/workflows/sito.yml`) rigenera il sito a ogni pull request e a ogni modifica di `main`. Il job «pubblica» manda il sito su Cloudflare Pages a ogni modifica di `main`: dal 16/10/2026 nel repository ci sono la variabile `PUBBLICA_CLOUDFLARE` = `si` e i secret `CLOUDFLARE_API_TOKEN` (token Cloudflare «github-actions-app-acquerello», permesso Cloudflare Pages: Edit) e `CLOUDFLARE_ACCOUNT_ID`. Quindi unire una pull request su `main` vuol dire pubblicare. Per spegnere la pubblicazione automatica basta cambiare la variabile.

Resta la pubblicazione a mano dal W520, dalla cartella `software/applicazioni-github/app-acquerello`, stando su `main`:

```bat
npm run deploy
```

Il comando allinea prima la copia locale a GitHub (`git pull --ff-only`) e si ferma se non ci riesce, poi rigenera e pubblica.

Prima creazione del progetto Pages (una tantum, fatta il 15/10/2026):

```bat
npx --yes wrangler pages project create app-acquerello --production-branch main
```

Indirizzo Cloudflare Pages: `https://app-acquerello.pages.dev` (sezione alberi: `https://app-acquerello.pages.dev/alberi/`).

## Aggiungere una nuova sezione

1. Studio del tema nel workspace, nella cartella sorella `pit/acquerello-<tema>/`.
2. Sorgenti della pagina e generatore in `dati/<tema>/`.
3. Dizionario della nuova sezione nella lista `SEZIONI` di `scripts/genera-sito.py`.
4. Pull request; dopo l'unione, pubblicazione come sopra.

## File per gli agenti e per GitHub

- `AGENTS.md`, `CLAUDE.md`: istruzioni per gli agenti, comprese le sessioni cloud.
- `app-acquerello-261016-prompt-avvio-agente.md`: prompt per far partire da zero un agente.
- `scripts/requisiti.txt`: dipendenze della generazione.
- `.claude/settings.json`: nelle sessioni cloud installa Pillow all'avvio.
- `.github/workflows/sito.yml`: controllo «costruisci» e pubblicazione.

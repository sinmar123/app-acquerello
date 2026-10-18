---
title: Index - app-acquerello
tags: [index]
ultimo-aggiornamento: 2026-10-18
---

# Index - app-acquerello

Sito statico a sezioni del Quaderno di acquerello su Cloudflare Pages e GitHub (`sinmar123/app-acquerello`). Dal 16/10/2026 GitHub è la copia principale, come per le NTC.

| Voce | Dettaglio |
|------|-----------|
| Path | `software/applicazioni-github/app-acquerello` |
| Sorgenti sezioni | `dati/alberi/` (lo studio resta in `pit/acquerello-alberi/`), `dati/colori/` (Teoria dei colori e calcolatore di miscele) |
| Generatore | `scripts/genera-sito.py`, dipendenze in `scripts/requisiti.txt` |
| Output | `site/index.html`, `site/alberi/index.html` e `site/colori/index.html` (in `.gitignore`) |
| Controllo e deploy | `.github/workflows/sito.yml`: controllo su ogni pull request e, dal 16/10/2026, pubblicazione automatica sul progetto Cloudflare Pages `app-acquerello` a ogni modifica di `main`; dal W520 resta `npm run deploy` |
| Agenti | `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json`, prompt `app-acquerello-261016-prompt-avvio-agente.md` |
| Diario | [[app-acquerello-giornale]] |

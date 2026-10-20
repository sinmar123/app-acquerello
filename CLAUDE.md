# CLAUDE.md - Quaderno di acquerello

Ingresso per Claude Code. Importa le istruzioni comuni:

@AGENTS.md

## Sessione cloud

Il repository contiene tutto il necessario per generare e verificare il sito:

- all'avvio `.claude/settings.json` installa da solo Pillow (`scripts/requisiti.txt`), così gira `scripts/genera-sito.py`;
- si lavora su un ramo e si chiude con una pull request senza unirla su `main`: l'unione su `main` pubblica il sito su Cloudflare Pages (`https://app-acquerello.pages.dev`) tramite il job «pubblica» e richiede l'approvazione del curatore del progetto;
- aperta la pull request, si invia il riepilogo con il collegamento e lo stato del controllo «costruisci».

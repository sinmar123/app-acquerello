# CLAUDE.md - Quaderno di acquerello

Ingresso per Claude Code. Importa le istruzioni comuni:

@AGENTS.md

## Sessione cloud (claude.ai/code), dal 2026-10-16

Dal 2026-10-16, per scelta di Sandro, GitHub è la copia principale, come per il repository delle NTC. Una sessione cloud vede soltanto il repository: niente workspace, skill, giornale né server MCP del W520. Regole in più per lei:

- all'avvio `.claude/settings.json` installa da solo Pillow (`scripts/requisiti.txt`), così gira `scripts/genera-sito.py`;
- chiude con una pull request e non la unisce: l'unione su `main` pubblica il sito, quindi si fa solo con l'ok esplicito di Sandro per quella pull request. Aperta la pull request, manda a Sandro il riepilogo con il collegamento e lo stato del controllo «costruisci». Le proposte sui testi delle guide si portano comunque a Sandro prima di scriverle;
- il CHANGELOG fa anche da giornale, con firma `CC cloud`: il giornale del workspace non è raggiungibile;
- dal 2026-10-16 l'unione su `main` pubblica da sola il sito su Cloudflare Pages (`https://app-acquerello.pages.dev`) col job «pubblica»: dopo l'unione approvata da Sandro si controlla che il job sia verde e lo si scrive nel riepilogo.

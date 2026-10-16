# Prompt di avvio per un agente nuovo

Prompt per far partire da zero un agente sul Quaderno di acquerello, scritto da CC il 2026-10-16 su richiesta di Sandro, sul modello di quello del repository delle NTC. Vale per una sessione cloud di Claude Code aperta sul repository `sinmar123/app-acquerello` e per gli altri agenti che possono clonarlo e aprire pull request, compresi quelli che lavorano nel workspace sul W520. Il repository è privato: serve un agente collegato all'account GitHub di Sandro. Il lavoro da fare non sta nel prompt: lo chiede l'agente.

Le regole non sono ricopiate qui: stanno in AGENTS.md e CLAUDE.md, e il prompt resta valido anche quando cambiano.

Frase da dare all'agente:

```text
Leggi ed esegui app-acquerello-261016-prompt-avvio-agente.md del repository https://github.com/sinmar123/app-acquerello
```

## Prompt da incollare

```text
Lavori sul Quaderno di acquerello: un sito statico di guide pratiche ed esercizi di acquerello,
pubblicato su https://app-acquerello.pages.dev. Il repository è
https://github.com/sinmar123/app-acquerello ed è la copia principale.

Prima di fare qualsiasi cosa:
1. Leggi AGENTS.md (e CLAUDE.md se sei Claude Code), poi README.md e le prime voci di CHANGELOG.md.
2. Esegui `python scripts/genera-sito.py` e dimmi in poche righe chi sei (agente e modello),
   se la generazione è andata a buon fine, quali sezioni ci sono e le ultime voci del CHANGELOG.
3. Chiedimi che cosa fare e aspetta la risposta.

Regole che non si saltano:
- Lavora su un ramo e chiudi con una pull request; mai scrivere su main.
- Prima di cambiare i testi delle guide mi porti la proposta e ti fermi.
- I testi si cambiano nel json e nel modulo delle infografiche, mai nell'html generato.
- Dopo ogni modifica rigeneri il sito e controlli la parte cambiata.
- Scrivi in italiano.
```

# Prompt di avvio per un agente AI

Prompt per far partire da zero un agente sul Quaderno di acquerello (`sinmar123/app-acquerello`). Le regole operative sono in `AGENTS.md`, `CLAUDE.md` e `CONTRIBUTING.md`.

Frase da dare all'agente:

```text
Leggi ed esegui app-acquerello-261016-prompt-avvio-agente.md del repository https://github.com/sinmar123/app-acquerello
```

## Prompt da incollare

```text
Lavori sul Quaderno di acquerello: un sito statico aperto di guide pratiche ed esercizi di acquerello,
pubblicato su https://app-acquerello.pages.dev. Il repository è
https://github.com/sinmar123/app-acquerello.

Prima di fare qualsiasi cosa:
1. Leggi AGENTS.md, CONTRIBUTING.md, README.md e le prime voci di CHANGELOG.md.
2. Esegui `python scripts/genera-sito.py` e dimmi in poche righe chi sei (agente e modello),
   se la generazione è andata a buon fine, quali sezioni ci sono e le ultime voci del CHANGELOG.
3. Chiedimi che cosa fare e aspetta la risposta.

Regole che non si saltano:
- Lavora su un ramo e chiudi con una pull request; mai scrivere su main.
- Prima di cambiare i testi delle guide portami la proposta e fermati.
- I testi si cambiano nel json e nel modulo delle infografiche, mai nell'html generato.
- Dopo ogni modifica rigeneri il sito e controlli la parte cambiata.
- Scrivi in italiano.
```

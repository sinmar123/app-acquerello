# Quaderno di acquerello (`app-acquerello`)

Sito statico aperto di guide pratiche, miscele, gesti nei video ed esercizi su foglietti di prova per chi studia l'acquerello.

- **Sito online:** [https://app-acquerello.pages.dev](https://app-acquerello.pages.dev)
- **Repository GitHub:** [https://github.com/sinmar123/app-acquerello](https://github.com/sinmar123/app-acquerello)
- **Licenza:** [CC BY 4.0 per testi, dati e illustrazioni · MIT per il codice](LICENSE)

Il repository è autonomo: contiene tutti i file di dati, le infografiche SVG, le illustrazioni e gli script necessari a generare l'intero sito. Chiunque può proporre correzioni, nuove marche, nuovi esempi o nuove sezioni direttamente tramite la casella in fondo a ogni pagina del sito oppure secondo le indicazioni di [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sezioni attive

| Percorso | Sezione | Sorgenti |
|----------|---------|----------|
| `/` (`site/index.html`) | Indice generale del Quaderno di acquerello | `scripts/genera-sito.py` |
| `/principi/` (`site/principi/index.html`) | **1. Principi generali: acqua, colore e carta** (tè, latte, miele; stati della carta e momenti di mezzo; pennello e carta; bordi, asciugatura, tipi di carta; ogni frase con la fonte, video aperti al minuto) | `dati/principi/` |
| `/alberi/` (`site/alberi/index.html`) | **2. Alberi ad acquerello: esempi, modalità e gesti nei video** (6 esempi di alberi e arbusti, 24 modalità nei video con un'infografica SVG in 3 fasi per ciascun video, 31 estratti video, proposte di colore libere per lo studio e tavolozza da 6 colori e 12 miscele per l'aperto) | `dati/alberi/` |
| `/colori/` (`site/colori/index.html`) | **3. Teoria dei colori per l'acquerello** (Munsell, luce e pigmento, velature, schede dei 6 colori della tavolozza ridotta col nome comune e il pigmento, calcolatore di miscele in JavaScript che gira nel browser) | `dati/colori/` |
| `/marche/` (`site/marche/index.html`) | **4. Marche e tubetti** (i 6 colori della tavolozza ridotta in sei serie: Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu; dati solo da pagine ufficiali, con link e data su ogni riga; stesso nome, pigmenti diversi) | `dati/marche/` |

## Generare il sito in locale

Requisiti: Python 3.10+ e Pillow (`pip install -r scripts/requisiti.txt`).

Dalla radice del repository:

```bash
python scripts/genera-sito.py
```

Lo script:
1. rigenera la pagina di ogni sezione col suo generatore in `dati/<sezione>/`;
2. la copia in `site/<sezione>/index.html` aggiungendo la barra superiore e la casella per i suggerimenti;
3. genera la home `site/index.html`.

La cartella `site/` e le pagine HTML generate dentro `dati/` sono escluse da Git (`.gitignore`). La funzione Cloudflare Pages `functions/api/suggerimento.js` riceve i suggerimenti inviati dalla casella del sito e apre una Issue pubblica etichettata `suggerimento-dal-sito` sul repository GitHub.

## Come contribuire

Leggi [`CONTRIBUTING.md`](CONTRIBUTING.md) per le regole editoriali (fonti obbligatorie, colori indicati col nome comune e il pigmento nelle guide, nessun fotogramma estratto dai video YouTube) e per il flusso tramite la casella del sito, Issue o Pull Request.

Per aggiungere una nuova sezione:
1. Crea la cartella `dati/<tema>/` con i sorgenti e lo script generatore.
2. Aggiungi il dizionario della nuova sezione nella lista `SEZIONI` di `scripts/genera-sito.py`.
3. Verifica con `python scripts/genera-sito.py` e apri una Pull Request.

## Controllo automatico e pubblicazione

Su GitHub il controllo «costruisci» (`.github/workflows/sito.yml`) rigenera il sito a ogni Pull Request e a ogni modifica di `main`, verificando che tutte le sezioni compilino senza errori. Quando una Pull Request viene approvata e unita su `main`, il job «pubblica» aggiorna automaticamente il sito su Cloudflare Pages (`https://app-acquerello.pages.dev`).

## Lavorare con un agente AI

Il repository include le istruzioni per gli agenti di codifica in [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md) e il prompt di avvio [`app-acquerello-261016-prompt-avvio-agente.md`](app-acquerello-261016-prompt-avvio-agente.md).

# Quaderno di acquerello (`app-acquerello`)

Repertorio tecnico-didattico ad accesso aperto dedicato allo studio sistematico della pittura ad acquerello: principi idrodinamici, morfologia ed esecuzione degli alberi con tavole sinottiche e analisi dei gesti nei video, colorimetria e simulatore spettrale, merceologia dei pigmenti.

- **Sito online:** [https://app-acquerello.pages.dev](https://app-acquerello.pages.dev)
- **Repository GitHub:** [https://github.com/sinmar123/app-acquerello](https://github.com/sinmar123/app-acquerello)
- **Licenza:** [CC BY 4.0 per testi, dati e illustrazioni · MIT per il codice](LICENSE)

Il repository è autonomo: contiene tutti i file di dati, le tavole sinottiche SVG, le illustrazioni e gli script necessari a generare l'intero sito. **Il repertorio è in fase di sviluppo e progressiva estensione:** accanto alle sezioni teorico-metodologiche generali (*Principi tecnici*, *Colorimetria*, *Merceologia*), il modulo sulla *Morfologia degli alberi* è il primo pubblicato in quanto primo argomento affrontato nel corso di studio; seguiranno progressivamente nuove monografie dedicate agli altri temi classici dell'acquerello (cieli e formazioni nuvolose, elementi botanici e fiori, specchi d'acqua e riflessi, masse rocciose e architetture). Chiunque può proporre rettifiche, integrazioni documentali o nuovi riferimenti video tramite il modulo in calce a ogni pagina del sito oppure secondo le indicazioni di [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sezioni attive

| Percorso | Sezione | Sorgenti |
|----------|---------|----------|
| `/` (`site/index.html`) | Indice generale e metodo di consultazione del Quaderno di acquerello | `scripts/genera-sito.py` |
| `/principi/` (`site/principi/index.html`) | **1. Principi tecnici: diluizione del pigmento e stati del supporto** (scala tè, latte, miele; stati della carta e fasi di transizione; bilancio idrico pennello-supporto; gestione dei bordi, asciugatura, caratteristiche delle carte; apparato di 33 fonti con rimandi al minuto) | `dati/principi/` |
| `/studio-plein-air/` (`site/studio-plein-air/index.html`) | **2. Pittura in studio ed en plein air: metodo, dotazione e tavolozze** (confronto tra banco di studio e pittura all'aperto, protocollo sui campioni A5, tavolozza estesa da studio, tavolozza ristretta a 6 pigmenti e prontuario completo delle 12 miscele `M1`-`M12`) | `dati/studio-plein-air/` |
| `/colori/` (`site/colori/index.html`) | **3. Colorimetria applicata e ottica della velatura** (spazio colorimetrico di Munsell, sintesi sottrattiva, velature e granulazione, schede tecniche dei 6 pigmenti di base col codice Colour Index, simulatore spettrale Kubelka-Munk in JavaScript) | `dati/colori/` |
| `/marche/` (`site/marche/index.html`) | **4. Merceologia dei pigmenti e confronto tra serie commerciali** (i 6 pigmenti della tavolozza essenziale messi a confronto in sei serie: Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu; dati da schede ufficiali con link e data di verifica; analisi della variabilità formulativa) | `dati/marche/` |
| `/soggetti/` (`site/soggetti/index.html`) | **5. Repertorio dei soggetti pittorici: monografie esecutive** (sezione contenitore dei soggetti affrontati nel corso: `S1` Alberi attivo, `S2` Cieli e nuvole, `S3` Fiori e botanica, `S4` Acqua e riflessi, `S5` Rocce e rilievi, `S6` Architetture) | `dati/soggetti/` |
| `/alberi/` (`site/alberi/index.html`) | **5.1 Soggetto S1 · Morfologia degli alberi** (6 tipologie arboree e vegetazionali, 24 modalità esecutive con tavola sinottica SVG in 3 fasi per ciascun video, 31 estratti video indicizzati) | `dati/alberi/` |

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

La cartella `site/` e le pagine HTML generate dentro `dati/` sono escluse da Git (`.gitignore`). Le funzioni Cloudflare Pages in `functions/api/` gestiscono:
- `functions/api/chat.js`: l'assistente didattico sull'acquerello basato su **Gemini 4 Argon** (`gemini-4-argon`), con accesso tramite email e limite di 5 domande gratuite per utente salvato sul database Cloudflare D1 (`wrangler.toml`);
- `functions/api/suggerimento.js`: l'invio dei suggerimenti dalla casella pubblica del sito come Issue etichettata `suggerimento-dal-sito` sul repository GitHub.

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

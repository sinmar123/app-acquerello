# Quaderno di acquerello (`app-acquerello`)

Il Quaderno nasce tra dilettanti ed è rivolto ad altri dilettanti. Raccoglie ciò che si impara strada facendo, con i limiti di chi non è un maestro, ed è aperto ai contributi di tutti gli appassionati.

Appunti di studio dell'acquerello aperti al pubblico: le tre consistenze della miscela e gli stati della carta, la teoria dei colori con un calcolatore di miscele, i tubetti marca per marca e gli esercizi per soggetto, a cominciare dagli alberi, con i passaggi dei video didattici indicati al secondo.

Chi oggi apprende una disciplina pratica dispone di una documentazione vastissima ma frammentata; gli strumenti di intelligenza artificiale consentono di compiere a monte il lavoro di spoglio, confronto e classificazione delle fonti, così da ritrovare il dato tecnico nel momento dell'esercizio. Il Quaderno applica questo approccio allo studio dell'acquerello.

- **Sito:** [https://app-acquerello.pages.dev](https://app-acquerello.pages.dev)
- **Repository:** [https://github.com/sinmar123/app-acquerello](https://github.com/sinmar123/app-acquerello)
- **Licenza:** [CC BY 4.0 per testi, dati e illustrazioni · MIT per il codice](LICENSE)

Il repository è autonomo: contiene i dati, le infografiche, le illustrazioni e gli script che generano l'intero sito. **Il Quaderno è in costruzione:** alle sezioni generali (*Principi generali*, *Teoria dei colori*, *Marche e tubetti*) si aggiunge un modulo per ogni soggetto; il primo, sugli alberi, è pubblicato, e seguiranno cieli e nuvole, fiori, acqua e riflessi, rocce, architetture. La sezione *Eventi* raccoglie il calendario, la scheda di ogni evento (locandina, programma e fotografie) e l'archivio per anno. Correzioni, integrazioni e nuovi video si propongono con la casella in fondo a ogni pagina o secondo [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sezioni

| Percorso | Sezione | Sorgenti |
|----------|---------|----------|
| `/` | Indice e organizzazione del Quaderno | `scripts/genera-sito.py` |
| `/principi/` | **1. Principi generali: acqua, colore e carta**: tè, latte e miele; carta bagnata, umida, asciutta e i momenti intermedi; acqua nel pennello e acqua nella carta; bordi, asciugatura, carte; nel capitolo 8, *In studio e all'aperto* (`#studio-aperto`), il lavoro in studio e all'aperto a confronto, la tavolozza estesa e i sei colori proposti con le 12 miscele `M1`-`M12`; 42 fonti, elencate in fondo a ogni capitolo, dai corsi, dai video al minuto indicato e dalle altre sezioni del Quaderno | `dati/principi/` |
| `/colori/` | **2. Teoria dei colori**: Munsell, luce e pigmento, velature, i sei colori proposti col pigmento e un calcolatore di miscele Kubelka-Munk in JavaScript; rimandi alle fonti paragrafo per paragrafo | `dati/colori/` |
| `/marche/` | **3. Marche e tubetti**: i sei colori proposti in sei serie (Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu), con pagina ufficiale e data di controllo su ogni riga | `dati/marche/` |
| `/soggetti/` | **4. Soggetti**: un modulo per tema; `S1` Alberi pubblicato, `S2`-`S6` in preparazione | `dati/soggetti/` |
| `/alberi/` | **4.1 S1 · Alberi ad acquerello**: 6 esempi, 24 modalità tratte dai video con un'infografica SVG in 3 fasi ciascuna, 31 estratti video | `dati/alberi/` |
| `/eventi/` | **5. Eventi**: calendario di festival, mostre, demo e uscite en plein air, in corso, in arrivo e passati; scheda per evento con locandina, programma e fotografie di chi ha partecipato; archivio `/eventi/<anno>/` e scheda `/eventi/<anno>/<slug>/` | `dati/eventi/` |

Le frasi «L'autore, in sintesi» della sezione Alberi riassumono in italiano il parlato dei video, con l'aiuto dell'IA: non sono trascrizioni.

## Generare il sito in locale

Requisiti: Python 3.10+ e Pillow (`pip install -r scripts/requisiti.txt`). Dalla radice del repository:

```bash
python scripts/genera-sito.py
```

Lo script:
1. controlla che il menu della casella dei suggerimenti e le pagine del sito coincidano con gli elenchi che le funzioni del server accettano, e che i nomi delle marche non compaiano fuori dalla sezione Marche;
2. rigenera la pagina di ogni sezione col suo generatore in `dati/<sezione>/`, che fa i controlli propri della sezione (fonti dei Principi, fonti e date delle Marche, coerenza della tavolozza);
3. la copia in `site/<sezione>/index.html` con la barra delle sezioni, la chat e la casella dei suggerimenti, e scrive la home, `robots.txt`, `sitemap.xml` e la favicon;
4. scrive `lib/prompt-chat.js`, il prompt della chat ricavato dai dati del sito;
5. misura la leggibilità di ogni pagina (indice Gulpease) e si ferma se una pagina scende sotto 52.

`site/` e le pagine HTML generate dentro `dati/` sono escluse da Git (`.gitignore`); `lib/prompt-chat.js` invece si committa, perché lo usa la funzione della chat.

## Funzioni del server

Due funzioni Cloudflare Pages in `functions/api/`, con il database D1 `app-acquerello` (`wrangler.toml`):

- `chat.js`: l'assistente sull'acquerello basato su **Gemini 4 Argon** (`gemini-4-argon`), istruito con `lib/prompt-chat.js`. Non chiede l'email e non conserva né le domande né le risposte: concede 5 domande a settimana per connessione, con un tetto di 10 domande al giorno in tutto, contate su D1 con un'impronta dell'indirizzo IP calcolata con una chiave segreta e cancellata entro 14 giorni. La cronologia della conversazione torna dal browser firmata dal server, che scarta le risposte non sue. Segreti: `GEMINI_API_KEY` (obbligatorio), `SALE_IP` e `CHIAVE_FIRMA` (facoltativi).
- `suggerimento.js`: apre una Issue etichettata `suggerimento-dal-sito` sul repository con il segreto `GITHUB_SUGGERIMENTI_TOKEN`. Accetta solo le sezioni del menu e le pagine del sito, oscura gli indirizzi email, neutralizza le menzioni `@utente` e concede 5 invii al giorno per connessione e 30 in tutto, contati come le domande della chat, sulla stessa tabella di D1 (segreto facoltativo `SALE_IP`).

## Controllo automatico e pubblicazione

Su GitHub il controllo «costruisci» (`.github/workflows/sito.yml`) rigenera il sito a ogni pull request e a ogni modifica di `main`, verifica che tutte le sezioni compilino e che `lib/prompt-chat.js` corrisponda ai dati. Quando una pull request approvata viene unita su `main`, il job «pubblica» aggiorna il sito su Cloudflare Pages: parte perché nel repository sono impostati la variabile `PUBBLICA_CLOUDFLARE` e i segreti di Cloudflare. Dal PC si pubblica con `npm run deploy`, che parte solo da `main` pulito e allineato a GitHub (`scripts/pubblica-locale.py`).

## Come contribuire

[`CONTRIBUTING.md`](CONTRIBUTING.md) descrive le regole editoriali (fonti, colori col nome comune e il pigmento, nessun fotogramma dei video, registro dei testi) e il flusso tramite la casella del sito, le Issue o le pull request. Per aggiungere una sezione: cartella `dati/<tema>/` con sorgenti e generatore, voce nella lista `SEZIONI` di `scripts/genera-sito.py` e nei due elenchi `PAGINE_VALIDE` delle funzioni, poi `python scripts/genera-sito.py` e una pull request.

## Lavorare con un agente AI

Le istruzioni per gli agenti di codifica sono in [`AGENTS.md`](AGENTS.md) e [`CLAUDE.md`](CLAUDE.md), con il prompt di avvio [`app-acquerello-261016-prompt-avvio-agente.md`](app-acquerello-261016-prompt-avvio-agente.md).

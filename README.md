# Quaderno di acquerello con IA (`app-acquerello`)

Il titolo è «Quaderno di acquerello con IA», come richiesto dal curatore nel topic dell’app il 7 novembre 2026. Il curatore ha autorizzato nello stesso topic l’unione e la pubblicazione della [PR #72](https://github.com/sinmar123/app-acquerello/pull/72). L’indirizzo del sito e il nome del repository restano invariati.

Il Quaderno nasce dall’iniziativa personale di un appassionato che dipinge ad acquerello per hobby. Il curatore usa i modelli di intelligenza artificiale nel proprio lavoro e li sperimenta anche per organizzare le informazioni sull’acquerello e come aiuto allo studio. Il progetto è aperto alla collaborazione di altri appassionati, sia sui contenuti sia sullo sviluppo del sito, tramite GitHub.

Appunti di studio dell'acquerello aperti al pubblico: le tre consistenze della miscela e gli stati della carta, la teoria dei colori con un calcolatore di miscele, i tubetti marca per marca e gli esercizi per soggetto, a cominciare dagli alberi, con i passaggi dei video didattici indicati al secondo.

L’apertura della Home, «Perché questo Quaderno», racconta l’esperimento e riunisce presentazione e metodo, senza una nota separata. La revisione del 7 novembre 2026 mantiene i primi due capoversi approvati il 4 novembre e rende il finale meno personale: precisa i limiti della rilettura dei testi rielaborati e delle ricerche approfondite con l’IA, invita i lettori a contribuire anche come co-curatori e presenta il Quaderno come un piccolo esperimento di cura condivisa dei contenuti. Il curatore ha autorizzato l’unione e la pubblicazione della [PR #73](https://github.com/sinmar123/app-acquerello/pull/73) nel topic dell’app il 7 novembre 2026. Restano invariate le note specifiche delle guide e il loro registro tecnico.

- **Sito:** [https://app-acquerello.pages.dev](https://app-acquerello.pages.dev)
- **Repository:** [https://github.com/sinmar123/app-acquerello](https://github.com/sinmar123/app-acquerello)
- **Licenza:** [CC BY 4.0 per testi, dati e illustrazioni · MIT per il codice](LICENSE); le opere della sezione *Opere* restano dei rispettivi autori

Il repository è autonomo: contiene i dati, le infografiche, le illustrazioni e gli script che generano l'intero sito. **Il Quaderno è in costruzione:** alle sezioni generali (*Principi generali*, *Teoria dei colori*, *Marche e tubetti*) si aggiunge un modulo per ogni soggetto; il primo, sugli alberi, è pubblicato, e seguiranno cieli e nuvole, fiori, acqua e riflessi, rocce, architetture. La sezione *Approfondimenti* dedica una pagina a ogni questione che torna spesso fra chi dipinge, con il bianco e il blu oltremare nell'acquerello. La sezione *Eventi* raccoglie il calendario, la scheda di ogni evento (locandina, programma e fotografie) e l'archivio per anno. La sezione *Opere di non professionisti* raccoglie gli acquerelli di appassionati, una sottosezione per autore, a cominciare da quelli di sinmar. Correzioni, integrazioni e nuovi video si propongono con la casella in fondo a ogni pagina o secondo [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sezioni

| Percorso | Sezione | Sorgenti |
|----------|---------|----------|
| `/` | Indice e organizzazione del Quaderno | `scripts/genera-sito.py` |
| `/principi/` | **1. Principi generali: acqua, colore e carta**: tè, latte e miele; carta bagnata, umida, asciutta e i momenti intermedi; acqua nel pennello e acqua nella carta; bordi, asciugatura, carte; nel capitolo 8, *In studio e all'aperto* (`#studio-aperto`), il lavoro in studio e all'aperto a confronto, la tavolozza estesa e, per quando conviene lavorare con pochi colori, la tavolozza ridotta di sei colori con le 12 miscele `M1`-`M12` (l'unico punto del sito dove stanno i sei colori); 42 fonti, elencate in fondo a ogni capitolo, dai corsi, dai video al minuto indicato e dalle altre sezioni del Quaderno | `dati/principi/` |
| `/colori/` | **2. Teoria dei colori**: Munsell, luce e pigmento, velature e un calcolatore di miscele Kubelka-Munk in JavaScript, che lavora con la tavolozza ridotta del capitolo 8 dei Principi; rimandi alle fonti paragrafo per paragrafo | `dati/colori/` |
| `/marche/` | **3. Marche e tubetti**: guida generale ai colori in commercio, cioè tubetti e pastiglie, serie per chi comincia e per artisti, come leggere l'etichetta, stesso nome e pigmenti diversi, una scheda per ognuna di sei serie (Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu); in fondo, come esempio, i sei colori della tavolozza ridotta nelle sei serie, con pagina ufficiale e data di controllo su ogni riga | `dati/marche/` |
| `/soggetti/` | **4. Soggetti**: un modulo per tema; `S1` Alberi pubblicato, `S2`-`S6` in preparazione | `dati/soggetti/` |
| `/alberi/` | **4.1 S1 · Alberi**: si apre con sommario, indice e premessa; 6 esempi, 25 modalità tratte dai video con un'infografica SVG in 3 fasi ciascuna, 32 estratti video; ogni video si carica da YouTube solo quando si preme «Guarda il video» | `dati/alberi/` |
| `/approfondimenti/` | **5. Approfondimenti**: una pagina per ogni questione che torna spesso fra chi dipinge ad acquerello, una sottosezione per tema (`5.1` Il bianco nell'acquerello, `/approfondimenti/bianco/`: storia della regola, bandi di società e concorsi, pigmenti bianchi, riserve, opinioni dei pittori, perché la carta sembra più luminosa, conservazione e proposte pratiche); in cima la sintesi e la premessa, in fondo a ogni capitolo le fonti, con il passo originale delle citazioni tradotte; le valutazioni del Quaderno sono dichiarate. La pagina `5.2`, `/approfondimenti/blu-oltremare/`, tratta PB29, granulazione, stesure, mescolanze, conservazione e sei prove comparative, con otto capitoli e 16 fonti | `dati/approfondimenti/` |
| `/eventi/` | **6. Eventi**: calendario di festival, mostre, demo e uscite en plein air, in corso, in arrivo e passati; scheda per evento con locandina, programma e fotografie di chi ha partecipato; archivio `/eventi/<anno>/` e scheda `/eventi/<anno>/<slug>/` | `dati/eventi/` |
| `/opere/` | **7. Opere di non professionisti**: acquerelli di dilettanti, cioè di appassionati che non dipingono per mestiere, una sottosezione per autore (`7.1` sinmar, `/opere/<autore>/`) con la presentazione e le opere nell'ordine che l'autore sceglie; il titolo è la data in cui l'opera è stata dipinta, scritta sul foglio o, dove manca, la data della fotografia, con il numero del foglio quando c'è; sotto ogni acquerello, se l'autore lo chiede, uno o più brevi pareri dell'IA, ognuno col suo modello (per la 7.1 Claude Opus 5.5 e GPT-6 Astra); le opere restano dei rispettivi autori, fuori dalla licenza CC BY 4.0 | `dati/opere/` |
| `/informativa/` | Informativa sulla privacy: titolare, cookie, video di YouTube caricati al clic, chat e suggerimenti; collegata dal piè di pagina di ogni pagina | `scripts/genera-sito.py` |

## Organizzazione dei testi

### Riferimenti bibliografici

Il formato segue lo [studio sulle convenzioni italiane e sui riferimenti del Quaderno](ricerche/app-acquerello-261104-studio-riferimenti-bibliografici.md), acquisito con la PR #68. Il 4 novembre 2026 il curatore ha chiesto di applicarlo e di controllare tutte le fonti del sito. La revisione è nella [PR #69](https://github.com/sinmar123/app-acquerello/pull/69), la cui unione e pubblicazione sono state autorizzate dal curatore il 4 novembre 2026.

Si conservano i numeri nel testo e le «Fonti del capitolo». Le voci riportano autore o ente responsabile e titolo, quando disponibili. Le descrizioni sono in italiano: «Scheda del produttore», «Confronto di campioni», «Consultato soltanto il riassunto; testo integrale non letto». Non si usano classificazioni isolate come «primaria commerciale». I titoli delle opere restano nella lingua originale; una descrizione redazionale non diventa un titolo d’autore inventato.

Il titolo o la descrizione del documento apre la fonte nella stessa scheda, al posto di «apri». Nei riferimenti ai corsi non più disponibili, il collegamento identifica il video affine o il canale attuale e non viene attribuito al filmato originario. «Torna al testo» riporta al richiamo effettivamente seguito; senza JavaScript resta il primo richiamo della fonte nel capitolo. La barra fissa conserva il proprio calcolo dello spazio necessario sopra le ancore. Sono aumentati corpo e spaziatura delle fonti; titoli e DOI lunghi possono andare a capo.

Le fonti possono mantenere `testo` e indicare in `titolo_link` la porzione esatta da collegare. Nella pagina sul blu oltremare sono separati `autore`, `titolo`, `pubblicazione`, `url`, `nota`, `consultazione` e, quando presenti, `doi` e `limite`. La nota e il limite essenziale restano visibili; il dettaglio della lettura è apribile. `registro_precedente` conserva la registrazione originaria senza riproporne l’etichetta al lettore. La generazione si ferma se manca un campo necessario o il titolo da collegare non compare nel testo. Numeri, identificativi e rimandi esistenti restano stabili.

Il controllo riguarda anche gli indirizzi nei dati delle marche, degli eventi e nei cataloghi video. Una risposta negata, un limite di richieste o un mancato accesso automatico non dimostrano che la fonte sia inesistente e non autorizzano a cancellarla. Il controllo dei riferimenti non viene presentato come una nuova lettura scientifica integrale dei documenti. Il collaudo visivo su telefono resta da eseguire quando sarà disponibile un browser. Registrazione: OpenClaw / OC.

Le aperture presentano il contenuto della pagina; le note di metodo e i dettagli del modello di calcolo si possono aprire a parte. Nei Principi il capitolo 8 ha collegamenti ai propri argomenti. Nella Teoria dei colori, i concetti e gli esempi precedono la storia di Munsell e i dettagli matematici del calcolatore.

Negli Alberi, ogni modalità ha un titolo breve e una sintesi iniziale; l'infografica conserva le tre fasi. La descrizione estesa del metodo e i riquadri «Dal video, in sintesi» si possono aprire per approfondire. Le sintesi del parlato sono preparate con l'aiuto dell'IA, non sono trascrizioni. Video, tempi e cautele sui colori restano dichiarati.

Le Marche usano gli stessi rimandi numerati per capitolo delle altre guide. Le date di controllo restano nelle fonti e nelle righe delle tabelle. Nelle Opere, l'invito e le condizioni di pubblicazione sono separati dalla presentazione; la pagina dell'autore distingue «Come leggere le schede» dalla presentazione personale. I pareri dei modelli restano attribuiti e non vengono riscritti.

## Generare il sito in locale

Requisiti: Python 3.10+ e Pillow (`pip install -r scripts/requisiti.txt`). Dalla radice del repository:

```bash
python scripts/genera-sito.py
```

Lo script:
1. controlla che il menu della casella dei suggerimenti e le pagine del sito coincidano con gli elenchi che le funzioni del server accettano, e che i nomi delle marche non compaiano fuori dalla sezione Marche, salvo l'elenco delle fonti degli Approfondimenti;
2. rigenera la pagina di ogni sezione col suo generatore in `dati/<sezione>/`, che fa i controlli propri della sezione (fonti dei Principi e degli Approfondimenti, fonti e date delle Marche, coerenza della tavolozza, foto e date delle Opere);
3. la copia in `site/<sezione>/index.html` con la barra delle sezioni, la chat e la casella dei suggerimenti, e scrive la home, l'informativa sulla privacy, `robots.txt`, `sitemap.xml` e la favicon;
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

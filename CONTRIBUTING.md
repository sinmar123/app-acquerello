# Come contribuire al Quaderno di acquerello

Il **Quaderno di acquerello** (`https://app-acquerello.pages.dev`) è un progetto aperto: chiunque può segnalare correzioni, proporre nuovi esempi o contribuire con dati, infografiche e sezioni.

## 1. Segnalazioni e proposte, senza programmare

1. **Dal sito (`https://app-acquerello.pages.dev/#suggerimenti`):** in fondo a ogni pagina c'è la casella *«Suggerimenti: correzioni, integrazioni e video»*. Non richiede registrazione né un account GitHub e pubblica la segnalazione nell'elenco aperto delle Issue del progetto.
2. **Con una Issue su GitHub**, indicando:
   - **per un nuovo video o una nuova modalità di esercizio:** l'indirizzo del video YouTube, il minuto d'inizio e di fine del passaggio, i colori e i pennelli usati dall'autore e che cosa mostra il gesto;
   - **per una nuova serie nella sezione Marche e tubetti:** il nome della serie e, per ciascuno dei sei colori proposti, il collegamento alla pagina ufficiale del produttore da cui risultano nome commerciale, numero, pigmento (Colour Index) e trasparenza;
   - **per una correzione ai testi o alle ricette:** la sezione, il punto preciso e la fonte di riferimento.

## 2. Modifiche dirette con una pull request

1. Si fa un **fork** del repository e si crea un ramo dedicato (es. `feat/nuova-marca` o `fix/principi-carta`).
2. Si modificano i file sorgente in `dati/<sezione>/` (`.json`, `.csv`, `.py` o `.js`). **I file `.html` non si modificano mai**: li rigenerano gli script.
3. Si verifica la generazione del sito in locale:
   ```bash
   pip install -r scripts/requisiti.txt
   python scripts/genera-sito.py
   ```
   Il comando deve terminare senza errori e produrre le pagine in `site/`; se cambia `lib/prompt-chat.js`, va committato.
4. Si aggiunge una voce in cima a `CHANGELOG.md`, con la data e la descrizione della modifica.
5. Si apre una **pull request** verso `main`: il controllo automatico «costruisci» verifica che l'intero sito si generi senza errori.

## 3. Regole editoriali e di qualità

I generatori controllano la coerenza dei dati e fermano la generazione se una regola non è rispettata:

- **Ogni affermazione ha una fonte** nelle sezioni *Principi generali* (`dati/principi/principi.json`, ogni blocco rimanda a una fonte dell'elenco) e *Marche e tubetti* (`dati/marche/marche.json`, ogni tubetto ha il collegamento alla pagina ufficiale e la data di controllo). Non sono ammessi testi con la dicitura «da verificare».
- **Colori senza marche nelle guide:** in *Principi generali*, *Teoria dei colori*, *Soggetti* e *Alberi* i colori si indicano con il **nome comune e il codice del pigmento** (es. *terra di Siena bruciata (PR101)*, *blu oltremare (PB29)*). Marche e serie commerciali stanno solo in *Marche e tubetti*: `scripts/genera-sito.py` si ferma se ne trova il nome altrove.
- **Nessun fotogramma estratto dai video YouTube:** i passaggi sono spiegati con infografiche SVG in 3 fasi, accanto al lettore ufficiale di YouTube che apre il video al secondo indicato.
- **Nel sito non si usano immagini generate con l'IA** che imitano un acquerello o un dipinto; sono ammessi solo schemi, infografiche e figure disegnate.
- **Onestà del dato:** ciò che è stimato, provvisorio o da provare su carta lo resta anche nel testo; un riassunto non si presenta come citazione.
- **Registro dei testi**, scelto dal curatore il 21/10/2026: quello di un buon manuale tecnico, leggibile da un appassionato. Termini esatti della pittura ad acquerello, usati nel loro senso (campitura, velo, velatura solo per lo strato steso su un fondo asciutto, bagnato su bagnato, pennello scarico, risparmio del bianco); frasi compiute, di norma entro 25 parole; forma impersonale («si stende», «si lascia asciugare») o terza persona per l'autore di un video. Niente parlato, niente seconda persona nei testi delle guide, niente paroloni pseudo-scientifici («idrodinamico», «igrometrico», «cloruro di sodio» per il sale). `scripts/genera-sito.py` si ferma se l'indice di leggibilità Gulpease di una pagina scende sotto 52.
- **Lingua:** italiano, con gli accenti grafici corretti (`è`, `é`, `à`, `ò`, `ù`, `ì`) e senza trattino lungo.

## 4. Licenza dei contributi

Inviando un contributo a questo repository (tramite la casella pubblica sul sito, pull request, Issue o altra comunicazione), dichiari di avere il diritto di inviarlo e accetti che sia rilasciato con le licenze aperte del progetto indicate nel file [`LICENSE`](LICENSE): **MIT** per il codice sorgente, **CC BY 4.0** per i testi, i dati, le schede e le illustrazioni.

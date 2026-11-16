# Quaderno di acquerello con IA (`app-acquerello`)

Appunti di studio dell'acquerello aperti al pubblico: le tre consistenze della miscela e gli stati della carta, la teoria dei colori con un calcolatore di miscele, i tubetti marca per marca, gli esercizi guidati per soggetto con infografiche in tre fasi e passaggi dei video didattici indicati al secondo, gli approfondimenti documentati sulle questioni tecniche e storiche, gli eventi e le opere di appassionati.

Il Quaderno nasce dall'iniziativa personale di un appassionato (`sinmar`) che dipinge ad acquerello per diletto e sperimenta i modelli di intelligenza artificiale per raccogliere fonti, confrontare informazioni e costruire strumenti di studio verificabili. Il progetto è aperto alla collaborazione di altri appassionati, sia sui contenuti sia sullo sviluppo del sito, tramite la casella dei suggerimenti in fondo a ogni pagina o su GitHub.

- **Sito:** [https://app-acquerello.pages.dev](https://app-acquerello.pages.dev)
- **Repository:** [https://github.com/sinmar123/app-acquerello](https://github.com/sinmar123/app-acquerello)
- **Licenza:** [CC BY 4.0 per testi, dati e illustrazioni · MIT per il codice](LICENSE); le opere della sezione *Opere* restano dei rispettivi autori

## Sezioni del sito

| Percorso | Sezione | Sorgenti |
|----------|---------|----------|
| `/` | Presentazione («Perché questo Quaderno»), indice navigabile e organizzazione delle sezioni | `scripts/genera-sito.py` |
| `/principi/` | **1. Principi generali: acqua, colore e carta**: consistenze tè, latte e miele; carta bagnata, umida, asciutta e momenti intermedi; acqua nel pennello e nella carta; bordi, asciugatura e carte; nel capitolo 8, *In studio e all'aperto* (`#studio-aperto`), il confronto fra studio e plein air e la tavolozza ridotta di sei colori con le 12 miscele `M1`-`M12` (`#tavolozza-plein-air`); 42 fonti elencate per capitolo | `dati/principi/` |
| `/colori/` | **2. Teoria dei colori**: tinta, valore e croma secondo Munsell, sintesi additiva e sottrattiva, velature, tasselli dei sei colori di partenza e calcolatore di miscele Kubelka-Munk in JavaScript sulla tavolozza ridotta del capitolo 8 dei Principi, con strumento di taratura su carta vera (`dati/colori/taratura-campioni.py`); rimandi alle fonti paragrafo per paragrafo | `dati/colori/` |
| `/marche/` | **3. Marche e tubetti**: tubetti e pastiglie, serie da studio e professionali, lettura dell'etichetta, differenze di pigmento a parità di nome, schede di sei serie (Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu) e confronto finale sui sei colori della tavolozza ridotta, con pagina ufficiale e data di controllo su ogni riga | `dati/marche/` |
| `/soggetti/` | **4. Soggetti**: repertorio di esercizi per tema; pubblicati `S1 · Alberi` e `S6 · Paesaggio urbano`; in preparazione `S2 · Cieli e nuvole`, `S3 · Fiori`, `S4 · Acqua e riflessi` e `S5 · Rocce, montagne e terreni` | `dati/soggetti/` |
| `/alberi/` | **4.1 S1 · Alberi**: 6 esempi tipici di alberi, siepi e arbusti sviluppati in 25 modalità tratte dai video didattici, con proposte di colore per studio e plein air, 25 infografiche SVG in tre fasi e 32 estratti video caricati da YouTube solo al clic | `dati/alberi/` |
| `/urbano/` | **4.6 S6 · Paesaggio urbano**: 3 esempi architettonici (vicoli e scalinate, facciate al sole con ombre portate, strade bagnate e figure in scala) sviluppati in 6 modalità tratte dai video didattici, con proposte di colore per studio e plein air, 6 infografiche SVG in tre fasi e passaggi video tutti riproducibili nel lettore incorporato | `dati/urbano/` |
| `/approfondimenti/` | **5. Approfondimenti**: monografie documentate con sintesi iniziale, nota di metodo apribile e un unico elenco continuo delle fonti in fondo alla pagina: `5.1` *Il bianco nell'acquerello* (`/approfondimenti/bianco/`), `5.2` *Il blu e i blu nell'acquerello* (`/approfondimenti/blu/`, con capitoli dedicati all'oltremare PB29 e a Yves Klein, e rinvio da `/approfondimenti/blu-oltremare/`), `5.3` *Gli abbinamenti di Sanzo Wada nell'acquerello* (`/approfondimenti/sanzo-wada/`), `5.4` *Come nascono tinta, valore e croma* (`/approfondimenti/attributi-colore/`) e `5.5` *Rudolf Steiner e il colore* (`/approfondimenti/rudolf-steiner/`) | `dati/approfondimenti/` |
| `/eventi/` | **6. Eventi**: calendario di festival, mostre, demo e uscite en plein air, con locandina, programma ufficiale, fotografie dei partecipanti e archivio annuale (`/eventi/<anno>/<slug>/`) | `dati/eventi/` |
| `/opere/` | **7. Opere di non professionisti**: acquerelli di appassionati organizzati per autore (`7.1 sinmar`, `/opere/sinmar/`), con immagini prive di metadati EXIF/GPS e, su richiesta dell'autore, pareri tecnici apribili redatti da modelli di IA dichiarati | `dati/opere/` |
| `/informativa/` | Informativa sulla privacy: titolare (`sinmar`), assenza di cookie di profilazione, caricamento su richiesta dei video YouTube, funzionamento della chat e della casella suggerimenti | `scripts/genera-sito.py` |

## Organizzazione dei testi e dei riferimenti bibliografici

Le pagine didattiche si aprono con un sommario e una premessa; le note di metodo, le descrizioni estese dei procedimenti e i dettagli matematici del modello di calcolo si aprono a parte in blocchi `<details>` per non appesantire la lettura.

I riferimenti bibliografici mantengono i rimandi numerati nel testo:
- in *Principi generali*, *Teoria dei colori* e *Marche e tubetti* le fonti sono raccolte in fondo a ciascun capitolo;
- negli *Approfondimenti* tutte le fonti sono raccolte in un unico elenco finale per pagina, numerato nell'ordine della prima citazione, senza duplicazioni fra capitoli e con collegamento «Torna al testo» che riporta al punto effettivamente letto. Gli indirizzi dei riferimenti possono restare stabili anche quando l’inserimento di un capitolo cambia i numeri visibili.

Ogni voce riporta autore o ente responsabile e titolo originale quando disponibili, seguiti da una descrizione chiara in italiano («Scheda del produttore», «Confronto di campioni», «Consultato soltanto il riassunto; testo integrale non letto»). Le fonti nei JSON usano `testo` con `titolo_link` per la porzione cliccabile, oppure i campi strutturati `autore`, `titolo`, `pubblicazione`, `url`, `nota`, `consultazione`, `doi` e `limite` gestiti da `scripts/rimandi_fonti.py`.

## Generare il sito in locale

Requisiti: Python 3.10+ e Pillow (`pip install -r scripts/requisiti.txt`). Dalla radice del repository:

```bash
python scripts/genera-sito.py
```

Lo script:
1. controlla che il menu della casella dei suggerimenti e le pagine del sito coincidano con gli elenchi accettati dalle funzioni del server, e che nessun nome di marca commerciale compaia fuori da `dati/marche/` (salvo l'elenco bibliografico finale degli Approfondimenti);
2. rigenera la pagina di ogni sezione col rispettivo generatore in `dati/<sezione>/`, eseguendo i controlli di integrità su fonti, date, ancore, tavolozza, segmenti video e metadati delle fotografie;
3. compone `site/` aggiungendo barra di navigazione, assistente IA, casella dei suggerimenti, home page, informativa sulla privacy, `_redirects`, `robots.txt`, `sitemap.xml` e favicon;
4. aggiorna `lib/prompt-chat.js`, il prompt di sistema della chat ricavato automaticamente dai dati del sito;
5. misura la leggibilità di ogni pagina (indice Gulpease) e interrompe la generazione se una pagina scende sotto 52.

`site/` e i file HTML intermedi dentro `dati/` sono esclusi da Git (`.gitignore`); `lib/prompt-chat.js` viene invece tracciato perché è importato dalla funzione serverless della chat.

## Funzioni del server

Due funzioni Cloudflare Pages in `functions/api/`, appoggiate al database D1 `app-acquerello` (`wrangler.toml`):

- `chat.js`: assistente sull'acquerello basato su **Gemini 4 Argon** (`gemini-4-argon`), istruito con `lib/prompt-chat.js`. Non chiede l'email e non archivia domande né risposte; applica un limite di 5 domande a settimana per connessione e 10 al giorno complessive, contate su D1 tramite impronta crittografica dell'IP cancellata entro 14 giorni, e verifica con firma HMAC la cronologia restituita dal browser. Segreti: `GEMINI_API_KEY` (obbligatorio), `SALE_IP` e `CHIAVE_FIRMA` (facoltativi).
- `suggerimento.js`: apre una Issue pubblica etichettata `suggerimento-dal-sito` sul repository tramite `GITHUB_SUGGERIMENTI_TOKEN`. Accetta solo le sezioni e pagine valide del sito, oscura eventuali indirizzi email, neutralizza le menzioni `@utente` e applica un limite di 5 invii al giorno per connessione e 30 complessivi sulla stessa tabella D1.

## Controllo automatico e pubblicazione

Su GitHub il workflow `.github/workflows/sito.yml` esegue il controllo «costruisci» su ogni pull request e su `main`, verificando che tutte le sezioni compilino senza errori e che `lib/prompt-chat.js` sia allineato ai sorgenti. All'unione su `main`, il job «pubblica» aggiorna automaticamente il sito su Cloudflare Pages. Da locale la pubblicazione avviene con `npm run deploy` (`scripts/pubblica-locale.py`), che consente l'invio solo da `main` pulito e allineato a GitHub.

## Come contribuire

[`CONTRIBUTING.md`](CONTRIBUTING.md) raccoglie le regole editoriali (fonti obbligatorie, indicazione dei colori tramite nome comune e codice Colour Index, assenza di fotogrammi estratti dai video o dipinti generati con IA, registro tecnico leggibile) e le istruzioni per inviare segnalazioni o pull request. Le indicazioni operative per gli agenti di codifica sono in [`AGENTS.md`](AGENTS.md) e [`CLAUDE.md`](CLAUDE.md).

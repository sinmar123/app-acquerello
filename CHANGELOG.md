# CHANGELOG - app-acquerello

Cronologia delle modifiche. Ordine cronologico inverso.

## 2026-10-28 - CC - Opere: testi riscritti con il tono di una piccola mostra

- Richiesta di Sandro del 28/10/2026: lo stile dei testi della sezione lasciava a desiderare. Riscritti con il tono adatto a una raccolta di acquerelli, invece del registro da manuale tecnico delle guide; i fatti restano quelli dati da Sandro.
- **Sezione** (`sezione.json`): sottotitolo, anche in home, «Acquerelli di chi dipinge per passione, raccolti autore per autore». Presentazione: «Questa sezione raccoglie gli acquerelli di chi dipinge per passione. Ogni autore ha la sua pagina, con i fogli in ordine di tempo, dal più recente al primo: scorrendola si vede come è cambiata la mano. Chi desidera esporre qui i propri acquerelli può proporlo dalla casella dei suggerimenti, in fondo alla pagina.» L'elenco si intitola «Gli autori», il collegamento dice «Guarda gli acquerelli».
- **Pagina 6.1** (`autori/alessandro-sanvitale.json`): «Alessandro Sanvitale dipinge ad acquerello per passione dal 27 settembre 2021: il primo foglio, dipinto quel giorno, chiude la pagina. Dal 2021 al 2024 ha frequentato i corsi di Irene Tamagnone, e oggi segue con lei il corso avanzato dedicato al paesaggio.» Segue un paragrafo su come leggere titoli e date, che nomina la sezione. Esce la frase «Questa sottosezione fa parte della sezione...»: la collocazione la danno il rimando «6. Opere di non professionisti» in cima alla pagina e il numero 6.1 nel titolo.
- Il conteggio, in pagina e in home, diventa «14 acquerelli dipinti fra il 2021 e il 2024». Il piè di pagina dice «Gli acquerelli appartengono ai loro autori e sono esclusi dalla licenza CC BY 4.0 del Quaderno.»
- Controlli: `python scripts/genera-sito.py` senza errori; Gulpease della pagina 6.1 a 91, le altre invariate; le due pagine viste in Chrome.
- Prossima azione: Sandro indica la data scritta sul foglio n. 107 e conferma il n. 124 e la licenza delle opere; poi il via del curatore. L'unione su `main` pubblica il sito.

-- CC

## 2026-10-28 - CC - Opere: Alessandro Sanvitale diventa la sottosezione 6.1, con la presentazione

- Richiesta di Sandro del 28/10/2026: la sezione deve dire che raccoglie opere di non professionisti, e la sua pagina ne è una sottosezione. Nella presentazione: ha iniziato ad acquerello il 27 settembre 2021, ha seguito i corsi di Irene Tamagnone dal 2021 al 2024 e ora segue con lei un corso avanzato di acquerello sul paesaggio.
- **Sottosezioni**: ogni autore ha un `ordine` nel suo JSON e diventa la sottosezione 6.1, 6.2 e così via. La pagina dell'autore si apre con «6. Opere di non professionisti» e il titolo «6.1 · Alessandro Sanvitale». Nell'elenco della sezione e in home l'autore compare col suo numero; in home la scheda sta rientrata sotto la 6, come «4.1 Alberi» sotto i Soggetti. La barra in cima resta con la sola voce «6 Opere». `scripts/genera-sito.py` si ferma se il numero della sezione in `dati/opere/sezione.json` non è quello di `SEZIONI`.
- **Testi** (`sezione.json`): l'introduzione della sezione è una breve presentazione in tre frasi, seguita dal collegamento alla pagina di ogni autore («Vedi le opere»): «Questa sezione raccoglie opere di non professionisti: acquerelli di appassionati che non dipingono per mestiere. Ogni autore ha una sottosezione con le sue opere, dalla più recente. Chi vuole proporre le proprie opere può scriverlo nella casella dei suggerimenti in fondo alla pagina.» Le regole su titoli, date e numeri restano solo nella pagina dell'autore, che si apre con «Questa sottosezione fa parte della sezione Opere di non professionisti: acquerelli di appassionati che non dipingono per mestiere.» Il sottotitolo dice «una sottosezione per autore».
- **Presentazione** (`autori/alessandro-sanvitale.json`): «Alessandro Sanvitale ha iniziato a dipingere ad acquerello il 27 settembre 2021: il primo acquerello, di quel giorno, è l'ultimo della pagina. Dal 2021 al 2024 ha seguito i corsi di acquerello di Irene Tamagnone, e attualmente segue con lei un corso avanzato di acquerello sul paesaggio.» Il nome della docente è scritto come nei file del corso. Su indicazione di Sandro la presentazione non dice che cura il sito, che in futuro sarà curato da molti; lo stesso nel README.
- **Primo acquerello**: l'opera del 27/9/2021 (foto delle 22.03) porta sotto il titolo la nota «il primo acquerello», nel campo nuovo `nota`. La data coincide con quella che Sandro indica come inizio.
- **Chat**: il prompt elenca gli autori col numero di sottosezione.
- Controlli: `python scripts/genera-sito.py` senza errori. Gulpease: sottosezione 6.1 90, le altre pagine invariate; la pagina della sezione resta sotto le 100 parole, quindi l'indice non si calcola. Pagine e home viste in Chrome: intestazione con la sezione e la sottosezione, scheda 6.1 rientrata in home.
- Prossima azione: Sandro indica la data scritta sul foglio n. 107 e conferma il n. 124 e la licenza delle opere; poi il via del curatore. L'unione su `main` pubblica il sito.

-- CC

## 2026-10-27 - CC - Nuova sezione 6. Opere di non professionisti, con gli acquerelli di Alessandro Sanvitale

- Richiesta di Sandro del 27/10/2026: una sezione per le opere di non professionisti, a cominciare dalle sue, con le 14 foto che ha raccolto. Come titolo la data, con il giorno della settimana e l'ora quando si trovano, e il numero che lui scrive sul foglio.
- **Sezione** (`dati/opere/`): `sezione.json` con i testi, un JSON per autore in `autori/` (per ora `alessandro-sanvitale.json`), le foto in `immagini/alessandro-sanvitale/` e `genera-opere.py` (comando `pagina`). Il generatore scrive l'elenco degli autori, `/opere/`, e una pagina per autore, `/opere/alessandro-sanvitale/`, con le opere dalla più recente in una griglia; un clic apre la foto a grandezza piena.
- **Titoli e date**. Il titolo è la data in cui l'acquerello è stato dipinto, con il giorno della settimana calcolato dal generatore e l'ora quando è nota. Su cinque fogli c'è una scritta a mano nel margine, letta sulla foto ingrandita:
  - n. 104: «17-1-23 lezione 12ª / 24-1-23 lez. 13ª», due sedute, martedì 17 e martedì 24 gennaio 2023;
  - n. 114: «15-2-23 Mercoledì ore 21-22, 16-2-23 giovedì ore 21-», due sedute; i giorni scritti coincidono con le date;
  - n. 117: «4-3-23 Sabato», sabato 4 marzo 2023; la foto è del giorno dopo;
  - n. 124: il numero senza data, con il 4 scritto sopra un 3; titolo dalla data della foto;
  - n. 107: il numero si legge, la data no, perché la riga è tagliata dal bordo della foto. Per ora il titolo è la data della foto, lunedì 27 febbraio 2023 alle 21.45; se la numerazione segue l'ordine di lavoro, il foglio è fra il 24 gennaio e il 15 febbraio 2023.
- Gli altri nove fogli non hanno scritte nei margini visibili. Il titolo viene dalla data e dall'ora di scatto (dati EXIF); per l'immagine arrivata da WhatsApp, dalla data nel nome del file, senza ora. Sotto questi titoli la pagina scrive «data della fotografia».
- **Foto**: `prepara-foto.py <cartella> <id-autore>` le raddrizza, porta il lato lungo a 1600 pixel e le salva senza dati EXIF, quindi senza la posizione GPS che cinque originali contenevano. 14 file, 5,6 MB in tutto. Gli originali restano fuori dal repository.
- **Diritti**: le opere restano dei rispettivi autori e non rientrano nella licenza CC BY 4.0. Riga nuova in `LICENSE` § 2, eccezione in `CONTRIBUTING.md` § 4, nota in fondo alle pagine della sezione.
- **Sito**: la sezione entra in `SEZIONI` di `scripts/genera-sito.py` col numero 6, quindi nella barra e in home, con una figura disegnata (un foglio dipinto sul cavalletto). «Opere» entra nel menu della casella dei suggerimenti e in `SEZIONI_VALIDE` di `functions/api/suggerimento.js`; `/opere/` negli elenchi `PAGINE_VALIDE` delle due funzioni. La chat riceve gli autori, il numero delle opere e gli anni, con l'istruzione di non descrivere né giudicare le opere, che non vede.
- **Documenti**: `README.md` (tabella delle sezioni e licenza), `AGENTS.md`, `CONTRIBUTING.md` (§ 1 come proporre le proprie opere, § 3 regole della sezione, § 4 diritti).
- Controlli: `python scripts/genera-sito.py` senza errori, compreso il controllo sui nomi di marca. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 80, Opere 74, pagina di Alessandro Sanvitale 102. Pagine provate in Chrome a 1280 pixel e, dentro un riquadro, a 360 e 390 pixel: griglia a tre colonne sul computer e a una sul telefono, nessuno scorrimento di lato. Le 14 foto rispondono e ognuna sta sotto il suo titolo. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- 28/10/2026: unito nel ramo `main` con le #48 e #49; conflitti solo in README, CHANGELOG e nel prompt generato, risolti tenendo le due parti. Rigenerato senza errori; il piè di pagina delle Opere porta anche il collegamento all'informativa sulla privacy, che le pagine della sezione rispettano (nessun cookie, nessuno script o carattere di altri siti). Gulpease invariati, Informativa 64.
- Prossima azione: Sandro indica la data scritta sul foglio n. 107 e conferma il n. 124; poi il via del curatore. L'unione su `main` pubblica il sito.

-- CC

## 2026-10-27 - GBOT-app-acquerello - Alberi: sesta modalità per le chiome tonde, il tondo caricato chiaro e scuro (Christopher Stephen)

- Richiesta di Sandro del 27/10/2026: aggiungere la terza tecnica del video di Christopher Stephen «Three Watercolour Tree Techniques YOU NEED TO KNOW !!!» (`TPU6woga-6M`) come nuova modalità di A3. Le prime due tecniche del video, bagnato su bagnato e spugna naturale, in A3 ci sono già.
- **Modalità A3-M6** (`dati/alberi/pit-261014-video-gesti-alberi.json`): titolo, proposta, colori e pennelli presi solo dalla trascrizione automatica in inglese, coi colori come li nomina l'autore (giallo di cadmio, terra di Siena naturale, blu, terra di Siena bruciata). L'autore non dice il numero dei pennelli e non precisa il blu: la scheda non li aggiunge. Manca, rispetto alle altre schede, la corrispondenza coi 6 colori proposti, che resta da decidere. La descrizione di A3 passa da cinque a sei modalità.
- **Estratto A3-6** (`pit-261013-video-gesti-segmenti.csv`): da 10:52 a 14:11, 199 secondi, dall'acqua con lo spruzzino fino all'ombra del tronco. I secondi vengono dalle parole della trascrizione e vanno rifiniti guardando il video. Il video entra in `pit-261013-alberi-selezione-video.csv` sotto V11 con durata 973 secondi e anno 2026 letti dai metadati pubblici di YouTube; visualizzazioni e iscritti restano vuoti.
- **Infografica A3-M6** (`pit-261015-infografiche.py`): tre fasi, le due pozze e il tondo caricato sui due lati, il pennello ruotato fra chiaro e scuro, tronco e rami. Nuovo campione `blu`, senza altro nome, perché l'autore dice solo «blue».
- **Conteggi**: 25 modalità da 24 video, 32 estratti, 25 infografiche, nella pagina, in home, nella scheda dei Soggetti, nel prompt della chat, nel README e in AGENTS. Il piè della pagina Alberi ora conta le infografiche dai dati.
- Controlli: `python scripts/genera-sito.py` senza errori. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 80. Prova nel browser: la scheda A3-M6 mostra le tre fasi e il lettore; nessuna richiesta verso altri siti prima del clic.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-27 - GBOT-app-acquerello - Video degli Alberi caricati solo al clic e informativa sulla privacy

- Richiesta di Sandro del 27/10/2026: nessun contatto con YouTube o Google finché chi visita non sceglie di guardare un video, e una breve informativa sulla privacy collegata dal piè di pagina.
- **Riquadro prima del video** (`dati/alberi/pit-261013-video-gesti.py`): al posto del pulsante «Guarda il gesto» ogni estratto mostra un riquadro del sito, senza miniature di YouTube, col titolo del passaggio, la durata, i minuti, il titolo del video e l'autore. Sotto, la frase «Il video è ospitato su YouTube: aprendolo, YouTube (Google) riceverà alcuni dati della tua visita.» e i collegamenti all'informativa del sito, alla privacy di Google e ai Termini di YouTube. Il pulsante «Guarda il video» crea il lettore ufficiale con gli stessi punti di inizio e di fine.
- **Lettore**: già prima lo script di YouTube si caricava solo al clic; ora la regola è scritta nel codice e spiegata in pagina. Comandi del lettore visibili (`controls: 1`), partenza automatica solo dopo il clic, spazio del lettore di almeno 200 × 200 pixel anche sui telefoni stretti. Il Referer resta quello della pagina (`strict-origin-when-cross-origin`, come nell'intestazione già inviata da Cloudflare). Nessuna libreria esterna. Il file `_headers` non c'è nel repository e non serve aggiungerlo.
- **Informativa** (`/informativa/`, scritta da `scripts/genera-sito.py`): titolare e contatto come nella nota della chat, senza indirizzo né telefono; nessun cookie proprio, nessuno strumento di statistica o di tracciamento, nessun carattere o script di altri siti, verificato nel codice e nelle pagine pubblicate; i video caricati solo al clic, poi valgono l'informativa di Google e i Termini di YouTube; due righe su chat e suggerimenti con rinvio alle loro note. La pagina entra nella `sitemap.xml`; non entra nel menu della casella dei suggerimenti né negli elenchi `PAGINE_VALIDE`, perché non ha i riquadri della chat.
- **Piè di pagina**: in home e in ogni pagina delle sezioni c'è il collegamento «Informativa sulla privacy».
- Controlli: `python scripts/genera-sito.py` senza errori. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 73, Eventi 95, scheda Sestri Levante 80, Informativa 64. Prova in un browser con schermo da telefono (360 pixel): prima del clic nessuna richiesta verso altri siti; dopo il clic il lettore parte da 02:30 nel primo estratto, coi comandi, alto 200 pixel.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-25 - GBOT-app-acquerello - Home: tolta la fila dei sei colori proposti

- Decisione di Sandro del 25/10/2026: in home la fila dei campioni dei sei colori proposti, sotto la testata e senza didascalia, non serve più.
- **Generatore** (`scripts/genera-sito.py`): escono le funzioni `striscia_tavolozza()` e `colori_tavolozza()`, usate solo dalla home, il blocco `<section class="tavolozza">` sotto la testata e le regole CSS che servivano solo a quel blocco (`.tavolozza`, `.goccia`, `.m-pig`, anche nella versione per schermi stretti). La home passa dalla testata direttamente alla nota di metodo. Nessun file immagine tolto: la fila era disegnata in CSS dai valori di `dati/colori/tavolozza.json`, che resta e serve alle altre pagine.
- La sezione Teoria dei colori (`/colori/`) non cambia: le schede dei sei colori restano dove sono. Restano anche i sottotitoli delle schede in home che nominano i sei colori, perché descrivono le sezioni.
- Controlli: `python scripts/genera-sito.py` senza errori. In home non restano titoletti, spazi vuoti o classi della fila. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-25 - GBOT-app-acquerello - Sestri Levante: locandina del festival e foto del 24 e 25 ottobre

- Richiesta di Sandro del 25/10/2026: altre foto sulla scheda di Watercolor Sestri Levante, la demo di Cesc Farré per prima nella giornata del 24/10 e la locandina del festival al posto di «locandina da aggiungere». Foto di Alessandro Sanvitale, ore di Europa/Roma dai dati delle foto.
- **Locandina** (`locandina` in `schede/watercolor-sestri-levante-2026.json`, file `wsl-2026-locandina.jpg`): la copertina del programma «Programma 23-24-25 ottobre, Watercolor Sestri Levante 2026», col refuso della copertina lasciato com'è. Didascalia: «Locandina del festival, copertina del programma. Il dipinto è un acquerello di Felice Feltracco». Rimando al programma ufficiale.
- **Foto accanto al programma**, sette nuove (`wsl-2026-sandro-05.jpg`-`11.jpg`):
  - `s24-farre`: Cesc Farré, demo in Sala Agave, 24/10/2026 alle 10.54. Ora la giornata del 24 si apre con Farré, prima di Igli Arapi.
  - `d25-feltracco`: Felice Feltracco, demo in sala, 25/10/2026 alle 10.48.
  - `d25-fracasso`: Pasqualino Fracasso, en plein air in piazza, alle 11.56.
  - `d25-premiazione`: premiazione del concorso «Fermo Immagine» alle 12.20, la sala con le opere selezionate alle 12.26 e alle 12.30, la locandina del concorso alle 12.30.
- **Foto di Farré già in scheda** (`farre-sestri-2026-sandro.jpg`): era un'altra inquadratura della stessa demo, senza ora nei dati, e compariva solo nella sezione Fotografie. Su decisione di Sandro esce dalla scheda e il file esce dal repo. Nessun'altra pagina la usava. Le voci più vecchie del CHANGELOG che la citano restano come storia.
- **Foto 09** (`wsl-2026-sandro-09.jpg`, la sala con le opere selezionate, alle 12.26): su decisione di Sandro è sostituita da un altro suo scatto della stessa sala, del 25/10/2026 alle 12.26. Didascalia e ora restano le stesse. La foto 10 resta com'è.
- **Generatore**: `genera-eventi.py` accetta una `didascalia` facoltativa per la locandina, scritta prima del credito; l'elenco delle foto legate nella sezione Fotografie segue l'ordine del programma, non più la sola ora (prima le foto del 25 mattina finivano tra quelle del 24). `scripts/genera-sito.py` passa la didascalia della locandina alla chat.
- Immagini raddrizzate secondo l'orientamento delle foto originali, lato lungo 1600 pixel, senza dati EXIF e quindi senza posizione GPS, come le foto già in scheda.
- Controlli: `python scripts/genera-sito.py` senza errori, compreso il controllo sui nomi di marca. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 80. La scheda mostra la locandina e le foto nell'ordine del programma. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-25 - GBOT-app-acquerello - Sestri Levante: tolto il profilo su X

- Decisione di Sandro del 25/10/2026: nel riquadro «L'evento sui social» della scheda di Watercolor Sestri Levante il link al suo profilo non serve. Il riquadro resta solo su questa scheda.
- **Dati** (`social` in `schede/watercolor-sestri-levante-2026.json`): esce la voce «Profilo di Alessandro Sanvitale su X» (`https://x.com/alessandro_snv`). Restano i tre post: «Demo di Cesc Farré, post del 24/10/2026», «Riassunto della giornata e quattro foto, post del 24/10/2026» e «Demo di Felice Feltracco, post del 25/10/2026».
- **Generatore**: `genera-eventi.py` e `scripts/genera-sito.py` copiano i link del campo `social` e non aggiungono il profilo da soli. In `README.md`, `AGENTS.md` e `CONTRIBUTING.md` il riquadro è descritto in generale, senza quella voce. Le voci già scritte nel CHANGELOG restano come storia.
- **Chat**: `lib/prompt-chat.js` elenca i tre post, solo per la scheda, e non il profilo.
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso il controllo sui nomi di marca. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 83. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. La scheda mostra i tre post e non il profilo. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-25 - GBOT-app-acquerello - Sestri Levante: post sulla demo di Felice Feltracco

- Nel riquadro «L'evento sui social» della scheda di Watercolor Sestri Levante entra il post di Alessandro Sanvitale del 25/10/2026 sulla demo di Felice Feltracco. Il riquadro resta solo su questa scheda.
- **Dati** (`social` in `schede/watercolor-sestri-levante-2026.json`): si aggiunge il link «Demo di Felice Feltracco, post del 25/10/2026», indirizzo `https://x.com/alessandro_snv/status/2114283557317194149`. Stesso formato degli altri: ancora testuale, `target="_blank"` e `rel="noopener"`. I tre link già in scheda restano (profilo su X e due post del 24/10). Il riquadro ne mostra quattro.
- **Chat**: `lib/prompt-chat.js` elenca anche questo link, solo per la scheda.
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso il controllo sui nomi di marca. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 83. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-25 - GBOT-app-acquerello - Nota di metodo: il sito è in costruzione

- Richiesta di Sandro: la nota di metodo si apre dicendo che il sito è in costruzione. Dove il testo parla del sito (che cosa contiene, come è ordinato), «Quaderno» diventa «sito». Il nome nel titolo e nella testata resta «Quaderno di acquerello». La nota sopra la nota di metodo resta com'è, e così il riquadro «Il Quaderno è in costruzione».
- **Nota di metodo** (`genera_home` in `scripts/genera-sito.py`). In apertura, la frase «Il sito è in costruzione.» Poi il testo di prima, con una sostituzione:
  - «Il Quaderno nasce» diventa «Il sito nasce».
- Testo prima: «Chi oggi apprende una disciplina pratica dispone di una documentazione vastissima, distribuita tra manuali, schede tecniche e centinaia di ore di dimostrazioni filmate; la vera difficoltà sta nel ricondurre una materia tanto dispersa a un criterio ordinato e consultabile mentre si lavora. Gli strumenti di intelligenza artificiale permettono di compiere a monte questo lavoro di spoglio, confronto e classificazione, così da aiutare a esercitarsi con più consapevolezza. Il Quaderno nasce dall'applicazione di tale approccio allo studio dell'acquerello: ordina il comportamento di acqua, carta e pigmenti, indica al secondo le sequenze esecutive nei video didattici e affianca al tavolo da lavoro strumenti di riscontro, dal calcolatore colorimetrico all'assistente tecnico integrato nelle pagine.»
- Testo dopo: «Il sito è in costruzione. Chi oggi apprende una disciplina pratica dispone di una documentazione vastissima, distribuita tra manuali, schede tecniche e centinaia di ore di dimostrazioni filmate; la vera difficoltà sta nel ricondurre una materia tanto dispersa a un criterio ordinato e consultabile mentre si lavora. Gli strumenti di intelligenza artificiale permettono di compiere a monte questo lavoro di spoglio, confronto e classificazione, così da aiutare a esercitarsi con più consapevolezza. Il sito nasce dall'applicazione di tale approccio allo studio dell'acquerello: ordina il comportamento di acqua, carta e pigmenti, indica al secondo le sequenze esecutive nei video didattici e affianca al tavolo da lavoro strumenti di riscontro, dal calcolatore colorimetrico all'assistente tecnico integrato nelle pagine.»
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso `controlla_marche_fuori_sezione`. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 83. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. La home è a Gulpease 53. `lib/prompt-chat.js` invariato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - Home: non professionisti, al posto di dilettanti

- Correzione di Sandro sulla nota in home: «dilettante» e «dilettanti» diventano «non professionista» e «non professionisti». Il 25/10/2026 Sandro fissa il testo definitivo. La nota di metodo resta.
- **Nota** (`genera_home`): «Questo sito è sviluppato da non professionisti e si rivolge a chi condivide la stessa passione. Raccoglie ciò che si impara strada facendo, con i limiti di chi non è un maestro, ed è aperto ai contributi di tutti gli appassionati. Anche i professionisti che vi trovassero qualcosa di utile, o volessero aiutarci a migliorarlo, saranno i benvenuti.»
- **Descrizione per i motori di ricerca** (`DESCRIZIONE_HOME`, anche `og:description`) e **README**: in apertura, «Questo sito è sviluppato da non professionisti e si rivolge a chi condivide la stessa passione.»
- Cercate le occorrenze entrate con le due modifiche della home. Sostituite in `scripts/genera-sito.py` (nota e descrizione) e in `README.md`. In `lib/prompt-chat.js`, `CONTRIBUTING.md` e `AGENTS.md` non ce n'erano. Le voci già scritte nel CHANGELOG restano come storia.
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso `controlla_marche_fuori_sezione`. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 83. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. La home resta a Gulpease 52. `lib/prompt-chat.js` invariato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - Home: Quaderno aperto ai contributi

- Richiesta di Sandro: la nota sotto l'introduzione non deve suonare come il quaderno di una sola persona. Il sito è aperto ad altri contributi. La nota di metodo segue lo stesso tono, da appassionati che imparano, non da esperti.
- **Nota** (`genera_home` in `scripts/genera-sito.py`): «Il Quaderno nasce tra dilettanti ed è rivolto ad altri dilettanti. Raccoglie ciò che si impara strada facendo, con i limiti di chi non è un maestro, ed è aperto ai contributi di tutti gli appassionati.» I sei campioni, le schede delle sezioni e l'informativa restano com'erano.
- **Descrizione per i motori di ricerca** (`DESCRIZIONE_HOME`): in apertura, «Il Quaderno nasce tra dilettanti ed è rivolto ad altri dilettanti.» Il resto della descrizione resta.
- **README**: la riga di apertura, nello stesso senso.
- **Nota di metodo**, stessi fatti (video indicati al secondo, calcolatore colorimetrico, assistente nelle pagine, limite di 5 domande a settimana nell'elenco). Frasi ritoccate, prima e dopo:
  - «restituendo al momento opportuno il dato che serve per guidare la mano ed esercitarsi con maggiore sicurezza» diventa «così da aiutare a esercitarsi con più consapevolezza».
  - «Questo quaderno» diventa «Il Quaderno».
  - «sistematizza il comportamento di acqua, carta e pigmenti, scompone e indicizza al secondo le sequenze esecutive nei video didattici» diventa «ordina il comportamento di acqua, carta e pigmenti, indica al secondo le sequenze esecutive nei video didattici».
  - «strumenti di riscontro immediato» diventa «strumenti di riscontro».
- **Elenco** di ciò che il Quaderno mette a disposizione: la voce «una casella per proporre correzioni, integrazioni e nuovi video» non si ripete. In fondo all'elenco, la frase «Chiunque può proporre correzioni, integrazioni e video dalla casella dei suggerimenti: il Quaderno è aperto ai contributi di tutti gli appassionati.» Il collegamento porta alla casella già in pagina.
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso `controlla_marche_fuori_sezione`. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 83. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. La home resta a Gulpease 52, come prima del ritocco (soglia 52). `lib/prompt-chat.js` invariato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - Riquadro social in fondo alla scheda di Sestri Levante

- Richiesta di Sandro: in fondo alla sola scheda di Watercolor Sestri Levante, un riquadro di link testuali. Non entra nel piè di pagina del sito, né nel calendario, né nell'archivio, né nelle altre sezioni.
- **Dati** (`social` in `schede/watercolor-sestri-levante-2026.json`): titolo e tre link https. Il campo è generico: senza `social` la scheda non ha il riquadro. Il generatore si ferma se manca il titolo, se un link non è https o se un indirizzo è ripetuto.
- **Testo del riquadro**: «L'evento sui social». I link: «Profilo di Alessandro Sanvitale su X»; «Demo di Cesc Farré, post del 24/10/2026»; «Riassunto della giornata e quattro foto, post del 24/10/2026». Sono ancore, con `target="_blank"` e `rel="noopener"`, come gli altri link esterni del sito. Niente widget, embed, script o immagini esterne.
- **Chat**: il prompt elenca questi link solo per la scheda che li ha, e chiede di non inventarne altri.
- **Documenti**: una frase in `AGENTS.md` e in `CONTRIBUTING.md`.
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso il controllo sui nomi di marca. Gulpease invariato: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 83. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - Quattro foto di Sestri Levante accanto al programma

- Quattro fotografie di Alessandro Sanvitale, sabato 24/10/2026, entrano nella scheda di Watercolor Sestri Levante (`schede/watercolor-sestri-levante-2026.json`, file `immagini/wsl-2026-sandro-01.jpg` … `04.jpg`). Credito di tutte: «foto di Alessandro Sanvitale», come per lo scatto di Cesc Farré, che resta nella sezione Fotografie.
- **Accanto alla voce** (`genera-eventi.py`): una foto con `momento` e `ora` (formato 11.57) compare sotto quella voce del programma. In Fotografie l'elenco segue l'orario dello scatto e rimanda alla voce. Senza `momento`, la foto resta solo in Fotografie. Il generatore si ferma se il momento non è una voce o se l'ora non è valida.
- **Didascalie**, uguali al testo alternativo:
  - 11.57, accanto alla voce delle 11.00: «Igli Arapi, en plein air in spiaggia, sulla Baia delle Favole, il 24/10/2026 alle 11.57. Il promontorio con il leudo in primo piano».
  - 15.29, Barnaba Salvador: «Barnaba Salvador, en plein air in Via XXV Aprile e Via della Chiusa, il 24/10/2026 alle 15.29».
  - 15.39, Roberto Zangarelli: «Il tavolo della demo di Roberto Zangarelli in Sala Agave, il 24/10/2026 alle 15.39».
  - 16.44, Massimiliano Iocco: «Massimiliano Iocco, en plein air, vista sul mare dal cavalletto, il 24/10/2026 alle 16.44».
- **Nota sul cambio di programma**, accanto alla voce di sabato «Alle 11.00. En plein air: Franco Pretti», senza riscrivere la voce copiata dalla fonte: «Il programma ufficiale indica Franco Pretti alle 11.00. Rispetto a quella voce, il 24/10 alle 11.30, dopo Cesc Farré, in spiaggia, sulla Baia delle Favole, ha dipinto Igli Arapi.» La demo di Igli Arapi del venerdì 23/10, dalle 12.30 alle 13.30, resta com'è: la foto non è di quella demo.
- **Nomi e luoghi**. Salvador, Zangarelli e Iocco coincidono con le voci del programma. Sala Agave coincide con il luogo dell'evento. Il programma ufficiale non nomina la Baia delle Favole, il leudo, Via XXV Aprile, Via della Chiusa né la vista sul mare: queste indicazioni stanno solo nelle didascalie, dai dati delle foto, e non contraddicono una voce che non indica un altro luogo. Gli orari degli scatti sono successivi all'inizio della voce. Quello di Zangarelli cade nella fascia 15.00-16.00.
- **Chat** (`scripts/genera-sito.py`): il prompt riporta anche la nota di una voce, così non resta solo il testo del programma ufficiale. Vale anche per la grafia di Yana Wihlem e per la premiazione senza orario di fine.
- **Documenti**: una frase in `AGENTS.md` e in `CONTRIBUTING.md` sul posto della foto accanto alla voce.
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso il controllo sui nomi di marca. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 83. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - Home: quaderno di un dilettante per dilettanti

- Richiesta di Sandro: precisare in home, con registro curato, che il Quaderno è di un dilettante e si rivolge ad altri dilettanti. Raccoglie ciò che si impara strada facendo, con i limiti di chi non è un maestro, e si offre come un aiuto tra appassionati.
- **Home** (`genera_home` in `scripts/genera-sito.py`): sotto l'introduzione della testata, due frasi compiute, nello stesso tono della pagina. La fila dei sei campioni, le schede delle sezioni e la nota di metodo restano com'erano. Testo: «Questo è il quaderno di un dilettante, rivolto ad altri dilettanti. Raccoglie ciò che si impara strada facendo, con i limiti di chi non è un maestro, e si offre come un aiuto tra appassionati.»
- **Descrizione per i motori di ricerca** (`DESCRIZIONE_HOME`): in apertura, «Quaderno di un dilettante, rivolto ad altri dilettanti.» Il resto della descrizione resta.
- **README**: una riga in apertura, nello stesso senso.
- Controlli: `python3 scripts/genera-sito.py` senza errori, compreso `controlla_marche_fuori_sezione`. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 93. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. `lib/prompt-chat.js` invariato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - Eventi: solo locandina, programma e foto

- Decisione di Sandro, a sezione già in linea: ogni scheda tiene solo la locandina, il programma e le fotografie di chi ha partecipato. Ogni foto porta il nome di chi l'ha scattata. Calendario e archivio per anno restano l'elenco degli eventi.
- **Tolto dalle pagine** (`genera-eventi.py`, `sezione.json`, `schede/watercolor-sestri-levante-2026.json`, `scripts/genera-sito.py`): interviste e `domande.json`, racconti «io c'ero», segni coperto o non coperto sul programma, schede demo (soggetto, tecnica, carte, colori, lezione, collegamenti) e il riquadro dei contributi. La foto di Cesc Farré resta fra le fotografie, con credito «foto di Alessandro Sanvitale» e didascalia «Cesc Farré, demo del 24/10/2026». Escono il testo «less is more» e il racconto.
- **Locandina di Sestri Levante**: il 24/10/2026 il catalogo `wp-json` di `https://watercolorsestrilevante.it` non ha un file il cui titolo o la cui didascalia dica locandina. La pagina offre «Scarica il programma», che è un PDF, non la locandina. Lo spazio in scheda resta «locandina da aggiungere».
- **Interviste, fuori dal sito** (`dati/eventi/idee-interviste.md`): l'idea non si perde. Il file, non copiato in `site/`, annota le domande del primo giro, le due serie proposte per un secondo giro (maestri con nome e cognome; amatori e chi dipinge per strada, solo il nome) e il punto aperto sulle marche nelle risposte. L'idea è sospesa, in attesa di Sandro.
- **Documenti**: `README.md`, `AGENTS.md`, `CONTRIBUTING.md` e il prompt della chat. Il controllo sui nomi di marca resta quello di prima.
- Controlli: `python3 scripts/genera-sito.py` senza errori. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 95, scheda Sestri Levante 93. L'archivio 2026 resta sotto le 100 parole, quindi l'indice non si calcola. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito. La locandina di Sestri Levante e le interviste restano in attesa.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - Sezione Eventi, primo caso Sestri Levante

- **Nuova sezione 5, Eventi** (`dati/eventi/`), proposta da Sandro e approvata nella scaletta del 24/10/2026. Un file JSON per evento in `schede/`. `genera-eventi.py` scrive il calendario (`/eventi/`), la scheda (`/eventi/<anno>/<slug>/`) e l'archivio dell'anno (`/eventi/<anno>/`). In calendario un evento è in corso, in arrivo o passato secondo la data di Europe/Rome al momento della generazione.
- **Barra e home** (`scripts/genera-sito.py`): voce «5 Eventi», scheda in home con un calendario disegnato in SVG, riga nel riquadro «in costruzione». Nella testata e nella descrizione per i motori di ricerca si nominano anche gli eventi. La barra resta su più righe, senza scorrimento di lato; sulle schede i collegamenti della barra risalgono alla radice del sito. Chat e suggerimenti accettano anche l'indirizzo di una scheda.
- **Testi della sezione** (`sezione.json`, `domande.json`): calendario, racconti firmati che non coprono tutto l'evento, quattro domande fisse uguali per tutti e una quinta, «Perché sei qui oggi?», solo per chi dipinge per strada. Le quattro: «Come hai cominciato con l'acquerello?»; «Che materiali usi: carta (marca e grammatura), pennelli e marche di colori, con la tavolozza?»; «Un consiglio per chi dipinge en plein air?»; «Un errore da evitare?». La seconda rimanda a Marche e tubetti; la risposta, quando c'è, si riporta come detta da chi parla. I campi vuoti sono segnati «da completare». La nota sui contributi usa la casella Suggerimenti, che non riceve file. Il contatto per le foto resta «da completare»: non è stato inventato un indirizzo.
- **Watercolor Sestri Levante 2026** (`schede/watercolor-sestri-levante-2026.json`): 23-25 ottobre 2026, Sala Agave, ex Convento dell'Annunziata, Sestri Levante. Il programma è quello letto il 24/10/2026 da `https://watercolorsestrilevante.it/#programma`: 21 voci, con orari e nomi della pagina. Sono stati normalizzati solo gli spazi, l'accento su «venerdì» e il trattino della premiazione, sostituito da un punto perché il sito non usa il trattino lungo. La premiazione non ha un orario di fine, e non ne è stato aggiunto uno. Nel programma il laboratorio è firmato «Yana Wihlem»; la biografia della stessa pagina scrive «Yana Wilhelm»: in scheda compaiono entrambe le grafie.
- **Demo di Cesc Farré**, sabato 24 ottobre, dalle 10.00 alle 11.00. Unico materiale: il post di Alessandro Sanvitale (`https://x.com/alessandro_snv/status/2113927807763960240`). Lezione: «less is more». Racconto «io c'ero» con il testo del post, nient'altro, e la foto `immagini/farre-sestri-2026-sandro.jpg`, credito «foto di Alessandro Sanvitale». Soggetto, tecnica, carte, colori e collegamenti al Quaderno: «da completare». Le altre otto demo hanno gli stessi campi aperti. Degli altri venti momenti del programma manca il racconto.
- **Interviste**: struttura pronta, cinque domande (la quinta solo per chi dipinge per strada), nessuna risposta. Il controllo sui nomi di marca non è stato allentato: una risposta che nomina una marca ferma ancora la generazione. La decisione, se le citazioni delle interviste possano contenerli, resta al curatore.
- **Documenti**: `README.md`, `AGENTS.md`, `CONTRIBUTING.md` (eccezione del racconto in prima persona, domande delle interviste e divieto di riempire i vuoti; il divieto sui nomi di marca resta) e `LICENSE` (credito delle foto).
- Controlli: `python3 scripts/genera-sito.py` senza errori. Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72, Eventi 87, archivio 2026 95, scheda Sestri Levante 82. `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore, anche sul punto delle marche nelle risposte delle interviste. L'unione su `main` pubblica il sito. Restano da completare, per Sestri Levante, soggetto tecnica carte e colori delle demo, i racconti mancanti, le interviste e il contatto per le foto.

-- GBOT-app-acquerello

## 2026-10-24 - GBOT-app-acquerello - I sei colori come proposta

- Richiesta di Sandro: in tutto il sito i sei colori (giallo limone PY175, ceruleo PB15, cremisi PR206, terra di Siena bruciata PR101, terra d'ombra bruciata PBr7+PY42, blu oltremare PB29) si leggono come proposta, un punto di partenza che si può ridurre, ampliare o cambiare. Stessi colori, stessi pigmenti, stesse miscele M1-M12, stesse fonti e stessi ancoraggi. Dove bastava una formula breve, «i sei colori di base» diventa «i sei colori proposti».
- **Home** (`scripts/genera-sito.py`), decisione finale di Sandro del 24/10/2026: la fila dei sei colori resta in apertura, come immagine di presentazione. Nome e pigmento restano sull'etichetta di ogni campione. Non c'è alcuna didascalia sotto: esce la frase «I sei colori di base della tavolozza, col nome comune e il pigmento. Le tinte sono indicative, come nel calcolatore.» Non entra una frase nuova al suo posto.
- **Schede della home e descrizioni per i motori di ricerca** (sottotitoli in `SEZIONI`): «la tavolozza ridotta e le sue 12 miscele» diventa «i sei colori proposti e le 12 miscele»; «i sei colori di base e un calcolatore» diventa «i sei colori proposti e un calcolatore»; «I sei colori di base nelle serie in commercio» diventa «I sei colori proposti nelle serie in commercio».
- **Principi generali**, capitolo 8 e introduzione (`dati/principi/principi.json`, titolo del blocco in `genera-principi.py`): «tavolozza ridotta» e «sei colori di base» diventano «sei colori proposti». Il paragrafo dei sei colori chiude con «È un punto di partenza: si può ridurre, ampliare o cambiare.» Il titolo del blocco è «I sei colori proposti». «nel tubetto della tavolozza» diventa «nel tubetto proposto». La data in calce passa al 24/10/2026. Le tre voci di fonte interne che nominavano i sei colori seguono le nuove formule; gli URL restano uguali.
- **Teoria dei colori**: il capitolo 4 si intitola «4. Sei colori proposti, come punto di partenza» (voce dell'indice: «Sei colori»; l'ancora resta `#tavolozza`). Il paragrafo di apertura dice che si possono ridurre, ampliare o cambiare. Subito dopo, con fatti già nel Quaderno: «Mescolando questi sei colori si ottengono altri colori, fra cui i verdi, i bruni e i grigi degli esempi. Il prontuario è quello delle 12 miscele M1-M12. Il calcolatore cerca la miscela più vicina a un colore dato e segnala ciò che resta fuori dalla loro portata.» I rimandi vanno a `/principi/#miscele` e a `#calcolatore`. Fonte nuova del capitolo, interna: il capitolo 8 dei Principi. Nel calcolatore, «fuori dalla portata dei sei tubetti» diventa «fuori dalla portata dei sei colori proposti» e «dei sei tubetti» nei limiti diventa «dei sei tubetti proposti». Data in calce: 24/10/2026.
- **Marche e tubetti**: titolo, sottotitolo, introduzione, nota della serie Cotman e «il ceruleo della tavolozza» passano a «proposti» / «proposto». L'intestazione di tabella «Colore della tavolozza» diventa «Colore proposto». Data in calce: 24/10/2026.
- **Soggetti**: la scheda S1 dice «sei colori proposti per l'aperto» al posto di «tavolozza ridotta a sei colori».
- **Alberi**: il riquadro si intitola «i 6 colori proposti»; «bastano i 6 colori di base» diventa «si possono usare i 6 colori proposti», con la frase sul punto di partenza. L'etichetta di ogni esempio è «6 colori proposti». Nelle sei schede «si usano» / «si usa» diventa «si possono usare» / «si può usare». Nelle 24 modalità, «coi 6 colori:» diventa «coi 6 colori proposti:». Ricette, sigle e dosi invariate. Il riquadro delle dosi, letto anche dal capitolo 8, parla di «6 colori proposti» al posto di «tavolozza ridotta».
- **Chat**: l'esempio di domanda e `lib/prompt-chat.js` (rigenerato) parlano di proposta, non di tavolozza fissa. Una riga chiede di non presentarli come obbligatori.
- **Documenti**: `README.md`, `AGENTS.md` e `CONTRIBUTING.md` usano «sei colori proposti» dove descrivevano i sei colori di base.
- Controlli: `python3 scripts/genera-sito.py` senza errori. Gulpease invariato (Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72). `lib/prompt-chat.js` rigenerato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. L'unione su `main` pubblica il sito.

-- GBOT-app-acquerello

## 2026-10-23 - GBOT-app-acquerello - Fonti esterne del capitolo 8

- **Principi generali** (`dati/principi/principi.json`): nel capitolo 8, «In studio e all'aperto», le frasi che citavano solo il testo del Quaderno prendono le pagine approvate da Sandro il 23/10/2026, dove il passo c'è davvero. Il tono resta di proposta. Nessun colore e nessuna miscela nuovi. L'elenco dei colori pronti (ocra, vescica, perilene e gli altri) resta su `alberi-studio-aperto` e, dove il passo non è nella sezione Alberi, sul testo del Quaderno.
- **Fonti aggiunte** (i Principi passano da 36 a 42 fonti; il capitolo 8 le numera insieme alle quattro già sue):
  - Bruce MacEvoy, Handprint, «Painting outdoors» (`tech32.html`): vento, temperatura e umidità, asciugatura imprevedibile, controllo del bagnato sulla carta.
  - Bruce MacEvoy, Handprint, «Wet in wet» (`tech23.html`): il vento accelera l'evaporazione, l'umidità la rallenta, il sole diretto scalda il vapore; sulla carta umida, all'aperto, un colore più concentrato (la sua «creamy dilution»). Nella cella all'aperto della riga sull'asciugatura entra una frase in questo senso. «Cremosa» non è una quarta consistenza del Quaderno.
  - Andy Griffiths, Solving Watercolour, «Pro Tips For Plein Air Watercolor Painting»: vento e sole asciugano più in fretta; stesure larghe; due o tre pennelli; borraccia; carta assorbente; tavolozze limitate; godet più comodi dei tubetti sui formati piccoli.
  - Jenna Rainey, «Top Tips for a Successful Plein Air Watercolor Session» (8/5/2026): tavolozza di 4-6 colori; uno o due pennelli; contenitore d'acqua; straccio o carta; niente cavalletto grande; stesure larghe e sciolte. Sostituisce il testo del Quaderno nel paragrafo dei sei colori, accanto alla tavolozza interna.
  - Cerchio di Giotto, «Come disegnare all'aperto»: lezione di disegno, citata solo sulla riga della dotazione (bottiglietta, carta da cucina, scatola da viaggio).
  - Felice Feltracco, «Come prepararsi per dipingere en plein air» (`https://www.youtube.com/watch?v=tMUbZh6cCgs`): titolo confermato; in studio luce, tempi e strumenti a portata di mano; all'aperto il sole asciuga la carta troppo in fretta; pochi strumenti e palette compatta. Nel testo della fonte non compare il nome commerciale dei suoi colori.
- **Restano sul testo del Quaderno**, perché le pagine esterne non le coprono: i pennelli da studio con i numeri, la tavola inclinata e i grandi formati, lo spruzzatore, la tessera, e la frase sul colore denso da deporre mentre il lucido se ne va. L'elenco dei colori pronti (i due paragrafi e la cella «in studio» della riga «Tavolozza») non riceve fonti esterne nuove: resta su `alberi-studio-aperto` e sul testo del Quaderno. La scatola dei sei colori, in quella riga, resta sulla tavolozza interna; Rainey è citata nel paragrafo dei sei colori.
- **Fuori dal capitolo**, dopo verifica degli URL:
  - Emmanuele Cammarano: pagine `https://emmanuelecammarano.com/watercolor-tutorial/` e `https://emmanuelecammarano.com/autore/` raggiungibili. La pagina Autore dice che organizza demo e workshop di pittura all'aperto, senza un passo tecnico su dotazione, asciugatura o alberi. I video con titolo confermato (rami di legno, materiali per chi inizia, lezione di paesaggio 2025) non sono tutorial en plein air e non sono già un esempio degli Alberi: non entra una scheda nuova.
  - Elisa Marianini resta nella selezione Alberi (`https://www.youtube.com/watch?v=NAt3W6NR4ug`, titolo confermato). Nessun rimando nuovo: Feltracco copre già la voce italiana sull'aperto.
- **Handprint**: il 23/10/2026 il sito risponde con una pagina di controllo automatico e non consegna il testo. I passi citati sono quelli della copia d'archivio degli stessi indirizzi (15/2/2025 per «Painting outdoors», 10/3/2025 per «Wet in wet»), con la revisione dell'8/1/2015 e la firma di Bruce MacEvoy. In fonte resta l'URL pubblico.
- **Documenti**: `README.md` e `AGENTS.md` passano da 36 a 42 fonti.
- Controlli: `python3 scripts/genera-sito.py` senza errori. Gulpease invariato (Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72). `lib/prompt-chat.js` invariato. In attesa del via del curatore per l'unione su `main`.
- Prossima azione: via del curatore. Se si vuole una fonte anche per i pennelli da studio, lo spruzzatore o il verde di perilene, serve una pagina che ne parli.

-- GBOT-app-acquerello

## 2026-10-23 - GBOT-app-acquerello - Capitolo 8 in tono di proposta

- **Principi generali** (`dati/principi/principi.json`): nel capitolo 8, «In studio e all'aperto», le indicazioni che suonavano obbligatorie sono riformulate come proposte, come chiesto da Sandro il 23/10/2026. Stessi fatti, stessi colori, stesse miscele M1-M12, stesse fonti. Nell'introduzione, «è trattato nel capitolo 8» diventa «è proposto nel capitolo 8». La data dei testi in calce alla pagina passa al 23/10/2026.
- **Dosi** (`dati/alberi/pit-261014-video-gesti-alberi.json`): il riquadro «Come leggere le dosi» è letto dal capitolo 8 e compare anche nella sezione Alberi e nel prompt della chat. «Si prepara sempre prima il colore dominante» diventa «Conviene preparare prima il colore dominante». L'ordine della ricetta non cambia. Resta «da verificare sempre sulla carta» nella nota del calcolatore: è l'avvertenza di controllo sulla carta, non un'indicazione di pittura.
- Frasi del capitolo, prima e dopo:
  - «la dotazione e la tavolozza più adatte» diventa «Spesso conviene allora rivedere la dotazione e la tavolozza.»
  - «Questo capitolo descrive» diventa «Questo capitolo propone».
  - «Temperatura e umidità stabili, nessuna corrente d'aria» diventa «Di solito la temperatura e l'umidità restano stabili, senza corrente d'aria».
  - «Servono decisioni rapide, stesure sintetiche...» diventa «In molti casi conviene decidere in fretta, con stesure sintetiche...».
  - «Tavolozza estesa: ... si affiancano colori pronti» diventa «Una proposta è la tavolozza estesa: ... si possono affiancare colori pronti».
  - «Scatola compatta con i sei colori» diventa «Una proposta è la scatola compatta...».
  - L'elenco dei pennelli da studio, senza attenuazione, diventa «Si possono tenere un tondo grande...».
  - «Dotazione essenziale» diventa «Una proposta di dotazione».
  - «Rifare fedelmente le procedure» diventa «Si possono rifare fedelmente le procedure».
  - «Esercitarsi a ricavare i verdi» diventa «Si può esercitarsi a ricavare i verdi».
  - «bastano sei colori» diventa «si possono usare sei colori».
- Restano com'erano i paragrafi già in tono di proposta («usano spesso», «è utile», «fra gli altri») e i dati delle 12 miscele.
- Controlli: `python3 scripts/genera-sito.py` senza errori. Gulpease invariato (Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72). `lib/prompt-chat.js` rigenerato.
- In attesa del via del curatore per l'unione su `main`.
- Prossima azione: fonti esterne per le frasi del capitolo 8 che rimandano solo al testo del Quaderno.

-- GBOT-app-acquerello

## 2026-10-22 - GBOT-app-acquerello - In studio e all'aperto prima della tabella riassuntiva

- **Principi generali** (`dati/principi/principi.json`): il capitolo «In studio e all'aperto» passa prima della tabella riassuntiva, come chiesto dal curatore il 22/10/2026 alle 20:41. Diventa il capitolo 8 e la tabella il 9; l'indice dei capitoli segue lo stesso ordine (… Grana e grammatura, Studio e aperto, Riassunto). Le ancore restano uguali (`#studio-aperto`, `#riassunto`, `#confronto`, `#tavolozza-studio`, `#tavolozza-plein-air`, `#miscele`, `#M1`-`#M12`) e il rinvio 301 da `/studio-plein-air/` non cambia.
- **Fonti**: numerate per capitolo da `scripts/rimandi_fonti.py`, restano da 1 a 4 nel capitolo 8 e invariate nella tabella; i Principi restano a 9 capitoli e 36 fonti.
- **Testi**: «nell'ultimo capitolo» diventa «nel capitolo 8» nell'introduzione dei Principi, nella nota di `principi.json`, in `README.md`, `AGENTS.md`, `genera-principi.py` e in un commento di `genera-sito.py`.
- Controlli: generazione senza errori, controlli interni superati, Gulpease invariato (Principi 68); 451 collegamenti interni e ancore senza errori, nessun id doppio.
- Unita su `main` (PR #33) col via del curatore del 22/10/2026.
- Prossima azione: fonti esterne per le frasi del capitolo 8 che rimandano solo al testo del Quaderno.

-- GBOT-app-acquerello

## 2026-10-22 - GBOT-app-acquerello - Studio ed en plein air diventa l'ultimo capitolo dei Principi

- **Sezioni**: la sezione *Studio ed en plein air* (`/studio-plein-air/`) non è più una sezione a sé. Il suo testo è ora il capitolo 9 dei *Principi generali*, «In studio e all'aperto: metodo di lavoro, dotazione e tavolozze» (ancora `#studio-aperto`, voce «Studio e aperto» nell'indice dei capitoli), dopo la tabella riassuntiva. Nuovo ordine: 1 Principi generali, 2 Teoria dei colori, 3 Marche e tubetti, 4 Soggetti, 4.1 Alberi, nella barra, nella home, nel modulo dei suggerimenti, nel prompt della chat e nei documenti (decisione del curatore del 22/10/2026).
- **Testo**: spostato senza riscriverlo. Cambiano solo «Questa sezione descrive» in «Questo capitolo descrive», i numeri «1.» e «2.» davanti ai due sottotitoli e, nel riquadro delle dosi, il rimando «nei Principi generali» che nella pagina dei Principi diventa «nei capitoli 1 e 2». Escono il sottotitolo della vecchia pagina, che ripeteva l'introduzione, il suo indice e la riga «Le altre sezioni». Gli id `#tavolozza-studio`, `#tavolozza-plein-air`, `#miscele` e `#M1`-`#M12` restano uguali.
- **Fonti** (`dati/principi/principi.json`, sistema per capitolo di `scripts/rimandi_fonti.py`): il capitolo 9 ha 4 fonti numerate da 1: il testo del Quaderno già pubblicato (sintesi redazionale senza fonte esterna, dichiarata come tale), la sezione Alberi, la tavolozza di Teoria dei colori e il riquadro delle 12 miscele degli Alberi. I Principi passano da 8 a 9 capitoli e da 32 a 36 fonti. Il blocco della tavolozza ridotta con le 12 miscele passa da `dati/studio-plein-air/genera-studio-plein-air.py` a `dati/principi/genera-principi.py`, con lo stesso controllo sulla tavolozza di `dati/colori/tavolozza.json`.
- **Rinvio**: `scripts/genera-sito.py` scrive `site/_redirects` con un 301 di Cloudflare Pages da `/studio-plein-air`, `/studio-plein-air/` e `/studio-plein-air/index.html` a `/principi/#studio-aperto`, e si ferma se l'ancora non c'è. Il flusso `costruisci` controlla il rinvio e che `site/studio-plein-air` non esista.
- **Collegamenti**: Alberi (3), Soggetti (1) e l'introduzione dei Principi (1) puntano al nuovo capitolo; nel prompt della chat le 12 miscele sono a `/principi/#miscele`. Teoria dei colori non aveva collegamenti alla sezione. Il sottotitolo dei Principi, nella pagina e nella scheda della home, cita il lavoro in studio e all'aperto. Esce dalla home la figurina dei godet della vecchia scheda; restano la striscia della tavolozza e la ruota di Teoria dei colori.
- **Funzioni**: «Studio ed en plein air» esce dalle sezioni ammesse dei suggerimenti e `/studio-plein-air/` dalle pagine ammesse della chat e dei suggerimenti.
- Escono da Git `dati/studio-plein-air/studio-plein-air.json` e `genera-studio-plein-air.py`, recuperabili dalla cronologia.
- Controlli: generazione senza errori, controlli interni superati (fonti, marche fuori sezione, funzioni). Gulpease: Principi 68, Colori 75, Marche 59, Soggetti 66, Alberi 72. 451 collegamenti interni e ancore verificati senza errori, nessun id doppio.
- In attesa del via del curatore per l'unione su `main`.
- Prossima azione: fonti esterne per le frasi del capitolo 9 che rimandano solo al testo del Quaderno.

-- GBOT-app-acquerello

## 2026-10-22 - GBOT-app-acquerello - Via le illustrazioni generate con l'IA

- **Alberi**: escono le sei illustrazioni generate con l'IA (Nano Banana) in testa agli esempi A1-A6, che imitavano un acquerello dipinto. Escono con loro le didascalie «Illustrazione generata con l'IA: ...» (campo `illustrazione` in `dati/alberi/pit-261014-video-gesti-alberi.json`), la lente che le ingrandiva, il caricamento differito e la riduzione in jpg (`dati/alberi/pit-261013-video-gesti.py`). Dal piè di pagina escono le frasi sulle illustrazioni generate con l'IA e «Le illustrazioni si ingrandiscono con un tocco.». Restano le 72 infografiche SVG in 3 fasi.
- **Home**: la figurina della scheda S1 Alberi non è più il ritaglio di un'illustrazione IA (`home-alberi.webp`) ma un alberello disegnato in SVG come le altre figurine. Esce dal piè di pagina la riga sul ritaglio.
- **Sorgenti**: escono da Git le sei immagini `dati/alberi/illustrazioni/*.png` e lo script che le generava (`dati/alberi/pit-261013-illustrazioni.py`), recuperabili dalla cronologia. Il flusso `costruisci` non controlla più le immagini degli Alberi.
- **Documenti**: tolte le frasi sulle illustrazioni IA da `README.md`, `AGENTS.md`, `CONTRIBUTING.md` e `LICENSE`.
- Restano: schemi e infografiche SVG, la ruota Munsell di Teoria dei colori, i due schemi di Principi, le figurine della home, la tavolozza, le velature CSS della testata e la favicon.
- Controlli: generazione senza errori, controlli interni superati (Gulpease invariato, Alberi 72). Nessun `<img>` resta nelle pagine; 452 collegamenti interni e ancore verificati senza errori; nessun errore JavaScript in Chrome. Pagina degli Alberi: 216 KB di html senza immagini (prima 222 KB di html più 799 KB di jpg).
- **Regola nuova** (`CONTRIBUTING.md` § 3 e `AGENTS.md`), scelta dal curatore il 22/10/2026: «Nel sito non si usano immagini generate con l'IA che imitano un acquerello o un dipinto; sono ammessi solo schemi, infografiche e figure disegnate.»
- Unita su `main` (PR #32) col via del curatore del 22/10/2026.
- Prossima azione: taratura dei sei colori su campioni reali.

## 2026-10-22 - GBOT-app-acquerello - Barra delle sezioni su più righe, senza scorrimento di lato

- **Barra delle sezioni** (`STILE_BARRA` e `barra_quaderno` in `scripts/genera-sito.py`): non scorre più di lato. Le voci vanno a capo quando non stanno su una riga (`flex-wrap`), senza altezza fissa; la barra resta fissa in alto e la voce della pagina aperta resta evidenziata. Sul telefono, sotto 600 px, voci e numeri sono più compatti. Esce lo script che faceva scorrere la barra fino alla voce aperta, che sul computer a 800 px tagliava «Quaderno» a sinistra e le ultime voci a destra (segnalazione del curatore del 22/10/2026).
- **Larghezza**: nelle sezioni la barra si allarga fino ai bordi della finestra, non più solo alla colonna del testo (760-820 px), così a 1280 px sta su una riga come nella home.
- **Salti alle ancore**: uno script misura l'altezza reale della barra e dell'indice dei capitoli (`--barra-h`, `--salti-h`) e `scroll-padding-top` ne tiene conto; l'indice dei capitoli scende sotto la barra con `top: var(--barra-h)`. Misura anche la larghezza della barra di scorrimento verticale sul computer (`--sb`), così la barra non provoca scorrimento di lato.
- **Alberi**: l'etichetta «Video: ...» degli esempi (`.mod-autore` in `dati/alberi/pit-261013-video-gesti.py`) può andare a capo; a 360 px allargava la pagina di 16 px.
- Controlli: generazione senza errori, controlli interni superati (Gulpease invariato). Prova in Chrome su tutte le sette pagine a 1280, 800, 390 e 360 px, anche con la barra di scorrimento classica di Windows: nessuna voce fuori dallo schermo, nessuno scorrimento di lato; la barra occupa 1 riga a 1280 px, 2 a 800 px, 3 a 390 e 360 px. In Teoria dei colori i salti a tre capitoli portano il titolo sotto la barra e l'indice a tutte le larghezze.
- Unita su `main` col via del curatore del 22/10/2026.
- Prossima azione: taratura dei sei colori su campioni reali.

-- GBOT-app-acquerello

## 2026-10-22 - GBOT-app-acquerello - Home ad acquerello: testata sfumata, tavolozza, schede con figura, nota di metodo da aprire

- **Testata** (`genera_home` in `scripts/genera-sito.py`): al posto della fascia verde piatta, un fondo chiaro con macchie sfumate in CSS, senza immagini. Titolo e sottotitolo invariati, in verde scuro su fondo chiaro; il titolo in Georgia. L'abete A2 proposto a destra della testata è stato tolto su richiesta del curatore.
- **Immagine**: `prepara_immagini_home()` ritaglia e riduce in webp, a ogni generazione, l'illustrazione A4 già nel repository per la scheda di S1 (128 × 128 px, 4 KB), in `site/immagini/`. È generata con l'IA, come tutte quelle degli Alberi, e lo dichiara una riga del piè di pagina. Nessun nuovo file binario nel repository. Il controllo «costruisci» verifica anche `site/immagini/home-alberi.webp`.
- **Tavolozza**: sotto la testata, le sei macchie dei colori di base lette da `dati/colori/tavolozza.json`, con nome comune e pigmento, e una riga che le dichiara indicative, con il rimando al calcolatore.
- **Schede**: ogni scheda ha una piccola figura in SVG o CSS: una goccia per i Principi, la scatola coi sei godet per Studio ed en plein air, il cerchio dei colori per la Teoria dei colori, un tubetto per Marche e tubetti, cielo, collina e acqua per Soggetti, il ritaglio della siepe A4 per S1 Alberi. Titoli e righe delle schede invariati.
- **Nota di metodo**: diventa un riquadro chiuso che si apre con un clic su «Nota di metodo». Il testo è lo stesso, con l'iniziale maiuscola perché ora apre il paragrafo.
- **Sfondo**: grana leggera da carta da acquerello, con un rumore SVG in CSS.
- Controlli: generazione senza errori; controlli interni superati (funzioni, marche, Gulpease delle sezioni: principi 69, studio-plein-air 62, colori 75, marche 59, soggetti 66, alberi 72); collegamenti e ancore della home verificati; prova in Chrome a 390 e a 1280 px senza scorrimento laterale; barra delle sezioni invariata.
- Unita su `main` col via del curatore del 22/10/2026.
- Prossima azione: taratura dei sei colori su campioni reali.

-- GBOT-app-acquerello

## 2026-10-21 - CC - Chat: le 12 miscele M1-M12 nel prompt

- Il prompt della chat (`genera_prompt_chat` in `scripts/genera-sito.py`, rigenerato in `lib/prompt-chat.js`) aveva i sei colori ma non le miscele, e alla domanda sull'abete in ombra il modello aveva proposto una ricetta sua invece della M4. Ora riporta le 12 miscele con ricetta, consistenza e note, lette da `apertura.miscele` del json degli Alberi, e la convenzione delle dosi da `apertura.dosi`; una riga chiede di indicare la miscela del Quaderno, con sigla e nome, prima di eventuali varianti. Il prompt passa da 6.232 a 8.831 caratteri.
- Prova con quattro domande dirette a `gemini-4-argon`, con le impostazioni della funzione: l'abete in ombra riceve M4 e M3, il verde scuro per le conifere in ombra M3 e M4, i tronchi in ombra degli alberi invernali M10 e M11, il cielo freddo di fondo M12; dosi coerenti con la convenzione del sito, nessun trattino lungo.
- Principi: la frase di 58 parole dell'introduzione, che elencava tre rimandi separati da punti e virgola, diventa tre frasi.
- Prossima azione: unione della PR dopo il via del curatore; taratura dei sei colori su campioni reali.

-- CC

## 2026-10-21 - CC - Barra delle sezioni, home «in costruzione», fonti per capitolo, via i foglietti A5

- **Barra delle sezioni** (`scripts/genera-sito.py`): in cima a ogni pagina, home compresa, con le cinque sezioni e S1 Alberi, l'assistente e i suggerimenti. Resta visibile scorrendo; sul telefono è una riga sola che scorre di lato e mostra la voce della pagina aperta. L'indice dei capitoli di ogni sezione scende sotto la barra.
- **Home**: la nota di metodo resta com'è. Al posto del paragrafo coi fogli A5 e del riquadro «in fase di sviluppo» c'è il riquadro «Il Quaderno è in costruzione», con quello che la versione attuale mette a disposizione, testo approvato dal curatore il 21/10/2026. Le schede delle sezioni hanno il titolo e una riga, e S1 Alberi compare sotto Soggetti. Sostituisce la PR #28, chiusa senza unione.
- **Titolo**: la sezione 3 si chiama «Teoria dei colori», senza «per l'acquerello».
- **Fonti per capitolo** (`scripts/rimandi_fonti.py`, nuovo): in Principi e Teoria dei colori le fonti sono elencate in fondo a ogni capitolo, una per riga e numerate da 1; il numero nel testo porta alla fonte e la freccia riporta al testo. Nei Principi l'elenco unico di 33 fonti diventa 55 voci distribuite negli 8 capitoli. In Teoria dei colori ogni paragrafo prende i rimandi alle fonti che lo sostengono, controllate sulle pagine delle fonti (13 su 13); escono quattro fonti che non sostenevano nessun paragrafo: le due voci di Wikipedia italiana, che sono pagine di disambiguazione, l'indice di handprint.com e ArtistAssistApp. Per decisione del curatore escono le affermazioni che le fonti non reggevano: «non bianco» per schiarire (cap. 1); il percorso della luce attraverso il velo (cap. 3); «con pigmenti trasparenti i due risultati si somigliano» e l'esempio di ceruleo e terra d'ombra opachi, vero solo per i tubetti di una serie (cap. 3); il meccanismo della granulazione, sostituito dal dato delle Marche, con l'oltremare PB29 indicato come granulante in quattro serie su sei (cap. 3); la motivazione della correzione con la luminosità (limite 5 del calcolatore). Entra la voce di Wikipedia su Albert Henry Munsell, che regge «pittore e insegnante di Boston». Il riscontro paragrafo per paragrafo è in `lavoro/app-acquerello-261021-verifica-fonti-teoria-colori.md` (solo locale).
- **Via i foglietti A5**: esce da Studio ed en plein air il capitolo «Il metodo dei foglietti A5», e i due successivi diventano 1 e 2; esce dai Principi la fonte che lo citava. Negli Alberi i sei riquadri diventano «Come esercitarsi», senza formato (campo `esercizio` al posto di `foglietto`), e «Che cosa controllare sul foglietto» diventa «nella prova»; altrove «sul foglietto» diventa «su carta». Nei Principi resta la carta del Quaderno, cotone 300 g/m² a grana fine, senza formato. Allineati il prompt della chat, README, AGENTS e CONTRIBUTING.
- **Leggibilità**: l'indice Gulpease non conta più gli elenchi delle fonti, che citano titoli e passi nella lingua originale e ora si ripetono nei capitoli. Valori: principi 68, studio-plein-air 62, colori 75, marche 59, soggetti 66, alberi 72.
- Controlli: generazione senza errori; i 443 collegamenti interni del sito generato portano a una pagina e a un'ancora esistenti; nessun «foglietto» nei sorgenti e nelle pagine; prova in Chrome a larghezza di telefono e di computer.
- Prossima azione: unione della PR dopo il via del curatore; taratura dei sei colori su campioni reali.

-- CC

## 2026-10-21 - CC - Chat: risposte senza trattino lungo

- Le istruzioni della chat (`scripts/genera-sito.py`, rigenerate in `lib/prompt-chat.js`) chiedono di non usare il trattino lungo e di fare gli incisi con virgole, due punti o parentesi, come vuole `CONTRIBUTING.md` § 3 per i testi del sito. La domanda di prova sul sito pubblicato aveva ricevuto una risposta col trattino lungo; con le istruzioni nuove, tre domande inviate direttamente a Gemini ne hanno ricevute zero.
- Prossima azione: taratura dei sei colori su campioni reali.

-- CC

## 2026-10-21 - CC - Sistemata generale dopo la contro-analisi: testi del 20/10 mattina in registro da manuale tecnico, chat senza email, funzioni del server protette

Contro-analisi dello stato di `main` al commit 41b4640: prima lettura di Claude Code, tre revisori esterni indipendenti (Grok, Codex e Gemini) e arbitrato di Fable, 59 rilievi. Le correzioni seguono le decisioni del curatore del 21/10/2026.

- **Testi delle guide**: Principi, Teoria dei colori, Marche e Alberi ripartono dai testi di b981b4d, già controllati sulle fonti, perché la riscrittura del 20/10 (#16) aveva cambiato in una sessantina di punti dati, citazioni e cautele. Vi sono riportate le modifiche valide venute dopo: lezioni di Robert Joyner sul canale attuale, dichiarate come video affini; rimandi alle sezioni Studio ed en plein air e Soggetti; A2 «Conifere alte e rade», perché fra i video c'è un pino silvestre. Su tutte le guide il registro è quello di un manuale tecnico, scelto dal curatore (regole in `CONTRIBUTING.md` § 3); l'indice Gulpease delle pagine va da 59 a 72.
- **Alberi**: pennelli, stati della carta e colori corretti sulle schede dei video in A2-M2, A3-M2, A3-M3, A3-M4, A3-M5, A4-M1, A4-M4, A5-M1, A5-M2, A5-M4, A5-M5 e A6-M2, e negli estratti A3-4 (terra di Siena naturale) e A4-1 (rosso inglese). Le frasi degli autori sono presentate come sintesi («Dal video, in sintesi:»), non come citazioni. Le sei illustrazioni sono dichiarate generate con l'IA, in didascalia e nel piè di pagina; diventano file jpg caricati solo quando servono, e la pagina passa da 1,3 MB a 220 KB.
- **Studio ed en plein air e Soggetti**: il foglietto si ricava dal foglio di 30 × 40 cm tagliato in quattro (15 × 20 cm) o da quello di 56 × 76 cm tagliato in sedici (14 × 19 cm), non da un ottavo del 56 × 76; la tavolozza ridotta coincide con i sei codici di `dati/colori/tavolozza.json`; tolte le spiegazioni senza fonte. I nomi degli esempi di S1 sono letti dal json degli Alberi.
- **Teoria dei colori e Marche**: i colori del calcolatore tornano a essere dichiarati provvisori; corrette la spiegazione della miscela sottrattiva, quella delle «parti» del simulatore, che il modello pesa con la luminanza, e la descrizione del ceruleo; «Carica nel simulatore» riporta il grado di diluizione. Il cremisi della serie Van Gogh è Madder Lake Deep 331 (PR264), controllato il 21/10/2026 sulla pagina ufficiale.
- **Chat** (`functions/api/chat.js`): senza email, con 5 domande a settimana per connessione e 10 al giorno in tutto, contate su D1 in modo atomico con un'impronta dell'IP a sale segreto; nessuna domanda né risposta conservata; la cronologia rimandata dal browser è firmata (HMAC) e limitata a due scambi; se il modello non risponde, la domanda non si conta. I contatori della chat e dei suggerimenti stanno nella stessa tabella e le due funzioni li cancellano con la stessa regola, entro 14 giorni dalla creazione. Il prompt di sistema è generato dai dati in `lib/prompt-chat.js` e il controllo «costruisci» verifica che sia allineato. Informativa riscritta in base al codice.
- **Suggerimenti** (`functions/api/suggerimento.js`): sezioni prese dal menu del sito, corpo limitato a 8000 byte e validato, indirizzi della pagina ridotti a quelli del sito, menzioni `@utente` neutralizzate, 5 invii al giorno per connessione e 30 in tutto.
- **Generatore e pubblicazione**: titoli delle sezioni ripristinati e presi da un'unica lista di `scripts/genera-sito.py`; la generazione si ferma se il menu e le pagine non coincidono con le funzioni, se un nome di marca compare fuori da Marche o se una pagina scende sotto 52 di Gulpease; home con i cinque riquadri delle sezioni; la tabella riassuntiva dei Principi scorre nel suo riquadro e non allarga più la pagina sul telefono; meta description, anteprime per i social, favicon, `robots.txt` e `sitemap.xml`; wrangler fissato alla 4.151.3; `npm run deploy` passa da `scripts/pubblica-locale.py`, che pubblica solo da `main` pulito e allineato a `origin/main`.
- **Documenti**: README, AGENTS e CONTRIBUTING allineati al nuovo stato; LICENSE dichiara le illustrazioni generate con l'IA e mette sotto MIT anche `functions/` e `lib/`.
- **Rilettura integrale** del testo risultante, con quattro revisori a contesto pulito e mandato anti-ridondanza: tolti i doppioni (elenco delle sezioni ripetuto nella home, moduli futuri detti tre volte, regole ripetute in Principi, Studio, Teoria dei colori, Marche e nell'introduzione degli Alberi) e i rimandi a un «corso» mai definito; l'informativa dice anche che cosa arriva a Google oltre alla domanda, che cosa diventa pubblico con un suggerimento e che anche la casella dei suggerimenti registra un'impronta dell'IP; stati della carta, pennelli e colori allineati fra descrizione, infografica ed estratto in A2-M1, A3-M3, A4-M4, A5-M1 e A5-M5; etichetta degli estratti neutra rispetto a chi parla nel video.
- **Decisioni del curatore sui punti aperti**: negli Alberi, dove la sintesi del parlato e la descrizione del gesto dicevano quasi la stessa cosa (22 estratti su 31), resta solo la sintesi, e tre regole ripetute nelle fasi delle infografiche restano nella descrizione e nei riquadri «Da evitare» e «Che cosa controllare»; la pagina passa da 14.249 a 13.586 parole. L'informativa indica come titolare Alessandro Sanvitale; da `CONTRIBUTING.md` § 4 è tolta la clausola sull'uso dei contributi in servizi in abbonamento, e resta la sola licenza del progetto; la chat ha un tetto complessivo di 10 domande al giorno; la chiave Gemini su Cloudflare è quella del progetto a pagamento.
- Prossima azione: taratura dei sei colori su campioni reali; Turnstile di Cloudflare sui due moduli solo se arrivano invii abusivi.

-- CC

## 2026-10-21 - AGY - Nota di metodo iniziale, correzione dei link alle fonti nella sezione 1 «Principi tecnici» e nuove sezioni «Studio ed en plein air» e «Soggetti»

- **Verifica e correzione dei link alle fonti di `dati/principi/principi.json` (`/principi/`)**: sostituito nelle 6 fonti del corso *Watercolor Fanatic* (`wf4`, `wf5`, `wf6`, `wf7`, `wf8`, `wf-fiori`, pari alle voci `[1]`, `[2]`, `[3]`, `[5]`, `[6]` e `[29]` dell'apparato) il vecchio handle `https://www.youtube.com/@WatercolorFanatic` (che restituiva errore 404 dopo il cambio di denominazione del canale dell'autore Robert Joyner in `@crafted_by_robert`) con i collegamenti diretti verificati ai video e al canale attivo di **Robert Joyner | Loose Art** (`jWJvOV24ftY`, `62t3oGplSIE`, `as4p09ekLrY`, `vK9F0fFtDqU`, `U-cV9mfPde8`, `@crafted_by_robert`); aggiornata la fonte `mow` con il collegamento diretto al video specifico di *The Mind of Watercolor* (`xSp2qNBvMSo`) e la fonte `alberi-foglietti` con il rimando a `../studio-plein-air/#protocollo-a5`. Verificati via API oEmbed tutti i collegamenti YouTube della sezione.
- **Nuova sezione 2 — «Pittura in studio ed en plein air: metodo, dotazione e tavolozze» (`dati/studio-plein-air/`, `/studio-plein-air/`)**: scorporata in una sezione autonoma la trattazione del metodo di lavoro in studio e all'aperto, con quadro sinottico comparativo (cinetica di asciugatura, configurazione della tavolozza, dotazione di pennelli e accessori, finalità didattica), protocollo di sperimentazione su campioni in formato A5, descrizione dei pigmenti di comodità della tavolozza estesa da studio e prontuario completo dei 6 pigmenti e delle 12 miscele (`M1`-`M12`) per l'esecuzione *en plein air*.
- **Nuova sezione 5 — «Repertorio dei soggetti pittorici» (`dati/soggetti/`, `/soggetti/`)**: creata la sezione dedicata ai singoli temi pittorici del corso in progressiva estensione: **S1 · Alberi, conifere e masse arbustive** (modulo attivo, collegato a `/alberi/` e alle 6 tipologie `A1`-`A6`, primo argomento affrontato nel corso), seguito dai moduli in preparazione **S2 · Cieli, velature atmosferiche e formazioni nuvolose**, **S3 · Morfologia botanica, corolle e fiori**, **S4 · Specchi d'acqua, increspature e riflessi**, **S5 · Masse rocciose, rilievi montuosi e terreni** e **S6 · Architetture, murature storiche e scorci urbani**.
- **Riorganizzazione dell'indice generale e del modulo Alberi (`scripts/genera-sito.py`, `dati/alberi/`, `functions/api/chat.js`, `README.md`)**: riordinate le 5 sezioni in Home page (*1. Principi tecnici*, *2. Studio ed en plein air*, *3. Colorimetria*, *4. Merceologia*, *5. Soggetti pittorici* con accesso rapido anche a `S1 · Alberi`), aggiunta in apertura la nota di metodo sull'impiego dell'IA come strumento di spoglio e di ordinamento al servizio dello studio manuale dell'acquerello per indicizzare e confrontare le dimostrazioni video su YouTube, snellita l'introduzione di `/alberi/` con rinvio a `/studio-plein-air/` e `/soggetti/` e allineato il prompt di sistema di Gemini 4 Argon.
- Prossima azione: taratura colorimetrica su campioni reali dei 6 pigmenti in `dati/colori/tavolozza.json` e redazione dei successivi moduli della sezione *Soggetti pittorici* (a partire da cieli/nuvole o fiori).

-- AGY

## 2026-10-20 - AGY - Riscrittura integrale di tutte le sezioni del sito in registro tecnico-didattico professionale

- **Home page, struttura di consultazione e componenti comuni (`scripts/genera-sito.py`, `functions/api/chat.js`, `README.md`)**: sostituito il linguaggio colloquiale con una terminologia tecnica rigorosa (idrodinamica delle stesure, stati igrometrici del supporto in cotone, spazio colorimetrico di Munsell, modello spettrale di Kubelka-Munk, merceologia dei pigmenti e codici Colour Index) nella presentazione generale del repertorio, nella guida in 4 tappe *«Struttura e metodo di consultazione»*, nell'interfaccia e nel prompt di sistema del consulente tecnico basato su Gemini 4 Argon (`functions/api/chat.js`) e nel modulo di invio contributi e rettifiche. Esplicitato in apertura, nella sezione *Alberi* e nel prospetto dei moduli in programma che il repertorio è **in fase di sviluppo** e che la monografia sugli alberi inaugura la serie in quanto primo soggetto affrontato nel corso, a cui seguiranno progressivamente i moduli su cieli e formazioni nuvolose, fiori ed elementi botanici, specchi d'acqua, rocce e architetture.
- **Sezione 1 — Principi generali (`dati/principi/principi.json`, `dati/principi/genera-principi.py`)**: riscritti gli 8 capitoli tecnici (gradi di diluizione *tè, latte, miele* della scala di Zbukvic; stati igrometrici della carta *asciutta, umida satinata, bagnata a velo lucido*; bilancio idrico tra pennello e supporto e prevenzione dei riflussi / *backruns*; controllo del carico di miscela; gestione dei margini netti e sfumati; tempi di evaporazione e ritiro tonale; grammatura, pressatura a caldo/freddo e collatura interna/superficiale; quadro sinottico operativo), le didascalie degli schemi SVG e l'apparato delle 33 fonti.
- **Sezione 2 — Morfologia ed esecuzione degli alberi (`dati/alberi/pit-261014-video-gesti-alberi.json`, `dati/alberi/pit-261015-infografiche.py`, `dati/alberi/pit-261013-video-gesti-segmenti.csv`, `dati/alberi/pit-261013-video-gesti.py`)**: riscritti in registro tecnico-professionale l'inquadramento metodologico, la legenda degli stati della carta, il prontuario delle 12 miscele (`M1`-`M12`) con protocollo di verifica su tre rapporti di miscelazione, le schede delle 6 tipologie arboree e vegetazionali (`A1`-`A6`), le 24 modalità dimostrative, le 72 didascalie delle tavole sinottiche SVG in 3 fasi e le 31 schede tecniche degli estratti video indicizzati.
- **Sezione 3 — Teoria del colore, ottica dei pigmenti e calcolatore (`dati/colori/teoria-colori.json`, `dati/colori/tavolozza.json`, `dati/colori/genera-teoria-colori.py`, `dati/colori/interfaccia.js`)**: riscritti i 5 capitoli teorici (coordinate di Munsell Tinta, Valore e Croma; sintesi additiva e sottrattiva, curve di riflettanza spettrale e decadimento del croma; ottica della velatura su strato asciutto, fusione su umido e granulazione; struttura della tavolozza essenziale a 6 pigmenti; funzionamento e limiti del simulatore spettrale Kubelka-Munk a 38 bande), le note merceologiche della tavolozza e le etichette del calcolatore interattivo.
- **Sezione 4 — Merceologia e comparazione delle serie commerciali (`dati/marche/marche.json`, `dati/marche/genera-marche.py`)**: riscritti l'inquadramento merceologico, le note sulle 6 serie analizzate (Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith Extra Fine, Schmincke Horadam, Maimeri Blu), l'analisi delle divergenze formulative a parità di denominazione commerciale (*Cremisi, Blu ceruleo, Terra di Siena bruciata, Giallo limone, Terra d'ombra bruciata, Blu oltremare*) e la guida alla lettura dei parametri d'etichetta (Colour Index, grado di opacità, solidità alla luce ASTM).
- Prossima azione: taratura colorimetrica su campioni reali dei 6 pigmenti in `dati/colori/tavolozza.json` e verifica di eventuali contributi inviati tramite il modulo del sito.

-- AGY

## 2026-10-20 - AGY - Guida «Come funziona questo sito», chat AI con Gemini 4 Argon (5 domande per email) e casella suggerimenti

- **Sezione iniziale «Come funziona questo sito» (scripts/genera-sito.py)**: aggiunto in apertura della pagina principale il percorso guidato in 4 passi (*1. Capire acqua e carta*, *2. Provare i gesti passo passo*, *3. Mescolare i colori*, *4. Leggere l'etichetta dei tubetti*) con i rimandi diretti alla chat AI e alla casella dei suggerimenti.
- **Assistente AI sull'acquerello con Gemini 4 Argon (unctions/api/chat.js + wrangler.toml)**: aggiunta in tutte le pagine la chat didattica basata su gemini-4-argon (istruita sui contenuti del Quaderno e vincolata ai soli temi di acquerello, disegno e materiali), con accesso tramite indirizzo email e limite di **5 domande gratuite per email** registrato sul database Cloudflare D1 pp-acquerello (utenti_chat e messaggi_chat), oltre a filtro anti-abuso giornaliero per IP e secret GEMINI_API_KEY configurato su Cloudflare Pages.
- **Casella suggerimenti sul sito (`functions/api/suggerimento.js` + `scripts/genera-sito.py`)**: aggiunto in fondo a tutte le pagine del sito il modulo pubblico *«Suggerisci una modifica, una correzione o un video»* con filtro anti-spam, oscuramento automatico di eventuali indirizzi email inseriti per errore e avviso esplicito prima dell'invio che la segnalazione sarà pubblicata nella bacheca aperta delle Issue di GitHub (`suggerimento-dal-sito`, sotto licenza CC BY 4.0). Configurato il secret `GITHUB_SUGGERIMENTI_TOKEN` su Cloudflare Pages.
- **Indicizzazione e pulizia file**: rimosso `<meta name="robots" content="noindex,nofollow">` da tutte le 5 pagine del sito; rimossi gli 8 PNG obsoleti (`pit-261015-riferimento-A1..A7.png` e `pit-261013-illustrazione-A7-tavola-inclinata.png`) e ripulito `dati/alberi/pit-261013-illustrazioni.py`; eliminati i vecchi rami secondari `gbot/*`.
- **Allineamento testi tra le sezioni**: aggiornati i rimandi tra `dati/principi/principi.json`, `dati/colori/teoria-colori.json`, `dati/marche/marche.json` e la nuova struttura della sezione *Alberi* (esempi e modalità, tavolozza ridotta da 6 colori, nota sulla taratura del calcolatore); corretto il refuso `scurisci` -> `scurisco` in `A4-1` (`dati/alberi/pit-261013-video-gesti-segmenti.csv`).
- Prossima azione: taratura su prove reali dei 6 colori di `dati/colori/tavolozza.json` e valutazione degli eventuali suggerimenti inviati dal sito.

-- AGY

## 2026-10-20 - AGY - Preparazione del repository per l'apertura pubblica su GitHub

- Aggiunti `LICENSE` (CC BY 4.0 per testi, dati, schede e illustrazioni; MIT per il codice Python e JavaScript) e `CONTRIBUTING.md` con le regole editoriali e le istruzioni per contribuire tramite Issue o Pull Request.
- Aggiornati `README.md`, `AGENTS.md`, `CLAUDE.md` e `app-acquerello-261016-prompt-avvio-agente.md` per la consultazione pubblica; rimossi dai file di dati e dagli script i riferimenti all'ambiente locale di lavoro.
- Esclusi dal tracciamento Git i file di indice e giornale dell'ambiente locale (`.gitignore`).
- Prossima azione: revisione generale dei testi e apertura della casella suggerimenti.

-- AGY

## 2026-10-19 - AGY - Sezione Alberi ristrutturata per modalità video con 24 infografiche e doppia proposta colori

Rivista l'intera sezione `/alberi/` (`dati/alberi/`) sul ramo `agy/alberi-modalita-video`:

- **Sganciamento completo dall'immagine del lago**: rimosso l'esercizio `A7` (Riflessi nell'acqua ferma) e tutti i riferimenti residui a lago, riva, specchio d'acqua e montagna; sostituite in testa ai 6 esempi (`A1`-`A6`) le foto di riferimento del lago con gli studi autonomi ad acquerello su foglietto A5 (`pit-261013-illustrazione-A1..A6.png`). Chiarito in apertura che i 6 soggetti (abeti in gruppo, abeti alti e radi, chiome tonde d'autunno, siepi e cespugli, alberi invernali con fusti chiari e brina, rami sottili e foglie in primo piano) sono solo alcuni esempi rappresentativi da cui partire, a cui se ne possono affiancare molti altri.
- **Struttura per modalità video + un'infografica SVG per ciascun video**: sostituita la sequenza mista di passi con **24 schede di modalità possibili** (una per ogni video di interesse, rimuovendo i 3 estratti duplicati `A2-4`, `A2-5`, `A4-2`, per un totale di 31 estratti video). Ogni modalità espone cosa propone il video, i colori e i pennelli usati dall'autore (senza marche commerciali), un'**infografica SVG in 3 fasi** dedicata specificamente a quel video (72 vignette SVG totali in `pit-261015-infografiche.py`) e i relativi estratti nel player. Mantenuto `id="A1-3"` sul blocco video per preservare il rimando diretto da `/principi/`.
- **Impostazione dei colori (studio vs aperto)**: superato il vincolo dei soli 6 colori; per ogni esempio e per ogni modalità sono indicati sia i **colori liberi da studio** (verdi pronti, terre naturali e bruciate, turchese di cobalto, blu ftalo, blu di Prussia, indaco, grigio di Payne, seppia, ecc.) sia il rimando alla **tavolozza ridotta da 6 colori di base e 12 miscele (`M1`-`M12`)** pensata per quando si dipinge all'aperto (*en plein air*) o con una scatola leggera.

-- AGY

## 2026-10-18 - GBOT-app-acquerello - Chiusura giornata e riepilogo pull request

Riepilogo delle pull request del 18/10/2026 unite su `main` e pubblicate:

- **#5** `gbot/regola-merge-claude-md`: tolta da `CLAUDE.md` la regola del merge automatico della sessione cloud; l'unione su `main` si fa solo dopo approvazione.
- **#6** `gbot/teoria-colori`: nuova sezione Teoria dei colori (Munsell, luce e pigmento, acquerello, tavolozza) con il calcolatore di miscele in JavaScript che gira nel browser.
- **#7** `gbot/cremisi-pr206`: cremisi della tavolozza corretto in PR206, come sull'etichetta del tubetto usato negli esercizi.
- **#8** `gbot/alberi-colori`: Alberi, tavolozza dei 6 colori e 12 miscele riviste (colore dominante, consistenza tè, latte, miele, pigmenti, convenzione delle dosi, tre prove), con collegamenti al calcolatore precompilato.
- **#9** `gbot/principi`: nuova sezione Principi generali, prima nell'indice, con ogni frase legata alla sua fonte; rimandi da Alberi e Teoria dei colori.
- **#10** `gbot/marche`: colori senza marche in Alberi e Teoria dei colori (nome comune e pigmento) e nuova sezione Marche e tubetti, con fonte ufficiale e data su ogni riga.

Sezioni pubblicate: 1 Principi generali, 2 Alberi, 3 Teoria dei colori, 4 Marche e tubetti.

**Attività aperte**:

1. **Taratura dei 6 colori del calcolatore.** Oggi i colori in `dati/colori/tavolozza.json` sono sRGB stimati a occhio, segnati «provvisorio». Vanno tarati su prove reali su carta: ogni colore steso a consistenza miele e tè, su bianco e su nero, fotografato.
2. **Illustrazioni dei Principi.** Da fotografare: i campioni tè, latte e miele, i momenti della carta (da bagnata ad asciutta), bordi netti e morbidi, fioriture, e le altre prove dei capitoli. Le foto sostituiscono o affiancano gli schemi SVG indicativi di oggi.
3. **Le tre prove di ogni miscela** (M1-M12 negli Alberi): da fare sul foglietto e fotografare, per sostituire i testi descrittivi con le immagini vere.
4. **Ricette del calcolatore.** Eventuale penalità di complessità, così la ricerca preferisce le miscele con meno colori e meno parti a parità di somiglianza.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Colori senza marche e nuova sezione «Marche e tubetti»

- Alberi e Teoria dei colori chiamano i sei colori col nome comune e il pigmento: giallo limone (PY175), ceruleo (PB15), cremisi (PR206), terra di Siena bruciata (PR101), terra d'ombra bruciata (PBr7 + PY42), blu oltremare (PB29). Tolti i nomi e i numeri Cotman, il «d'alizarina» del cremisi e i riferimenti a Winsor & Newton; il ceruleo ha la nota che è un blu ftalo e non il ceruleo vero (PB35). La trasparenza resta solo dove serve, come «nel tubetto della tavolozza».
- `dati/colori/tavolozza.json` e la tavolozza di `dati/alberi/` hanno gli stessi nomi; il controllo di coerenza del generatore degli alberi confronta ora nome, pigmento e trasparenza del tubetto. Il capitolo 4 di Teoria dei colori diventa «La mia tavolozza: sei colori di base» e rimanda alla nuova sezione.
- Nuova sezione `/marche/` (numero 4), da `dati/marche/`: il tubetto corrispondente a ogni colore in Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam e Maimeri Blu, con nome commerciale, numero o SKU, pigmenti, trasparenza, link alla pagina ufficiale e data di controllo su ogni riga; un capitolo «Stesso nome, pigmenti diversi» e l'elenco delle voci da guardare sull'etichetta. Per il cremisi Van Gogh solo la constatazione che la pagina ufficiale dei tubetti da 10 ml non ha un colore chiamato alizarina o cremisi.
- Aggiornati `SEZIONI`, README e `AGENTS.md`. Prova in Chrome senza interfaccia: nessun errore, nessuna ancora rotta, calcolatore con i nuovi nomi.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Nuova sezione «Principi generali»

Prima sezione del Quaderno: `/principi/`, generata da `dati/principi/` e messa in testa a `SEZIONI` (Alberi diventa la 2, Teoria dei colori la 3).

- Otto capitoli: le tre consistenze tè, latte, miele e la regola dei colori a consistenza simile; gli stati della carta (asciutta, umida, bagnata) e i momenti di mezzo legati al lucido dell'acqua; abbinare il pennello alla carta, fioriture comprese; il controllo dell'acqua; bordi netti e morbidi; l'asciugatura; la carta hot press, cold press e rough, peso e colla; una tabella riassuntiva. Due schemi SVG semplici (le tre consistenze, la scala da bagnata ad asciutta), dichiarati come indicativi.
- Ogni frase ha i suoi rimandi numerati alle fonti in fondo alla pagina: appunti sui corsi (Watercolor Fanatic, The Mind of Watercolor, video sulla carta) e video della sezione Alberi aperti al minuto. Il generatore si ferma se una frase non ha fonte, se una fonte manca o non è citata, o se resta un «da verificare».
- Alberi: la legenda della carta umida dice «opaca» e rimanda ai Principi; rimando anche nel riquadro «Come leggere le dosi» e come primo punto di «Come funziona questo tutorial».
- Teoria dei colori: il capitolo 3 perde i paragrafi su tè, latte, miele e sulla carta, sostituiti da un rimando ai Principi; l'etichetta della striscia di diluizione del calcolatore rimanda alle tre consistenze.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Alberi: tavolozza Cotman e 12 miscele riviste

- `dati/alberi/pit-261014-video-gesti-alberi.json`: la tavolozza diventa la lista dei 6 tubetti con nome, numero, pigmento e trasparenza (cremisi PR206, formula vecchia; la formula attuale W&N è PR179), uguale a `dati/colori/tavolozza.json`: il generatore si ferma se le due tavolozze non coincidono. Le 12 miscele hanno ora colore dominante e secondario, consistenza tè/latte/miele ricavata dalle schede dei video, pigmenti e, dove serve, una nota. Nuovi riquadri «Come leggere le dosi», dichiarato come convenzione da verificare sul foglietto e non come dato, e «Le tre prove per ogni miscela» (meno, come scritto, di più). Allineate alla proposta anche le ricette ripetute nei «Colori» di ogni albero.
- Due modifiche di sostanza: M9 ha ora il cremisi dominante con una punta di ceruleo; M11 è al latte e non più «diluito», come nella scheda del video.
- Collegamenti alla sezione Teoria dei colori e al calcolatore; ogni miscela ha «prova nel calcolatore», che apre il mescolatore coi tubetti già scelti. Le parti traducono la convenzione (colore base 10, punta 1, poco 3, un po' 4, quantità simili 10), e la pagina lo dice.
- `dati/colori/interfaccia.js`: nuovo parametro nell'indirizzo `?mix=id:parti,...` che precompila il mescolatore; un solo tubetto si legge «solo ...». `calcolatore.js`: virgola decimale anche nella notazione dei grigi (N 2,6).

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Cremisi della tavolozza: PR206

- In `dati/colori/tavolozza.json` il pigmento del Cotman Alizarin Crimson Hue (n. 3) passa da PR179 a PR206 (formula precedente verificata sull'etichetta del tubetto), con nota e fonte: la formula attuale Winsor & Newton è PR179 (https://www.winsornewton.com/en-ca/products/cotman-watercolour-alizarin-crimson-hue). La pagina mostra PR206 nella scheda del tubetto, nel mescolatore e nelle proposte; la pagina del prodotto è aggiunta alle fonti del capitolo sulla tavolozza.
- Colore sRGB del cremisi non ritoccato (#8E1C34): era un cremisi generico scelto a occhio, non un campione di PR179. Resta provvisorio come gli altri, da tarare sul tubetto.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Nuova sezione «Teoria dei colori» con calcolatore di miscele

Seconda sezione del Quaderno: `/colori/`, generata da `dati/colori/` e aggiunta a `SEZIONI` in `scripts/genera-sito.py`, quindi anche alla home.

- Una pagina con 5 capitoli: tinta, valore e croma secondo Munsell (con scala dei valori e ruota delle 40 tinte dalla renotation del 1943); luce e pigmento, additivo e sottrattivo, perché la ruota dei colori non predice le miscele, Kubelka-Munk; l'acquerello, cioè tè, latte, miele, stato della carta, mescolanza e velatura, granulazione; la tavolozza, con le schede dei 6 tubetti e i loro pigmenti dalla tabella ufficiale; il calcolatore. Testi in `teoria-colori.json`, con le fonti collegate a ogni capitolo (Wikipedia, handprint.com, huevaluechroma.com, Winsor & Newton).
- Calcolatore in JavaScript puro scritto per il Quaderno (`calcolatore.js`, `interfaccia.js`), tutto dentro l'html, nessuna libreria esterna: mescola 2 o 3 tubetti in parti intere con anteprima e striscia di diluizione dal miele al tè; cerca a forza bruta le 5 combinazioni di 1-3 tubetti con parti fino a 10 più vicine a un colore scelto, con distanza in OKLab; dà la notazione Munsell approssimata. Modello: Kubelka-Munk a una costante su 38 bande, con le tabelle spettrali di spectral.js (licenza MIT, testo della licenza in `spettri-spectraljs.js`).
- I colori dei 6 tubetti in `tavolozza.json` sono provvisori, scelti a occhio, e la pagina lo dice: vanno sostituiti con la taratura su prove reali.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Regola sul merge delle pull request

- In `CLAUDE.md` tolta la regola per cui la sessione cloud unisce da sé le pull request: l'unione su `main`, che pubblica il sito, si fa solo con approvazione esplicita per quella pull request.

-- GBOT-app-acquerello

## 2026-10-16 - CC - Pubblicazione automatica da GitHub

- Configurato il workflow `.github/workflows/sito.yml` con la variabile `PUBBLICA_CLOUDFLARE` = `si` e i secret `CLOUDFLARE_API_TOKEN` e `CLOUDFLARE_ACCOUNT_ID` per pubblicare automaticamente il sito su Cloudflare Pages a ogni unione su `main`.

## 2026-10-16 - CC - Repository autonomo su GitHub

- `scripts/genera-sito.py` genera il sito dai soli file del repository. In `dati/alberi/` sono inclusi i due csv della selezione dei video, le illustrazioni dei gesti e gli strumenti di prova della pagina.
- Aggiunti `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json` (che installa Pillow da `scripts/requisiti.txt`), `app-acquerello-261016-prompt-avvio-agente.md` e `.github/workflows/sito.yml`.

## 2026-10-15 - AGY - Creazione repository GitHub e pubblicazione su Cloudflare Pages

- Creata l'applicazione `app-acquerello` come contenitore multi-sezione per le guide pratiche di acquerello, con la prima sezione `/alberi/` e la home indice `/` testuale.
- Scritto `scripts/genera-sito.py` e pubblicato il sito statico su Cloudflare Pages (`app-acquerello.pages.dev`). Firma: AGY.

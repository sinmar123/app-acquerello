# Riferimenti bibliografici per il Quaderno di acquerello

Studio e proposta editoriale, 4 novembre 2026. Autore: Codex / CDX.

**Stato: proposta da sottoporre al curatore. Non applicata alle pagine del sito.**

## Sintesi della proposta

Si propone di conservare i **rimandi numerati e le «Fonti del capitolo»**, già presenti nel Quaderno. Ogni voce dovrebbe iniziare dall’autore o dall’ente responsabile, non da una classificazione della fonte. Seguono titolo originale, dati di pubblicazione e collegamento. Una breve frase italiana spiega, quando serve, che cosa documenta la fonte e quali limiti ha il suo impiego.

Le diciture «Primaria sperimentale:.» e «Primaria commerciale:.» andrebbero quindi sostituite, non perché «fonte primaria» sia un’espressione scorretta, ma perché non rispondono bene alle domande del lettore. Interessa sapere chi scrive, che cosa ha osservato, se vende il prodotto e se il Quaderno ha letto il testo o soltanto il riassunto.

Non si propone una nuova serie di etichette obbligatorie. «Scheda del produttore», «confronto di campioni» e «articolo scientifico» sono descrizioni da usare solo quando aggiungono informazione. Restano sempre visibili i limiti decisivi: lettura del solo riassunto, dichiarazioni commerciali, risultati ottenuti con materiali diversi da quelli della guida.

## 1. Oggetto e materiale esaminato

L’incarico proviene da Sandro, attraverso il topic dell’app, il 4 novembre 2026. Chiede uno studio sulle convenzioni italiane e una proposta per il sito, con terminologia italiana naturale e comprensibile. I titoli originali delle opere straniere vanno distinti dalle descrizioni italiane. Non autorizza modifiche alle pagine, pubblicazioni del sito o corse a pagamento con altri modelli.

Il caso è [5.2, Il blu oltremare nell’acquerello](https://app-acquerello.pages.dev/approfondimenti/blu-oltremare/). È stata usata la copia `lavoro/oc-261103-blu-oltremare`, commit `38416c4`, non il checkout principale arretrato. La [PR 67](https://github.com/sinmar123/app-acquerello/pull/67) risulta unita; il testo pubblico è stato acquisito direttamente dal sito.

Il confronto fra JSON e pagina pubblicata ha riscontrato tutte le **16 voci di fonte**, presenti in **otto elenchi di capitolo**. Per effetto delle ripetizioni fra capitoli, le voci visualizzate sono 31. I gruppi di richiami nel testo sono 36. Questi conteggi descrivono la struttura, non misurano la qualità delle prove.

Sono stati letti `AGENTS.md`, `README.md`, le voci pertinenti di `CHANGELOG.md`, `CONTRIBUTING.md`, il JSON della pagina e `scripts/rimandi_fonti.py`. Le indicazioni sulla lettura svolta nella ricerca del 3 novembre sono state conservate come registrazioni di quella ricerca: questo studio non è una nuova verifica scientifica integrale dei 15 documenti esterni.

## 2. Che cosa indicano le fonti italiane

### 2.1 Norma tecnica, regola di redazione e consuetudine

| Livello | Riscontro | Conseguenza per il Quaderno |
|---|---|---|
| Norma tecnica | La scheda UNI indica **UNI ISO 690:2021** in vigore. Riguarda riferimenti e citazioni per molte risorse, comprese opere artistiche e documenti digitali. | È un riferimento tecnico pertinente. La sua esistenza non dimostra che un sito divulgativo debba adottare un unico stile nazionale. |
| Indicazione bibliotecaria | Il Sistema Bibliotecario di Padova presenta autore-data, numeri e note. Richiede coerenza e identificazione dei documenti; non sceglie uno stile valido in ogni occasione. | Il criterio generale è rendere reperibile la fonte con un sistema uniforme. |
| Regola di una redazione scientifica | *AIB studi* richiede il sistema con richiami in apice e note bibliografiche. | È una prescrizione per i contributi a quella rivista, non per tutti i testi italiani. |
| Regola di un’istituzione culturale | Le norme di *DigItalia*, pubblicata dall’ICCU, prevedono note bibliografiche e ammettono, per apparati numerosi, richiami brevi autore-anno. | Anche entro una redazione esistono soluzioni diverse, motivate dalla forma del contributo. |
| Scelta didattica | Le linee guida di Archeologia dell’Università di Bologna suggeriscono autore-anno, da concordare con chi segue la tesi. | È un orientamento circoscritto, non una norma nazionale. |
| Consuetudine redazionale | Maiuscole, corsivi, punteggiatura, nomi estesi o abbreviati e separazione della sitografia variano fra le guide. | Il Quaderno deve fissare una propria convenzione, senza presentarla come l’unica italiana corretta. |

Fonti: [scheda UNI](https://store.uni.com/uni-iso-690-2021), [Sistema Bibliotecario di Padova](https://biblio.unipd.it/strumenti-di-ricerca/gestione-bibliografie), [AIB studi](https://aibstudi.aib.it/norme), [ICCU, norme di DigItalia, §§ 3.1-3.2, p. 11-15](https://www.iccu.sbn.it/export/sites/iccu/documenti/2022/Norme-redazionali-DigItalia.pdf), [Archeologia, Bologna, «Sistema di citazione»](https://corsi.unibo.it/magistrale/archeologia/linee-guida-per-la-prova-finale).

**Limite della verifica normativa:** della UNI ISO 690 è stata consultata la scheda pubblica, non il testo integrale a pagamento. Non si attribuiscono quindi alla norma requisiti di dettaglio non verificati. Del PDF ICCU, di 15 pagine, sono state estratte e lette le pagine 11-15, che contengono il capitolo sulle citazioni.

### 2.2 «Fonte primaria» è italiano corretto, ma non è un voto

L’Università di Firenze usa esplicitamente «fonti primarie» per i materiali oggetto della ricerca e «fonti secondarie» per gli studi critici e metodologici. È una distinzione scientifica italiana, non un’espressione da eliminare perché straniera. La sua definizione dipende anche dal contesto disciplinare. [Università di Firenze, La ricerca bibliografica](https://www.cl-llsi.unifi.it/vp-383-la-ricerca-bibliografica.html).

Per il caso del Quaderno, la distinzione va riferita alla domanda concreta:

- un articolo può presentare esperimenti originali e, nell’introduzione, riassumere studi storici altrui;
- il produttore è fonte diretta delle caratteristiche che dichiara per il proprio tubetto, ma non è per questo un valutatore indipendente;
- il pittore è testimone del proprio procedimento, non necessariamente dell’effetto su qualsiasi prodotto o carta;
- un museo può esporre risultati del proprio laboratorio oppure sintetizzare letteratura precedente.

Questa applicazione al caso è una valutazione editoriale dello studio. «Primaria» non significa automaticamente «più attendibile», «indipendente», «sperimentale» o «letta per intero». Per descrivere una fonte al pubblico, conviene dire direttamente quale di queste informazioni è pertinente.

## 3. Come organizzare rimandi ed elenchi

### 3.1 Numeri oppure autore-data

| Sistema | Vantaggio | Limite in questo sito |
|---|---|---|
| Autore-data | Nel testo si riconoscono subito autore e anno; utile quando si confrontano più studi. | Autori-ente lunghi, pagine senza data e più documenti dello stesso produttore appesantiscono una guida da telefono. |
| Numeri | Occupano poco spazio e funzionano bene per singole affermazioni e tabelle. | Il numero da solo non dice chi scrive: occorrono un elenco vicino e un ritorno al richiamo. |
| Note bibliografiche estese nel testo | Evitano il salto all’elenco. | Interrompono il procedimento pratico e ripetono molti dati. |

**Scelta proposta:** numerazione autonoma per capitolo, nell’ordine della prima citazione, come ora. Lo stesso numero, dentro lo stesso capitolo, rinvia sempre alla stessa fonte. Il numero può cambiare in un altro capitolo. Gli identificativi interni `F01`, `F02` ecc. restano stabili nei dati, ma non diventano sigle da spiegare al lettore.

Non è una prescrizione ricavata dalle guide universitarie: è la scelta editoriale ritenuta più adatta alla struttura esistente. Se nel discorso conta riconoscere l’autore, lo si nomina nella frase, mantenendo il richiamo numerico.

### 3.2 Fonti a fine capitolo oppure a fine pagina

**Si propone di mantenere le fonti a fine capitolo.** Il lettore che apre una parte della pagina trova lì anche il suo apparato. Nel caso esaminato, la ripetizione produce 31 voci per 16 fonti distinte: è un costo accettabile per rendere ogni capitolo consultabile da solo.

Un elenco unico a fine pagina ridurrebbe le ripetizioni, ma allontanerebbe molto le fonti dai capitoli iniziali. Non si propone di aggiungere anche una seconda bibliografia completa: si avrebbero due elenchi da mantenere e da distinguere. Un eventuale indice generale delle fonti del sito sarebbe un altro strumento, non necessario per questa revisione.

Per i rimandi fra capitoli, l’ancora deve comprendere il capitolo: non basta un generico `#fonte-1`. Questo è già previsto dal generatore esaminato.

### 3.3 Bibliografia e risorse in rete

«Sitografia» è una parola italiana usata anche nelle [indicazioni bibliografiche di Loredana Chines, Università di Bologna](https://www.unibo.it/sitoweb/loredana.chines/useful-contents/5f34e495). Non è quindi una forma da dichiarare sbagliata. La separazione, però, non è obbligatoria per il Quaderno.

**Si propone un elenco unico intitolato «Fonti del capitolo».** Un articolo scientifico non cessa di essere un articolo perché lo si legge in rete; lo stesso vale per un libro digitalizzato. Dividere in «bibliografia» e «siti» separerebbe risorse simili in base al mezzo di accesso. Nello stesso elenco possono invece convivere libro, articolo, scheda di museo, pagina commerciale e video, identificati correttamente.

Le letture utili ma non impiegate a sostegno del testo, se presenti, dovrebbero stare in un distinto «Per approfondire». Non dovrebbero essere mescolate alle fonti che sorreggono le affermazioni.

### 3.4 Telefono e ritorno al punto citato

Il generatore attuale conserva in JavaScript l’ultimo richiamo selezionato. La freccia della fonte riporta lì; senza JavaScript, il collegamento porta al primo richiamo di quella fonte nel capitolo. La pagina pubblicata usa anche «apri» per i collegamenti esterni e li apre in una nuova scheda.

La proposta conserva il ritorno, ma lo rende più esplicito:

- titolo della risorsa come collegamento, invece di una sequenza di generici «apri»;
- comando «Torna al testo», con nome accessibile che identifichi il richiamo;
- ritorno all’effettivo punto di partenza, anche da tastiera, e posizione non coperta dalla barra fissa;
- quando manca il contesto di partenza, collegamento al primo richiamo e possibilità di raggiungere gli altri punti che citano la fonte;
- fonti leggibili senza caratteri eccessivamente piccoli; indirizzi e DOI lunghi devono andare a capo;
- nessuna informazione essenziale disponibile soltanto al passaggio del mouse;
- apertura ordinaria dei collegamenti nella stessa scheda; se si mantiene la nuova scheda, indicazione riconoscibile e ritorno alla pagina del Quaderno non compromesso.

Sono raccomandazioni di progetto. Il [W3C, criterio 2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html), richiede che lo scopo del collegamento sia comprensibile nel contesto; «apri» non costituisce da solo una violazione automatica. Il [criterio 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) indica un minimo di 24 × 24 pixel CSS, con eccezioni fra cui i collegamenti nel testo. Non va trasformato nell’affermazione che ogni numero bibliografico debba obbligatoriamente misurare 24 × 24 pixel.

Non è stata eseguita una prova grafica su telefono né un collaudo con lettore di schermo. Le osservazioni sul comportamento attuale derivano da HTML e codice; l’eventuale realizzazione richiederà quelle prove.

## 4. Quali dati conservare

La proposta adotta un ordine semplice: **autore o ente. Titolo. Dati di pubblicazione. Collegamento. Eventuale nota d’uso.** È una convenzione del Quaderno, non una dichiarazione di aderenza integrale a uno stile codificato.

| Documento | Dati da riportare | Dati ulteriori quando pertinenti |
|---|---|---|
| Articolo scientifico | Autori, titolo, rivista, anno, volume e fascicolo se presenti, pagine o identificativo dell’articolo, DOI se assegnato. | Data completa se importante; versione consultata; sezione o figura cui si rinvia. |
| Libro | Autore, titolo, editore, anno dell’edizione effettivamente usata. | Edizione, curatore o traduttore se rilevanti; luogo se richiesto dalla convenzione o utile all’identificazione; pagina o capitolo per il passo citato. ISBN facoltativo. |
| Pagina di museo | Autore personale se firmata, altrimenti ente responsabile, titolo della pagina, museo o progetto, data o aggiornamento, collegamento alla pagina e consultazione. | Numero d’inventario solo quando serve a riconoscere l’opera discussa. |
| Scheda del produttore | Produttore, titolo o nome esatto del prodotto, gamma e variante necessarie a identificarlo, data o «senza data», collegamento diretto e consultazione. | Codice del prodotto o revisione del documento, se utili; descrizione «scheda del produttore». |
| Articolo di un pittore | Autore, titolo, sito o rivista, data e aggiornamento distinti, collegamento e consultazione. | Se riguarda campioni, materiali o esperienze personali, dirlo nella nota senza farne un giudizio generale di qualità. |
| Video | Autore o canale responsabile, titolo originale, piattaforma, data di pubblicazione, collegamento. | Inizio e fine del passaggio usato, durata se utile, consultazione; dichiarazione se si è letta soltanto una trascrizione. |

La base per gli elementi identificativi è il [Sistema Bibliotecario di Padova](https://biblio.unipd.it/strumenti-di-ricerca/gestione-bibliografie); le precisazioni per i materiali del Quaderno sono scelte operative di questo studio.

### Regole comuni proposte

1. **Autori:** nome e cognome nell’ordine diretto. Fino a tre, tutti; oltre tre, primo autore e «e altri». L’elenco completo resta nei dati, quando disponibile. L’ente che ospita una registrazione non sostituisce gli autori dell’articolo.
2. **Titoli:** originali e non riscritti in italiano. Una spiegazione italiana, se necessaria, è una frase distinta, non un titolo tradotto presentato come originale.
3. **Date:** per articoli e libri normalmente basta l’anno; per pagine e video si usa la data completa quando disponibile. Pubblicazione, aggiornamento, deposito e consultazione non sono intercambiabili.
4. **Collegamenti:** pagina del documento, non home del sito. Per gli articoli si preferisce il DOI risolvibile; l’eventuale copia liberamente accessibile può avere un secondo collegamento.
5. **DOI:** si mostra come indirizzo cliccabile `https://doi.org/...`, secondo le [indicazioni di Crossref](https://www.crossref.org/display-guidelines/). Il DOI identifica la risorsa, ma non certifica la qualità della ricerca o l’accesso gratuito.
6. **Consultazione:** necessaria per pagine mutevoli, schede commerciali e risorse senza data. Per un articolo identificato da DOI e versione non occorre ripeterla nella riga visibile, salvo che interessi documentare l’accesso al solo riassunto o una copia particolare. La data si conserva comunque nel registro interno. Questa selezione è una scelta editoriale; alcune redazioni la richiedono per tutti gli indirizzi web.
7. **Passi precisi:** un richiamo a una frase, tabella o passaggio video conserva pagina, figura, sezione o intervallo temporale. È un’informazione del richiamo, non necessariamente della citazione generale della fonte.

Le [norme AIB per le monografie](https://www.aib.it/pubblicazioni/libri/norme-redazionali-citazioni/) distinguono citazione generale e individuazione del passo e ammettono una dichiarazione comune della data di consultazione. Il Quaderno può accorpare una data comune solo se è vera per tutte le voci interessate; le date differenti vanno conservate.

### Dati mancanti

- Se manca la data della risorsa, scrivere **«senza data»**, dopo aver controllato pagina e documento. Non ricavarla dall’anno del copyright del sito.
- Se manca una firma personale ma la responsabilità dell’ente è chiara, indicare l’ente. Non attribuire al museo il ruolo di autore scientifico solo perché ospita un articolo altrui.
- Se non risultano né autore né ente responsabile, iniziare dal titolo. «Autore non indicato» si aggiunge soltanto se la mancanza conta per la valutazione.
- Se non c’è un titolo formale, dare una breve descrizione redazionale dichiarata come tale, senza simulare un titolo d’autore.
- Se non risultano DOI, fascicolo o pagine, non inventarli e non lasciare campi vuoti visibili. Un identificativo d’articolo non va trasformato in un numero di pagina.
- Se esiste una data di revisione ma non quella di pubblicazione, indicare **«aggiornato il…»**. Una revisione della pagina non data automaticamente tutti i suoi esperimenti.
- Per un contenuto ritirato o non più raggiungibile, conservare gli estremi e dichiarare l’eventuale copia consultata. Un risultato del motore di ricerca non equivale alla lettura della fonte.

## 5. Descrizione della fonte e limiti della lettura

Sono informazioni diverse e vanno registrate separatamente:

| Domanda | Esempio | Che cosa non autorizza a dire |
|---|---|---|
| Che documento è? | Articolo scientifico, video, scheda di prodotto. | Che sia attendibile per ogni affermazione. |
| Chi lo produce? | Museo, produttore, pittore, gruppo di ricerca. | Che sia indipendente da interessi commerciali. |
| Su che cosa si basa? | Esperimenti, campioni dipinti, sintesi di studi, esperienza personale. | Che i risultati valgano per tutti i materiali. |
| Che cosa è stato consultato? | Testo, sezioni pertinenti, solo riassunto, trascrizione. | Che il resto sia stato letto o verificato. |
| Per quale affermazione serve? | Dati dichiarati per un tubetto, analisi di un’opera, comportamento di una miscela. | Che sostenga altre conclusioni non documentate. |

### Quanto mostrare al lettore

**Nella voce, sempre visibile:** il limite che cambia il peso dell’informazione. Esempi pronti all’uso:

- «Consultato soltanto il riassunto; testo integrale non letto.»
- «Scheda del produttore; caratteristiche dichiarate per questo prodotto.»
- «Confronto di campioni dell’autrice; le riproduzioni non sono misure del colore.»
- «Lo studio riguarda olio e resina, non acquerello su carta.»

**Nel registro di lavoro:** sezioni lette, copia consultata, data effettiva, versione, eventuali allegati non esaminati e motivi di una valutazione di indipendenza. Queste informazioni si conservano, ma non tutte devono occupare ogni voce pubblica.

**Nel corpo del capitolo:** il limite da conoscere prima di accettare l’affermazione. Se un risultato riguarda un altro legante, non basta nascondere la cautela nell’elenco delle fonti. Analogamente, «secondo il produttore» deve accompagnare l’affermazione quando altrimenti sembrerebbe una verifica del Quaderno.

Il «testo integrale letto» non è un certificato di correttezza, e «consultate le sezioni pertinenti» non significa «letto tutto». Non si propone di cancellare le indicazioni positive di lettura: si spostano nel registro, rendendole disponibili nei dettagli se utili. I limiti negativi decisivi rimangono subito leggibili.

Anche **«indipendente» richiede un riscontro**. Una pagina personale non basta a escludere collaborazioni, sponsorizzazioni o interessi. In assenza di verifica, è più preciso descrivere prove e materiali, senza assegnare alla persona un’etichetta generale.

## 6. Esempi prima/dopo dalla pagina sul blu oltremare

I codici seguenti sono quelli del JSON, non numeri proposti per la pagina. In «Prima» è riportata soltanto l’apertura attuale: il resto della voce non è cancellato tacitamente. Il «Dopo» è una formulazione completa proposta. I limiti della lettura del 3 novembre derivano dalle voci attuali; i metadati aggiunti sono stati riscontrati sulle pagine collegate il 4 novembre.

### F01. Un articolo con esperimenti originali

**Prima:** «Primaria sperimentale:.»

**Dopo:**

Ian Hamerton, Lauren Tedaldi, Nicholas Eastaugh. *A Systematic Examination of Colour Development in Synthetic Ultramarine According to Historical Methods*. «PLOS ONE», 8(2), 2013, e50364. [https://doi.org/10.1371/journal.pone.0050364](https://doi.org/10.1371/journal.pone.0050364).

Consultati il riassunto, l’introduzione, i metodi e la discussione chimica. Gli esperimenti riguardano la preparazione del pigmento, non prove di acquerello su carta; la parte storica ricostruisce studi precedenti.

**Motivo:** recupera gli autori, assenti nella voce attuale, e identifica articolo e ambito senza trasformare «primaria» in una garanzia generale. Autori, volume, fascicolo e identificativo sono verificabili sulla [pagina della rivista](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0050364).

### F02. Una scheda di museo

**Prima:** «Museo, sintesi tecnico-scientifica del progetto:.»

**Dopo:**

Fitzwilliam Museum. *[Ultramarine](https://fitzmuseum.cam.ac.uk/illuminated/lab/overview-of-artists-materials/ultramarine/type/material)*. Progetto ILLUMINATED: Manuscripts in the making, senza data. Consultato il 4 novembre 2026.

Scheda sul pigmento e sulla sua identificazione nei manoscritti studiati dal museo.

**Motivo:** l’ente e il progetto identificano la provenienza. La descrizione italiana precisa l’oggetto; non si attribuisce alla pagina un esperimento di stesura ad acquerello. La registrazione di lettura integrale resta nel materiale di ricerca.

### F03. Una pagina di prove personali

**Prima:** «Primaria indipendente per i test dell’autore:.»

**Dopo:**

Bruce MacEvoy. *[Guide to watercolor pigments: blue](https://www.handprint.com/HP/WCL/waterb.html#PB29)*, sezione PB29. Handprint, pagina aggiornata il 7 gennaio 2015. Consultato il 4 novembre 2026.

Prove e osservazioni dell’autore sui prodotti esaminati, con riferimenti storici. Nella ricerca è stata letta la sezione PB29 dal testo completo; la data della pagina non identifica quella di ogni singola prova.

**Motivo:** descrive ciò che è documentato, senza certificare un’indipendenza non verificata in questo studio. Il fondo della pagina riporta «Last revised 07.I.2015»; questo permette di precisare l’aggiornamento senza datare retroattivamente tutti i risultati.

### F05. Il confronto di una pittrice

**Prima:** «Primaria testimoniale e comparativa:.»

**Dopo:**

Jane Blundell. *[Watercolour Comparisons 1 Ultramarine Blue PB29](https://janeblundellart.blogspot.com/2013/06/watercolour-comparisons-1-ultramarine.html)*. Jane Blundell Artist, 18 giugno 2013; aggiornamento dichiarato nel 2015, con ulteriori aggiunte non datate singolarmente. Consultato il 4 novembre 2026.

Confronto di campioni dell’autrice. Le riproduzioni dei colori non sono misure colorimetriche.

**Motivo:** conserva il valore della testimonianza diretta senza la formula astratta «testimoniale e comparativa». L’avvertenza sulle riproduzioni è coerente anche con le cautele dell’autrice su scansioni e resa del colore. Titolo, data e aggiornamento sono stati riscontrati nel testo acquisito direttamente dal blog.

### F07. Una scheda del produttore

**Prima:** «Primaria commerciale:.»

**Dopo:**

Da Vinci. *[Ultramarine (Green Shade) (8mL Watercolor)](https://davincipaints.com/ultramarine-green-shade-8ml-watercolor/)*. Senza data. Consultato il 4 novembre 2026.

Scheda del produttore; caratteristiche dichiarate per questo prodotto, non verificate qui con prove indipendenti.

**Motivo:** il titolo identifica la variante, mentre la frase italiana chiarisce l’interesse commerciale e il limite del riscontro. Non si declassa automaticamente la fonte: è appropriata per sapere che cosa il produttore dichiara.

### F10. Una versione depositata in un archivio

**Prima:** «Primaria sperimentale, versione preprint:.»

**Dopo:**

Jorge González-Gutiérrez e altri. *[Pattern formation by droplet evaporation and imbibition in watercolor paintings](https://arxiv.org/abs/1909.09098v1)*. arXiv:1909.09098v1, manoscritto di ricerca depositato il 19 settembre 2019. [Testo consultato nella ricerca: resa HTML](https://arxiv.org/html/1909.09098v1).

Consultati metodi, risultati e discussione pertinenti; non esaminati separatamente tutti i materiali supplementari. La data del deposito non coincide con quella mostrata nella resa HTML successiva.

**Motivo:** descrive in italiano la versione senza alterare il titolo e non pretende di certificare lo stato editoriale di tutte le versioni del lavoro. La [scheda arXiv della versione](https://arxiv.org/abs/1909.09098v1) conferma autori e deposito; la data del 2026 nella pagina HTML non sostituisce quella del 2019. La scheda, da sola, non dimostra l’identità testuale fra la resa HTML successiva e il file originariamente depositato: il registro deve conservare quale testo è stato effettivamente letto.

### F11. Un articolo conosciuto soltanto attraverso il riassunto

**Prima:** «Primaria scientifica, solo abstract:.»

**Dopo:**

Eleonora Del Federico e altri. *Insight into Framework Destruction in Ultramarine Pigments*. «Inorganic Chemistry», 45(3), 2006, p. 1270-1276. [https://doi.org/10.1021/ic050903z](https://doi.org/10.1021/ic050903z). [Registrazione con riassunto](https://digitalcommons.montclair.edu/chem-biochem-facpubs/501/), consultata il 4 novembre 2026.

**Consultato soltanto il riassunto; testo integrale non letto.**

**Motivo:** la limitazione non si perde nell’apertura della voce e non si confonde con il tipo di documento. Autori, anno e DOI sono nella registrazione dell’università; volume, fascicolo e pagine sono stati riscontrati nei [metadati DOI di Crossref](https://api.crossref.org/works/10.1021/ic050903z). Il testo integrale non è stato recuperato per questo studio.

### F12. Un riassunto ospitato da un’università

**Prima:** «Primaria scientifica, solo abstract istituzionale:.»

**Dopo:**

E. René de la Rie e altri. *Photo-catalytic degradation of binding media of ultramarine blue containing paint layers: A new perspective on the phenomenon of “ultramarine disease” in paintings*. «Polymer Degradation and Stability», 144, 2017, p. 43-52. [https://doi.org/10.1016/j.polymdegradstab.2017.08.002](https://doi.org/10.1016/j.polymdegradstab.2017.08.002). [Registrazione con riassunto nel portale TU Delft](https://research.tudelft.nl/en/publications/photo-catalytic-degradation-of-binding-media-of-ultramarine-blue-/), consultata il 4 novembre 2026.

**Consultato soltanto il riassunto; testo integrale non letto.** Gli esperimenti riguardano olio di lino e resina, non acquerello su carta.

**Motivo:** aggiunge autore e titolo completo, distinguendo l’articolo dal portale che ne ospita i dati. «Istituzionale» descrive il sito consultato, non un diverso tipo di riassunto o una verifica indipendente dei risultati.

### F15. Il resoconto di un laboratorio museale

**Prima:** «Primaria museale, resoconto del laboratorio:.»

**Dopo:**

Marina Ruiz Molina. *[What Lies Beneath a Tiffany Drawing, Part Two](https://www.metmuseum.org/perspectives/conservation-louis-comfort-tiffany)*. The Metropolitan Museum of Art, 26 febbraio 2018. Consultato il 4 novembre 2026.

Resoconto di conservazione con analisi dei pigmenti su opere della collezione. Documenta i casi esaminati, non una prova generale sulla durata degli acquerelli.

**Motivo:** autore, museo e descrizione separano responsabilità, sede e contenuto. La cautela impedisce di generalizzare un risultato analitico su opere particolari. La lettura registrata nella ricerca del 3 novembre non viene trasformata in una nuova analisi delle opere.

### Due precisazioni prima dell’eventuale applicazione

La F06 chiama «tabella tecnica» il documento ma collega la pagina generale *Professional Watercolour*. Nel testo HTML acquisito il 4 novembre non è stato individuato un prospetto tecnico completo. Prima di cambiare la voce andrà riscontrato il documento effettivamente usato nella ricerca e, se possibile, collegata la tabella precisa. La mancata individuazione nel testo acquisito non dimostra che il sito non offra una tabella tramite altre funzioni.

La fonte interna `quaderno-prove` non deve sembrare un risultato sperimentale. La formula proposta è: «Quaderno di acquerello. Proposta di prove comparative sul blu oltremare, 3 novembre 2026. Esercizi da svolgere sui propri materiali; non sono prove già eseguite né un protocollo normalizzato». Il collegamento, se aggiunto, dovrà portare alla sezione delle prove, non simulare una pubblicazione esterna.

## 7. Modelli d’uso trasferibili alle altre sezioni

Gli esempi della sezione 6 costituiscono già i modelli completi per articolo, museo, produttore e pittore. Per libro e video, non presenti fra le fonti del blu oltremare, si aggiungono due esempi reali. Servono a mostrare la forma e non diventano nuove prove a sostegno della pagina.

### Libro

Jeanne Dobie. *Making Color Sing*. Edizione del venticinquesimo anniversario. Watson-Guptill, 2011. ISBN 9780823031153. [Scheda dell’editore](https://www.penguinrandomhouse.com/books/203191/making-color-sing-25th-anniversary-edition-by-jeanne-dobie/).

In questo studio sono stati verificati soltanto i dati editoriali della scheda, non il contenuto del libro. In una guida che utilizzasse un suo passo andrebbero indicate le pagine effettivamente lette. L’anno deve restare quello di questa edizione, non quello della prima edizione.

### Video

Paul Clark. *[How to paint trees in Watercolour by Paul Clark](https://www.youtube.com/watch?v=ygV5PuvzjE4)*. YouTube, 25 aprile 2020. Consultati i dati della pagina il 4 novembre 2026.

Questo è un esempio bibliografico: non dichiara la visione integrale del filmato. Per un passaggio didattico si aggiungono l’intervallo effettivamente usato e il collegamento temporizzato, dopo averli verificati. Se si è letta soltanto la trascrizione, si scrive «Consultata la trascrizione del passaggio citato; filmato non visionato», senza inventare un intervallo.

### Testo introduttivo pronto per un elenco di fonti

«I numeri nel testo rimandano alle fonti elencate alla fine di ogni capitolo. Per ogni documento sono indicati l’autore o l’ente responsabile, il titolo e i dati utili a ritrovarlo. Quando la consultazione è limitata al riassunto, o i dati provengono dal produttore, la voce lo precisa. I titoli restano nella lingua originale.»

### Organizzazione dei dati, senza cambiare ora il generatore

Una sola registrazione per fonte dovrebbe contenere separatamente:

- identificativo stabile;
- autori o ente responsabile;
- titolo originale e sede di pubblicazione;
- data di pubblicazione, aggiornamento ed eventuale versione;
- volume, fascicolo, pagine o identificativo, quando presenti;
- DOI e indirizzo del documento effettivamente consultato;
- data di consultazione;
- tipo di documento e provenienza, come dati distinti;
- ampiezza della lettura e copia usata;
- nota pubblica breve e registrazione interna più estesa, quando necessaria.

Pagina, figura, sezione e intervallo temporale appartengono invece al singolo richiamo. Non si propone di imporre tutte le chiavi a ogni tipo di documento: un video non ha un fascicolo, una scheda commerciale può non avere una data editoriale.

La forma pubblica si genera da questi dati. Le registrazioni di lettura già presenti non vanno eliminate durante la separazione dei campi. Non serve introdurre per forza un nuovo programma bibliografico: il primo intervento può riguardare soltanto la struttura dei dati esistenti.

## 8. Decisione proposta e applicazione successiva

Si propone al curatore un unico indirizzo editoriale:

1. conservare numeri e fonti per capitolo;
2. iniziare le voci con autore o ente, non con «primaria…»;
3. usare un solo elenco «Fonti del capitolo», senza separare automaticamente la sitografia;
4. conservare titoli originali e descrivere in italiano documento, uso e limiti;
5. lasciare subito visibili lettura del solo riassunto, provenienza commerciale e limiti di trasferibilità;
6. registrare a parte il dettaglio della lettura, senza perdere quello già raccolto;
7. rendere espliciti collegamenti e ritorno al testo, verificandoli poi su telefono e da tastiera.

L’eventuale applicazione dovrebbe partire dalle fonti della pagina 5.2 e dal modulo condiviso dei rimandi, poi estendersi alle altre guide. Prima di pubblicare andranno confrontate le nuove voci con le vecchie, verificando che nessun limite sia scomparso. Andranno inoltre provati ritorni, ancore, apertura dei collegamenti, numerazione nei diversi capitoli e leggibilità dei titoli lunghi.

**Questo studio non ha modificato JSON, generatori, pagine HTML o contenuti pubblicati. La scelta editoriale e l’applicazione attendono la valutazione di Sandro.**

## Fonti dello studio

Tutte consultate il 4 novembre 2026. Le fonti specifiche sul blu oltremare sono collegate negli esempi; qui si raccolgono gli orientamenti generali.

- UNI, [UNI ISO 690:2021](https://store.uni.com/uni-iso-690-2021): consultata la scheda pubblica, non il testo normativo integrale.
- Università di Padova, Sistema Bibliotecario di Ateneo, [Gestione bibliografie](https://biblio.unipd.it/strumenti-di-ricerca/gestione-bibliografie): sistemi citazionali ed elementi identificativi dei documenti.
- *AIB studi*, [Norme redazionali](https://aibstudi.aib.it/norme): convenzione della rivista e data di consultazione degli indirizzi web.
- Associazione Italiana Biblioteche, [Norme per le citazioni bibliografiche e la bibliografia finale](https://www.aib.it/pubblicazioni/libri/norme-redazionali-citazioni/): versione indicata dalla pagina come aggiornata ad aprile 2021; campo di applicazione alle monografie, esclusa la collana ET.
- ICCU, [Norme redazionali di DigItalia](https://www.iccu.sbn.it/export/sites/iccu/documenti/2022/Norme-redazionali-DigItalia.pdf), p. 11-15: citazioni bibliografiche e documenti in rete. Il nome della cartella web non è assunto come data di edizione del PDF.
- Università di Bologna, Laurea magistrale in Archeologia, [Linee guida per la prova finale](https://corsi.unibo.it/magistrale/archeologia/linee-guida-per-la-prova-finale): scelta del sistema e bibliografia finale.
- Università di Firenze, [La ricerca bibliografica](https://www.cl-llsi.unifi.it/vp-383-la-ricerca-bibliografica.html), aggiornamento indicato 31 ottobre 2025: uso italiano di fonti primarie e secondarie nel contesto della ricerca umanistica.
- Loredana Chines, Università di Bologna, [Norme bibliografiche per tesi di laurea e laurea magistrale](https://www.unibo.it/sitoweb/loredana.chines/useful-contents/5f34e495): esempio di convenzione didattica che distingue bibliografia e sitografia.
- Crossref, [Display guidelines](https://www.crossref.org/display-guidelines/): presentazione dei DOI come collegamenti risolvibili.
- W3C, [Understanding SC 2.4.4: Link Purpose (In Context)](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html) e [Understanding SC 2.5.8: Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): documenti esplicativi dei criteri WCAG, non norme bibliografiche italiane.

Prossima azione: sottoporre questa proposta editoriale a Sandro, senza applicarla al sito prima della sua decisione.

Firma: Codex / CDX.

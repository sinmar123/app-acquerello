# CHANGELOG - app-acquerello

Cronologia delle modifiche. Ordine cronologico inverso.

## 2026-10-19 - AGY - Sezione Alberi ristrutturata per modalità video con 24 infografiche e doppia proposta colori

Su richiesta e approvazione di Sandro, rivista l'intera sezione `/alberi/` (`dati/alberi/`) sul ramo `agy/alberi-modalita-video`:

- **Sganciamento completo dall'immagine del lago**: rimosso l'esercizio `A7` (Riflessi nell'acqua ferma) e tutti i riferimenti residui a lago, riva, specchio d'acqua e montagna; sostituite in testa ai 6 esempi (`A1`-`A6`) le foto di riferimento del lago con gli studi autonomi ad acquerello su foglietto A5 (`pit-261013-illustrazione-A1..A6.png`). Chiarito in apertura che i 6 soggetti (abeti in gruppo, abeti alti e radi, chiome tonde d'autunno, siepi e cespugli, alberi invernali con fusti chiari e brina, rami sottili e foglie in primo piano) sono solo alcuni esempi rappresentativi da cui partire, a cui se ne possono affiancare molti altri.
- **Struttura per modalità video + un'infografica SVG per ciascun video**: sostituita la sequenza mista di passi con **24 schede di modalità possibili** (una per ogni video di interesse, rimuovendo i 3 estratti duplicati `A2-4`, `A2-5`, `A4-2`, per un totale di 31 estratti video). Ogni modalità espone cosa propone il video, i colori e i pennelli usati dall'autore (ricavati dalle schede Gemini in `pit/acquerello-alberi/schede/`, senza marche commerciali), un'**infografica SVG in 3 fasi** dedicata specificamente a quel video (72 vignette SVG totali in `pit-261015-infografiche.py`) e i relativi estratti nel player. Mantenuto `id="A1-3"` sul blocco video per preservare il rimando diretto da `/principi/`.
- **Impostazione dei colori (studio vs aperto)**: superato il vincolo dei soli 6 colori; per ogni esempio e per ogni modalità sono indicati sia i **colori liberi da studio** (verdi pronti, terre naturali e bruciate, turchese di cobalto, blu ftalo, blu di Prussia, indaco, grigio di Payne, seppia, ecc.) sia il rimando alla **tavolozza ridotta da 6 colori di base e 12 miscele (`M1`-`M12`)** pensata per quando si dipinge all'aperto (*en plein air*) o con una scatola leggera.

Prossima azione: dopo la verifica e l'eventuale approvazione di Sandro, unire la pull request su `main` per pubblicare su Cloudflare Pages; proseguire con la taratura dei 6 colori del calcolatore e le foto dei campioni per Principi e miscele.

-- AGY

## 2026-10-18 - GBOT-app-acquerello - Chiusura giornata e consegne per il prossimo agente

Riepilogo delle pull request del 18/10/2026, tutte unite su `main` da Sandro e pubblicate:

- **#5** `gbot/regola-merge-claude-md`: tolta da `CLAUDE.md` la regola del merge automatico della sessione cloud; l'unione su `main` si fa solo con l'ok di Sandro.
- **#6** `gbot/teoria-colori`: nuova sezione Teoria dei colori (Munsell, luce e pigmento, acquerello, tavolozza) con il calcolatore di miscele in JavaScript che gira nel browser.
- **#7** `gbot/cremisi-pr206`: cremisi della tavolozza corretto in PR206, come sull'etichetta del tubetto di Sandro.
- **#8** `gbot/alberi-colori`: Alberi, tavolozza dei 6 colori e 12 miscele riviste (colore dominante, consistenza tè, latte, miele, pigmenti, convenzione delle dosi, tre prove), con collegamenti al calcolatore precompilato.
- **#9** `gbot/principi`: nuova sezione Principi generali, prima nell'indice, con ogni frase legata alla sua fonte; rimandi da Alberi e Teoria dei colori.
- **#10** `gbot/marche`: colori senza marche in Alberi e Teoria dei colori (nome comune e pigmento) e nuova sezione Marche e tubetti, con fonte ufficiale e data su ogni riga.

Sezioni pubblicate: 1 Principi generali, 2 Alberi, 3 Teoria dei colori, 4 Marche e tubetti. Il README è allineato.

**Prossima azione** (cose aperte per il prossimo agente):

1. **Taratura dei 6 colori del calcolatore.** Oggi i colori in `dati/colori/tavolozza.json` sono sRGB stimati a occhio, segnati «provvisorio». Vanno tarati sulle prove di Sandro: ogni colore steso a consistenza miele e tè, su bianco e su nero, fotografato.
2. **Illustrazioni dei Principi.** Da fotografare: i campioni tè, latte e miele, i momenti della carta (da bagnata ad asciutta), bordi netti e morbidi, fioriture, e le altre prove dei capitoli. Le foto sostituiscono o affiancano gli schemi SVG indicativi di oggi.
3. **Le tre prove di ogni miscela** (M1-M12 negli Alberi): da fare sul foglietto e fotografare, per sostituire i testi descrittivi con le immagini vere.
4. **Ricette del calcolatore.** Eventuale penalità di complessità, così la ricerca preferisce le miscele con meno colori e meno parti a parità di somiglianza.
5. **Vaghezze residue nei passi Alberi, non toccate oggi**: «un po' di cremisi» in A3-2 e A4-2, e le indicazioni ancora vaghe nei passi di A6 e A7, da rileggere passo per passo.

**Regola**: si lavora su un ramo e si chiude con una pull request; l'unione su `main` (che pubblica il sito) solo con l'ok esplicito di Sandro.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Colori senza marche e nuova sezione «Marche e tubetti»

Con l'ok di Sandro alla proposta del 18/10 preparata da GBOT-app-acquerello. Parte dal ramo `gbot/principi`.

- Alberi e Teoria dei colori chiamano i sei colori col nome comune e il pigmento: giallo limone (PY175), ceruleo (PB15), cremisi (PR206), terra di Siena bruciata (PR101), terra d'ombra bruciata (PBr7 + PY42), blu oltremare (PB29). Tolti i nomi e i numeri Cotman, il «d'alizarina» del cremisi e i riferimenti a Winsor & Newton; il ceruleo ha la nota che è un blu ftalo e non il ceruleo vero (PB35). La trasparenza resta solo dove serve, come «nel tubetto della tavolozza».
- `dati/colori/tavolozza.json` e la tavolozza di `dati/alberi/` hanno gli stessi nomi; il controllo di coerenza del generatore degli alberi confronta ora nome, pigmento e trasparenza del tubetto. Il capitolo 4 di Teoria dei colori diventa «La mia tavolozza: sei colori di base» e rimanda alla nuova sezione.
- Nuova sezione `/marche/` (numero 4), da `dati/marche/`: il tubetto corrispondente a ogni colore in Winsor & Newton Cotman e Professional, Van Gogh, Daniel Smith, Schmincke Horadam e Maimeri Blu, con nome commerciale, numero o SKU, pigmenti, trasparenza, link alla pagina ufficiale e data di controllo su ogni riga; un capitolo «Stesso nome, pigmenti diversi» e l'elenco delle voci da guardare sull'etichetta. Per il cremisi Van Gogh solo la constatazione che la pagina ufficiale dei tubetti da 10 ml non ha un colore chiamato alizarina o cremisi.
- Aggiornati `SEZIONI`, README e `AGENTS.md`. Prova in Chrome senza interfaccia: nessun errore, nessuna ancora rotta, calcolatore con i nuovi nomi.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Nuova sezione «Principi generali»

Con l'ok di Sandro alla proposta del 18/10 preparata da GBOT-app-acquerello, prima sezione del Quaderno: `/principi/`, generata da `dati/principi/` e messa in testa a `SEZIONI` (Alberi diventa la 2, Teoria dei colori la 3).

- Otto capitoli: le tre consistenze tè, latte, miele e la regola dei colori a consistenza simile; gli stati della carta (asciutta, umida, bagnata) e i momenti di mezzo legati al lucido dell'acqua; abbinare il pennello alla carta, fioriture comprese; il controllo dell'acqua; bordi netti e morbidi; l'asciugatura; la carta hot press, cold press e rough, peso e colla; una tabella riassuntiva. Due schemi SVG semplici (le tre consistenze, la scala da bagnata ad asciutta), dichiarati come indicativi.
- Ogni frase ha i suoi rimandi numerati alle fonti in fondo alla pagina: appunti di Sandro sui corsi (Watercolor Fanatic, The Mind of Watercolor, video sulla carta) e video della sezione Alberi aperti al minuto. Il generatore si ferma se una frase non ha fonte, se una fonte manca o non è citata, o se resta un «da verificare». Rimasti fuori, come deciso da Sandro, «satinata» per la hot press e la carta umida «fredda»; «umida» è descritta dagli esempi dei video, e la pagina lo dice.
- Alberi: la legenda della carta umida dice «opaca» (tolto «fredda») e rimanda ai Principi; rimando anche nel riquadro «Come leggere le dosi» e come primo punto di «Come funziona questo tutorial».
- Teoria dei colori: il capitolo 3 perde i paragrafi su tè, latte, miele e sulla carta, sostituiti da un rimando ai Principi; l'etichetta della striscia di diluizione del calcolatore rimanda alle tre consistenze.
- Aggiornati README e `AGENTS.md`. Prova in Chrome senza interfaccia: nessun errore, nessuna ancora rotta, rimandi interni corretti.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Alberi: tavolozza Cotman e 12 miscele riviste

Con l'ok di Sandro alla proposta sui testi delle miscele (bozza del 18/10 preparata da GBOT-app-acquerello).

- `dati/alberi/pit-261014-video-gesti-alberi.json`: la tavolozza diventa la lista dei 6 tubetti Winsor & Newton Cotman con nome, numero, pigmento e trasparenza (cremisi PR206, formula vecchia; la formula attuale W&N è PR179), uguale a `dati/colori/tavolozza.json`: il generatore si ferma se le due tavolozze non coincidono. Le 12 miscele hanno ora colore dominante e secondario, consistenza tè/latte/miele ricavata dalle schede dei video, pigmenti e, dove serve, una nota. Nuovi riquadri «Come leggere le dosi», dichiarato come convenzione da verificare sul foglietto e non come dato, e «Le tre prove per ogni miscela» (meno, come scritto, di più). Allineate alla proposta anche le ricette ripetute nei «Colori» di ogni albero; i testi dei passi non cambiano.
- Due modifiche di sostanza: M9 ha ora il cremisi dominante con una punta di ceruleo; M11 è al latte e non più «diluito», come nella scheda del video.
- Collegamenti alla sezione Teoria dei colori e al calcolatore; ogni miscela ha «prova nel calcolatore», che apre il mescolatore coi tubetti già scelti. Le parti traducono la convenzione (colore base 10, punta 1, poco 3, un po' 4, quantità simili 10), e la pagina lo dice.
- `dati/colori/interfaccia.js`: nuovo parametro nell'indirizzo `?mix=id:parti,...` che precompila il mescolatore; un solo tubetto si legge «solo ...». `calcolatore.js`: virgola decimale anche nella notazione dei grigi (N 2,6).
- Prova in Chrome senza interfaccia: i 13 collegamenti aprono il mescolatore con i colori giusti, nessun errore in console.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Cremisi della tavolozza: PR206

- Sandro ha controllato l'etichetta: il suo Cotman Alizarin Crimson Hue (n. 3) è PR206, la formula vecchia. In `dati/colori/tavolozza.json` il pigmento passa da PR179 a PR206, con nota e fonte: la formula attuale Winsor & Newton è PR179 (https://www.winsornewton.com/en-ca/products/cotman-watercolour-alizarin-crimson-hue). La pagina mostra PR206 nella scheda del tubetto, nel mescolatore e nelle proposte; la pagina del prodotto è aggiunta alle fonti del capitolo sulla tavolozza.
- Colore sRGB del cremisi non ritoccato (#8E1C34): era un cremisi generico scelto a occhio, non un campione di PR179. Resta provvisorio come gli altri, da tarare sul tubetto.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Nuova sezione «Teoria dei colori» con calcolatore di miscele

Su richiesta di Sandro, seconda sezione del Quaderno: `/colori/`, generata da `dati/colori/` e aggiunta a `SEZIONI` in `scripts/genera-sito.py`, quindi anche alla home.

- Una pagina con 5 capitoli: tinta, valore e croma secondo Munsell (con scala dei valori e ruota delle 40 tinte dalla renotation del 1943); luce e pigmento, additivo e sottrattivo, perché la ruota dei colori non predice le miscele, Kubelka-Munk; l'acquerello, cioè tè, latte, miele, stato della carta, mescolanza e velatura, granulazione; la tavolozza, con le schede dei 6 tubetti Winsor & Newton Cotman e i loro pigmenti dalla tabella ufficiale; il calcolatore. Testi in `teoria-colori.json`, con le fonti collegate a ogni capitolo (Wikipedia, handprint.com, huevaluechroma.com, Winsor & Newton).
- Calcolatore in JavaScript puro scritto per il Quaderno (`calcolatore.js`, `interfaccia.js`), tutto dentro l'html, nessuna libreria esterna: mescola 2 o 3 tubetti in parti intere con anteprima e striscia di diluizione dal miele al tè; cerca a forza bruta le 5 combinazioni di 1-3 tubetti con parti fino a 10 più vicine a un colore scelto, con distanza in OKLab; dà la notazione Munsell approssimata. Modello: Kubelka-Munk a una costante su 38 bande, con le tabelle spettrali di spectral.js (licenza MIT, testo della licenza in `spettri-spectraljs.js`). Niente Mixbox né codice di ArtistAssistApp, che è solo collegata.
- I colori dei 6 tubetti in `tavolozza.json` sono provvisori, scelti a occhio, e la pagina lo dice: vanno sostituiti con la taratura sulle prove di Sandro. In pagina anche i limiti del calcolatore.
- Prove nel browser senza interfaccia: giallo limone + oltremare 1:1 dà un verde (7,5GY 6,2/6,1), oltremare + Siena bruciata 1:1 un grigio scuro (7Y 2,9/1,1), oltremare + cremisi un viola; nessun errore nella console e nessuna richiesta esterna.
- Aggiornati README, `AGENTS.md` e la data della home.

Prossima azione: Sandro guarda la pagina e conferma il cremisi (PR179 o PR206); poi si tarano i 6 tubetti sulle sue prove. La proposta sui testi delle 12 miscele della sezione Alberi è a parte, da approvare prima di scriverla nel json.

-- GBOT-app-acquerello

## 2026-10-18 - GBOT-app-acquerello - Niente merge automatico della sessione cloud

- In `CLAUDE.md` tolta la regola per cui la sessione cloud unisce da sé le pull request: su decisione di Sandro, l'unione su `main`, che pubblica il sito, si fa solo con il suo ok esplicito per quella pull request. Chiude così la prossima azione lasciata aperta il 2026-10-16.

-- GBOT-app-acquerello

## 2026-10-16 - CC - Pubblicazione automatica da GitHub

- Token Cloudflare «github-actions-app-acquerello», col solo permesso Cloudflare Pages: Edit sull'account del progetto, creato da Claude su Chrome e passato a GitHub dagli appunti senza mai mostrarlo. Prima di salvarlo è stato verificato: attivo, e in grado di leggere il progetto Pages `app-acquerello`.
- Nel repository: secret `CLOUDFLARE_API_TOKEN` e `CLOUDFLARE_ACCOUNT_ID`, variabile `PUBBLICA_CLOUDFLARE` = `si`.
- Prova: workflow avviato a mano su `main`, «costruisci» e «pubblica» verdi, pubblicazione `ac921423` in produzione; home e pagina degli alberi rispondono 200 coi titoli giusti.
- Da ora unire su `main` vuol dire pubblicare: aggiornati README, `AGENTS.md`, `CLAUDE.md` e `_index`.

Prossima azione: alla prima sessione cloud, se claude.ai/code non vede il repository privato, aggiungerlo all'app Claude su GitHub; Sandro conferma o toglie da `CLAUDE.md` la regola per cui la sessione cloud unisce da sé le pull request.

## 2026-10-16 - CC - GitHub copia principale, come per le NTC

Su richiesta di Sandro il repository basta a se stesso, e ci possono lavorare anche le sessioni cloud.

- `scripts/genera-sito.py` genera il sito dai soli file del repository, senza più copiare da `pit/acquerello-alberi/`. In `dati/alberi/` sono entrati i due csv della selezione dei video, le 7 illustrazioni dei gesti (`pit-261013-illustrazione-A*.png`) e i due strumenti di prova della pagina. Il generatore `pit-261013-video-gesti.py` contiene ora i quattro aiuti che prendeva dallo script del tutorial, rimasto nel workspace per i pdf, e cerca nel workspace le schede dei video solo per il comando `mandati`; `pit-261013-illustrazioni.py` prende dal workspace le foto del corso.
- Verifica: home e pagina degli alberi generate col flusso nuovo sono identiche byte per byte a quelle pubblicate (md5 `7fd52a42…` e `c181bde4…`), sia nel workspace sia in una copia isolata fuori dal workspace coi soli file del repository.
- Per gli agenti: `AGENTS.md`, `CLAUDE.md` con le regole della sessione cloud sul modello delle NTC, `.claude/settings.json` che installa Pillow da `scripts/requisiti.txt`, prompt di avvio `app-acquerello-261016-prompt-avvio-agente.md`.
- `.github/workflows/sito.yml`: controllo «costruisci» su ogni pull request e su `main`; job «pubblica» su Cloudflare Pages, fermo finché non ci sono la variabile `PUBBLICA_CLOUDFLARE` e la chiave Cloudflare.
- `npm run deploy` allinea prima la copia locale con `git pull --ff-only`.
- Nel workspace, da `pit/acquerello-alberi/` sono usciti i file passati qui; restano lo studio, le schede, i tutorial e le tavole in pdf, con le loro copie della selezione dei video e delle illustrazioni.

Prossima azione: con la chiave Cloudflare di Sandro, impostare i secret e la variabile per la pubblicazione automatica.

## 2026-10-15 - AGY - Creazione repository GitHub e pubblicazione su Cloudflare Pages

- Creata l'applicazione `software/applicazioni-github/app-acquerello/` come contenitore multi-sezione per le guide pratiche di acquerello, con la prima sezione `/alberi/` («Alberi ad acquerello: i gesti nei video», generata da `pit/acquerello-alberi/` con le 7 immagini panoramiche di Nano Banana 2.1 al posto dei ritagli della stampa del corso, senza catture di schermo tratte dai video YouTube) e la home indice `/` testuale.
- Scritto `scripts/genera-sito.py`, che sincronizza in `dati/alberi/` i sorgenti riproducibili (JSON, CSV dei segmenti, script Python e le 7 illustrazioni `pit-261015-riferimento-*.png`) e compila `site/index.html` (3 KB) e `site/alberi/index.html` (1.673 KB).
- Creato il repository privato GitHub `sinmar123/app-acquerello` e pubblicato il sito statico su Cloudflare Pages (`app-acquerello.pages.dev`). Firma: AGY.

Prossima azione: aggiungere le prossime sezioni di acquerello in `SEZIONI` man mano che vengono preparate in `pit/`.

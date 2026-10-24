# AGENTS.md - Quaderno di acquerello (app-acquerello)

Istruzioni per gli agenti AI che lavorano su questo repository, in locale o in una sessione cloud.

## Che cosa c'è

- `dati/<sezione>/`: i sorgenti di ogni sezione del sito.
  - `dati/principi/` (**1. Principi generali**): `principi.json` (9 capitoli e 42 fonti, elencate in fondo a ogni capitolo) e `genera-principi.py` (comando `pagina`; si ferma se una frase non ha fonte, se una fonte manca o non è citata, o se un testo contiene «da verificare»). Il capitolo 8, *In studio e all'aperto* (ancora `#studio-aperto`, dal 22/10/2026 al posto della sezione Studio ed en plein air), legge i sei colori e le 12 miscele `M1`-`M12` da `dati/alberi/pit-261014-video-gesti-alberi.json` e si ferma se la tavolozza non coincide con `dati/colori/tavolozza.json`.
  - `dati/colori/` (**2. Teoria dei colori**): `teoria-colori.json`, `tavolozza.json` (i sei colori proposti, coi valori sRGB provvisori del calcolatore), `munsell-tinte.json`, `calcolatore.js`, `interfaccia.js`, `spettri-spectraljs.js` (licenza MIT) e `genera-teoria-colori.py` (comando `pagina`).
  - `dati/marche/` (**3. Marche e tubetti**): `marche.json` (pagina ufficiale e data di controllo su ogni riga) e `genera-marche.py` (comando `pagina`; si ferma se manca la fonte o la data, o se un colore non è nella tavolozza).
  - `dati/soggetti/` (**4. Soggetti**): `soggetti.json` e `genera-soggetti.py` (comando `pagina`), che legge i nomi degli esempi di `S1` dal json degli Alberi.
  - `dati/alberi/` (**4.1 S1 · Alberi**): `pit-261014-video-gesti-alberi.json` (6 esempi `A1`-`A6`, 24 modalità, tavolozza e miscele), `pit-261013-video-gesti-segmenti.csv` (31 estratti video al secondo), `pit-261013-alberi-selezione-video*.csv`, `pit-261015-infografiche.py` (24 infografiche SVG in 3 fasi) e `pit-261013-video-gesti.py` (comando `pagina`).
  - `dati/eventi/` (**5. Eventi**): `sezione.json` (testi della sezione), un JSON per evento in `schede/` e le foto in `immagini/`. Ogni scheda ha solo locandina, programma e fotografie. `genera-eventi.py` (comando `pagina`) scrive il calendario, la scheda e l'archivio per anno; si ferma se una foto o la fonte del programma manca, se una scheda contiene racconti, demo o interviste, o se un testo contiene «da verificare» o il trattino lungo. Una foto con `momento` e `ora` sta accanto a quella voce del programma; senza `momento` resta nella sezione fotografie. Senza file di locandina la pagina scrive «locandina da aggiungere». `idee-interviste.md` conserva l'idea delle interviste, sospesa: non è una pagina e non va pubblicato. Un evento sta in un solo anno.
- `scripts/genera-sito.py`: genera `site/` dai soli file del repository, scrive `site/_redirects` (rinvii 301 di Cloudflare Pages per gli indirizzi vecchi, come `/studio-plein-air/` verso `/principi/#studio-aperto`), inietta la barra delle sezioni, fissa in cima a ogni pagina, la chat e la casella dei suggerimenti, scrive `lib/prompt-chat.js` dai dati e fa i controlli comuni: menu e pagine coincidenti con le funzioni, nessun nome di marca fuori da `dati/marche/`, leggibilità (Gulpease) non sotto 52.
- `scripts/rimandi_fonti.py`: i rimandi numerati alle fonti, con l'elenco in fondo a ogni capitolo e la freccia che riporta al testo, nello stesso formato per Principi e Teoria dei colori.
- `functions/api/`: `chat.js` (assistente su `gemini-4-argon`, senza email e senza archivio, 5 domande a settimana per connessione e 10 al giorno in tutto, contate su D1) e `suggerimento.js` (Issue pubbliche dalla casella del sito, 5 invii al giorno per connessione e 30 in tutto).
- `lib/prompt-chat.js`: prompt di sistema della chat, generato; non si modifica a mano.
- `site/` e le pagine html generate dentro `dati/` restano fuori da git (`.gitignore`).

## Come si lavora

- Si lavora su un ramo e si chiude con una pull request; mai scrivere direttamente su `main`.
- Unire su `main` vuol dire pubblicare: a ogni modifica di `main` il job «pubblica» di `.github/workflows/sito.yml` manda il sito su Cloudflare Pages.
- I testi si cambiano nei file `.json` e `.csv` e nei moduli delle infografiche, mai nell'html generato. Prima di cambiare i testi delle guide si porta la proposta al curatore e ci si ferma.
- Nel sito non si usano immagini generate con l'IA che imitano un acquerello o un dipinto; sono ammessi solo schemi, infografiche e figure disegnate. Regola del curatore del 22/10/2026, in [`CONTRIBUTING.md`](CONTRIBUTING.md) § 3.
- Il registro dei testi è quello di un manuale tecnico, scelto dal curatore il 21/10/2026: regole in [`CONTRIBUTING.md`](CONTRIBUTING.md) § 3.
- Dopo ogni modifica si lancia `python scripts/genera-sito.py`, che deve finire senza errori, si controlla la parte cambiata in `site/` e si committa anche `lib/prompt-chat.js` se è cambiato. Su ogni pull request GitHub rifà la generazione nel controllo «costruisci».
- Nuova sezione: cartella `dati/<tema>/` col suo generatore e i suoi dati, voce nella lista `SEZIONI` di `scripts/genera-sito.py` e negli elenchi `PAGINE_VALIDE` di `functions/api/chat.js` e `functions/api/suggerimento.js`.
- Ogni intervento ha la sua voce in cima a `CHANGELOG.md`, con data e firma, chiusa dalla riga «Prossima azione».
- Si scrive in italiano, rispettando le regole di [`CONTRIBUTING.md`](CONTRIBUTING.md).

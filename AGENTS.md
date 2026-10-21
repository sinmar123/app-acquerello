# AGENTS.md - Quaderno di acquerello (app-acquerello)

Istruzioni per gli agenti AI che lavorano su questo repository, in locale o in una sessione cloud.

## Che cosa c'è

- `dati/<sezione>/`: i sorgenti di ogni sezione del sito:
  - `dati/principi/` (**1. Principi tecnici**): `principi.json` (8 capitoli tecnici con chiavi delle fonti e apparato di 33 fonti verificate) e `genera-principi.py` (comando `pagina`; blocca la compilazione se una frase non ha fonte, se una fonte manca o non è citata, o se un testo contiene «da verificare»).
  - `dati/studio-plein-air/` (**2. Pittura in studio ed en plein air**): `studio-plein-air.json` (confronto metodologico studio/aperto, protocollo su campioni A5, tavolozza estesa da studio) e `genera-studio-plein-air.py` (comando `pagina`; legge anche i 6 pigmenti e le 12 miscele `M1`-`M12` da `dati/alberi/pit-261014-video-gesti-alberi.json` e verifica l'assenza di marche commerciali).
  - `dati/colori/` (**3. Colorimetria applicata e ottica della velatura**): `teoria-colori.json` (5 capitoli, limiti del simulatore e fonti), `tavolozza.json` (i 6 pigmenti di base col codice Colour Index, allineati a `dati/alberi/`), `munsell-tinte.json`, `calcolatore.js`, `interfaccia.js`, `spettri-spectraljs.js` (licenza MIT) e `genera-teoria-colori.py` (comando `pagina`).
  - `dati/marche/` (**4. Merceologia dei pigmenti e confronto tra serie commerciali**): `marche.json` (i 6 pigmenti di base confrontati in 6 serie commerciali, con link ufficiale e data di verifica su ogni riga) e `genera-marche.py` (comando `pagina`; blocca se manca fonte o data o se un colore non è nella tavolozza).
  - `dati/soggetti/` (**5. Repertorio dei soggetti pittorici**): `soggetti.json` (indice ragionato dei moduli esecutivi per soggetto: `S1` Alberi attivo, `S2` Cieli e nuvole, `S3` Fiori, `S4` Acqua, `S5` Rocce, `S6` Architetture in preparazione) e `genera-soggetti.py` (comando `pagina`).
  - `dati/alberi/` (**5.1 Soggetto S1 · Morfologia degli alberi**): `pit-261014-video-gesti-alberi.json` (6 tipologie arboree `A1`-`A6`, 24 modalità dimostrative, 6 pigmenti e 12 miscele), `pit-261013-video-gesti-segmenti.csv` (31 estratti video indicizzati al secondo), `pit-261013-alberi-selezione-video*.csv`, `pit-261015-infografiche.py` (24 tavole sinottiche SVG in 3 fasi), `pit-261013-video-gesti.py` (comando `pagina`) e `illustrazioni/` (`pit-261013-illustrazioni.py`).
- I nomi delle marche commerciali stanno esclusivamente in `dati/marche/`: in tutte le altre sezioni i colori si indicano col nome comune e il codice del pigmento (Colour Index).
- `scripts/genera-sito.py`: genera `site/` (home e tutte le sezioni) dai soli file del repository e inietta la barra di navigazione superiore, l'assistente tecnico AI e il modulo di invio contributi.
- `functions/api/`: funzioni Cloudflare Pages (`chat.js` per il consulente tecnico basato su `gemini-4-argon` con limite di 5 quesiti per email su database D1 `wrangler.toml`; `suggerimento.js` per l'apertura automatica di Issue su GitHub dalla casella pubblica del sito).
- `site/` e le pagine html generate dentro `dati/` restano fuori da git (`.gitignore`).

## Come si lavora

- Si lavora su un ramo e si chiude con una pull request; mai scrivere direttamente su `main`.
- Unire su `main` vuol dire pubblicare: a ogni modifica di `main` il job «pubblica» di `.github/workflows/sito.yml` manda il sito su Cloudflare Pages.
- I testi si cambiano nei file `.json` e nei moduli delle infografiche, mai nell'html generato.
- Dopo ogni modifica si lancia `python scripts/genera-sito.py`, che deve finire senza errori, e si controlla la parte cambiata in `site/`. Su ogni pull request GitHub rifà la generazione nel controllo «costruisci».
- Nuova sezione: cartella `dati/<tema>/` col suo generatore e i suoi dati, e voce nella lista `SEZIONI` di `scripts/genera-sito.py`.
- Ogni intervento ha la sua voce in cima a `CHANGELOG.md`, con data e firma.
- Si scrive in italiano, rispettando le regole di [`CONTRIBUTING.md`](CONTRIBUTING.md).

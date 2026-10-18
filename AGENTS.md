# AGENTS.md - Quaderno di acquerello (app-acquerello)

Istruzioni per gli agenti che lavorano su questo repository, nel workspace di Sandro o in una sessione cloud. Dove l'agente vede anche il workspace, si aggiungono alle sue regole.

## Che cosa c'è

- `dati/<sezione>/`: i sorgenti di ogni sezione del sito. Per `alberi`:
  - `pit-261014-video-gesti-alberi.json`: testi della pagina, alberi, passi, colori e miscele;
  - `pit-261013-video-gesti-segmenti.csv`: gli estratti dei video, un pezzo per riga con inizio e fine;
  - `pit-261013-alberi-selezione-video*.csv`: canale e titolo dei video scelti;
  - `pit-261015-infografiche.py`: le infografiche in 4 fasi in fondo a ogni albero;
  - `pit-261013-video-gesti.py`: il generatore della pagina (comando `pagina`) e gli strumenti di studio dei video;
  - `illustrazioni/`: le immagini della pagina, fatte con Nano Banana da `pit-261013-illustrazioni.py`.
- `dati/colori/`, la sezione Teoria dei colori:
  - `teoria-colori.json`: testi dei 5 capitoli, limiti del calcolatore e fonti;
  - `tavolozza.json`: i 6 tubetti Cotman, con colori sRGB provvisori da sostituire con la taratura sulle prove di Sandro;
  - `munsell-tinte.json`: tabella delle 40 tinte Munsell per la notazione approssimata;
  - `calcolatore.js` e `interfaccia.js`: il calcolatore di miscele, JavaScript puro scritto per il Quaderno; `spettri-spectraljs.js`: tabelle spettrali di spectral.js (licenza MIT, testo nel file);
  - `genera-teoria-colori.py`: il generatore della pagina (comando `pagina`), che mette tutto dentro un solo html.
- `scripts/genera-sito.py`: genera `site/` (home e sezioni) dai soli file del repository.
- `site/` e le pagine html dentro `dati/` sono generate e restano fuori da git.

## Come si lavora

- Si lavora su un ramo e si chiude con una pull request; mai scrivere su `main`.
- Unire su `main` vuol dire pubblicare: a ogni modifica di `main` il job «pubblica» manda il sito su Cloudflare Pages.
- I testi si cambiano nel json e nel modulo delle infografiche, mai nell'html generato.
- Dopo ogni modifica si lancia `python scripts/genera-sito.py`, che deve finire senza errori, e si guarda la parte cambiata in `site/`. Su ogni pull request GitHub rifà la generazione nel controllo «costruisci».
- Nuova sezione: cartella `dati/<tema>/` col suo generatore e i suoi dati, e voce nella lista `SEZIONI` di `scripts/genera-sito.py`.
- Ogni intervento ha la sua voce in cima a `CHANGELOG.md`, con data e firma dell'agente.
- Si scrive in italiano.

## Che cosa si fa solo dal W520

Le schede dei video con Gemini, le illustrazioni con Nano Banana, i fotogrammi e i sottotitoli da YouTube richiedono chiavi e programmi che stanno sul W520 di Sandro. Lo studio dei video, cioè schede, tutorial e tavole in pdf, sta nel workspace, in `pit/acquerello-alberi/`. Un agente in cloud che ne ha bisogno lo dice e si ferma.

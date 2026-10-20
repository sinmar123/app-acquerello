# Come contribuire al Quaderno di acquerello

Il **Quaderno di acquerello** (`https://app-acquerello.pages.dev`) è un progetto aperto: chiunque può segnalare correzioni, proporre nuovi esempi o contribuire con dati, infografiche e sezioni didattiche.

## 1. Segnalazioni e proposte (senza programmare)

Se vuoi proporre un miglioramento senza toccare il codice, apri una **Issue** su GitHub indicando:

- **Per un nuovo video o modalità di esercizio:** l'indirizzo del video YouTube, il minuto di inizio e fine del passaggio interessante, i colori e i pennelli usati dall'autore e cosa mostra il gesto.
- **Per una nuova serie nella sezione Marche e tubetti:** il nome della serie e, per ciascuno dei 6 colori di base, il link alla pagina ufficiale del produttore da cui risultano nome commerciale, numero, codice pigmento (Colour Index) e trasparenza.
- **Per una correzione ai testi o alle ricette:** la sezione, il punto preciso e la fonte di riferimento.

## 2. Modifiche dirette tramite Pull Request

1. Fai un **Fork** del repository e crea un ramo dedicato (es. `feat/nuova-marca` o `fix/principi-carta`).
2. Modifica i file sorgente in `dati/<sezione>/` (file `.json`, `.csv`, `.py` o `.js`). **Non modificare mai direttamente i file `.html`**, che vengono rigenerati dagli script.
3. Verifica la generazione del sito sul tuo computer:
   ```bash
   pip install -r scripts/requisiti.txt
   python scripts/genera-sito.py
   ```
   Il comando deve terminare senza errori e produrre le pagine in `site/`.
4. Aggiungi una riga in cima a `CHANGELOG.md` con la data e la descrizione sintetica della modifica.
5. Apri una **Pull Request** verso il ramo `main`: il controllo automatico «costruisci» su GitHub verificherà che l'intero sito si generi senza errori.

## 3. Regole editoriali e di qualità

I generatori Python controllano automaticamente la coerenza dei dati e bloccano la compilazione se una regola viene violata:

- **Ogni affermazione ha una fonte:** nella sezione *Principi generali* (`dati/principi/principi.json`) ogni blocco di testo deve rimandare a una fonte presente nell'elenco delle fonti; nella sezione *Marche e tubetti* (`dati/marche/marche.json`) ogni tubetto deve avere il link alla pagina ufficiale del produttore (`fonte`) e la data di verifica (`controllato`). Non sono ammessi testi con la dicitura «da verificare».
- **Colori senza marche commerciali nelle guide:** nelle sezioni *Principi generali*, *Alberi* e *Teoria dei colori* i colori si indicano con il **nome comune e il codice del pigmento** (es. *terra di Siena bruciata (PR101)*, *blu oltremare (PB29)*). I nomi commerciali e i codici delle case produttrici vanno esclusivamente nella sezione *Marche e tubetti*.
- **Nessun fotogramma estratto dai video YouTube:** per rispettare il diritto d'autore dei creatori dei video, il sito non incorpora fotogrammi catturati dai video. I passaggi sono spiegati tramite infografiche SVG in 3 fasi e illustrazioni originali, affiancate al lettore YouTube ufficiale che apre il video al secondo esatto.
- **Lingua:** si scrive in italiano chiaro e diretto, usando sempre gli accenti grafici corretti (`è`, `é`, `à`, `ò`, `ù`, `ì`).

## 4. Licenza dei contributi

Inviando un contributo a questo repository (tramite Pull Request, Issue o altra comunicazione), dichiari di avere il diritto di inviarlo e accetti che il contributo:

1. sia rilasciato con le licenze aperte del progetto indicate nel file [`LICENSE`](LICENSE) (**MIT** per il codice sorgente, **CC BY 4.0** per i testi, i dati, le schede e le illustrazioni);
2. possa essere utilizzato, adattato, pubblicato e integrato senza limiti di tempo o di territorio dal curatore del progetto (`sinmar123`) anche nella versione ospitata dell'applicazione web e in eventuali funzionalità, moduli o servizi aggiuntivi futuri, gratuiti o in abbonamento.

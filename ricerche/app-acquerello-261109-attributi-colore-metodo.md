# Tinta, valore e croma: ricerca storica e revisione Wada

Ricerca del 9 novembre 2026. Coordinamento e riscontri sulle fonti: OpenClaw / OC. Letture a parti dei rapporti: Codex / CDX. Questa nota accompagna il nuovo approfondimento 5.4 e l’integrazione della scheda Wada, senza pubblicazione autorizzata.

## Corse effettive

| Motore | Esito e attività registrate | Durata osservata | Costo monetario |
|---|---|---|---|
| GPT-6 Astra, high, sottoagente nativo nel bot | Concluso; 54 query e 32 unità documentarie dichiarate | Non misurata separatamente | Quota ChatGPT; nessuna corsa API aggiuntiva |
| GLM 5.2 via DashScope | Concluso; 31 ricerche e 4 estrazioni | Circa 7 min 31 s | Circa 0,57 USD, stima |
| DeepSeek v4 Pro via DashScope | Concluso; 40 ricerche e 3 estrazioni | Circa 8 min 28 s | Circa 0,90 USD, stima |
| Gemini Deep Research standard | Concluso; 41 ricerche Google e 1.450.376 token totali dichiarati | Raccolta in 8 min 50 s, non durata esatta sui server | Addebito non esposto |
| Qwen 3.8 Max via DashScope | Testo parziale; response.failed, server_error. 17 ricerche, alcune multiquery, e 27 estrazioni | Circa 44 min 11 s | Consumi non restituiti; costo sconosciuto, non zero |

Sono quattro rapporti conclusi e uno parziale, non cinque successi. Qwen non è stato rilanciato. Le corse a consumo sono partite in parallelo e le durate non vanno sommate. Le 54 query GPT non sono la stessa unità delle chiamate multiquery di altri motori. Non è disponibile una misura separata del tempo di coordinamento, verifica e scrittura.

## Stime e limiti di costo

I circa 1,47 USD sono esclusivamente la stima GLM e DeepSeek di questa ricerca, non un consuntivo complessivo. Il calcolo usa i consumi restituiti e le tariffe Singapore documentate: GLM 1,40/0,28/4,40 e DeepSeek 2,40/0,48/4,80 USD per milione di token ingresso/cache/uscita, più 0,01 USD per chiamata di ricerca. Le estrazioni sono considerate gratuite secondo il listino.

GLM: 93.335 token ingresso non in cache, 228.864 cache, 15.010 uscita e 31 ricerche: 0,5707949 USD. DeepSeek: 89.050 ingresso non in cache, 476.160 cache, 11.915 uscita e 40 ricerche: 0,8994688 USD. Prezzi e cache riaperti il 9 novembre 2026 sulle pagine ufficiali [listino Alibaba](https://www.alibabacloud.com/help/en/model-studio/model-pricing) e [cache implicita](https://www.alibabacloud.com/help/en/model-studio/context-cache).

Questi importi escludono Qwen, Gemini e la preparazione del piano. Non sono addebiti verificati in console e non si sommano ai 2,77 USD della precedente ricerca Wada come se ne risultasse un totale completo. La previsione approvata per le quattro corse era 3,70-6,10 USD, con scenario prudente di circa 18,80 USD, non un tetto garantito. I dati di saldi e account restano nel dossier privato e non sono riportati qui.

## Copertura e decisioni editoriali

Letti i cinque testi per intero, 285.281 caratteri e 1.820 righe, con letture a parti e ritorni distinti: GPT 298 righe, Qwen 643, Gemini 234, GLM 350, DeepSeek 295. Questa misura riguarda i rapporti, non la lettura integrale delle fonti da essi citate. Il consenso fra modelli non è stato considerato una prova; Qwen, GLM e DeepSeek condividono gli strumenti web DashScope.

I riscontri storici distinguono il facsimile Munsell 1905 dalla seconda edizione 1907. La conferenza Wada del 1930 documenta l’ordinamento Ostwald dei campioni standard, ma non prova il metodo di scelta di tutte le combinazioni. La notizia istituzionale Tōbunken del 1956 sulle tavole Munsell migliorate non viene retrodatata. MacEvoy rimane un autore tecnico contemporaneo, non l’origine della terna.

Scartati l’attribuzione a Wada del 60-30-10, l’identità croma-saturazione, i primati assoluti non dimostrati e gli automatismi sulle diluizioni. Il nuovo approfondimento distingue antecedenti, notazione HVC, sviluppi colorimetrici e lessico CIE. Nella scheda Wada restano separati documenti storici, lettura odierna e prove proposte dal Quaderno.

Le fonti nelle due pagine dichiarano edizioni, pagine e parti consultate. Non sono dichiarate letture integrali dei libri moderni o dell’appendice storica; le traduzioni dal giapponese sono di lavoro. Nessuna prova pittorica, misura colorimetrica o verifica delle tabelle numeriche di rinotazione è stata eseguita.

Firma: OpenClaw / OC.

Prossima azione: Rivedere le due pagine nella PR #78; unione e pubblicazione solo con nuovo via libera esplicito del curatore.

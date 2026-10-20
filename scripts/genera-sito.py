#!/usr/bin/env python3
"""Genera il sito statico delle guide di acquerello in site/ dai sorgenti delle sezioni in dati/<sezione>/.

Il repository è autonomo: contiene tutti i file di dati, le infografiche e gli script necessari a generare le pagine."""
import base64
import io
import pathlib
import subprocess
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

APP_DIR = pathlib.Path(__file__).resolve().parent.parent
SITE_DIR = APP_DIR / "site"
DATI_DIR = APP_DIR / "dati"

SEZIONI = [
    {
        "slug": "principi",
        "numero": "1",
        "nome_form": "Principi",
        "titolo": "Principi tecnici: diluizione del pigmento e stati del supporto",
        "sottotitolo": "Controllo del rapporto acqua-pigmento, grado di umidità della carta e tecniche di stesura",
        "descrizione": (
            "Classificazione operativa della diluizione sulla tavolozza (tè, latte, miele); fasi di asciugatura del supporto "
            "individuate tramite la riflessione speculare del velo d'acqua; equilibrio idrodinamico tra carica del pennello e "
            "umidità della fibra per prevenire o governare i riflussi (backruns); gestione dei margini, proprietà fisiche delle "
            "carte (satinata, grana fina, ruvida) e correzioni a umido o a secco. Ogni indicazione è corredata dal riferimento puntuale alla fonte."
        ),
        "badge": ["8 capitoli", "diluizione e supporto", "controllo dei riflussi", "riferimenti verificati"],
        "script_genera": DATI_DIR / "principi" / "genera-principi.py",
        "html_generato": DATI_DIR / "principi" / "principi.html",
    },
    {
        "slug": "studio-plein-air",
        "numero": "2",
        "nome_form": "Studio ed en plein air",
        "titolo": "Pittura in studio ed en plein air: metodo, dotazione e tavolozze",
        "sottotitolo": "Differenze operative tra banco di studio e pittura all'aperto, protocollo su campioni A5 e prontuario delle 12 miscele (M1-M12)",
        "descrizione": (
            "Confronto sistematico tra l'esecuzione in ambiente controllato (tavolozza estesa con pigmenti di comodità, tempi di evaporazione "
            "distesi, dotazione strumentale completa) e la pratica all'aperto en plein air (sintesi rapida, selezione ristretta a 6 pigmenti "
            "fondamentali, prontuario completo delle 12 miscele M1-M12 e protocollo di verifica su campioni in formato A5)."
        ),
        "badge": ["studio vs plein air", "protocollo campioni A5", "tavolozza estesa e a 6 pigmenti", "prontuario 12 miscele"],
        "script_genera": DATI_DIR / "studio-plein-air" / "genera-studio-plein-air.py",
        "html_generato": DATI_DIR / "studio-plein-air" / "studio-plein-air.html",
    },
    {
        "slug": "colori",
        "numero": "3",
        "nome_form": "Teoria dei colori",
        "titolo": "Colorimetria applicata e ottica della velatura",
        "sottotitolo": "Spazio cromatico di Munsell, sintesi sottrattiva, comportamento ottico dei pigmenti e simulatore Kubelka-Munk",
        "descrizione": (
            "Coordinate di tinta, valore e croma nel sistema Munsell; assorbimento selettivo e diffusione luminosa nello strato pittorico "
            "fino al supporto cartaceo; differenze ottiche tra miscelazione fisica su tavolozza e sovrapposizione per velatura trasparente; "
            "criteri di composizione della tavolozza ristretta a sei monopigmento (coppia caldo/freddo per primario) e calcolatore "
            "interattivo delle miscele basato sul modello spettrale di Kubelka-Munk."
        ),
        "badge": ["5 capitoli", "6 pigmenti primari", "modello Kubelka-Munk", "simulatore spettrale"],
        "script_genera": DATI_DIR / "colori" / "genera-teoria-colori.py",
        "html_generato": DATI_DIR / "colori" / "teoria-colori.html",
    },
    {
        "slug": "marche",
        "numero": "4",
        "nome_form": "Confronto marche",
        "titolo": "Merceologia dei pigmenti e confronto tra serie commerciali",
        "sottotitolo": "Corrispondenze nel Colour Index, trasparenza dichiarata e variabilità formulativa tra sei linee produttive",
        "descrizione": (
            "Tabella comparativa dei sei pigmenti della tavolozza ridotta nelle serie Winsor &amp; Newton (Cotman e Professional), "
            "Royal Talens Van Gogh, Daniel Smith Extra Fine, Schmincke Horadam e Maimeri Blu. Tutti i dati sono rilevati dai "
            "cataloghi tecnici ufficiali dei produttori e illustrano le divergenze di composizione chimica tra tubetti commercializzati "
            "con la medesima denominazione tradizionale."
        ),
        "badge": ["6 serie commerciali", "sigle Colour Index", "fonti tecniche ufficiali", "lettura dell'etichetta"],
        "script_genera": DATI_DIR / "marche" / "genera-marche.py",
        "html_generato": DATI_DIR / "marche" / "marche.html",
    },
    {
        "slug": "soggetti",
        "numero": "5",
        "nome_form": "Soggetti (Alberi, Nuvole, Fiori...)",
        "titolo": "Repertorio dei soggetti pittorici: monografie esecutive e analisi dei gesti",
        "sottotitolo": "Sezione in progressiva estensione: 1. Alberi e masse arbustive (attivo) · 2. Cieli e nuvole · 3. Fiori e botanica · 4. Acqua e riflessi · 5. Rocce · 6. Architetture",
        "descrizione": (
            "Raccolta delle monografie operative dedicate ai singoli soggetti affrontati nel percorso di studio. Il modulo inaugurale "
            "è dedicato alla Morfologia degli alberi (6 tipologie arboree, 24 procedure comparative, 72 stadi in tavola sinottica SVG e "
            "31 estratti video al secondo); i moduli successivi su formazioni nuvolose, fiori, specchi d'acqua, rilievi rocciosi e architetture "
            "sono in fase di progressivo inserimento."
        ),
        "badge": ["S1 Alberi (pubblicato)", "S2 Cieli e nuvole (in prep.)", "S3 Fiori (in prep.)", "S4-S6 Acqua, Rocce, Architetture"],
        "script_genera": DATI_DIR / "soggetti" / "genera-soggetti.py",
        "html_generato": DATI_DIR / "soggetti" / "soggetti.html",
    },
    {
        "slug": "alberi",
        "in_home": False,
        "numero": "5.1",
        "nome_form": "Soggetti (Alberi, Nuvole, Fiori...)",
        "titolo": "Soggetto S1 · Morfologia degli alberi",
        "sottotitolo": "Sei tipologie arboree analizzate attraverso 24 procedure comparative",
        "descrizione": "",
        "badge": [],
        "script_genera": DATI_DIR / "alberi" / "pit-261013-video-gesti.py",
        "html_generato": DATI_DIR / "alberi" / "pit-261014-video-gesti-alberi.html",
    },
]

OPZIONI_SEZIONE = [
    "Generale / Nuovo argomento",
    "Principi",
    "Studio ed en plein air",
    "Teoria dei colori",
    "Confronto marche",
    "Soggetti (Alberi, Nuvole, Fiori...)",
]


def miniatura_data_uri(percorso: pathlib.Path, larghezza: int = 720, qualita: int = 80) -> str:
    if not percorso.exists():
        return ""
    im = Image.open(percorso).convert("RGB")
    if im.width > larghezza:
        im = im.resize((larghezza, int(im.height * larghezza / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=qualita, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


def blocco_chat_e_suggerimenti(sezione_predefinita: str, pagina_path: str) -> str:
    opts = []
    for opz in OPZIONI_SEZIONE:
        sel = " selected" if opz == sezione_predefinita else ""
        opts.append(f'<option value="{opz}"{sel}>{opz}</option>')
    options_html = "".join(opts)

    return f"""
<style>
.sugg-wrap{{max-width:820px;margin:24px auto 18px;padding:0 14px;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.sugg-box,.chat-box{{background:#fffdf8;border:1px solid #d8ccb8;border-left:4px solid #2f5e4e;border-radius:10px;padding:18px 20px;box-shadow:0 2px 8px rgba(31,28,23,.05);color:#1f1c17;margin-bottom:22px}}
.chat-box{{border-left-color:#8c4a27}}
.sugg-box h2,.chat-box h2{{margin:0 0 6px;font-size:1.15rem;color:#263529}}
.chat-box h2{{color:#6b3418}}
.sugg-sub{{margin:0 0 14px;font-size:.9rem;color:#4a4236;line-height:1.45}}
.sugg-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}}
@media(max-width:600px){{.sugg-grid{{grid-template-columns:1fr}}}}
.sugg-field{{display:flex;flex-direction:column;gap:4px;margin-bottom:12px}}
.sugg-field label{{font-size:.83rem;font-weight:600;color:#3d352b}}
.sugg-field input,.sugg-field select,.sugg-field textarea{{font:inherit;font-size:.92rem;padding:8px 10px;border:1px solid #c9bba3;border-radius:6px;background:#ffffff;color:#1f1c17}}
.sugg-field textarea{{min-height:92px;resize:vertical}}
.sugg-avviso{{background:#f5efe2;border:1px solid #dfd3be;border-radius:7px;padding:10px 12px;margin:10px 0 14px;font-size:.82rem;color:#3d352b;line-height:1.45}}
.sugg-avviso a{{color:#2f5e4e;font-weight:600}}
.sugg-actions{{display:flex;flex-wrap:wrap;align-items:center;gap:12px}}
.sugg-btn{{background:#263529;color:#f7f2e7;border:0;border-radius:7px;padding:9px 16px;font:inherit;font-size:.9rem;font-weight:600;cursor:pointer}}
.sugg-btn:hover{{background:#1c281f}}
.sugg-btn.arancio{{background:#8c4a27}}
.sugg-btn.arancio:hover{{background:#6b3418}}
.sugg-btn:disabled{{opacity:.6;cursor:wait}}
.sugg-link-gh{{font-size:.82rem;color:#5c5142;text-decoration:none}}
.sugg-link-gh:hover{{text-decoration:underline}}
.sugg-esito{{margin-top:12px;padding:10px 12px;border-radius:7px;font-size:.88rem;display:none}}
.sugg-esito.ok{{display:block;background:#e6f4ea;border:1px solid #a8dab5;color:#135225}}
.sugg-esito.err{{display:block;background:#fce8e6;border:1px solid #f5c2c0;color:#7a1c18}}
.sugg-hp{{position:absolute;left:-9999px;opacity:0;pointer-events:none;height:0;overflow:hidden}}
.chat-login-row{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.chat-login-row input{{flex:1;min-width:220px;font:inherit;font-size:.92rem;padding:8px 11px;border:1px solid #c9bba3;border-radius:6px;background:#fff}}
.chat-barra-stato{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:8px;background:#f5efe2;border:1px solid #dfd3be;border-radius:7px;padding:8px 12px;margin-bottom:12px;font-size:.84rem}}
.chat-badge-quota{{font-weight:700;color:#6b3418;padding:2px 8px;border-radius:999px;border:1px solid #d5b8a3;background:#fff8f3}}
.chat-esempi{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}}
.chat-chip{{background:#f3ece0;border:1px solid #d8ccb8;color:#3d352b;border-radius:999px;padding:4px 10px;font:inherit;font-size:.79rem;cursor:pointer;text-align:left}}
.chat-chip:hover{{background:#e6dbc8}}
.chat-messaggi{{max-height:360px;overflow-y:auto;border:1px solid #e2d7c5;border-radius:8px;background:#faf6ee;padding:12px;margin-bottom:12px;display:none;flex-direction:column;gap:10px}}
.chat-msg{{padding:10px 12px;border-radius:8px;font-size:.9rem;line-height:1.5;max-width:92%}}
.chat-msg.utente{{align-self:flex-end;background:#263529;color:#f7f2e7}}
.chat-msg.ai{{align-self:flex-start;background:#ffffff;border:1px solid #dfd5c3;color:#1f1c17}}
.chat-msg.ai p{{margin:0 0 8px}}
.chat-msg.ai p:last-child{{margin-bottom:0}}
.chat-input-row{{display:flex;gap:8px;align-items:flex-end}}
.chat-input-row textarea{{flex:1;font:inherit;font-size:.92rem;padding:8px 10px;border:1px solid #c9bba3;border-radius:6px;min-height:54px;max-height:140px;resize:vertical;background:#fff}}
.chat-nota-privacy{{margin:8px 0 0;font-size:.78rem;color:#6b5e4c}}
</style>

<section id="assistente-ai" class="sugg-wrap" aria-label="Consulenza tecnica AI sull'acquerello">
  <div class="chat-box" data-pagina="{pagina_path}">
    <h2>🎨 Assistente tecnico di studio (Gemini 4 Argon)</h2>
    <p class="sugg-sub">
      Per approfondimenti operativi sul bilanciamento idrico tra pennello e supporto, sulla formulazione delle miscele, sulla prevenzione dei riflussi o sull'esecuzione delle sequenze illustrate:
      inserendo il proprio indirizzo email è possibile sottoporre fino a <strong>5 quesiti gratuiti</strong> al modello linguistico configurato sulla base documentale di questo repertorio.
    </p>

    <div id="chat-step-email">
      <form id="form-chat-login" class="chat-login-row">
        <input id="chat-email-input" type="email" required maxlength="120" placeholder="Indirizzo email (es. nome@dominio.it)" autocomplete="email">
        <button type="submit" class="sugg-btn arancio" id="chat-login-btn">Accedi al servizio (5 quesiti)</button>
      </form>
      <p class="chat-nota-privacy">
        L'indirizzo email viene impiegato esclusivamente per la contabilizzazione della quota di 5 quesiti associata all'utente: non vengono effettuate iscrizioni a liste di distribuzione né cessioni a terzi.
      </p>
    </div>

    <div id="chat-step-conversazione" style="display:none">
      <div class="chat-barra-stato">
        <span>Sessione attiva: <strong id="chat-email-attiva"></strong> · <button type="button" id="chat-cambia-email" style="background:none;border:0;color:#6b4226;text-decoration:underline;cursor:pointer;font:inherit;padding:0">modifica indirizzo</button></span>
        <span class="chat-badge-quota" id="chat-quota-label">Quesiti disponibili: 5 su 5</span>
      </div>

      <div class="chat-esempi" id="chat-esempi-wrap">
        <span style="font-size:.79rem;color:#6b5e4c;align-self:center;margin-right:2px">Quesiti di esempio:</span>
        <button type="button" class="chat-chip">Quale squilibrio idrico provoca i riflussi a cavolfiore durante una seconda stesura?</button>
        <button type="button" class="chat-chip">Come si formula un verde profondo per le conifere in ombra con i 6 pigmenti di base?</button>
        <button type="button" class="chat-chip">In quale stadio di umidità della carta va applicato il sale per ottenere la cristallizzazione radiale?</button>
      </div>

      <div id="chat-messaggi" class="chat-messaggi" aria-live="polite"></div>

      <form id="form-chat-domanda">
        <div class="chat-input-row">
          <textarea id="chat-domanda-input" required minlength="4" maxlength="1000" placeholder="Formula qui il quesito tecnico sull'acquerello..."></textarea>
          <button type="submit" class="sugg-btn arancio" id="chat-invia-btn">Invia</button>
        </div>
      </form>
    </div>

    <div id="chat-esito-err" class="sugg-esito err" role="alert" style="display:none"></div>
  </div>
</section>

<section id="suggerimenti" class="sugg-wrap" aria-label="Invio contributi e rettifiche">
  <div class="sugg-box">
    <h2>💬 Invio di contributi tecnici, rettifiche o riferimenti video</h2>
    <p class="sugg-sub">
      Per segnalare imprecisioni, proporre integrazioni documentali o indicare passaggi dimostrativi rilevanti all'interno di video didattici su YouTube (specificando il minutaggio di inizio e fine):
      il modulo seguente trasmette direttamente la segnalazione al registro pubblico del progetto, dove viene sottoposta a verifica redazionale prima dell'eventuale recepimento.
    </p>
    <form id="form-suggerimento" data-pagina="{pagina_path}">
      <div class="sugg-hp" aria-hidden="true">
        <label>Non compilare questo campo <input type="text" name="miele" tabindex="-1" autocomplete="off"></label>
      </div>
      <div class="sugg-grid">
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-sezione">Sezione di riferimento</label>
          <select id="sugg-sezione" name="sezione">
            {options_html}
          </select>
        </div>
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-firma">Autore della segnalazione (facoltativo)</label>
          <input id="sugg-firma" name="firma" type="text" maxlength="60" placeholder="Lasciare vuoto per invio anonimo">
        </div>
      </div>
      <div class="sugg-field" style="margin-top:12px">
        <label for="sugg-titolo">Oggetto sintetico *</label>
        <input id="sugg-titolo" name="titolo" type="text" required minlength="4" maxlength="120" placeholder="Es. Riferimento video sulla chioma del pino marittimo / Rettifica sigla Colour Index">
      </div>
      <div class="sugg-field">
        <label for="sugg-testo">Descrizione dettagliata *</label>
        <textarea id="sugg-testo" name="testo" required minlength="10" maxlength="3500" placeholder="Esporre la proposta o la rettifica. Nel caso di un riferimento video su YouTube, riportare l'URL e l'intervallo temporale esatto (mm:ss) della sequenza esecutiva."></textarea>
      </div>
      <div class="sugg-avviso">
        <strong>Informativa sulla pubblicazione:</strong> l'invio non richiede registrazione.
        Selezionando <em>Trasmetti contributo</em>, il testo inserito e l'eventuale nominativo indicato
        <strong>vengono resi pubblici</strong> nel registro aperto delle
        <a href="https://github.com/sinmar123/app-acquerello/issues" target="_blank" rel="noopener">segnalazioni del progetto su GitHub</a>
        (con licenza Creative Commons CC BY 4.0) ai fini della revisione tecnica e dell'aggiornamento del repertorio.
        <strong>Non inserire indirizzi di posta elettronica, recapiti telefonici o altri dati personali riservati.</strong>
      </div>
      <div class="sugg-actions">
        <button type="submit" class="sugg-btn" id="sugg-submit">Trasmetti contributo</button>
        <a class="sugg-link-gh" href="https://github.com/sinmar123/app-acquerello/issues" target="_blank" rel="noopener">Consulta il registro delle segnalazioni pubblicate →</a>
      </div>
      <div id="sugg-esito" class="sugg-esito" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
<script>
(function(){{
  // --- 1. GESTIONE CHAT AI (GEMINI 4 ARGON, 5 QUESITI PER EMAIL) ---
  var STORAGE_KEY = "acquerello_chat_email";
  var stepEmail = document.getElementById("chat-step-email");
  var stepConv = document.getElementById("chat-step-conversazione");
  var formLogin = document.getElementById("form-chat-login");
  var inputEmail = document.getElementById("chat-email-input");
  var btnLogin = document.getElementById("chat-login-btn");
  var labelEmail = document.getElementById("chat-email-attiva");
  var btnCambia = document.getElementById("chat-cambia-email");
  var labelQuota = document.getElementById("chat-quota-label");
  var boxMessaggi = document.getElementById("chat-messaggi");
  var formDomanda = document.getElementById("form-chat-domanda");
  var inputDomanda = document.getElementById("chat-domanda-input");
  var btnInvia = document.getElementById("chat-invia-btn");
  var boxErr = document.getElementById("chat-esito-err");
  var chatBox = document.querySelector(".chat-box");
  var paginaCorrente = (chatBox && chatBox.getAttribute("data-pagina")) || window.location.pathname;
  var emailAttiva = "";
  var storiaSessione = [];

  function formattaTestoAi(testo) {{
    var esc = testo
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    esc = esc.replace(/\\*\\*(.+?)\\*\\*/g, "<strong>$1</strong>");
    esc = esc.replace(/\\*(.+?)\\*/g, "<em>$1</em>");
    var blocchi = esc.split(/\\n\\n+/);
    return blocchi.map(function(b) {{
      return "<p>" + b.replace(/\\n/g, "<br>") + "</p>";
    }}).join("");
  }}

  function aggiornaStatoUi(dati) {{
    labelEmail.textContent = dati.email;
    labelQuota.textContent = "Quesiti disponibili: " + dati.rimanenti + " su " + dati.limite;
    if (dati.rimanenti <= 0) {{
      inputDomanda.disabled = true;
      btnInvia.disabled = true;
      inputDomanda.placeholder = "Quota di 5 quesiti gratuiti esaurita per questo indirizzo email.";
    }} else {{
      inputDomanda.disabled = false;
      btnInvia.disabled = false;
      inputDomanda.placeholder = "Formula qui il quesito tecnico sull'acquerello...";
    }}
  }}

  async function verificaEmail(email, silenzioso) {{
    if (!silenzioso) {{
      boxErr.style.display = "none";
      btnLogin.disabled = true;
      btnLogin.textContent = "Verifica...";
    }}
    try {{
      var r = await fetch("/api/chat", {{
        method: "POST",
        headers: {{"Content-Type": "application/json"}},
        body: JSON.stringify({{ azione: "stato", email: email }})
      }});
      var risp = await r.json();
      if (!r.ok || !risp.ok) {{
        throw new Error((risp && risp.errore) || "Indirizzo email non valido.");
      }}
      emailAttiva = risp.email;
      try {{ localStorage.setItem(STORAGE_KEY, emailAttiva); }} catch(e) {{}}
      stepEmail.style.display = "none";
      stepConv.style.display = "block";
      aggiornaStatoUi(risp);
    }} catch (err) {{
      if (!silenzioso) {{
        boxErr.textContent = err.message || "Impossibile avviare la sessione.";
        boxErr.style.display = "block";
      }}
    }} finally {{
      if (!silenzioso) {{
        btnLogin.disabled = false;
        btnLogin.textContent = "Accedi al servizio (5 quesiti)";
      }}
    }}
  }}

  if (formLogin) {{
    formLogin.addEventListener("submit", function(ev) {{
      ev.preventDefault();
      var em = inputEmail.value.trim();
      if (em) verificaEmail(em, false);
    }});
  }}

  if (btnCambia) {{
    btnCambia.addEventListener("click", function() {{
      emailAttiva = "";
      try {{ localStorage.removeItem(STORAGE_KEY); }} catch(e) {{}}
      stepConv.style.display = "none";
      stepEmail.style.display = "block";
      boxErr.style.display = "none";
      inputEmail.focus();
    }});
  }}

  document.querySelectorAll(".chat-chip").forEach(function(chip) {{
    chip.addEventListener("click", function() {{
      if (!inputDomanda.disabled) {{
        inputDomanda.value = chip.textContent;
        inputDomanda.focus();
      }}
    }});
  }});

  if (formDomanda) {{
    formDomanda.addEventListener("submit", async function(ev) {{
      ev.preventDefault();
      var testoDomanda = inputDomanda.value.trim();
      if (!testoDomanda || !emailAttiva) return;
      boxErr.style.display = "none";

      boxMessaggi.style.display = "flex";
      var divU = document.createElement("div");
      divU.className = "chat-msg utente";
      divU.textContent = testoDomanda;
      boxMessaggi.appendChild(divU);

      var divAttesa = document.createElement("div");
      divAttesa.className = "chat-msg ai";
      divAttesa.innerHTML = "<em>Elaborazione della risposta tecnica in corso (Gemini 4 Argon)...</em>";
      boxMessaggi.appendChild(divAttesa);
      boxMessaggi.scrollTop = boxMessaggi.scrollHeight;

      inputDomanda.value = "";
      btnInvia.disabled = true;
      btnInvia.textContent = "Attendere...";

      try {{
        var r = await fetch("/api/chat", {{
          method: "POST",
          headers: {{"Content-Type": "application/json"}},
          body: JSON.stringify({{
            azione: "chiedi",
            email: emailAttiva,
            domanda: testoDomanda,
            pagina: paginaCorrente,
            storia: storiaSessione
          }})
        }});
        var risp = await r.json();
        if (!r.ok || !risp.ok) {{
          boxMessaggi.removeChild(divAttesa);
          if (risp && typeof risp.rimanenti === "number") {{
            aggiornaStatoUi({{ email: emailAttiva, rimanenti: risp.rimanenti, limite: risp.limite || 5 }});
          }}
          throw new Error((risp && risp.errore) || "Errore durante l'elaborazione della richiesta.");
        }}
        divAttesa.innerHTML = formattaTestoAi(risp.risposta);
        storiaSessione.push({{ ruolo: "user", testo: testoDomanda }});
        storiaSessione.push({{ ruolo: "model", testo: risp.risposta }});
        aggiornaStatoUi({{ email: emailAttiva, rimanenti: risp.rimanenti, limite: risp.limite }});
        boxMessaggi.scrollTop = boxMessaggi.scrollHeight;
      }} catch (err) {{
        boxErr.textContent = err.message || "Errore di comunicazione con il servizio.";
        boxErr.style.display = "block";
      }} finally {{
        if (!inputDomanda.disabled) {{
          btnInvia.disabled = false;
        }}
        btnInvia.textContent = "Invia";
      }}
    }});
  }}

  try {{
    var salvata = localStorage.getItem(STORAGE_KEY);
    if (salvata) {{
      inputEmail.value = salvata;
      verificaEmail(salvata, true);
    }}
  }} catch(e) {{}}

  // --- 2. GESTIONE CASELLA SUGGERIMENTI PUBBLICI ---
  var form = document.getElementById("form-suggerimento");
  if (!form) return;
  var btn = document.getElementById("sugg-submit");
  var esito = document.getElementById("sugg-esito");
  form.addEventListener("submit", async function(ev) {{
    ev.preventDefault();
    esito.className = "sugg-esito";
    esito.style.display = "none";
    var dati = {{
      sezione: form.sezione.value,
      firma: form.firma.value.trim(),
      titolo: form.titolo.value.trim(),
      testo: form.testo.value.trim(),
      miele: form.miele.value,
      pagina: form.getAttribute("data-pagina") || window.location.pathname
    }};
    btn.disabled = true;
    btn.textContent = "Trasmissione in corso...";
    try {{
      var r = await fetch("/api/suggerimento", {{
        method: "POST",
        headers: {{"Content-Type": "application/json"}},
        body: JSON.stringify(dati)
      }});
      var risp = await r.json();
      if (r.ok && risp.ok) {{
        esito.className = "sugg-esito ok";
        esito.innerHTML = 'Segnalazione registrata (<strong>#' + risp.numero + '</strong>): <a href="' + risp.url + '" target="_blank" rel="noopener">consulta la scheda su GitHub</a>.';
        form.titolo.value = "";
        form.testo.value = "";
      }} else {{
        throw new Error((risp && risp.errore) || "Errore durante l'invio.");
      }}
    }} catch (err) {{
      esito.className = "sugg-esito err";
      var ghUrl = "https://github.com/sinmar123/app-acquerello/issues/new?title=" +
        encodeURIComponent("[Suggerimento · " + dati.sezione + "] " + dati.titolo) +
        "&body=" + encodeURIComponent(dati.testo);
      esito.innerHTML = (err.message || "Impossibile completare la trasmissione automatica.") +
        ' È possibile <a href="' + ghUrl + '" target="_blank" rel="noopener">inviare la segnalazione su GitHub tramite questo collegamento precompilato</a>.';
    }} finally {{
      btn.disabled = false;
      btn.textContent = "Trasmetti contributo";
    }}
  }});
}})();
</script>
"""


def inietta_elementi_comuni(html: str, sezione_predefinita: str, pagina_path: str) -> str:
    barra = (
        '<div style="background:#efe6d5;border-bottom:1px solid #d8ccb8;padding:6px 14px;'
        'font-size:.86rem;display:flex;justify-content:center;gap:18px;flex-wrap:wrap">'
        '<a href="../" style="color:#6b4226;text-decoration:none;font-weight:600">'
        '← Indice generale del repertorio</a>'
        '<a href="#assistente-ai" style="color:#8c4a27;text-decoration:none;font-weight:600">'
        '🎨 Assistente tecnico AI</a>'
        '<a href="#suggerimenti" style="color:#2f5e4e;text-decoration:none;font-weight:600">'
        '💬 Invia un contributo</a></div>\n'
    )
    if 'href="../"' not in html:
        html = html.replace("<body>", "<body>\n" + barra, 1)

    blocco = blocco_chat_e_suggerimenti(sezione_predefinita, pagina_path)
    if 'id="suggerimenti"' not in html:
        if "<footer" in html:
            html = html.replace("<footer", blocco + "\n<footer", 1)
        else:
            html = html.replace("</body>", blocco + "\n</body>", 1)
    return html


def genera_home(sezioni_pronte: list[dict]) -> str:
    cards = []
    for s in sezioni_pronte:
        if not s.get("in_home", True):
            continue
        badges = "".join(f'<span class="pill">{b}</span>' for b in s.get("badge", []))
        extra_btn = ""
        if s["slug"] == "soggetti":
            extra_btn = ' <a class="btn sec" href="./alberi/">Apri subito S1 · Alberi →</a>'
        cards.append(
            f"""<article class="card">
  <div class="card-body">
    <div class="card-head">
      <span class="sig">{s['numero']}</span>
      <div>
        <h2><a class="card-tit-link" href="./{s['slug']}/">{s['titolo']}</a></h2>
        <p class="card-sub">{s['sottotitolo']}</p>
      </div>
    </div>
    <p class="card-desc">{s['descrizione']}</p>
    <div class="pills">{badges}</div>
    <div class="btn-row"><a class="btn" href="./{s['slug']}/">Consulta la sezione →</a>{extra_btn}</div>
  </div>
</article>"""
        )

    cards_html = "\n".join(cards)
    blocco_sugg = blocco_chat_e_suggerimenti("Generale / Nuovo argomento", "/")
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quaderno tecnico di acquerello - Repertorio di studio, colorimetria ed esecuzione</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#faf6ee;color:#1f1c17;line-height:1.5}}
.testa{{padding:28px 18px 22px;background:#263529;color:#f7f2e7;text-align:center}}
.testa h1{{margin:0 0 6px;font-size:1.45rem;letter-spacing:.01em}}
.testa p{{margin:0 auto;max-width:680px;font-size:.95rem;color:#d8dfd5}}
main{{max-width:820px;margin:0 auto;padding:22px 14px 12px}}
.come-funziona{{background:#fffdf8;border:1px solid #dfd5c3;border-top:4px solid #263529;border-radius:12px;padding:18px 20px;margin-bottom:24px;box-shadow:0 2px 8px rgba(31,28,23,.05)}}
.come-funziona h2{{margin:0 0 8px;font-size:1.18rem;color:#263529}}
.come-funziona p{{margin:0 0 12px;font-size:.92rem;color:#363027}}
.cf-origine{{background:#eef4ef;border:1px solid #cadbce;border-left:4px solid #263529;border-radius:8px;padding:12px 14px;margin:0 0 14px;font-size:.91rem;color:#263529}}
.cf-origine strong{{color:#1b2b20}}
.cf-passi{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0 14px}}
@media(max-width:640px){{.cf-passi{{grid-template-columns:1fr}}}}
.cf-passo{{background:#f7f2e7;border:1px solid #e2d7c5;border-radius:8px;padding:10px 12px;font-size:.88rem;color:#2e2820}}
.cf-passo strong{{display:block;color:#263529;margin-bottom:3px;font-size:.92rem}}
.cf-strumenti{{display:flex;flex-wrap:wrap;gap:10px;padding-top:10px;border-top:1px solid #e9e0cf;font-size:.87rem}}
.cf-link{{display:inline-flex;align-items:center;gap:5px;padding:6px 12px;border-radius:7px;font-weight:600;text-decoration:none}}
.cf-link.chat{{background:#fdf3ec;border:1px solid #e2bfa8;color:#6b3418}}
.cf-link.sugg{{background:#eef6f2;border:1px solid #b8d8c8;color:#1e4638}}
.cf-sviluppo{{background:#f4efe4;border:1px solid #d8ccb8;border-left:4px solid #8c4a27;border-radius:8px;padding:11px 14px;margin:0 0 14px;font-size:.89rem;color:#2e2820}}
.cf-sviluppo strong{{color:#6b3418}}
.sezioni-tit{{margin:0 0 12px;font-size:1.12rem;color:#263529}}
.grid{{display:grid;grid-template-columns:1fr;gap:18px}}
.card{{background:#fffdf8;border:1px solid #dfd5c3;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(31,28,23,.06);transition:transform .15s ease,box-shadow .15s ease}}
.card:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(31,28,23,.12)}}
.card-tit-link{{color:inherit;text-decoration:none}}
.card-tit-link:hover{{text-decoration:underline}}
.card-body{{padding:16px 18px 18px}}
.card-head{{display:flex;align-items:flex-start;gap:12px;margin-bottom:8px}}
.sig{{display:inline-flex;align-items:center;justify-content:center;min-width:32px;height:32px;border-radius:8px;background:#263529;color:#f7f2e7;font-weight:700;font-size:.95rem;margin-top:2px}}
.card-head h2{{margin:0;font-size:1.18rem;color:#1f1c17}}
.card-sub{{margin:2px 0 0;font-size:.9rem;color:#6b5e4c;font-weight:500}}
.card-desc{{margin:10px 0 12px;font-size:.92rem;color:#363027}}
.pills{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}}
.pill{{background:#efe6d5;color:#4f3d27;border:1px solid #d8ccb8;border-radius:999px;padding:3px 10px;font-size:.78rem;font-weight:600}}
.btn-row{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.btn{{display:inline-block;background:#263529;color:#f7f2e7;padding:8px 14px;border-radius:8px;font-size:.88rem;font-weight:600;text-decoration:none}}
.btn.sec{{background:#eef4ef;color:#263529;border:1px solid #9ab5a3}}
footer{{text-align:center;padding:18px;font-size:.82rem;color:#7a6f5d;border-top:1px solid #e5dccb;margin-top:24px}}
footer a{{color:#5a4d3b}}
</style>
</head>
<body>
<header class="testa">
  <h1>Quaderno tecnico di acquerello</h1>
  <p>Repertorio analitico di procedimenti esecutivi, dinamica acqua-pigmento, colorimetria e soggetti pittorici</p>
</header>
<main>
  <section class="come-funziona" aria-label="Struttura e metodo di consultazione">
    <h2>Struttura e metodo di consultazione</h2>
    <div class="cf-origine">
      <strong>Nota di metodo:</strong> chi studia oggi l'acquerello dispone di una mole vastissima di informazioni (manuali, appunti di corso, schede chimiche dei produttori, dimostrazioni filmate), preziosa ma frammentata, difficile da classificare in modo coerente e ancor più da consultare al volo quando sorge un dubbio davanti al foglio. Chi cura queste pagine si occupa anche di intelligenza artificiale e ha provato a metterla al servizio di questo studio manuale con un doppio obiettivo pratico: strutturare e classificare quel patrimonio disperso e offrire una risposta precisa e immediata quando si affronta un problema tecnico. Ne sono esempio, da un lato, l'ordinamento sistematico delle regole su acqua, carta e pigmenti o la catalogazione al secondo esatto del vasto repertorio di video didattici su YouTube; dall'altro, il calcolatore colorimetrico e l'assistente tecnico integrato nelle pagine per risolvere sul momento un dubbio esecutivo.
    </div>
    <p>
      Il repertorio sistematizza i procedimenti fondamentali per la <strong>sperimentazione diretta su campioni di studio</strong> (formato consigliato A5 in puro cotone, 300 g/m²).
      Ogni affermazione tecnica, sequenza gestuale o dato merceologico è ricondotto a una fonte documentale verificabile secondo un percorso articolato in cinque sezioni:
    </p>
    <div class="cf-passi">
      <div class="cf-passo">
        <strong>1. Controllo di acqua e supporto (Principi)</strong>
        Valutazione dei tre gradi di concentrazione del pigmento sulla tavolozza (<em>tè, latte, miele</em>) e degli stadi di evaporazione del velo d'acqua sulla carta (<em>superficie asciutta, umida satinata, bagnata</em>), per governare la fusione o prevenire i riflussi capillari.
      </div>
      <div class="cf-passo">
        <strong>2. Assetto operativo (Studio ed en plein air)</strong>
        Differenze metodologiche tra il lavoro in studio (tavolozza estesa, dotazione completa, protocollo dei campioni A5) e la pittura all'aperto (sintesi rapida, tavolozza ristretta a 6 pigmenti e prontuario delle 12 miscele M1-M12).
      </div>
      <div class="cf-passo">
        <strong>3. Colorimetria e merceologia (Sezioni 3 e 4)</strong>
        Spazio cromatico di Munsell, ottica delle velature, calcolatore spettrale Kubelka-Munk e confronto chimico tra sei serie commerciali tramite i codici del <em>Colour Index</em>.
      </div>
      <div class="cf-passo">
        <strong>4. Monografie esecutive (Soggetti pittorici)</strong>
        Analisi dei singoli temi pittorici (alberi, nuvole, fiori, acqua, rocce, architetture) attraverso più varianti procedurali, tavole sinottiche in tre fasi e rimandi al secondo esatto delle dimostrazioni filmate.
      </div>
    </div>
    <div class="cf-sviluppo">
      <strong>Repertorio in fase di sviluppo:</strong> la sezione <strong>5. Soggetti pittorici</strong> si apre con il modulo completo dedicato alla <em>Morfologia degli alberi</em>, primo argomento affrontato nel corso di studio; seguiranno progressivamente le monografie dedicate a <strong>cieli e formazioni nuvolose</strong>, <strong>fiori ed elementi botanici</strong>, <strong>specchi d'acqua e riflessi</strong>, <strong>masse rocciose</strong> e <strong>architetture</strong>.
    </div>
    <div class="cf-strumenti">
      <a class="cf-link chat" href="#assistente-ai">🎨 Quesiti operativi: consulta l'assistente tecnico AI (5 domande gratuite) ↓</a>
      <a class="cf-link sugg" href="#suggerimenti">💬 Contributi e rettifiche: trasmetti una segnalazione documentata ↓</a>
    </div>
  </section>

  <h2 class="sezioni-tit">Sezioni del repertorio</h2>
  <div class="grid">
    {cards_html}
  </div>
</main>
{blocco_sugg}
<footer>
  Quaderno tecnico di acquerello · Progetto documentale aperto su <a href="https://github.com/sinmar123/app-acquerello" target="_blank" rel="noopener">GitHub</a>
  (testi e tavole <a href="https://creativecommons.org/licenses/by/4.0/deed.it" target="_blank" rel="noopener">CC BY 4.0</a>, codice MIT)
</footer>
</body>
</html>
"""


def main():
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    sezioni_pronte = []

    for s in SEZIONI:
        script = s["script_genera"]
        html_src = s["html_generato"]
        if script.exists():
            print(f"[{s['slug']}] Rigenerazione pagina da {script.name}...")
            subprocess.run([sys.executable, str(script), "pagina"], check=True)
        if not html_src.exists():
            raise FileNotFoundError(f"File HTML sorgente non trovato: {html_src}")

        dest_dir = SITE_DIR / s["slug"]
        dest_dir.mkdir(parents=True, exist_ok=True)
        html_text = html_src.read_text(encoding="utf-8")
        html_completo = inietta_elementi_comuni(
            html_text,
            s.get("nome_form", "Generale / Nuovo argomento"),
            f"/{s['slug']}/",
        )
        dest_html = dest_dir / "index.html"
        dest_html.write_text(html_completo, encoding="utf-8")
        print(f"[{s['slug']}] Scritto {dest_html.relative_to(APP_DIR)} ({dest_html.stat().st_size // 1024} KB)")

        sezioni_pronte.append(dict(s))

    index_html = SITE_DIR / "index.html"
    index_html.write_text(genera_home(sezioni_pronte), encoding="utf-8")
    print(f"[home] Scritto {index_html.relative_to(APP_DIR)} ({index_html.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

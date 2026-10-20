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
        "titolo": "Principi generali: acqua, colore e carta",
        "sottotitolo": "Da leggere prima degli esercizi: le tre consistenze, gli stati della carta e come abbinarli",
        "descrizione": (
            "Tè, latte e miele; carta asciutta, umida, bagnata e i momenti di mezzo, riconoscibili dal lucido dell'acqua; "
            "come abbinare il pennello alla carta, fioriture comprese; bordi netti e morbidi, asciugatura, "
            "carta hot press, cold press e rough. Ogni frase con la sua fonte, dai corsi e dai video al minuto giusto."
        ),
        "badge": ["8 capitoli", "tè · latte · miele", "stati della carta", "ogni frase con la fonte"],
        "script_genera": DATI_DIR / "principi" / "genera-principi.py",
        "html_generato": DATI_DIR / "principi" / "principi.html",
    },
    {
        "slug": "alberi",
        "numero": "2",
        "nome_form": "Alberi",
        "titolo": "Alberi ad acquerello: esempi, modalità e gesti nei video",
        "sottotitolo": "Sei esempi di alberi e arbusti con 24 modalità nei video, un'infografica per ciascun video e colori liberi in studio o 6 all'aperto",
        "descrizione": (
            "Abeti e conifere in gruppo, abeti alti e radi contro il cielo, chiome tonde d'autunno, siepi e cespugli, "
            "alberi invernali con fusti chiari e brina, rami sottili e foglie brinate in primo piano: per ciascun esempio "
            "i video propongono diverse modalità di sviluppo, ognuna spiegata da un'infografica in 3 fasi e da 31 estratti video al secondo esatto."
        ),
        "badge": ["6 esempi di alberi", "24 modalità e infografiche", "31 estratti video", "colori liberi in studio · 6 all'aperto"],
        "script_genera": DATI_DIR / "alberi" / "pit-261013-video-gesti.py",
        "html_generato": DATI_DIR / "alberi" / "pit-261014-video-gesti-alberi.html",
    },
    {
        "slug": "colori",
        "numero": "3",
        "nome_form": "Teoria dei colori",
        "titolo": "Teoria dei colori per l'acquerello",
        "sottotitolo": "Munsell, luce e pigmento, velature, i sei colori di base e un calcolatore di miscele",
        "descrizione": (
            "Tinta, valore e croma secondo Munsell; perché i pigmenti non si mescolano come le luci; "
            "mescolare o velare; le schede dei sei colori della tavolozza ridotta, col nome comune e il pigmento; un calcolatore "
            "che mescola i tubetti in parti intere e cerca la miscela per un colore scelto, tutto nel browser."
        ),
        "badge": ["5 capitoli", "6 colori di base", "calcolatore di miscele", "stime da verificare sul foglietto"],
        "script_genera": DATI_DIR / "colori" / "genera-teoria-colori.py",
        "html_generato": DATI_DIR / "colori" / "teoria-colori.html",
    },
    {
        "slug": "marche",
        "numero": "4",
        "nome_form": "Confronto marche",
        "titolo": "Marche e tubetti",
        "sottotitolo": "I sei colori di base nelle serie in commercio: nome del tubetto, numero, pigmento e trasparenza",
        "descrizione": (
            "Per ognuno dei sei colori della tavolozza ridotta, il tubetto corrispondente in sei serie: Winsor &amp; Newton Cotman e Professional, "
            "Van Gogh, Daniel Smith, Schmincke Horadam, Maimeri Blu. Dati solo dalle pagine ufficiali, con il link "
            "e la data di controllo su ogni riga; e perché lo stesso nome nasconde pigmenti diversi."
        ),
        "badge": ["6 serie", "6 colori di base", "fonte ufficiale su ogni riga", "stesso nome, pigmenti diversi"],
        "script_genera": DATI_DIR / "marche" / "genera-marche.py",
        "html_generato": DATI_DIR / "marche" / "marche.html",
    },
]

OPZIONI_SEZIONE = [
    "Generale / Nuovo argomento",
    "Principi",
    "Alberi",
    "Teoria dei colori",
    "Confronto marche",
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

<section id="assistente-ai" class="sugg-wrap" aria-label="Assistente AI sull'acquerello">
  <div class="chat-box" data-pagina="{pagina_path}">
    <h2>🎨 Chiedi all'assistente di acquerello (Gemini 4 Argon)</h2>
    <p class="sugg-sub">
      Hai un dubbio su come mescolare due colori, quanta acqua tenere nel pennello, come evitare le fioriture o come eseguire uno degli esercizi?
      Inserisci la tua email per fare fino a <strong>5 domande gratuite</strong> all'assistente AI istruito sui contenuti di questo quaderno.
    </p>

    <div id="chat-step-email">
      <form id="form-chat-login" class="chat-login-row">
        <input id="chat-email-input" type="email" required maxlength="120" placeholder="La tua email (es. nome@esempio.it)" autocomplete="email">
        <button type="submit" class="sugg-btn arancio" id="chat-login-btn">Entra nella chat (5 domande)</button>
      </form>
      <p class="chat-nota-privacy">
        L'email serve solo a contare le 5 domande gratuite associate al tuo indirizzo: non inviamo newsletter né cediamo l'indirizzo a terzi.
      </p>
    </div>

    <div id="chat-step-conversazione" style="display:none">
      <div class="chat-barra-stato">
        <span>Accesso con: <strong id="chat-email-attiva"></strong> · <button type="button" id="chat-cambia-email" style="background:none;border:0;color:#6b4226;text-decoration:underline;cursor:pointer;font:inherit;padding:0">cambia email</button></span>
        <span class="chat-badge-quota" id="chat-quota-label">Domande disponibili: 5 su 5</span>
      </div>

      <div class="chat-esempi" id="chat-esempi-wrap">
        <span style="font-size:.79rem;color:#6b5e4c;align-self:center;margin-right:2px">Prova a chiedere:</span>
        <button type="button" class="chat-chip">Perché mi vengono le macchie a cavolfiore quando aggiungo colore?</button>
        <button type="button" class="chat-chip">Come ottengo un verde scuro per gli abeti coi 6 colori di base?</button>
        <button type="button" class="chat-chip">Qual è il momento giusto per buttare il sale sulla carta?</button>
      </div>

      <div id="chat-messaggi" class="chat-messaggi" aria-live="polite"></div>

      <form id="form-chat-domanda">
        <div class="chat-input-row">
          <textarea id="chat-domanda-input" required minlength="4" maxlength="1000" placeholder="Scrivi qui la tua domanda sull'acquerello..."></textarea>
          <button type="submit" class="sugg-btn arancio" id="chat-invia-btn">Chiedi</button>
        </div>
      </form>
    </div>

    <div id="chat-esito-err" class="sugg-esito err" role="alert" style="display:none"></div>
  </div>
</section>

<section id="suggerimenti" class="sugg-wrap" aria-label="Invia un suggerimento">
  <div class="sugg-box">
    <h2>💬 Suggerisci una modifica, una correzione o un video</h2>
    <p class="sugg-sub">
      Hai trovato un refuso, conosci un bel passaggio in un video su YouTube (magari indicando il minuto esatto) o vuoi proporre un'aggiunta?
      Scrivilo qui sotto senza bisogno di conoscere GitHub o il codice: se la proposta è valida la inseriamo nel quaderno.
    </p>
    <form id="form-suggerimento" data-pagina="{pagina_path}">
      <div class="sugg-hp" aria-hidden="true">
        <label>Non compilare questo campo <input type="text" name="miele" tabindex="-1" autocomplete="off"></label>
      </div>
      <div class="sugg-grid">
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-sezione">Sezione</label>
          <select id="sugg-sezione" name="sezione">
            {options_html}
          </select>
        </div>
        <div class="sugg-field" style="margin-bottom:0">
          <label for="sugg-firma">Il tuo nome o soprannome (facoltativo)</label>
          <input id="sugg-firma" name="firma" type="text" maxlength="60" placeholder="Lascia vuoto per restare anonimo">
        </div>
      </div>
      <div class="sugg-field" style="margin-top:12px">
        <label for="sugg-titolo">Titolo breve *</label>
        <input id="sugg-titolo" name="titolo" type="text" required minlength="4" maxlength="120" placeholder="Es. Nuovo video sul pino marittimo / Correzione su un pigmento">
      </div>
      <div class="sugg-field">
        <label for="sugg-testo">Il tuo suggerimento *</label>
        <textarea id="sugg-testo" name="testo" required minlength="10" maxlength="3500" placeholder="Descrivi la proposta o la correzione. Se segnali un video YouTube, incolla il link e indica da che minuto a che minuto si vede il passaggio utile."></textarea>
      </div>
      <div class="sugg-avviso">
        <strong>Avviso sulla pubblicazione:</strong> non serve registrarsi né avere un account.
        Premendo <em>Invia suggerimento</em>, il testo che hai scritto e l'eventuale nome o soprannome
        <strong>saranno pubblicati pubblicamente</strong> nella bacheca aperta delle
        <a href="https://github.com/sinmar123/app-acquerello/issues" target="_blank" rel="noopener">segnalazioni del progetto su GitHub</a>
        (sotto licenza aperta CC BY 4.0) per essere valutati e integrati nel sito.
        <strong>Non inserire indirizzi email, numeri di telefono o altri dati personali riservati.</strong>
      </div>
      <div class="sugg-actions">
        <button type="submit" class="sugg-btn" id="sugg-submit">Invia suggerimento</button>
        <a class="sugg-link-gh" href="https://github.com/sinmar123/app-acquerello/issues" target="_blank" rel="noopener">Vedi le segnalazioni già pubblicate →</a>
      </div>
      <div id="sugg-esito" class="sugg-esito" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
<script>
(function(){{
  // --- 1. GESTIONE CHAT AI (GEMINI 4 ARGON, 5 DOMANDE PER EMAIL) ---
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
    labelQuota.textContent = "Domande disponibili: " + dati.rimanenti + " su " + dati.limite;
    if (dati.rimanenti <= 0) {{
      inputDomanda.disabled = true;
      btnInvia.disabled = true;
      inputDomanda.placeholder = "Hai esaurito le 5 domande gratuite per questa email.";
    }} else {{
      inputDomanda.disabled = false;
      btnInvia.disabled = false;
      inputDomanda.placeholder = "Scrivi qui la tua domanda sull'acquerello...";
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
        throw new Error((risp && risp.errore) || "Email non valida.");
      }}
      emailAttiva = risp.email;
      try {{ localStorage.setItem(STORAGE_KEY, emailAttiva); }} catch(e) {{}}
      stepEmail.style.display = "none";
      stepConv.style.display = "block";
      aggiornaStatoUi(risp);
    }} catch (err) {{
      if (!silenzioso) {{
        boxErr.textContent = err.message || "Impossibile accedere alla chat.";
        boxErr.style.display = "block";
      }}
    }} finally {{
      if (!silenzioso) {{
        btnLogin.disabled = false;
        btnLogin.textContent = "Entra nella chat (5 domande)";
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
      divAttesa.innerHTML = "<em>Gemini 4 Argon sta preparando la risposta...</em>";
      boxMessaggi.appendChild(divAttesa);
      boxMessaggi.scrollTop = boxMessaggi.scrollHeight;

      inputDomanda.value = "";
      btnInvia.disabled = true;
      btnInvia.textContent = "Attendi...";

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
          throw new Error((risp && risp.errore) || "Errore durante la richiesta.");
        }}
        divAttesa.innerHTML = formattaTestoAi(risp.risposta);
        storiaSessione.push({{ ruolo: "user", testo: testoDomanda }});
        storiaSessione.push({{ ruolo: "model", testo: risp.risposta }});
        aggiornaStatoUi({{ email: emailAttiva, rimanenti: risp.rimanenti, limite: risp.limite }});
        boxMessaggi.scrollTop = boxMessaggi.scrollHeight;
      }} catch (err) {{
        boxErr.textContent = err.message || "Errore di comunicazione con l'assistente.";
        boxErr.style.display = "block";
      }} finally {{
        if (!inputDomanda.disabled) {{
          btnInvia.disabled = false;
        }}
        btnInvia.textContent = "Chiedi";
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
    btn.textContent = "Invio in corso...";
    try {{
      var r = await fetch("/api/suggerimento", {{
        method: "POST",
        headers: {{"Content-Type": "application/json"}},
        body: JSON.stringify(dati)
      }});
      var risp = await r.json();
      if (r.ok && risp.ok) {{
        esito.className = "sugg-esito ok";
        esito.innerHTML = 'Grazie! La tua segnalazione (<strong>#' + risp.numero + '</strong>) è stata pubblicata: <a href="' + risp.url + '" target="_blank" rel="noopener">aprila su GitHub</a>.';
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
      esito.innerHTML = (err.message || "Impossibile inviare direttamente.") +
        ' Puoi comunque <a href="' + ghUrl + '" target="_blank" rel="noopener">inviare la segnalazione su GitHub da questo link precompilato</a>.';
    }} finally {{
      btn.disabled = false;
      btn.textContent = "Invia suggerimento";
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
        '← Tutte le guide di acquerello</a>'
        '<a href="#assistente-ai" style="color:#8c4a27;text-decoration:none;font-weight:600">'
        '🎨 Chiedi all\'assistente AI</a>'
        '<a href="#suggerimenti" style="color:#2f5e4e;text-decoration:none;font-weight:600">'
        '💬 Suggerisci una modifica</a></div>\n'
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
        badges = "".join(f'<span class="pill">{b}</span>' for b in s.get("badge", []))
        cards.append(
            f"""<article class="card">
  <a class="card-link" href="./{s['slug']}/">
    <div class="card-body">
      <div class="card-head">
        <span class="sig">{s['numero']}</span>
        <div>
          <h2>{s['titolo']}</h2>
          <p class="card-sub">{s['sottotitolo']}</p>
        </div>
      </div>
      <p class="card-desc">{s['descrizione']}</p>
      <div class="pills">{badges}</div>
      <span class="btn">Apri la sezione →</span>
    </div>
  </a>
</article>"""
        )

    cards_html = "\n".join(cards)
    blocco_sugg = blocco_chat_e_suggerimenti("Generale / Nuovo argomento", "/")
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quaderno di acquerello - Guide pratiche ed esercizi</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#faf6ee;color:#1f1c17;line-height:1.5}}
.testa{{padding:28px 18px 22px;background:#263529;color:#f7f2e7;text-align:center}}
.testa h1{{margin:0 0 6px;font-size:1.45rem;letter-spacing:.01em}}
.testa p{{margin:0 auto;max-width:640px;font-size:.95rem;color:#d8dfd5}}
main{{max-width:820px;margin:0 auto;padding:22px 14px 12px}}
.come-funziona{{background:#fffdf8;border:1px solid #dfd5c3;border-top:4px solid #263529;border-radius:12px;padding:18px 20px;margin-bottom:24px;box-shadow:0 2px 8px rgba(31,28,23,.05)}}
.come-funziona h2{{margin:0 0 8px;font-size:1.18rem;color:#263529}}
.come-funziona p{{margin:0 0 12px;font-size:.92rem;color:#363027}}
.cf-passi{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0 14px}}
@media(max-width:640px){{.cf-passi{{grid-template-columns:1fr}}}}
.cf-passo{{background:#f7f2e7;border:1px solid #e2d7c5;border-radius:8px;padding:10px 12px;font-size:.88rem;color:#2e2820}}
.cf-passo strong{{display:block;color:#263529;margin-bottom:3px;font-size:.92rem}}
.cf-strumenti{{display:flex;flex-wrap:wrap;gap:10px;padding-top:10px;border-top:1px solid #e9e0cf;font-size:.87rem}}
.cf-link{{display:inline-flex;align-items:center;gap:5px;padding:6px 12px;border-radius:7px;font-weight:600;text-decoration:none}}
.cf-link.chat{{background:#fdf3ec;border:1px solid #e2bfa8;color:#6b3418}}
.cf-link.sugg{{background:#eef6f2;border:1px solid #b8d8c8;color:#1e4638}}
.sezioni-tit{{margin:0 0 12px;font-size:1.12rem;color:#263529}}
.grid{{display:grid;grid-template-columns:1fr;gap:18px}}
.card{{background:#fffdf8;border:1px solid #dfd5c3;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(31,28,23,.06);transition:transform .15s ease,box-shadow .15s ease}}
.card:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(31,28,23,.12)}}
.card-link{{display:block;color:inherit;text-decoration:none}}
.card-body{{padding:16px 18px 18px}}
.card-head{{display:flex;align-items:flex-start;gap:12px;margin-bottom:8px}}
.sig{{display:inline-flex;align-items:center;justify-content:center;min-width:32px;height:32px;border-radius:8px;background:#263529;color:#f7f2e7;font-weight:700;font-size:.95rem;margin-top:2px}}
.card-head h2{{margin:0;font-size:1.18rem;color:#1f1c17}}
.card-sub{{margin:2px 0 0;font-size:.9rem;color:#6b5e4c;font-weight:500}}
.card-desc{{margin:10px 0 12px;font-size:.92rem;color:#363027}}
.pills{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}}
.pill{{background:#efe6d5;color:#4f3d27;border:1px solid #d8ccb8;border-radius:999px;padding:3px 10px;font-size:.78rem;font-weight:600}}
.btn{{display:inline-block;background:#263529;color:#f7f2e7;padding:8px 14px;border-radius:8px;font-size:.88rem;font-weight:600}}
footer{{text-align:center;padding:18px;font-size:.82rem;color:#7a6f5d;border-top:1px solid #e5dccb;margin-top:24px}}
footer a{{color:#5a4d3b}}
</style>
</head>
<body>
<header class="testa">
  <h1>Quaderno di acquerello</h1>
  <p>Guide pratiche per studiare i gesti, le miscele e i passaggi su foglietti di prova</p>
</header>
<main>
  <section class="come-funziona" aria-label="Come funziona questo sito">
    <h2>Come funziona questo sito</h2>
    <p>
      Questo non è un manuale da leggere tutto d'un fiato, ma un <strong>quaderno pratico da tenere sul tavolo mentre dipingi</strong>.
      Prendi un piccolo foglietto di carta da acquerello (formato A5, meglio 100% cotone) e prova un solo gesto o una sola miscela alla volta, seguendo questi quattro passi:
    </p>
    <div class="cf-passi">
      <div class="cf-passo">
        <strong>1. Capire acqua e carta (Principi)</strong>
        Impara a riconoscere a occhio le 3 densità del colore sulla tavolozza (<em>tè, latte, miele</em>) e il momento esatto in cui il foglio perde il lucido dell'acqua (<em>carta asciutta, umida opaca, bagnata</em>) per evitare macchie involontarie.
      </div>
      <div class="cf-passo">
        <strong>2. Provare i gesti passo passo (Alberi)</strong>
        Per ogni soggetto trovi più modalità tratte da lezioni video su YouTube: guarda l'infografica in 3 fasi per capire pennello, stato della carta e colori, poi premi sul pulsante del video che si apre <em>al secondo esatto</em> del gesto.
      </div>
      <div class="cf-passo">
        <strong>3. Mescolare i colori (Teoria e calcolatore)</strong>
        In studio puoi usare tutti i colori che hai; se invece vuoi dipingere all'aperto o iniziare con pochi tubetti, scopri la tavolozza ridotta da 6 colori e usa il calcolatore nel browser per simulare le miscele.
      </div>
      <div class="cf-passo">
        <strong>4. Leggere l'etichetta dei tubetti (Marche)</strong>
        Due tubetti con lo stesso nome commerciale possono contenere pigmenti del tutto diversi: la tabella confronta le sigle dei pigmenti (es. PB29, PR101) nelle principali marche in commercio.
      </div>
    </div>
    <div class="cf-strumenti">
      <a class="cf-link chat" href="#assistente-ai">🎨 Hai un dubbio mentre dipingi? Chiedi all'assistente AI (5 domande gratuite) ↓</a>
      <a class="cf-link sugg" href="#suggerimenti">💬 Vuoi segnalare un video o una correzione? Usa la casella in fondo ↓</a>
    </div>
  </section>

  <h2 class="sezioni-tit">Le sezioni del quaderno</h2>
  <div class="grid">
    {cards_html}
  </div>
</main>
{blocco_sugg}
<footer>
  Quaderno di studio ad acquerello · Progetto aperto su <a href="https://github.com/sinmar123/app-acquerello" target="_blank" rel="noopener">GitHub</a>
  (testi e schede <a href="https://creativecommons.org/licenses/by/4.0/deed.it" target="_blank" rel="noopener">CC BY 4.0</a>, codice MIT)
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

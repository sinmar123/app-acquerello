"""Rimandi numerati alle fonti, con numerazione autonoma per capitolo.

Le voci possono mantenere «testo» e indicare «titolo_link», una porzione
esatta da collegare. In alternativa separano autore, titolo, pubblicazione,
nota e consultazione. «link_aggiuntivi» permette di collegare più passi di
una stessa opera, senza moltiplicare le voci. Le cautele restano visibili.
Formato editoriale: README.md, Organizzazione dei testi. Dopo una modifica
si rigenera il sito con scripts/genera-sito.py.
"""
import html

CSS = """
sup.rif { font-size: .68em; color: #555; white-space: nowrap; } sup.rif a { text-decoration: none; }
sup.rif:target { background: #fff3cd; border-radius: 3px; }
.fonti-cap { margin: 16px 0 4px; font-size: .94em; line-height: 1.5; color: #444; background: #f1efe8; border-radius: 8px; padding: 10px 12px 4px; }
.fonti-cap .fonti-tit { margin: 0 0 8px; font-weight: 700; color: #2c4f3a; }
.fonti-cap ol { margin: 0 0 6px; padding-left: 24px; } .fonti-cap li { margin-bottom: 14px; overflow-wrap: anywhere; }
.fonti-cap li:target { background: #fff3cd; }
.fonti-cap p { margin: 4px 0; }
.fonti-cap a.torna { display: inline-block; margin-top: 5px; font-size: .9em; }
.fonti-cap .fonte-nota, .fonti-cap .fonte-limite { color: #333; }
.fonti-cap details { margin-top: 5px; }
.fonti-cap summary { cursor: pointer; }
.fonti-cap :focus-visible, sup.rif a:focus-visible { outline: 2px solid #2c6a4a; outline-offset: 3px; }
"""

JS = """<script>
(function () {
  function alPunto(id) {
    var punto = document.getElementById(id);
    if (!punto) return;
    punto.setAttribute('tabindex', '-1');
    punto.focus({preventScroll: true});
  }
  document.addEventListener('click', function (ev) {
    if (!ev.target.closest || ev.button !== 0 || ev.ctrlKey || ev.metaKey || ev.shiftKey || ev.altKey) return;
    var rif = ev.target.closest('sup.rif a');
    if (rif) {
      var fonte = document.getElementById(rif.hash.slice(1));
      if (!fonte) return;
      var torna = fonte.querySelector('a.torna');
      if (torna) torna.setAttribute('href', '#' + rif.parentNode.id);
      setTimeout(function () { alPunto(fonte.id); }, 0);
      return;
    }
    var ritorno = ev.target.closest('a.torna');
    if (ritorno) setTimeout(function () { alPunto(ritorno.hash.slice(1)); }, 0);
  });
})();
</script>"""


class Capitolo:
    """Fonti numerate nell'ordine della prima citazione.

    testo_html riguarda solo il vecchio campo «testo». I campi bibliografici
    separati e «titolo_link» sono sempre testo semplice, non HTML.
    """

    def __init__(self, id_cap, fonti, sezione, testo_html=False):
        self.id = id_cap
        self.fonti = fonti
        self.sezione = sezione
        self.testo_html = testo_html
        self.ordine = []
        self.prima = {}
        self.rimandi = 0

    def rif(self, chiavi, dove, obbligatorio=True):
        if not chiavi:
            if obbligatorio:
                raise SystemExit(f"{self.sezione}: frase senza fonte in {dove}")
            return ""
        self.rimandi += 1
        rid = f"{self.id}-r{self.rimandi}"
        numeri = set()
        for k in chiavi:
            if k not in self.fonti:
                raise SystemExit(f"{self.sezione}: fonte «{k}» non definita ({dove})")
            if k not in self.ordine:
                self.ordine.append(k)
                self.prima[k] = rid
            numeri.add(self.ordine.index(k) + 1)
        link = ", ".join(f'<a href="#{self.id}-f{n}" aria-label="Fonte {n}">{n}</a>' for n in sorted(numeri))
        return f'<sup class="rif" id="{rid}">[{link}]</sup>'

    def voce(self, k):
        f = self.fonti[k]
        if "titolo" in f:
            for campo in ("autore", "titolo", "pubblicazione", "nota"):
                if not isinstance(f.get(campo), str) or not f[campo].strip():
                    raise SystemExit(f"{self.sezione}: manca {campo} nella fonte «{k}»")
            titolo = html.escape(f["titolo"], quote=True)
            if f.get("url"):
                titolo = f'<a href="{html.escape(f["url"], quote=True)}">{titolo}</a>'
            testo = (f'<p class="fonte-riferimento">{html.escape(f["autore"], quote=True)}. '
                     f'<cite>{titolo}</cite>. {html.escape(f["pubblicazione"], quote=True)}')
            if f.get("doi"):
                doi = html.escape('https://doi.org/' + f["doi"], quote=True)
                testo += f' <a href="{doi}">{doi}</a>.'
            testo += '</p>'
            for link in f.get("link_aggiuntivi", []):
                if not link.get("testo") or not link.get("url"):
                    raise SystemExit(f"{self.sezione}: collegamento incompleto nella fonte «{k}»")
                testo += ('<p class="fonte-link"><a href="' + html.escape(link["url"], quote=True)
                          + '">' + html.escape(link["testo"], quote=True) + '</a>.</p>')
            if f.get("limite"):
                testo += f'<p class="fonte-limite"><strong>{html.escape(f["limite"], quote=True)}</strong></p>'
            testo += f'<p class="fonte-nota">{html.escape(f["nota"], quote=True)}</p>'
            if f.get("consultazione"):
                testo += ('<details class="fonte-lettura"><summary>Dettagli della consultazione</summary>'
                          f'<p>{html.escape(f["consultazione"], quote=True)}</p></details>')
            return testo
        testo = f["testo"] if self.testo_html else html.escape(f["testo"], quote=True)
        url = f.get("url")
        if url:
            titolo = f.get("titolo_link")
            if not titolo:
                raise SystemExit(f"{self.sezione}: manca titolo_link nella fonte «{k}»")
            cerca = html.escape(titolo, quote=True)
            if cerca not in testo:
                raise SystemExit(f"{self.sezione}: titolo_link non trovato nel testo della fonte «{k}»")
            link = f'<a href="{html.escape(url, quote=True)}">{cerca}</a>'
            testo = testo.replace(cerca, link, 1)
        return testo

    def elenco(self):
        if not self.ordine:
            return ""
        voci = "".join(f'<li id="{self.id}-f{n}">{self.voce(k)} '
                       f'<a class="torna" href="#{self.prima[k]}" aria-label="Torna al testo che cita la fonte {n}">↩ Torna al testo</a></li>'
                       for n, k in enumerate(self.ordine, 1))
        return f'<div class="fonti-cap"><p class="fonti-tit">Fonti del capitolo</p><ol>{voci}</ol></div>'

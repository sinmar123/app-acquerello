"""Rimandi numerati alle fonti, capitolo per capitolo, nello stesso formato in tutte le sezioni del Quaderno.

Ogni capitolo numera le proprie fonti da 1, nell'ordine in cui le cita, e le elenca in fondo al capitolo,
una per riga. Il numero nel testo porta alla fonte; la freccia accanto alla fonte riporta al rimando da cui
si è partiti, oppure, senza JavaScript, al primo rimando del capitolo. Lo usano dati/principi/genera-principi.py
e dati/colori/genera-teoria-colori.py: dopo una modifica si rigenera il sito con scripts/genera-sito.py."""
import html

CSS = """
sup.rif { font-size: .68em; color: #555; white-space: nowrap; } sup.rif a { text-decoration: none; }
sup.rif:target { background: #fff3cd; border-radius: 3px; }
.fonti-cap { margin: 16px 0 4px; font-size: .85em; color: #444; background: #f1efe8; border-radius: 8px; padding: 8px 12px 2px; }
.fonti-cap .fonti-tit { margin: 0 0 4px; font-weight: 700; color: #2c4f3a; }
.fonti-cap ol { margin: 0 0 6px; padding-left: 24px; } .fonti-cap li { margin-bottom: 5px; }
.fonti-cap li:target { background: #fff3cd; }
.fonti-cap a.torna { text-decoration: none; margin-right: 2px; }
"""

JS = """<script>
(function () {
  var da = null;
  document.addEventListener('click', function (ev) {
    if (!ev.target.closest) return;
    var rif = ev.target.closest('sup.rif a');
    if (rif) { da = rif.parentNode.id; return; }
    var torna = ev.target.closest('a.torna');
    if (torna && da) { ev.preventDefault(); location.hash = da; da = null; }
  });
})();
</script>"""


class Capitolo:
    """Le fonti citate in un capitolo, numerate nell'ordine della prima citazione.

    fonti è il dizionario delle fonti della sezione; testo_html dice se il campo «testo» di una fonte
    contiene già html (Teoria dei colori) o testo semplice da proteggere (Principi)."""

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
        link = ", ".join(f'<a href="#{self.id}-f{n}">{n}</a>' for n in sorted(numeri))
        return f'<sup class="rif" id="{rid}">[{link}]</sup>'

    def voce(self, k):
        f = self.fonti[k]
        testo = f["testo"] if self.testo_html else html.escape(f["testo"], quote=True)
        url = f.get("url")
        if url:
            esterno = url.startswith("http")
            attr = ' target="_blank" rel="noopener"' if esterno else ""
            testo += f' <a href="{html.escape(url, quote=True)}"{attr}>{"apri" if esterno else "nel Quaderno"}</a>'
        return testo

    def elenco(self):
        if not self.ordine:
            return ""
        voci = "".join(f'<li id="{self.id}-f{n}"><a class="torna" href="#{self.prima[k]}" title="Torna al testo">↩</a> '
                       f'{self.voce(k)}</li>' for n, k in enumerate(self.ordine, 1))
        return f'<div class="fonti-cap"><p class="fonti-tit">Fonti del capitolo</p><ol>{voci}</ol></div>'

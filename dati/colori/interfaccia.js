// Interfaccia del calcolatore (GBOT-app-acquerello, 18/10/2026). Usa Acq (calcolatore.js), TAVOLOZZA e MUNSELL.
(function () {
  'use strict';
  if (typeof document === 'undefined') return;
  Acq.prepara(TAVOLOZZA);
  Acq.preparaMunsell(MUNSELL);
  var COL = Acq.colori();
  var DILUIZIONI = [
    { q: 1, nome: 'miele' }, { q: 0.6, nome: 'latte' }, { q: 0.35, nome: 'latte chiaro' },
    { q: 0.2, nome: 'tè' }, { q: 0.1, nome: 'tè leggero' }, { q: 0.05, nome: 'velo' }
  ];
  function nomeDiluizione(q) { for (var i = 0; i < DILUIZIONI.length; i++) if (DILUIZIONI[i].q === q) return DILUIZIONI[i].nome; return ''; }
  function $(id) { return document.getElementById(id); }
  function hex(R) { return Acq.aHex(Acq.aSrgb(R)); }
  function ricetta(lista) {
    if (lista.length === 1) return 'solo ' + lista[0].col.nome.charAt(0).toLowerCase() + lista[0].col.nome.slice(1) + ' (' + lista[0].col.pigmento + ')';
    return lista.map(function (x) { return x.parti + ' ' + (x.parti === 1 ? 'parte' : 'parti') + ' di ' + x.col.nome.charAt(0).toLowerCase() + x.col.nome.slice(1) + ' (' + x.col.pigmento + ')'; }).join(' + ');
  }

  // --- Mescola ---
  var sel = [$('mc1'), $('mc2'), $('mc3')], parti = [$('mp1'), $('mp2'), $('mp3')];
  sel.forEach(function (s, i) {
    if (i === 2) { var o = document.createElement('option'); o.value = ''; o.textContent = '(nessun terzo colore)'; s.appendChild(o); }
    COL.forEach(function (c) { var o = document.createElement('option'); o.value = c.id; o.textContent = c.nome + ' (' + c.pigmento + ')'; s.appendChild(o); });
  });
  sel[0].value = 'giallo'; sel[1].value = 'oltremare'; sel[2].value = '';
  // parametro nell'indirizzo: ?mix=giallo:10,ceruleo:1 precompila il mescolatore (usato dalla sezione Alberi)
  (function () {
    var m = /[?&]mix=([^&#]*)/.exec(window.location.search);
    if (!m) return;
    var voci = decodeURIComponent(m[1]).split(',').map(function (v) { var p = v.split(':'); return { id: p[0], parti: parseInt(p[1], 10) || 1 }; })
      .filter(function (v) { return Acq.colore(v.id); }).slice(0, 3);
    if (!voci.length) return;
    if (voci.length === 1) voci.push({ id: voci[0].id, parti: voci[0].parti }); // un solo tubetto: stesso colore anche nella seconda riga
    [0, 1, 2].forEach(function (k) {
      var v = voci[k];
      sel[k].value = v ? v.id : '';
      parti[k].value = v ? Math.max(1, Math.min(10, v.parti)) : 1;
    });
  })();
  function leggiMix() {
    var lista = [];
    sel.forEach(function (s, i) {
      if (!s.value) return;
      var p = Math.max(1, Math.min(10, parseInt(parti[i].value, 10) || 1));
      parti[i].value = p;
      var c = Acq.colore(s.value), gia = null;
      lista.forEach(function (x) { if (x.col === c) gia = x; });
      if (gia) gia.parti += p; else lista.push({ col: c, parti: p });
    });
    return lista;
  }
  // consistenza della proposta aperta da «Trova la miscela»; torna al colore pieno (miele)
  // appena si cambiano a mano colori o parti
  var diluizioneScelta = 1;
  function aggiornaMix() {
    var lista = leggiMix();
    if (!lista.length) return;
    var R = Acq.mescola(lista);
    var Rs = diluizioneScelta === 1 ? R : Acq.diluisci(R, diluizioneScelta), m = Acq.munsell(Rs);
    $('mcamp').style.background = hex(Rs);
    $('mtxt').innerHTML = '<span class="ric">' + ricetta(lista) + '</span>' +
      (diluizioneScelta === 1 ? '' : '<br>Consistenza della proposta: <b>' + nomeDiluizione(diluizioneScelta) + '</b>') +
      '<br>Anteprima a schermo: ' + hex(Rs) +
      '<br>Munsell approssimato: <b>' + m.testo + '</b> (valore ' + m.valore.toFixed(1).replace('.', ',') + ' su 10)';
    var s = '';
    DILUIZIONI.forEach(function (d) {
      var Rq = d.q === 1 ? R : Acq.diluisci(R, d.q);
      s += '<div class="passo' + (d.q === diluizioneScelta ? ' scelto' : '') + '" style="background:' + hex(Rq) + '" title="' + d.nome + ': ' + Acq.munsell(Rq).testo + '"><span>' + d.nome + '</span></div>';
    });
    $('mstriscia').innerHTML = s;
  }
  function aggiornaAMano() { diluizioneScelta = 1; aggiornaMix(); }
  sel.concat(parti).forEach(function (el) { el.addEventListener('input', aggiornaAMano); el.addEventListener('change', aggiornaAMano); });
  aggiornaMix();

  // --- Trova la miscela ---
  function giudizio(d) {
    if (d <= 0.03) return '<span class="vicino si">molto vicino</span>';
    if (d <= 0.07) return '<span class="vicino quasi">abbastanza vicino</span>';
    return '<span class="vicino no">lontano: forse fuori dalla portata dei sei colori della tavolozza ridotta</span>';
  }
  function cerca() {
    var obj = $('tobj').value, dil = $('tdil').checked;
    $('tris').innerHTML = '<p class="aiuto">Calcolo in corso...</p>';
    setTimeout(function () {
      var ris = Acq.cerca(obj, 10, 5, dil, DILUIZIONI.map(function (d) { return d.q; })), h = '';
      ris.forEach(function (r, i) {
        var m = Acq.munsell(r.R);
        h += '<div class="prop"><div class="coppia"><div style="background:' + obj + '" title="obiettivo"></div><div style="background:' + hex(r.R) + '" title="proposta"></div></div>' +
          '<div class="prop-txt"><b>' + (i + 1) + '.</b> <b class="ric">' + ricetta(r.lista) + '</b>' +
          (dil ? '<br>consistenza: <b>' + nomeDiluizione(r.q) + '</b>' : '') +
          '<br>distanza OKLab ' + r.d.toFixed(3).replace('.', ',') + ', ' + giudizio(r.d) + ' · Munsell circa ' + m.testo +
          '<br><button class="usa" type="button" data-i="' + i + '">Apri nel mescolatore</button></div></div>';
      });
      $('tris').innerHTML = h + '<p class="aiuto">A sinistra di ogni coppia il colore scelto, a destra la proposta. Sono stime: vanno provate su carta in tre dosi (meno, come scritto, di più).</p>';
      Array.prototype.forEach.call(document.querySelectorAll('#tris .usa'), function (b) {
        b.addEventListener('click', function () {
          var r = ris[parseInt(b.getAttribute('data-i'), 10)];
          [0, 1, 2].forEach(function (k) {
            var x = r.lista[k];
            if (!x && k === 1) x = r.lista[0]; // un solo tubetto: stesso colore anche nella seconda riga
            sel[k].value = x ? x.col.id : '';
            if (x) parti[k].value = x.parti;
          });
          diluizioneScelta = r.q;
          aggiornaMix();
          $('mescola').scrollIntoView({ behavior: 'smooth' });
        });
      });
    }, 20);
  }
  $('tvai').addEventListener('click', cerca);
})();

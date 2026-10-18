// Calcolatore di miscele del Quaderno di acquerello.
// Scritto per il Quaderno (GBOT-app-acquerello, 18/10/2026), JavaScript puro, nessuna dipendenza esterna.
// Modello: Kubelka-Munk a una costante su spettri di 38 bande. Lo spettro di ogni tubetto si ricava
// dal suo colore sRGB con le tabelle di spectral.js (spettri-spectraljs.js, licenza MIT, vedi lì).
// Tutti i risultati sono stime: i colori dei tubetti in tavolozza.json sono provvisori.
var Acq = (function () {
  'use strict';
  var N = 38;

  // sRGB <-> lineare
  function decod(x) { x /= 255; return x > 0.04045 ? Math.pow((x + 0.055) / 1.055, 2.4) : x / 12.92; }
  function codif(x) { x = x > 0.0031308 ? 1.055 * Math.pow(x, 1 / 2.4) - 0.055 : 12.92 * x; return Math.max(0, Math.min(255, Math.round(x * 255))); }
  function daHex(h) { h = h.replace('#', ''); return [0, 2, 4].map(function (i) { return parseInt(h.substr(i, 2), 16); }); }
  function aHex(rgb) { return '#' + rgb.map(function (v) { return ('0' + v.toString(16)).slice(-2); }).join('').toUpperCase(); }

  // matrici sRGB (D65) e OKLab (Björn Ottosson, https://bottosson.github.io/posts/oklab/)
  var XYZ_RGB = [[3.2409699419, -1.5373831776, -0.4986107603], [-0.9692436363, 1.8759675015, 0.0415550574], [0.0556300797, -0.2039769589, 1.0569715142]];
  var XYZ_LMS = [[0.8190224380, 0.3619062601, -0.1288737815], [0.0329836539, 0.9292868616, 0.0361446664], [0.0481771894, 0.2642395318, 0.6335478285]];
  var LMS_LAB = [[0.2104542683, 0.7936177747, -0.0040720430], [1.9779985324, -2.4285922420, 0.4505937096], [0.0259040425, 0.7827717125, -0.8086757549]];
  function mv(m, v) { return [0, 1, 2].map(function (i) { return m[i][0] * v[0] + m[i][1] * v[1] + m[i][2] * v[2]; }); }

  // colore sRGB -> spettro di riflettanza: scomposizione in bianco + due primari secondari/primari
  function spettro(hex) {
    var l = daHex(hex).map(decod);
    var w = Math.min(l[0], l[1], l[2]);
    var r = l[0] - w, g = l[1] - w, b = l[2] - w;
    var c = Math.min(g, b), m = Math.min(r, b), y = Math.min(r, g);
    var rr = Math.max(0, Math.min(r - b, r - g)), gg = Math.max(0, Math.min(g - b, g - r)), bb = Math.max(0, Math.min(b - g, b - r));
    var S = SPETTRI, R = new Array(N);
    for (var i = 0; i < N; i++) {
      R[i] = Math.max(1e-6, w * S.W[i] + c * S.C[i] + m * S.M[i] + y * S.Y[i] + rr * S.R[i] + gg * S.G[i] + bb * S.B[i]);
    }
    return R;
  }
  function ks(r) { return (1 - r) * (1 - r) / (2 * r); }
  function km(k) { return 1 + k - Math.sqrt(k * k + 2 * k); }
  function xyz(R) {
    return SPETTRI.CMF.map(function (riga) { var s = 0; for (var i = 0; i < N; i++) s += riga[i] * R[i]; return s; });
  }
  var BIANCO = null;
  function bianco() { if (!BIANCO) { var u = []; for (var i = 0; i < N; i++) u.push(1); BIANCO = xyz(u); } return BIANCO; }

  // spettro -> sRGB, OKLab, CIELAB
  function aSrgb(R) { return mv(XYZ_RGB, xyz(R)).map(codif); }
  function oklabXyz(X) { var l = mv(XYZ_LMS, X).map(Math.cbrt); return mv(LMS_LAB, l); }
  function oklab(R) { return oklabXyz(xyz(R)); }
  function oklabHex(hex) { var l = daHex(hex).map(decod); var X = [0.4123907993 * l[0] + 0.3575843394 * l[1] + 0.1804807884 * l[2], 0.2126390059 * l[0] + 0.7151686788 * l[1] + 0.0721923154 * l[2], 0.0193308187 * l[0] + 0.1191947798 * l[1] + 0.9505321522 * l[2]]; return oklabXyz(X); }
  function lab(R) {
    var X = xyz(R), W = bianco();
    var f = function (t) { return t > 216 / 24389 ? Math.cbrt(t) : (24389 / 27 * t + 16) / 116; };
    var fx = f(X[0] / W[0]), fy = f(X[1] / W[1]), fz = f(X[2] / W[2]);
    return [116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)];
  }
  function distanza(a, b) { return Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2) + Math.pow(a[2] - b[2], 2)); }

  // peso di un tubetto nella media dei K/S: proporzionale alla sua luminanza Y, come in spectral.js.
  // Senza questo correttivo, con spettri ricavati dall'sRGB, i colori scuri coprirebbero quelli chiari
  // molto più che sulla carta. È una scelta del modello, da rivedere con la taratura (campo forza).
  function peso(R) { return Math.max(1e-4, xyz(R)[1]); }

  // tavolozza
  var COL = [], CARTA = null;
  function prepara(tav) {
    COL = tav.colori.map(function (c) {
      var R = spettro(c.srgb);
      return { id: c.id, nome: c.nome, pigmento: c.pigmento, srgb: c.srgb, forza: (c.forza || 1) * peso(R), R: R, KS: R.map(ks) };
    });
    var Rc = spettro(tav.carta.srgb);
    CARTA = { id: 'carta', nome: 'carta', R: Rc, KS: Rc.map(ks), forza: peso(Rc) };
    return COL;
  }
  function colore(id) { for (var i = 0; i < COL.length; i++) if (COL[i].id === id) return COL[i]; return null; }

  // mescolanza Kubelka-Munk a una costante: media dei K/S pesata con parti x forza di tintura
  function mescola(lista) {
    var R = new Array(N), tot = 0;
    lista.forEach(function (x) { tot += x.parti * x.col.forza; });
    for (var i = 0; i < N; i++) {
      var k = 0;
      lista.forEach(function (x) { k += x.col.KS[i] * x.parti * x.col.forza; });
      R[i] = km(k / tot);
    }
    return R;
  }

  // diluizione: velatura stesa sul bianco della carta, frazione di pigmento q (1 = miele, pieno)
  function diluisci(R, q) {
    var Rc = CARTA.R, out = new Array(N);
    for (var i = 0; i < N; i++) out[i] = km(q * ks(R[i]) + (1 - q) * ks(Rc[i]));
    return out;
  }

  // notazione Munsell approssimata: valore da L*, tinta e croma dalla tabella munsell-tinte.json
  var TINTE = [];
  function preparaMunsell(t) { TINTE = t.tinte.slice().sort(function (a, b) { return a.h - b.h; }); }
  var FAMIGLIE = ['R', 'YR', 'Y', 'GY', 'G', 'BG', 'B', 'PB', 'P', 'RP'];
  function indiceTinta(nome) { var m = nome.match(/^([\d.]+)([A-Z]+)$/); return FAMIGLIE.indexOf(m[2]) * 10 + parseFloat(m[1]); }
  function munsell(R) {
    var L = lab(R), V = L[0] / 10, C = Math.sqrt(L[1] * L[1] + L[2] * L[2]);
    if (C < 3) return { testo: 'N ' + V.toFixed(1), valore: V, croma: 0, tinta: 'N' };
    var h = (Math.atan2(L[2], L[1]) * 180 / Math.PI + 360) % 360;
    var n = TINTE.length, a = TINTE[n - 1], b = TINTE[0], ha = a.h - 360, hb = b.h;
    for (var i = 0; i < n - 1; i++) if (h >= TINTE[i].h && h < TINTE[i + 1].h) { a = TINTE[i]; b = TINTE[i + 1]; ha = a.h; hb = b.h; }
    if (h >= TINTE[n - 1].h) { a = TINTE[n - 1]; b = TINTE[0]; ha = a.h; hb = b.h + 360; }
    var t = (h - ha) / (hb - ha);
    var ia = indiceTinta(a.tinta), ib = indiceTinta(b.tinta); if (ib < ia) ib += 100;
    var idx = (ia + t * (ib - ia)) % 100;
    var fam = Math.floor(idx / 10), passo = Math.round((idx - fam * 10) * 2) / 2;
    if (passo === 0) { fam = (fam + 9) % 10; passo = 10; }
    var k = a.k + t * (b.k - a.k);
    var croma = C / k;
    var tinta = passo.toString().replace('.', ',') + FAMIGLIE[fam];
    return { testo: tinta + ' ' + V.toFixed(1).replace('.', ',') + '/' + croma.toFixed(1).replace('.', ','), valore: V, croma: croma, tinta: tinta };
  }

  // ricerca a forza bruta: coppie e terne dei 6 colori, parti intere da 1 a max, senza doppioni proporzionali
  function mcd(a, b) { return b ? mcd(b, a % b) : a; }
  function cerca(hexObiettivo, max, quanti, usaDiluizione) {
    var obj = oklabHex(hexObiettivo), ris = [], n = COL.length;
    max = max || 10; quanti = quanti || 5;
    var diluizioni = usaDiluizione ? [1, 0.6, 0.35, 0.2, 0.1] : [1];
    function prova(lista) {
      var R = mescola(lista);
      diluizioni.forEach(function (q) {
        var Rq = q === 1 ? R : diluisci(R, q);
        ris.push({ lista: lista, q: q, R: Rq, d: distanza(oklab(Rq), obj) });
      });
    }
    for (var i = 0; i < n; i++) {
      prova([{ col: COL[i], parti: 1 }]);
      for (var j = i + 1; j < n; j++) {
        for (var a = 1; a <= max; a++) for (var b = 1; b <= max; b++) {
          if (mcd(a, b) !== 1) continue;
          prova([{ col: COL[i], parti: a }, { col: COL[j], parti: b }]);
        }
        for (var k = j + 1; k < n; k++) {
          for (var a2 = 1; a2 <= max; a2++) for (var b2 = 1; b2 <= max; b2++) for (var c2 = 1; c2 <= max; c2++) {
            if (mcd(mcd(a2, b2), c2) !== 1) continue;
            prova([{ col: COL[i], parti: a2 }, { col: COL[j], parti: b2 }, { col: COL[k], parti: c2 }]);
          }
        }
      }
    }
    ris.sort(function (x, y) { return x.d - y.d; });
    // tiene una sola proposta per combinazione di colori e diluizione, così le 5 proposte sono diverse
    var visti = {}, out = [];
    for (var z = 0; z < ris.length && out.length < quanti; z++) {
      var chiave = ris[z].lista.map(function (x) { return x.col.id; }).join('+') + '@' + ris[z].q;
      if (visti[chiave]) continue;
      visti[chiave] = 1; out.push(ris[z]);
    }
    return out;
  }

  return {
    prepara: prepara, preparaMunsell: preparaMunsell, colore: colore, colori: function () { return COL; },
    mescola: mescola, diluisci: diluisci, aSrgb: aSrgb, aHex: aHex, daHex: daHex, oklab: oklab, oklabHex: oklabHex,
    lab: lab, munsell: munsell, cerca: cerca, distanza: distanza, spettro: spettro
  };
})();
if (typeof module !== 'undefined') module.exports = Acq;

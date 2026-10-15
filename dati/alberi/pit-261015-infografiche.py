# Infografiche di sintesi («La nostra proposta passo passo sul foglietto A5»)
# poste in fondo a ciascuna delle 7 sezioni (A1..A7), dopo tutti i video e le immagini.

COLORI_HEX = {
    "M1": ("#c8d946", "M1 verde giallo"),
    "M2": ("#5c9648", "M2 verde medio"),
    "M3": ("#2b5b3c", "M3 verde scuro"),
    "M4": ("#1d3d3d", "M4 verde-blu d'ombra"),
    "M5": ("#e59a28", "M5 arancio"),
    "M6": ("#c4512d", "M6 rame"),
    "M7": ("#6e2826", "M7 rosso cupo"),
    "M8": ("#4a3556", "M8 viola"),
    "M9": ("#9c94b4", "M9 grigio-lilla"),
    "M10": ("#222629", "M10 scuro"),
    "M11": ("#7d7365", "M11 grigio caldo"),
    "M12": ("#6ba4d6", "M12 azzurri"),
    "acqua": ("#b8ddf5", "acqua pulita"),
    "mascherante": ("#7ec8e3", "mascherante"),
    "sale": ("#d8d2c5", "sale fino"),
}


def svg_wrap(inner):
    return (
        '<svg viewBox="0 0 220 145" xmlns="http://www.w3.org/2000/svg" role="img">'
        '<rect x="2" y="2" width="216" height="141" rx="6" fill="#fcfaf4" stroke="#d5cfc0" stroke-width="1.5"/>'
        + inner
        + "</svg>"
    )


INFOGRAFICHE = {
    "A1": {
        "titolo": "La nostra proposta per gli abeti fitti (in 4 fasi sul foglietto A5)",
        "sottotitolo": "Sintesi consigliata combinando il fondo luminoso, la discesa col fianco del pennello e la sovrapposizione per piani.",
        "fasi": [
            {
                "titolo": "Fondo chiaro, assi e punte a V",
                "carta": "asciutta",
                "colori": ["M1", "M2"],
                "attrezzo": "Tondo n. 2 (punta)",
                "testo": "Sul velo chiaro di M1 già asciutto, traccia 3-4 assi verticali leggeri e discontinui ad altezze diverse; parti da ogni cima con piccoli tratti stretti a V rivolti verso l'alto.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#eef3c8" opacity="0.7"/>'
                    '<line x1="55" y1="32" x2="55" y2="120" stroke="#7a8c50" stroke-width="1.2" stroke-dasharray="4,5"/>'
                    '<line x1="105" y1="18" x2="105" y2="124" stroke="#7a8c50" stroke-width="1.2" stroke-dasharray="4,5"/>'
                    '<line x1="158" y1="28" x2="158" y2="122" stroke="#7a8c50" stroke-width="1.2" stroke-dasharray="4,5"/>'
                    '<path d="M55,30 L51,23 M55,30 L59,23 M55,36 L49,29 M55,36 L61,29" stroke="#5c9648" stroke-width="2" stroke-linecap="round"/>'
                    '<path d="M105,16 L101,9 M105,16 L109,9 M105,23 L98,15 M105,23 L112,15 M105,30 L96,22 M105,30 L114,22" stroke="#2b5b3c" stroke-width="2.2" stroke-linecap="round"/>'
                    '<path d="M158,26 L154,19 M158,26 L162,19 M158,33 L151,26 M158,33 L165,26" stroke="#5c9648" stroke-width="2" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Coni chiari dietro, scuri davanti",
                "carta": "asciutta",
                "colori": ["M2", "M3"],
                "attrezzo": "Tondo n. 8 (fianco)",
                "testo": "Dipingi prima i coni più lontani e chiari (M2) col fianco del pennello a zig-zag asimmetrico; lasciali asciugare e sovrapponi davanti i coni più grandi e densi in M3.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#eef3c8" opacity="0.7"/>'
                    '<g fill="#78a862" opacity="0.65">'
                    '<polygon points="55,24 34,116 76,116"/>'
                    '<polygon points="158,22 135,116 181,116"/>'
                    '</g>'
                    '<g stroke="#2b5b3c" stroke-linecap="round">'
                    '<path d="M105,12 L101,6 M105,12 L109,6" stroke-width="2"/>'
                    '<path d="M105,20 L92,28 M105,22 L119,31 M105,32 L85,43 M105,35 L125,46 M105,47 L78,61 M105,50 L132,64 M105,64 L72,80 M105,68 L138,83 M105,82 L65,102 M105,86 L144,105" stroke-width="5.5"/>'
                    '<path d="M95,38 L114,42 M89,56 L120,60 M84,74 L126,79 M78,94 L131,98" stroke-width="6.5"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Luce a sinistra e ombra a destra",
                "carta": "umida",
                "colori": ["M1", "M4"],
                "attrezzo": "Tondo n. 6",
                "testo": "Mentre il cono in M3 è ancora umido, tocca le punte a sinistra (lato al sole) con M1 giallo-verde o solleva il colore, e appoggia M4 sul lato destro e sotto i rami.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#eef3c8" opacity="0.7"/>'
                    '<polygon points="55,24 34,116 76,116" fill="#78a862" opacity="0.55"/>'
                    '<polygon points="158,22 135,116 181,116" fill="#78a862" opacity="0.55"/>'
                    '<path d="M105,12 L65,106 L144,106 Z" fill="#2b5b3c" opacity="0.88"/>'
                    '<path d="M103,18 L72,98 L98,98 Z" fill="#c8d946" opacity="0.75"/>'
                    '<path d="M106,20 L104,106 L144,106 Z" fill="#162e2e" opacity="0.85"/>'
                    '<circle cx="28" cy="24" r="9" fill="#f4d03f" opacity="0.85"/>'
                    '<path d="M40,28 L56,34" stroke="#d4ac0d" stroke-width="1.5"/>'
                ),
            },
            {
                "titolo": "Brevi tratti di tronco nei varchi",
                "carta": "asciutta",
                "colori": ["M10"],
                "attrezzo": "Tondo n. 2 o rigger",
                "testo": "A chioma completamente asciutta, segna il tronco e qualche rametto solo a brevi tratti discontinui negli spazi rimasti aperti fra i rami e alla base.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#eef3c8" opacity="0.7"/>'
                    '<polygon points="55,24 34,114 76,114" fill="#6a9b58" opacity="0.75"/>'
                    '<polygon points="158,22 135,114 181,114" fill="#6a9b58" opacity="0.75"/>'
                    '<path d="M105,12 L65,106 L144,106 Z" fill="#2b5b3c"/>'
                    '<path d="M103,18 L72,98 L98,98 Z" fill="#b8cc40" opacity="0.65"/>'
                    '<path d="M106,20 L104,106 L144,106 Z" fill="#162e2e" opacity="0.82"/>'
                    '<line x1="105" y1="44" x2="105" y2="53" stroke="#221a15" stroke-width="2.4"/>'
                    '<line x1="105" y1="72" x2="105" y2="83" stroke="#221a15" stroke-width="2.8"/>'
                    '<line x1="105" y1="104" x2="105" y2="124" stroke="#221a15" stroke-width="3.4"/>'
                    '<line x1="55" y1="112" x2="55" y2="124" stroke="#221a15" stroke-width="2.5"/>'
                    '<line x1="158" y1="112" x2="158" y2="124" stroke="#221a15" stroke-width="2.5"/>'
                ),
            },
        ],
    },
    "A2": {
        "titolo": "La nostra proposta per gli abeti alti contro il cielo (in 4 fasi)",
        "sottotitolo": "Costruzione sul cielo azzurro già asciutto: prima il fusto sottile, poi i piani staccati che lasciano passare il cielo.",
        "fasi": [
            {
                "titolo": "Il tronco lungo sul cielo asciutto",
                "carta": "asciutta",
                "colori": ["M12", "M5", "M11"],
                "attrezzo": "Rigger o tondo n. 2",
                "testo": "Sul cielo azzurro (M12) steso in anticipo e ben asciutto, tira col rigger il tronco dal basso verso l'alto: più largo alla base e sottilissimo in cima.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#cde3f5"/>'
                    '<path d="M108,130 L110,16" stroke="#8a5a36" stroke-width="2.6" stroke-linecap="round"/>'
                    '<path d="M109,130 L110,60" stroke="#4a3b32" stroke-width="3.6" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "La punta e i rami alti e radi",
                "carta": "asciutta",
                "colori": ["M2"],
                "attrezzo": "Tondo n. 4 (punta)",
                "testo": "Parti dalla cima con due o tre piccoli tocchi verticali, poi scendi nella metà alta con rami corti e ben distanziati in M2, lasciando larghi spazi di cielo.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#cde3f5"/>'
                    '<path d="M108,130 L110,16" stroke="#6b4c35" stroke-width="2.8" stroke-linecap="round"/>'
                    '<g stroke="#4e8742" stroke-width="3.2" stroke-linecap="round">'
                    '<path d="M110,15 L108,10 M110,15 L113,11"/>'
                    '<path d="M109,26 L98,30 M110,28 L122,32"/>'
                    '<path d="M109,42 L91,47 M110,45 L126,49"/>'
                    '<path d="M109,58 L86,64 M110,60 L131,66"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "I palchi bassi a tocchi saltellati",
                "carta": "asciutta",
                "colori": ["M2", "M3"],
                "attrezzo": "Tondo n. 6 (pancia)",
                "testo": "Nella metà bassa allarga i piani in M3 appoggiando e spingendo il pennello a scatti irregolari da un lato all'altro, senza mai chiudere i varchi d'azzurro.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#cde3f5"/>'
                    '<path d="M108,130 L110,16" stroke="#6b4c35" stroke-width="2.8" stroke-linecap="round"/>'
                    '<g stroke="#4e8742" stroke-width="3.4" stroke-linecap="round">'
                    '<path d="M109,26 L98,30 M110,28 L122,32 M109,42 L91,47 M110,45 L126,49 M109,58 L86,64 M110,60 L131,66"/>'
                    '</g>'
                    '<g stroke="#2b5b3c" stroke-width="5" stroke-linecap="round">'
                    '<path d="M108,75 L76,82 M110,78 L139,84"/>'
                    '<path d="M108,93 L68,101 M110,96 L146,103"/>'
                    '<path d="M108,110 L74,117 M110,112 L138,118"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Ombra sotto i piani e tronco nei varchi",
                "carta": "umida",
                "colori": ["M4", "M11"],
                "attrezzo": "Tondo n. 4",
                "testo": "Sul verde ancora umido appoggia pochi tocchi di M4 sotto i palchi bassi; a secco, ricollega e scurisci a tratti il tronco solo nei varchi tra i piani.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#cde3f5"/>'
                    '<path d="M108,130 L110,16" stroke="#5a3e2b" stroke-width="3" stroke-linecap="round"/>'
                    '<g stroke="#4e8742" stroke-width="3.4" stroke-linecap="round">'
                    '<path d="M109,26 L98,30 M110,28 L122,32 M109,42 L91,47 M110,45 L126,49 M109,58 L86,64 M110,60 L131,66"/>'
                    '</g>'
                    '<g stroke="#2b5b3c" stroke-width="5" stroke-linecap="round">'
                    '<path d="M108,75 L76,82 M110,78 L139,84 M108,93 L68,101 M110,96 L146,103 M108,110 L74,117 M110,112 L138,118"/>'
                    '</g>'
                    '<g stroke="#162e2e" stroke-width="3.2" stroke-linecap="round">'
                    '<path d="M110,80 L139,86 M110,98 L145,105 M110,114 L137,120"/>'
                    '</g>'
                ),
            },
        ],
    },
    "A3": {
        "titolo": "La nostra proposta per i faggi d'autunno (in 4 fasi)",
        "sottotitolo": "Lavorazione tutta a umido dal chiaro allo scuro: oro in alto, rame al centro, rosso cupo sotto e rametti scalfiti.",
        "fasi": [
            {
                "titolo": "I lobi dorati col pennello di pancia",
                "carta": "asciutta",
                "colori": ["M5"],
                "attrezzo": "Tondo grande n. 10",
                "testo": "Stendi 2-3 masse tondeggianti di M5 muovendo il pennello di pancia dal centro verso il bordo per ottenere un contorno frastagliato e qualche piccolo vuoto.",
                "svg": svg_wrap(
                    '<circle cx="78" cy="68" r="36" fill="#e59a28" opacity="0.82"/>'
                    '<circle cx="132" cy="62" r="40" fill="#e59a28" opacity="0.85"/>'
                    '<circle cx="106" cy="86" r="32" fill="#e59a28" opacity="0.8"/>'
                    '<circle cx="98" cy="58" r="5" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Gocce di rame e cremisi a fresco",
                "carta": "umida",
                "colori": ["M6"],
                "attrezzo": "Tondo medio n. 6",
                "testo": "Subito, mentre M5 è ben bagnato, lascia cadere gocce più dense di M6 al centro e nella metà bassa dei lobi: lasciale allargare da sole senza ripassare.",
                "svg": svg_wrap(
                    '<circle cx="78" cy="68" r="36" fill="#e59a28" opacity="0.82"/>'
                    '<circle cx="132" cy="62" r="40" fill="#e59a28" opacity="0.85"/>'
                    '<circle cx="106" cy="86" r="32" fill="#e59a28" opacity="0.8"/>'
                    '<ellipse cx="82" cy="76" rx="24" ry="18" fill="#c4512d" opacity="0.82"/>'
                    '<ellipse cx="134" cy="72" rx="26" ry="20" fill="#c4512d" opacity="0.85"/>'
                    '<circle cx="98" cy="58" r="5" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Ombra bassa (M7) e incontro col verde",
                "carta": "umida",
                "colori": ["M7", "M3"],
                "attrezzo": "Tondo medio n. 6",
                "testo": "Ancora a umido, picchietta M7 lungo la base di ogni lobo; sul fianco che tocca gli abeti, accosta di punta il verde scuro (M3) perché si sfrangi nel rame.",
                "svg": svg_wrap(
                    '<circle cx="78" cy="68" r="36" fill="#e59a28" opacity="0.82"/>'
                    '<circle cx="132" cy="62" r="40" fill="#e59a28" opacity="0.85"/>'
                    '<ellipse cx="82" cy="76" rx="24" ry="18" fill="#c4512d" opacity="0.82"/>'
                    '<ellipse cx="134" cy="72" rx="26" ry="20" fill="#c4512d" opacity="0.85"/>'
                    '<path d="M46,84 Q78,114 110,98 Q142,114 168,84 L164,98 Q110,122 50,98 Z" fill="#6e2826" opacity="0.9"/>'
                    '<polygon points="34,26 14,114 54,114" fill="#2b5b3c" opacity="0.9"/>'
                ),
            },
            {
                "titolo": "Fili chiari scalfiti con la tessera",
                "carta": "umida",
                "colori": ["M7"],
                "attrezzo": "Tessera di plastica",
                "testo": "Quando il colore ha perso il lucido (quasi asciutto), tira 3-4 tratti rapidi dal basso verso l'alto con lo spigolo della tessera per aprire sottili rametti chiari.",
                "svg": svg_wrap(
                    '<circle cx="78" cy="68" r="36" fill="#e59a28" opacity="0.82"/>'
                    '<circle cx="132" cy="62" r="40" fill="#e59a28" opacity="0.85"/>'
                    '<ellipse cx="82" cy="76" rx="24" ry="18" fill="#c4512d" opacity="0.82"/>'
                    '<ellipse cx="134" cy="72" rx="26" ry="20" fill="#c4512d" opacity="0.85"/>'
                    '<path d="M46,84 Q78,114 110,98 Q142,114 168,84 L164,98 Q110,122 50,98 Z" fill="#6e2826" opacity="0.9"/>'
                    '<polygon points="34,26 14,114 54,114" fill="#2b5b3c" opacity="0.9"/>'
                    '<path d="M82,96 L74,70 M82,86 L90,68 M132,94 L126,64 M130,80 L142,62" stroke="#fbeec8" stroke-width="1.8" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A4": {
        "titolo": "La nostra proposta per le siepi rosso-rame (in 4 fasi)",
        "sottotitolo": "Blocchi bassi a cima quasi piatta, fascia scura sciolta a tratti alla base, cupola scura in mezzo e prato davanti.",
        "fasi": [
            {
                "titolo": "I blocchi bassi a tocchi orizzontali",
                "carta": "asciutta",
                "colori": ["M5"],
                "attrezzo": "Tondo medio n. 6",
                "testo": "Stendi due blocchi bassi e larghi in M5 con piccoli tocchi orizzontali dalla cima quasi piatta in giù, lasciando uno spazio aperto fra i due.",
                "svg": svg_wrap(
                    '<rect x="18" y="48" width="74" height="36" rx="8" fill="#e59a28" opacity="0.85"/>'
                    '<rect x="124" y="45" width="78" height="39" rx="8" fill="#e59a28" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Rame a fresco e fascia scura alla base",
                "carta": "umida",
                "colori": ["M6", "M7"],
                "attrezzo": "Tondo medio n. 6",
                "testo": "Nel blocco ancora umido lascia cadere gocce di M6 al centro e una fascia stretta di M7 lungo la base, lasciando più chiaro il bordo alto al sole.",
                "svg": svg_wrap(
                    '<rect x="18" y="48" width="74" height="36" rx="8" fill="#e59a28" opacity="0.85"/>'
                    '<rect x="124" y="45" width="78" height="39" rx="8" fill="#e59a28" opacity="0.85"/>'
                    '<rect x="20" y="58" width="70" height="22" rx="5" fill="#c4512d" opacity="0.85"/>'
                    '<rect x="126" y="56" width="74" height="24" rx="5" fill="#c4512d" opacity="0.85"/>'
                    '<rect x="20" y="76" width="70" height="9" rx="3" fill="#6e2826"/>'
                    '<rect x="126" y="76" width="74" height="9" rx="3" fill="#6e2826"/>'
                ),
            },
            {
                "titolo": "Sciogliere la base e fare la cupola",
                "carta": "umida",
                "colori": ["acqua", "M4"],
                "attrezzo": "Piatto umido + tondo n. 6",
                "testo": "Col pennello pulito e umido sciogli la fascia scura solo in 2-3 punti verso il prato; nello spazio fra le due siepi dipingi la cupola scura del cespuglio in M4.",
                "svg": svg_wrap(
                    '<rect x="18" y="48" width="74" height="36" rx="8" fill="#c4512d" opacity="0.85"/>'
                    '<rect x="124" y="45" width="78" height="39" rx="8" fill="#c4512d" opacity="0.85"/>'
                    '<rect x="20" y="76" width="70" height="9" rx="3" fill="#6e2826"/>'
                    '<rect x="126" y="76" width="74" height="9" rx="3" fill="#6e2826"/>'
                    '<ellipse cx="45" cy="88" rx="14" ry="6" fill="#6e2826" opacity="0.45"/>'
                    '<ellipse cx="165" cy="88" rx="16" ry="6" fill="#6e2826" opacity="0.45"/>'
                    '<path d="M86,84 Q108,34 130,84 Z" fill="#1d3d3d"/>'
                ),
            },
            {
                "titolo": "La passata leggera sul prato brinato",
                "carta": "umida",
                "colori": ["acqua", "M9"],
                "attrezzo": "Piatto o tondo grande",
                "testo": "Bagna con acqua pulita la striscia del prato davanti e passa una pennellata leggera e semplice di grigio-lilla (M9) subito sotto le siepi.",
                "svg": svg_wrap(
                    '<rect x="18" y="48" width="74" height="36" rx="8" fill="#c4512d" opacity="0.85"/>'
                    '<rect x="124" y="45" width="78" height="39" rx="8" fill="#c4512d" opacity="0.85"/>'
                    '<rect x="20" y="76" width="70" height="9" rx="3" fill="#6e2826"/>'
                    '<rect x="126" y="76" width="74" height="9" rx="3" fill="#6e2826"/>'
                    '<path d="M86,84 Q108,34 130,84 Z" fill="#1d3d3d"/>'
                    '<rect x="12" y="84" width="196" height="46" rx="4" fill="#d9d4e6" opacity="0.7"/>'
                    '<rect x="16" y="84" width="188" height="12" rx="3" fill="#9c94b4" opacity="0.65"/>'
                ),
            },
        ],
    },
    "A5": {
        "titolo": "La nostra proposta per le latifoglie brinate (in 4 fasi)",
        "sottotitolo": "Fusti protetti all'inizio col mascherante, veli fusi sul bagnato col sale, massa scura dietro e ombra su un lato del fusto.",
        "fasi": [
            {
                "titolo": "I fusti sottili col mascherante",
                "carta": "asciutta",
                "colori": ["mascherante"],
                "attrezzo": "Tiralinee",
                "testo": "Prima di ogni colore, sulla carta bianca asciutta traccia col tiralinee e il mascherante 2-3 fusti sottili e biforcati a Y; lascia asciugare del tutto.",
                "svg": svg_wrap(
                    '<path d="M75,130 L78,24 M77,68 L94,34 M142,130 L138,28 M140,74 L124,42" stroke="#5bc0de" stroke-width="3" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Veli fusi sul bagnato e pizzico di sale",
                "carta": "bagnata",
                "colori": ["M5", "M9", "sale"],
                "attrezzo": "Tondo n. 10 + sale fino",
                "testo": "Bagna il foglio e stendi M5 oro in alto e M9 grigio-lilla in basso sopra il mascherante; appena il lilla perde il lucido dell'acqua, spargi qualche grano di sale.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="55" rx="6" fill="#e59a28" opacity="0.45"/>'
                    '<rect x="14" y="58" width="192" height="68" rx="6" fill="#9c94b4" opacity="0.6"/>'
                    '<path d="M75,130 L78,24 M77,68 L94,34 M142,130 L138,28 M140,74 L124,42" stroke="#5bc0de" stroke-width="3" stroke-linecap="round"/>'
                    '<g fill="#ffffff" opacity="0.9">'
                    '<circle cx="52" cy="78" r="2.2"/><circle cx="64" cy="92" r="1.8"/><circle cx="108" cy="74" r="2.4"/>'
                    '<circle cx="118" cy="88" r="2"/><circle cx="162" cy="82" r="2.2"/><circle cx="96" cy="98" r="1.8"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Massa scura (M8) e velo di rametti",
                "carta": "asciutta",
                "colori": ["M8"],
                "attrezzo": "Tondo n. 8 + ventaglio",
                "testo": "A carta asciutta spazzola via il sale, dipingi la massa scura in M8 nella fascia bassa (sfumando il bordo alto con acqua) e apri in alto il velo di rametti col ventaglio.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="55" rx="6" fill="#e59a28" opacity="0.4"/>'
                    '<rect x="14" y="58" width="192" height="68" rx="6" fill="#9c94b4" opacity="0.5"/>'
                    '<path d="M20,128 Q60,72 110,82 Q160,70 200,128 Z" fill="#4a3556" opacity="0.88"/>'
                    '<path d="M75,130 L78,24 M77,68 L94,34 M142,130 L138,28 M140,74 L124,42" stroke="#5bc0de" stroke-width="3" stroke-linecap="round"/>'
                    '<path d="M55,34 Q78,18 102,32 M116,36 Q140,20 166,34" stroke="#6d5678" stroke-width="1.2" stroke-dasharray="2,3" fill="none"/>'
                ),
            },
            {
                "titolo": "Togliere il mascherante e ombra sul fusto",
                "carta": "asciutta",
                "colori": ["M9"],
                "attrezzo": "Gomma crêpe + tondo n. 2",
                "testo": "Stacca il mascherante a secco per scoprire i fusti bianchi; con la punta del pennello passa un filo sottile di M9 lungo il solo bordo destro di ciascun fusto.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="55" rx="6" fill="#e59a28" opacity="0.4"/>'
                    '<rect x="14" y="58" width="192" height="68" rx="6" fill="#9c94b4" opacity="0.5"/>'
                    '<path d="M20,128 Q60,72 110,82 Q160,70 200,128 Z" fill="#4a3556" opacity="0.88"/>'
                    '<path d="M75,130 L78,24 M77,68 L94,34 M142,130 L138,28 M140,74 L124,42" stroke="#fcfaf4" stroke-width="3.6" stroke-linecap="round"/>'
                    '<path d="M76.5,130 L79.5,24 M143.5,130 L139.5,28" stroke="#6c6282" stroke-width="1.3" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A6": {
        "titolo": "La nostra proposta per gli arbusti brinati (in 4 fasi)",
        "sottotitolo": "Sul fondo chiaro dell'acqua già asciutto: filo sottilissimo di mascherante, rami rapidi dal basso, foglie scure e bordo ammorbidito.",
        "fasi": [
            {
                "titolo": "Il filo sottile di mascherante",
                "carta": "asciutta",
                "colori": ["M12", "mascherante"],
                "attrezzo": "Tiralinee",
                "testo": "Sul fondo azzurro chiaro (M12) completamente asciutto, traccia col tiralinee un arco sottilissimo (sotto il millimetro) dove andrà il bordo superiore di ogni foglia.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#d9ecfa"/>'
                    '<path d="M52,64 Q70,52 88,62 M116,48 Q136,36 154,46 M124,88 Q144,76 162,86" stroke="#3aa6d0" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "I rami sottili dal basso in alto",
                "carta": "asciutta",
                "colori": ["M10"],
                "attrezzo": "Rigger",
                "testo": "Quando il mascherante è asciutto, carica il rigger con M10 e tira pochi rami sottili e slanciati dal basso verso l'alto con un gesto continuo.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#d9ecfa"/>'
                    '<path d="M35,132 Q75,85 148,38 M78,94 Q112,86 158,82 M62,105 Q58,78 72,58" stroke="#222629" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
                    '<path d="M52,64 Q70,52 88,62 M116,48 Q136,36 154,46 M124,88 Q144,76 162,86" stroke="#3aa6d0" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Le foglie scure appoggiate al filo",
                "carta": "asciutta",
                "colori": ["M4", "M10"],
                "attrezzo": "Tondo fine n. 4",
                "testo": "Con la punta del tondo n. 4 in M4 e M10 dipingi le foglie ovali appoggiandoti contro e sopra il filo di mascherante.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#d9ecfa"/>'
                    '<path d="M35,132 Q75,85 148,38 M78,94 Q112,86 158,82 M62,105 Q58,78 72,58" stroke="#222629" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
                    '<path d="M50,65 Q70,52 90,63 Q72,78 50,65 Z" fill="#1d3d3d"/>'
                    '<path d="M114,49 Q136,36 156,47 Q138,63 114,49 Z" fill="#222629"/>'
                    '<path d="M122,89 Q144,76 164,87 Q146,102 122,89 Z" fill="#1d3d3d"/>'
                    '<path d="M52,64 Q70,52 88,62 M116,48 Q136,36 154,46 M124,88 Q144,76 162,86" stroke="#3aa6d0" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Togliere il mascherante e ammorbidire",
                "carta": "asciutta",
                "colori": ["acqua", "M12"],
                "attrezzo": "Gomma crêpe + tondo umido",
                "testo": "A foglia ben asciutta, stacca il mascherante per scoprire il filo bianco di brina e sfioralo appena con un pennello pulito e umido per legarlo alla foglia.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="133" rx="4" fill="#d9ecfa"/>'
                    '<path d="M35,132 Q75,85 148,38 M78,94 Q112,86 158,82 M62,105 Q58,78 72,58" stroke="#222629" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
                    '<path d="M50,65 Q70,52 90,63 Q72,78 50,65 Z" fill="#1d3d3d"/>'
                    '<path d="M114,49 Q136,36 156,47 Q138,63 114,49 Z" fill="#222629"/>'
                    '<path d="M122,89 Q144,76 164,87 Q146,102 122,89 Z" fill="#1d3d3d"/>'
                    '<path d="M52,64 Q70,52 88,62 M116,48 Q136,36 154,46 M124,88 Q144,76 162,86" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A7": {
        "titolo": "La nostra proposta per i riflessi nell'acqua ferma (in 4 fasi)",
        "sottotitolo": "Si dipingono quando gli alberi sopra la riva sono asciutti: acqua bagnata, discesa verticale a tavola inclinata, scuro sotto la riva e righe chiare a secco.",
        "fasi": [
            {
                "titolo": "Bagnare l'acqua sotto la riva asciutta",
                "carta": "asciutta",
                "colori": ["acqua"],
                "attrezzo": "Piatto largo",
                "testo": "Con gli alberi sopra la riva già ben asciutti, bagna tutta la zona dell'acqua con acqua pulita a pennellate orizzontali leggere senza strofinare il fondo.",
                "svg": svg_wrap(
                    '<polygon points="45,14 28,52 62,52" fill="#2b5b3c"/>'
                    '<circle cx="95" cy="36" r="18" fill="#e59a28"/>'
                    '<circle cx="122" cy="38" r="16" fill="#c4512d"/>'
                    '<polygon points="168,12 150,52 186,52" fill="#1d3d3d"/>'
                    '<line x1="12" y1="52" x2="208" y2="52" stroke="#5a4b3c" stroke-width="2"/>'
                    '<rect x="12" y="53" width="196" height="80" fill="#cbe4f7" opacity="0.65"/>'
                    '<path d="M28,72 L192,72 M36,94 L184,94 M28,116 L192,116" stroke="#85bce8" stroke-width="1.5" stroke-dasharray="6,4"/>'
                ),
            },
            {
                "titolo": "Calare i colori in verticale sull'acqua",
                "carta": "bagnata",
                "colori": ["M5", "M6", "M3"],
                "attrezzo": "Piatto da mezzo pollice",
                "testo": "Sull'acqua bagnata tira pennellate verticali dalla riva in giù riprendendo in corrispondenza i colori degli alberi sopra: prima i caldi, poi i verdi.",
                "svg": svg_wrap(
                    '<polygon points="45,14 28,52 62,52" fill="#2b5b3c"/>'
                    '<circle cx="95" cy="36" r="18" fill="#e59a28"/>'
                    '<circle cx="122" cy="38" r="16" fill="#c4512d"/>'
                    '<polygon points="168,12 150,52 186,52" fill="#1d3d3d"/>'
                    '<rect x="12" y="53" width="196" height="80" fill="#cbe4f7" opacity="0.65"/>'
                    '<rect x="34" y="53" width="24" height="46" rx="6" fill="#2b5b3c" opacity="0.55"/>'
                    '<rect x="82" y="53" width="28" height="42" rx="6" fill="#e59a28" opacity="0.6"/>'
                    '<rect x="110" y="53" width="26" height="42" rx="6" fill="#c4512d" opacity="0.6"/>'
                    '<rect x="156" y="53" width="24" height="48" rx="6" fill="#1d3d3d" opacity="0.55"/>'
                    '<line x1="12" y1="52" x2="208" y2="52" stroke="#5a4b3c" stroke-width="2"/>'
                ),
            },
            {
                "titolo": "Tavola inclinata e scuro sotto la riva",
                "carta": "bagnata",
                "colori": ["M10"],
                "attrezzo": "Tondo medio n. 6",
                "testo": "Inclina leggermente la tavoletta perché i colori scendano a strisce morbide nell'azzurro, e picchietta subito sotto la riva una linea scura discontinua in M10.",
                "svg": svg_wrap(
                    '<polygon points="45,14 28,52 62,52" fill="#2b5b3c"/>'
                    '<circle cx="95" cy="36" r="18" fill="#e59a28"/>'
                    '<circle cx="122" cy="38" r="16" fill="#c4512d"/>'
                    '<polygon points="168,12 150,52 186,52" fill="#1d3d3d"/>'
                    '<rect x="12" y="53" width="196" height="80" fill="#cbe4f7" opacity="0.65"/>'
                    '<rect x="34" y="53" width="24" height="62" rx="8" fill="#2b5b3c" opacity="0.5"/>'
                    '<rect x="82" y="53" width="28" height="56" rx="8" fill="#e59a28" opacity="0.55"/>'
                    '<rect x="110" y="53" width="26" height="56" rx="8" fill="#c4512d" opacity="0.55"/>'
                    '<rect x="156" y="53" width="24" height="64" rx="8" fill="#1d3d3d" opacity="0.5"/>'
                    '<rect x="24" y="52" width="170" height="7" rx="3" fill="#222629" opacity="0.82"/>'
                ),
            },
            {
                "titolo": "Poche linee chiare orizzontali a secco",
                "carta": "asciutta",
                "colori": ["acqua"],
                "attrezzo": "Piatto umido + fazzoletto",
                "testo": "A foglio completamente asciutto, passa un pennello pulito e umido in orizzontale avanti e indietro due volte e tampona subito col fazzoletto per aprire poche increspature.",
                "svg": svg_wrap(
                    '<polygon points="45,14 28,52 62,52" fill="#2b5b3c"/>'
                    '<circle cx="95" cy="36" r="18" fill="#e59a28"/>'
                    '<circle cx="122" cy="38" r="16" fill="#c4512d"/>'
                    '<polygon points="168,12 150,52 186,52" fill="#1d3d3d"/>'
                    '<rect x="12" y="53" width="196" height="80" fill="#cbe4f7" opacity="0.65"/>'
                    '<rect x="34" y="53" width="24" height="62" rx="8" fill="#2b5b3c" opacity="0.5"/>'
                    '<rect x="82" y="53" width="28" height="56" rx="8" fill="#e59a28" opacity="0.55"/>'
                    '<rect x="110" y="53" width="26" height="56" rx="8" fill="#c4512d" opacity="0.55"/>'
                    '<rect x="156" y="53" width="24" height="64" rx="8" fill="#1d3d3d" opacity="0.5"/>'
                    '<rect x="24" y="52" width="170" height="7" rx="3" fill="#222629" opacity="0.82"/>'
                    '<line x1="28" y1="74" x2="142" y2="74" stroke="#f7fbff" stroke-width="2.2" stroke-linecap="round"/>'
                    '<line x1="72" y1="92" x2="188" y2="92" stroke="#f7fbff" stroke-width="2" stroke-linecap="round"/>'
                    '<line x1="40" y1="108" x2="130" y2="108" stroke="#f7fbff" stroke-width="1.8" stroke-linecap="round"/>'
                ),
            },
        ],
    },
}


def rendi_infografica(sigla, t, e, pill):
    info = INFOGRAFICHE.get(sigla)
    if not info:
        return ""
    carte = []
    for i, f in enumerate(info["fasi"], 1):
        chips = []
        for c_id in f.get("colori", []):
            col_hex, col_lab = COLORI_HEX.get(c_id, ("#888", c_id))
            chips.append(
                f'<span class="chip-col"><span class="dot" style="background:{col_hex}"></span>{e(col_lab)}</span>'
            )
        riga_chips = " ".join(chips)
        carte.append(
            f'<div class="fase-card">'
            f'<div class="fase-testa"><span class="fase-num">{i}</span>'
            f'<span class="fase-tit">{e(f["titolo"])}</span></div>'
            f'<div class="fase-svg">{f["svg"]}</div>'
            f'<div class="fase-meta">{pill(f["carta"])} <span class="fase-pen">🖌 {e(f["attrezzo"])}</span></div>'
            f'<div class="fase-chips">{riga_chips}</div>'
            f'<p class="fase-txt">{e(f["testo"])}</p>'
            f"</div>"
        )
    coda = []
    if t.get("controllo"):
        coda.append(f'<div class="info-check ok"><b>✓ Cosa controllare sul foglietto:</b> {e(t["controllo"])}</div>')
    if t.get("attenzione"):
        att = " · ".join(e(x) for x in t["attenzione"])
        coda.append(f'<div class="info-check att"><b>⚠ Da evitare:</b> {att}</div>')
    return (
        f'<div class="proposta-info">'
        f'<div class="proposta-head">'
        f'<h3>{e(info["titolo"])}</h3>'
        f'<p>{e(info["sottotitolo"])}</p>'
        f"</div>"
        f'<div class="fasi-grid">{"".join(carte)}</div>'
        f'<div class="info-coda">{"".join(coda)}</div>'
        f"</div>"
    )

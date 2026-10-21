# Infografiche SVG passo-passo dedicate a ciascuna delle 24 modalità video (A1-M1 .. A6-M2).
# Ogni modalità ha 3 fasi illustrate che spiegano visivamente cosa propone quel video:
# stato della carta, pennello o attrezzo, colori usati nel video (senza marche commerciali) e gesto.

COLORI_HEX = {
    "giallo_limone": ("#ebd834", "giallo limone / cadmio"),
    "verde_oro": ("#b8c93a", "verde oro"),
    "oro_chinacridone": ("#c47f17", "oro chinacridone"),
    "verde_chiaro": ("#7cb356", "verde chiaro"),
    "verde_oliva": ("#6b8238", "verde oliva / vescica"),
    "verde_bosco": ("#2b5b3c", "verde medio / scuro"),
    "turchese_cob": ("#38a3a5", "turchese di cobalto"),
    "blu_ftalo": ("#1b4965", "blu ftalo"),
    "cobalto": ("#3a6ea5", "blu cobalto / ceruleo"),
    "oltremare": ("#2b4c8c", "blu oltremare"),
    "prussia": ("#1b365d", "blu di Prussia"),
    "indaco": ("#263248", "indaco / grigio di Payne"),
    "lilla": ("#8f85a8", "grigio-lilla / viola"),
    "cadmio_arancio": ("#e58728", "arancio / rosso chiaro"),
    "rosso_inglese": ("#b5482a", "rosso inglese / rame"),
    "cremisi": ("#8a2432", "cremisi / rosso scuro"),
    "siena_nat": ("#c98a2c", "terra di Siena naturale"),
    "siena_bruc": ("#9e4726", "terra di Siena bruciata"),
    "ombra_bruc": ("#4f3728", "terra d'ombra bruciata"),
    "seppia": ("#2e241f", "seppia / bruno scuro"),
    "acqua": ("#b8ddf5", "acqua pulita"),
    "mascherante": ("#5bc0de", "liquido mascherante"),
    "nastro": ("#e2d9c5", "nastro di carta"),
    "sale": ("#d8d2c5", "sale fino"),
}


def svg_wrap(inner):
    return (
        '<svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg" role="img">'
        '<rect x="2" y="2" width="216" height="136" rx="6" fill="#fcfaf4" stroke="#d5cfc0" stroke-width="1.5"/>'
        + inner
        + "</svg>"
    )


INFOGRAFICHE = {
    # =========================================================================
    # A1 - ABETI E CONIFERE IN GRUPPO (4 modalità)
    # =========================================================================
    "A1-M1": {
        "titolo": "Infografica del video: dall'abete singolo (di punta o di fianco) al gruppo per strati",
        "fasi": [
            {
                "titolo": "Abete vicino: asse e punta a V",
                "carta": "asciutta",
                "colori": ["ombra_bruc", "verde_bosco"],
                "attrezzo": "Tondo n. 6 (di punta)",
                "testo": "Si traccia un asse leggero e discontinuo. Si parte dalla cima con piccoli tratti stretti a V, rivolti verso l'alto, e si scende con tocchi minuti di punta.",
                "svg": svg_wrap(
                    '<line x1="110" y1="18" x2="110" y2="124" stroke="#7a5c43" stroke-width="1.5" stroke-dasharray="5,5"/>'
                    '<path d="M110,18 L105,11 M110,18 L115,11 M110,25 L103,18 M110,25 L117,18" stroke="#2b5b3c" stroke-width="2.2" stroke-linecap="round"/>'
                    '<path d="M110,33 L96,39 M110,35 L124,41 M110,44 L90,52 M110,46 L130,54 M110,56 L84,66 M110,58 L136,68 M110,70 L78,82 M110,72 L142,84" stroke="#2b5b3c" stroke-width="2.4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Abete medio: zig-zag col fianco",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo n. 6 (di fianco)",
                "testo": "Si scende più rapidamente dalla cima con il pennello inclinato, premendo il fianco a zig-zag asimmetrico e allargando verso la base.",
                "svg": svg_wrap(
                    '<line x1="110" y1="16" x2="110" y2="124" stroke="#7a5c43" stroke-width="1.4" stroke-dasharray="4,5"/>'
                    '<path d="M110,16 L106,10 M110,16 L114,10" stroke="#2b5b3c" stroke-width="2.2" stroke-linecap="round"/>'
                    '<path d="M108,24 L94,32 L122,40 L86,52 L130,62 L78,76 L138,88 L70,104 L146,114" fill="none" stroke="#2b5b3c" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>'
                ),
            },
            {
                "titolo": "Gruppo: chiari dietro, scuri davanti",
                "carta": "asciutta",
                "colori": ["verde_chiaro", "verde_bosco", "seppia"],
                "attrezzo": "Tondo n. 6",
                "testo": "Si dipinge prima la fila di abeti lontani molto diluiti, la si lascia asciugare del tutto e davanti si sovrappongono gli abeti medi e scuri.",
                "svg": svg_wrap(
                    '<polygon points="48,28 28,118 68,118" fill="#8abf6e" opacity="0.55"/>'
                    '<polygon points="92,22 70,118 114,118" fill="#8abf6e" opacity="0.55"/>'
                    '<polygon points="165,26 144,118 186,118" fill="#8abf6e" opacity="0.55"/>'
                    '<polygon points="68,20 44,122 92,122" fill="#4e8742" opacity="0.82"/>'
                    '<polygon points="140,24 116,122 164,122" fill="#4e8742" opacity="0.82"/>'
                    '<polygon points="112,12 80,126 144,126" fill="#1e442b"/>'
                ),
            },
        ],
    },
    "A1-M2": {
        "titolo": "Infografica del video: cono rapido, luce sollevata a sinistra e ombra a destra",
        "fasi": [
            {
                "titolo": "Cono rapido in verde-azzurro",
                "carta": "asciutta",
                "colori": ["cobalto", "giallo_limone"],
                "attrezzo": "Tondo n. 12",
                "testo": "Si traccia una linea centrale e si imposta in pochi secondi la sagoma del cono sui due lati, tirando verso l'esterno qualche punta col pennello.",
                "svg": svg_wrap(
                    '<line x1="110" y1="14" x2="110" y2="122" stroke="#2f6f5e" stroke-width="2.5"/>'
                    '<path d="M110,14 L72,114 L148,114 Z" fill="#3b7a68" opacity="0.85"/>'
                    '<path d="M96,38 L82,42 M124,40 L138,44 M88,64 L72,70 M132,66 L148,72 M80,92 L62,98 M138,94 L156,100" stroke="#2f6f5e" stroke-width="3" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Luce sollevata a sinistra",
                "carta": "umida",
                "colori": ["acqua"],
                "attrezzo": "Pennello pulito e asciugato",
                "testo": "Mentre il cono è ancora umido, si asciuga il pennello su un fazzoletto e si solleva il colore sul lato sinistro per aprire la luce.",
                "svg": svg_wrap(
                    '<circle cx="30" cy="26" r="10" fill="#f4d03f"/>'
                    '<path d="M110,14 L72,114 L148,114 Z" fill="#3b7a68" opacity="0.85"/>'
                    '<path d="M108,20 L76,108 L106,108 Z" fill="#dcebe4" opacity="0.78"/>'
                    '<path d="M62,56 L92,48" stroke="#85bce8" stroke-width="2" stroke-dasharray="3,3"/>'
                ),
            },
            {
                "titolo": "Ombra a destra e abeti lontani",
                "carta": "umida",
                "colori": ["indaco", "cobalto"],
                "attrezzo": "Tondo n. 12",
                "testo": "Si lascia cadere un tono scuro sul lato destro, in ombra; dietro si aggiungono abeti più piccoli con un grigio-azzurro molto diluito.",
                "svg": svg_wrap(
                    '<polygon points="56,34 38,114 74,114" fill="#8fa8b8" opacity="0.55"/>'
                    '<polygon points="166,30 148,114 184,114" fill="#8fa8b8" opacity="0.55"/>'
                    '<path d="M110,14 L72,116 L148,116 Z" fill="#3b7a68"/>'
                    '<path d="M108,20 L76,110 L105,110 Z" fill="#b8d8be" opacity="0.75"/>'
                    '<path d="M110,18 L108,116 L148,116 Z" fill="#182a30" opacity="0.88"/>'
                ),
            },
        ],
    },
    "A1-M3": {
        "titolo": "Infografica del video: abete sciolto, con verde oro, blu ftalo e rosso fusi a umido",
        "fasi": [
            {
                "titolo": "Rami sciolti in turchese e ftalo",
                "carta": "asciutta",
                "colori": ["turchese_cob", "blu_ftalo"],
                "attrezzo": "Tondo in martora n. 7",
                "testo": "Si parte dalla cima sottile e si scende con pennellate sciolte verso l'esterno, alternando turchese di cobalto e blu ftalo.",
                "svg": svg_wrap(
                    '<path d="M110,14 L110,124" stroke="#1b4965" stroke-width="2"/>'
                    '<path d="M110,20 Q96,28 88,30 M110,24 Q124,32 132,34 M110,38 Q90,48 76,50 M110,42 Q128,52 142,54" stroke="#38a3a5" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
                    '<path d="M110,60 Q86,72 68,74 M110,64 Q134,76 150,78 M110,84 Q82,98 62,102 M110,88 Q138,102 156,106" stroke="#1b4965" stroke-width="5.5" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Verde oro fuso nei rami umidi",
                "carta": "umida",
                "colori": ["verde_oro"],
                "attrezzo": "Tondo n. 7",
                "testo": "Mentre i rami blu-verdi sono ancora umidi, si toccano le zone in luce con il verde oro e lo si lascia espandere da sé.",
                "svg": svg_wrap(
                    '<path d="M110,14 L66,112 L154,112 Z" fill="#28666e" opacity="0.8"/>'
                    '<ellipse cx="94" cy="48" rx="16" ry="10" fill="#c5d63a" opacity="0.85"/>'
                    '<ellipse cx="86" cy="76" rx="20" ry="12" fill="#c5d63a" opacity="0.85"/>'
                    '<ellipse cx="118" cy="64" rx="14" ry="9" fill="#c5d63a" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Scuro nei rami e rosso sul tronco",
                "carta": "umida",
                "colori": ["blu_ftalo", "cadmio_arancio"],
                "attrezzo": "Tondo n. 7",
                "testo": "Si appoggia il blu-verde denso sotto i rami. Il tronco si tocca con rosso o arancio di cadmio, che col verde dà un bruno scuro neutro.",
                "svg": svg_wrap(
                    '<path d="M110,14 L66,112 L154,112 Z" fill="#28666e" opacity="0.82"/>'
                    '<ellipse cx="90" cy="62" rx="18" ry="14" fill="#c5d63a" opacity="0.8"/>'
                    '<path d="M108,52 L148,108 L106,108 Z" fill="#102a3a" opacity="0.85"/>'
                    '<line x1="110" y1="42" x2="110" y2="128" stroke="#8c2d19" stroke-width="4" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A1-M4": {
        "titolo": "Infografica del video: tronco e rami segnati solo a brevi tratti nei varchi",
        "fasi": [
            {
                "titolo": "Chioma con piccoli varchi aperti",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo medio",
                "testo": "Quando si dipinge la chioma, si lasciano in punti sparsi piccoli spazi bianchi irregolari fra i palchi di rami, soprattutto nella metà bassa.",
                "svg": svg_wrap(
                    '<path d="M110,14 L64,108 L156,108 Z" fill="#2b5b3c"/>'
                    '<ellipse cx="108" cy="48" rx="9" ry="6" fill="#fcfaf4"/>'
                    '<ellipse cx="112" cy="76" rx="12" ry="7" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Base e tratti di fusto nei varchi",
                "carta": "asciutta",
                "colori": ["siena_nat", "siena_bruc"],
                "attrezzo": "Tondo piccolo n. 2",
                "testo": "A chioma asciutta si accenna la base del tronco sotto l'albero e si prosegue verso l'alto solo con brevi segmenti dentro i varchi.",
                "svg": svg_wrap(
                    '<path d="M110,14 L64,108 L156,108 Z" fill="#2b5b3c"/>'
                    '<ellipse cx="108" cy="48" rx="9" ry="6" fill="#fcfaf4"/>'
                    '<ellipse cx="112" cy="76" rx="12" ry="7" fill="#fcfaf4"/>'
                    '<line x1="108" y1="42" x2="108" y2="54" stroke="#b86b35" stroke-width="3"/>'
                    '<line x1="110" y1="69" x2="110" y2="83" stroke="#b86b35" stroke-width="3.5"/>'
                    '<line x1="110" y1="106" x2="110" y2="128" stroke="#b86b35" stroke-width="4.5"/>'
                ),
            },
            {
                "titolo": "Ombra sul tronco e piccoli rami",
                "carta": "asciutta",
                "colori": ["siena_bruc", "oltremare"],
                "attrezzo": "Tondo piccolo n. 2",
                "testo": "Si scurisce il lato destro dei tratti di tronco con bruno scuro (Siena bruciata + oltremare) e si accennano due rametti che reggono la chioma.",
                "svg": svg_wrap(
                    '<path d="M110,14 L64,108 L156,108 Z" fill="#2b5b3c"/>'
                    '<ellipse cx="108" cy="48" rx="9" ry="6" fill="#fcfaf4"/>'
                    '<ellipse cx="112" cy="76" rx="12" ry="7" fill="#fcfaf4"/>'
                    '<line x1="108" y1="42" x2="108" y2="54" stroke="#3a2318" stroke-width="3"/>'
                    '<path d="M110,69 L110,83 M110,76 L120,71" stroke="#3a2318" stroke-width="3" stroke-linecap="round"/>'
                    '<line x1="110" y1="106" x2="110" y2="128" stroke="#3a2318" stroke-width="4.5"/>'
                ),
            },
        ],
    },

    # =========================================================================
    # A2 - ABETI ALTI E RADI CONTRO IL CIELO (3 modalità)
    # =========================================================================
    "A2-M1": {
        "titolo": "Infografica del video: prima i ciuffi tamponati, poi il tronco e i rami col rigger",
        "fasi": [
            {
                "titolo": "Ciuffi staccati e tamponati",
                "carta": "umida",
                "colori": ["verde_bosco", "ombra_bruc"],
                "attrezzo": "Tondo medio",
                "testo": "Sulla carta inumidita, con colore denso e poca acqua, si tamponano macchie irregolari di fogliame, più piccole in alto e più larghe in basso, lasciando il chiaro in mezzo.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<g fill="#2b5b3c">'
                    '<ellipse cx="110" cy="22" rx="8" ry="5"/>'
                    '<ellipse cx="96" cy="38" rx="14" ry="6"/><ellipse cx="122" cy="42" rx="12" ry="5"/>'
                    '<ellipse cx="88" cy="58" rx="18" ry="7"/><ellipse cx="126" cy="62" rx="16" ry="7"/>'
                    '<ellipse cx="82" cy="82" rx="22" ry="8"/><ellipse cx="130" cy="85" rx="20" ry="8"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Tronco e rami tirati col rigger",
                "carta": "asciutta",
                "colori": ["ombra_bruc"],
                "attrezzo": "Rigger / liner sottile",
                "testo": "Quando i ciuffi sono asciutti, si appoggia il rigger alla base e si tira il tronco verso l'alto, più largo sotto e sottilissimo in cima, collegando i rami.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<path d="M108,128 L110,16" stroke="#4f3728" stroke-width="3" stroke-linecap="round"/>'
                    '<path d="M110,38 L96,38 M110,42 L122,42 M109,58 L88,58 M110,62 L126,62 M109,82 L82,82 M109,85 L130,85" stroke="#4f3728" stroke-width="1.8"/>'
                    '<g fill="#2b5b3c" opacity="0.9">'
                    '<ellipse cx="110" cy="22" rx="8" ry="5"/>'
                    '<ellipse cx="96" cy="38" rx="14" ry="6"/><ellipse cx="122" cy="42" rx="12" ry="5"/>'
                    '<ellipse cx="88" cy="58" rx="18" ry="7"/><ellipse cx="126" cy="62" rx="16" ry="7"/>'
                    '<ellipse cx="82" cy="82" rx="22" ry="8"/><ellipse cx="130" cy="85" rx="20" ry="8"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Tocchi scuri sotto i ciuffi",
                "carta": "asciutta",
                "colori": ["verde_bosco", "indaco"],
                "attrezzo": "Tondo n. 6",
                "testo": "Si aggiunge un tocco scuro nella parte inferiore di ciascun ciuffo per dare volume e si stende una breve ombra orizzontale alla base del tronco.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<path d="M108,126 L110,16" stroke="#4f3728" stroke-width="3" stroke-linecap="round"/>'
                    '<ellipse cx="116" cy="126" rx="24" ry="4" fill="#1d3528" opacity="0.6"/>'
                    '<g fill="#2b5b3c">'
                    '<ellipse cx="110" cy="22" rx="8" ry="5"/>'
                    '<ellipse cx="96" cy="38" rx="14" ry="6"/><ellipse cx="122" cy="42" rx="12" ry="5"/>'
                    '<ellipse cx="88" cy="58" rx="18" ry="7"/><ellipse cx="126" cy="62" rx="16" ry="7"/>'
                    '<ellipse cx="82" cy="82" rx="22" ry="8"/><ellipse cx="130" cy="85" rx="20" ry="8"/>'
                    '</g>'
                    '<g fill="#14291d">'
                    '<ellipse cx="88" cy="61" rx="15" ry="3.5"/><ellipse cx="126" cy="65" rx="14" ry="3.5"/>'
                    '<ellipse cx="82" cy="86" rx="19" ry="4"/><ellipse cx="130" cy="89" rx="17" ry="4"/>'
                    '</g>'
                ),
            },
        ],
    },
    "A2-M2": {
        "titolo": "Infografica del video: tronco sottile, rami singoli distanziati e aghi fini",
        "fasi": [
            {
                "titolo": "Tronco lungo e sottile",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Liner / tondo n. 0-1",
                "testo": "Su carta asciutta si traccia una linea verticale sottilissima, lasciando scoperto il terzo inferiore del fusto, come nelle conifere alte di bosco.",
                "svg": svg_wrap(
                    '<path d="M110,128 L110,14" stroke="#4f3728" stroke-width="2.4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Linee singole di rami distanziati",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Liner / tondo n. 0-1",
                "testo": "Nella parte alta si tirano linee singole ben separate fra loro, leggermente piegate verso il basso e via via più lunghe scendendo.",
                "svg": svg_wrap(
                    '<path d="M110,128 L110,14" stroke="#4f3728" stroke-width="2.4" stroke-linecap="round"/>'
                    '<g stroke="#2b5b3c" stroke-width="2" stroke-linecap="round">'
                    '<path d="M110,22 L98,27 M110,24 L122,29"/>'
                    '<path d="M110,36 L90,43 M110,39 L128,46"/>'
                    '<path d="M110,54 L84,63 M110,57 L136,66"/>'
                    '<path d="M110,74 L78,84 M110,77 L142,87"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Piccoli aghi sottili sui rami",
                "carta": "asciutta",
                "colori": ["verde_bosco", "verde_chiaro"],
                "attrezzo": "Liner / tondo n. 0-1",
                "testo": "Si aggiungono corti tratti rapidi lungo ciascun ramo per suggerire gli aghi, senza mai chiudere gli spazi chiari tra un palco e l'altro.",
                "svg": svg_wrap(
                    '<path d="M110,128 L110,14" stroke="#4f3728" stroke-width="2.4" stroke-linecap="round"/>'
                    '<g stroke="#2b5b3c" stroke-width="2.2" stroke-linecap="round">'
                    '<path d="M110,22 L98,27 M110,24 L122,29 M110,36 L90,43 M110,39 L128,46 M110,54 L84,63 M110,57 L136,66 M110,74 L78,84 M110,77 L142,87"/>'
                    '</g>'
                    '<g stroke="#4e8742" stroke-width="1.6" stroke-linecap="round">'
                    '<path d="M96,41 L92,47 M102,39 L99,45 M118,42 L121,48 M124,44 L127,50"/>'
                    '<path d="M90,61 L86,68 M98,58 L95,65 M120,60 L124,67 M128,63 L132,70"/>'
                    '<path d="M84,82 L80,90 M94,79 L90,87 M124,81 L128,89 M134,84 L138,92"/>'
                    '</g>'
                ),
            },
        ],
    },
    "A2-M3": {
        "titolo": "Infografica del video: dalla punta alla base a tocchi saltellati sui due lati",
        "fasi": [
            {
                "titolo": "Punta sottile e primi tocchi",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Piatto 3/8\" o tondo",
                "testo": "Si parte dalla cima con un tocco verticale minimo e si inizia la discesa appoggiando l'angolo del pennello con piccoli tocchi staccati.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<path d="M110,14 L110,26 M106,28 L114,30 M100,38 L108,40 M112,42 L122,44" stroke="#2b5b3c" stroke-width="3.5" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Tocchi saltellati da un lato all'altro",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Piatto 3/8\" o tondo",
                "testo": "Si appoggia il pennello e lo si spinge appena, a scatti irregolari, alternando sinistra e destra; si allargano i palchi e si lascia passare il cielo.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<g stroke="#2b5b3c" stroke-width="4.5" stroke-linecap="round">'
                    '<path d="M110,14 L110,24 M102,30 L118,32 M94,44 L110,46 M108,50 L128,53"/>'
                    '<path d="M84,64 L106,68 M112,70 L136,74 M76,86 L104,90 M110,92 L144,96 M70,108 L148,112"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Ombra scura sotto i palchi",
                "carta": "umida",
                "colori": ["oltremare", "ombra_bruc"],
                "attrezzo": "Piatto 3/8\" o tondo",
                "testo": "Mentre il verde è ancora fresco, si toccano la parte inferiore dei palchi e il lato in ombra con blu oltremare e terra d'ombra bruciata.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<line x1="110" y1="24" x2="110" y2="126" stroke="#4f3728" stroke-width="2.5"/>'
                    '<g stroke="#2b5b3c" stroke-width="4.5" stroke-linecap="round">'
                    '<path d="M110,14 L110,24 M102,30 L118,32 M94,44 L110,46 M108,50 L128,53 M84,64 L106,68 M112,70 L136,74 M76,86 L104,90 M110,92 L144,96 M70,108 L148,112"/>'
                    '</g>'
                    '<g stroke="#182828" stroke-width="3.5" stroke-linecap="round">'
                    '<path d="M112,53 L128,56 M112,73 L136,77 M110,95 L144,99 M108,112 L148,115"/>'
                    '</g>'
                ),
            },
        ],
    },

    # =========================================================================
    # A3 - CHIOME TONDE D'AUTUNNO (5 modalità)
    # =========================================================================
    "A3-M1": {
        "titolo": "Infografica del video: pancia del pennello mossa in tondo, dal centro al bordo",
        "fasi": [
            {
                "titolo": "Pancia del pennello al centro",
                "carta": "asciutta",
                "colori": ["giallo_limone", "siena_nat"],
                "attrezzo": "Tondo grande n. 10",
                "testo": "Si appoggia la pancia del pennello grande, ben carico, al centro del lobo della chioma, evitando di stampare tocchi rigidi e ripetuti.",
                "svg": svg_wrap(
                    '<circle cx="110" cy="68" r="24" fill="#e59a28" opacity="0.88"/>'
                    '<path d="M98,68 A12,12 0 1,1 122,68" fill="none" stroke="#9e4726" stroke-width="2" stroke-dasharray="3,2"/>'
                ),
            },
            {
                "titolo": "Movimento in tondo verso il bordo",
                "carta": "asciutta",
                "colori": ["siena_nat", "siena_bruc"],
                "attrezzo": "Tondo grande n. 10",
                "testo": "Si muove il pennello in tondo verso l'esterno: scaricandosi sulla carta, lascia da sé il profilo frastagliato delle foglie e qualche vuoto.",
                "svg": svg_wrap(
                    '<circle cx="84" cy="66" r="34" fill="#e59a28" opacity="0.85"/>'
                    '<circle cx="134" cy="64" r="36" fill="#d98224" opacity="0.85"/>'
                    '<circle cx="106" cy="58" r="5" fill="#fcfaf4"/>'
                    '<circle cx="122" cy="74" r="4" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Ombra bruna nei lobi bassi",
                "carta": "umida",
                "colori": ["siena_bruc", "oltremare"],
                "attrezzo": "Tondo medio n. 6",
                "testo": "Sulla chioma ancora umida si appoggia sotto i lobi e sul lato in ombra un bruno scuro (terra di Siena bruciata + blu oltremare).",
                "svg": svg_wrap(
                    '<circle cx="84" cy="64" r="34" fill="#e59a28" opacity="0.85"/>'
                    '<circle cx="134" cy="62" r="36" fill="#d98224" opacity="0.85"/>'
                    '<path d="M54,78 Q84,104 110,88 Q138,104 166,78 L162,92 Q110,114 58,92 Z" fill="#5c2c1d" opacity="0.9"/>'
                    '<line x1="110" y1="94" x2="110" y2="126" stroke="#3b2316" stroke-width="4"/>'
                ),
            },
        ],
    },
    "A3-M2": {
        "titolo": "Infografica del video: chioma bagnato su bagnato, con gocce d'arancio e di rosso nel giallo",
        "fasi": [
            {
                "titolo": "Base gialla carica d'acqua",
                "carta": "asciutta",
                "colori": ["giallo_limone"],
                "attrezzo": "Piatto medio o tondo",
                "testo": "Su carta asciutta si stende una forma tondeggiante e mossa di giallo o arancio molto chiaro, ben carica d'acqua, lasciando qualche piccolo varco bianco.",
                "svg": svg_wrap(
                    '<circle cx="86" cy="64" r="34" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="132" cy="62" r="36" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="108" cy="80" r="30" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="104" cy="56" r="5" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Gocce di arancio e Siena a fresco",
                "carta": "bagnata",
                "colori": ["cadmio_arancio", "siena_bruc"],
                "attrezzo": "Tondo medio",
                "testo": "Subito, nella base ancora lucida d'acqua, si lasciano cadere gocce di arancio e terra di Siena bruciata al centro, e le si lascia espandere da sé.",
                "svg": svg_wrap(
                    '<circle cx="86" cy="64" r="34" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="132" cy="62" r="36" fill="#ebd834" opacity="0.8"/>'
                    '<ellipse cx="88" cy="70" rx="22" ry="16" fill="#e56b28" opacity="0.85"/>'
                    '<ellipse cx="132" cy="68" rx="24" ry="18" fill="#c4512d" opacity="0.85"/>'
                    '<circle cx="104" cy="56" r="5" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Rosso scuro sotto e tronco seppia",
                "carta": "umida",
                "colori": ["cremisi", "seppia"],
                "attrezzo": "Tondo fine n. 2",
                "testo": "Si picchietta il rosso scuro lungo il bordo basso dei lobi e sotto si tirano il tronco e i rami sottili in seppia.",
                "svg": svg_wrap(
                    '<circle cx="86" cy="62" r="34" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="132" cy="60" r="36" fill="#ebd834" opacity="0.8"/>'
                    '<ellipse cx="88" cy="68" rx="22" ry="16" fill="#e56b28" opacity="0.85"/>'
                    '<ellipse cx="132" cy="66" rx="24" ry="18" fill="#c4512d" opacity="0.85"/>'
                    '<path d="M56,78 Q86,104 110,88 Q136,104 164,78 L160,92 Q110,112 60,92 Z" fill="#6e2026" opacity="0.92"/>'
                    '<path d="M108,128 L108,92 M108,104 L94,88 M108,100 L124,86" stroke="#2e241f" stroke-width="3" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A3-M3": {
        "titolo": "Infografica del video: chioma tamponata con la spugna naturale e scuri a umido",
        "fasi": [
            {
                "titolo": "Arancio tamponato con la spugna",
                "carta": "asciutta",
                "colori": ["cadmio_arancio"],
                "attrezzo": "Spugna naturale marina",
                "testo": "Si inumidisce e si strizza la spugna naturale, la si intinge nell'arancio vivo e si tampona sulla carta per creare una trama ariosa di fogliame.",
                "svg": svg_wrap(
                    '<g fill="#e58728" opacity="0.85">'
                    '<circle cx="78" cy="54" r="14"/><circle cx="98" cy="44" r="16"/><circle cx="124" cy="48" r="15"/>'
                    '<circle cx="68" cy="72" r="15"/><circle cx="94" cy="68" r="18"/><circle cx="122" cy="68" r="17"/><circle cx="144" cy="64" r="14"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Primo rosso sul lato in ombra",
                "carta": "bagnata",
                "colori": ["cremisi"],
                "attrezzo": "Spugna naturale marina",
                "testo": "Mentre l'arancio è ancora bagnato, si tampona con la spugna un rosso più profondo nella parte bassa e sul lato destro della chioma.",
                "svg": svg_wrap(
                    '<g fill="#e58728" opacity="0.85">'
                    '<circle cx="78" cy="54" r="14"/><circle cx="98" cy="44" r="16"/><circle cx="124" cy="48" r="15"/>'
                    '<circle cx="68" cy="72" r="15"/><circle cx="94" cy="68" r="18"/><circle cx="122" cy="68" r="17"/><circle cx="144" cy="64" r="14"/>'
                    '</g>'
                    '<g fill="#9e2a2b" opacity="0.82">'
                    '<circle cx="104" cy="74" r="15"/><circle cx="128" cy="72" r="16"/><circle cx="146" cy="68" r="12"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Scuri nella chioma bagnata e rami col rigger",
                "carta": "bagnata",
                "colori": ["ombra_bruc", "cremisi"],
                "attrezzo": "Tondo n. 12 + rigger n. 3",
                "testo": "Col tondo n. 12 si lasciano cadere nella chioma ancora bagnata toni bruno-rossi molto scuri e se ne toccano appena i bordi di punta. Col rigger n. 3 si tirano poi i rami.",
                "svg": svg_wrap(
                    '<g fill="#e58728" opacity="0.85">'
                    '<circle cx="78" cy="54" r="14"/><circle cx="98" cy="44" r="16"/><circle cx="124" cy="48" r="15"/>'
                    '<circle cx="68" cy="72" r="15"/><circle cx="94" cy="68" r="18"/><circle cx="122" cy="68" r="17"/><circle cx="144" cy="64" r="14"/>'
                    '</g>'
                    '<g fill="#9e2a2b" opacity="0.85">'
                    '<circle cx="104" cy="74" r="15"/><circle cx="128" cy="72" r="16"/>'
                    '</g>'
                    '<g fill="#3d1814" opacity="0.92">'
                    '<ellipse cx="86" cy="84" rx="16" ry="8"/><ellipse cx="124" cy="82" rx="22" ry="9"/>'
                    '</g>'
                    '<path d="M106,126 L106,86 M106,102 L90,86 M106,98 L124,84" stroke="#3d1814" stroke-width="2.6" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A3-M4": {
        "titolo": "Infografica del video: chiome calde d'autunno e verdi scuri accostati a fresco",
        "fasi": [
            {
                "titolo": "Masse calde in terra di Siena",
                "carta": "bagnata",
                "colori": ["siena_nat", "oltremare"],
                "attrezzo": "Tondo medio",
                "testo": "Si bagna con acqua pulita la sagoma delle chiome, poi vi si lasciano cadere la terra di Siena naturale e una punta di blu oltremare, tenendo la luce a sinistra.",
                "svg": svg_wrap(
                    '<circle cx="68" cy="68" r="32" fill="#d48c2a" opacity="0.85"/>'
                    '<circle cx="104" cy="64" r="34" fill="#c97a26" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Verde scuro a fianco sull'umido",
                "carta": "umida",
                "colori": ["verde_bosco", "oltremare"],
                "attrezzo": "Tondo medio",
                "testo": "Mentre il bordo destro delle chiome calde è ancora umido, si appoggia a fianco il verde scuro (Siena + più oltremare) perché si fonda sul confine.",
                "svg": svg_wrap(
                    '<circle cx="68" cy="68" r="32" fill="#d48c2a" opacity="0.85"/>'
                    '<circle cx="104" cy="64" r="34" fill="#c97a26" opacity="0.85"/>'
                    '<circle cx="146" cy="66" r="34" fill="#2b5b3c" opacity="0.9"/>'
                    '<ellipse cx="124" cy="66" rx="12" ry="26" fill="#4d5e28" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Rosso inglese e bordi sgranati",
                "carta": "umida",
                "colori": ["rosso_inglese", "verde_bosco"],
                "attrezzo": "Pennello sagomato / tondo",
                "testo": "Si aggiunge qualche tocco caldo di rosso inglese nel fogliame e si sgrana il contorno esterno, per mantenere i bordi morbidi e frastagliati.",
                "svg": svg_wrap(
                    '<circle cx="68" cy="68" r="32" fill="#d48c2a" opacity="0.85"/>'
                    '<circle cx="104" cy="64" r="34" fill="#c97a26" opacity="0.85"/>'
                    '<ellipse cx="92" cy="76" rx="18" ry="12" fill="#a8422b" opacity="0.85"/>'
                    '<circle cx="146" cy="66" r="34" fill="#2b5b3c" opacity="0.92"/>'
                    '<path d="M50,96 L172,96" stroke="#1e3824" stroke-width="5" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A3-M5": {
        "titolo": "Infografica del video: rami scalfiti nel colore umido con l'angolo della tessera",
        "fasi": [
            {
                "titolo": "Stesura del colore e tavola in piano",
                "carta": "umida",
                "colori": ["siena_bruc", "indaco", "seppia"],
                "attrezzo": "Pennellessa piatta (mottler)",
                "testo": "Si stendono i toni caldi e scuri del fogliame. Appena il colore è sceso dove serve, si rimette la tavola in piano sul tavolo perché non coli più.",
                "svg": svg_wrap(
                    '<ellipse cx="110" cy="68" rx="68" ry="38" fill="#8c4a27" opacity="0.85"/>'
                    '<ellipse cx="122" cy="78" rx="52" ry="26" fill="#3b2d26" opacity="0.8"/>'
                ),
            },
            {
                "titolo": "Angolo della tessera nel colore umido",
                "carta": "umida",
                "colori": ["seppia"],
                "attrezzo": "Tessera di plastica",
                "testo": "Si impugna una tessera rigida di plastica e se ne trascina lo spigolo con piccoli scatti rapidi dentro il colore umido, per ricavare i rami.",
                "svg": svg_wrap(
                    '<ellipse cx="110" cy="68" rx="68" ry="38" fill="#8c4a27" opacity="0.85"/>'
                    '<ellipse cx="122" cy="78" rx="52" ry="26" fill="#3b2d26" opacity="0.8"/>'
                    '<polygon points="148,18 192,28 182,62 138,52" fill="#7ec8e3" stroke="#2b4c8c" stroke-width="1.5"/>'
                    '<path d="M84,96 L76,58 M112,98 L138,52" stroke="#fcfaf4" stroke-width="2" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Solco scuro o filo chiaro",
                "carta": "umida",
                "colori": ["siena_bruc"],
                "attrezzo": "Tessera di plastica",
                "testo": "Sul molto bagnato il solco raccoglie il pigmento e diventa scuro. Se si attende che la carta perda il lucido, il colore si sposta e si aprono fili chiari.",
                "svg": svg_wrap(
                    '<ellipse cx="110" cy="68" rx="68" ry="38" fill="#8c4a27" opacity="0.85"/>'
                    '<ellipse cx="122" cy="78" rx="52" ry="26" fill="#3b2d26" opacity="0.8"/>'
                    '<path d="M78,96 L68,54 M76,78 L88,60" stroke="#1c1410" stroke-width="2.2" stroke-linecap="round"/>'
                    '<path d="M126,96 L118,54 M124,76 L142,58 M150,92 L162,62" stroke="#fbeec8" stroke-width="2.2" stroke-linecap="round"/>'
                ),
            },
        ],
    },

    # =========================================================================
    # A4 - SIEPI E CESPUGLI NEL PAESAGGIO (5 modalità)
    # =========================================================================
    "A4-M1": {
        "titolo": "Infografica del video: siepe autunnale a tocchi caldi con rosso inglese e base scura",
        "fasi": [
            {
                "titolo": "Siepe in giallo limone e Siena",
                "carta": "asciutta",
                "colori": ["giallo_limone", "siena_nat"],
                "attrezzo": "Tondo n. 6",
                "testo": "Con giallo limone e terra di Siena naturale (più carichi di quelli del prato) si stende a piccoli tocchi la fascia bassa della siepe.",
                "svg": svg_wrap(
                    '<rect x="24" y="52" width="172" height="36" rx="10" fill="#d98a26" opacity="0.88"/>'
                ),
            },
            {
                "titolo": "Tocchi di rosso inglese a fresco",
                "carta": "umida",
                "colori": ["rosso_inglese"],
                "attrezzo": "Tondo n. 6",
                "testo": "Mentre la striscia della siepe è ancora umida, la si tocca in alcuni punti con rosso inglese, per variare il tono e scaldare il fogliame.",
                "svg": svg_wrap(
                    '<rect x="24" y="52" width="172" height="36" rx="10" fill="#d98a26" opacity="0.88"/>'
                    '<ellipse cx="64" cy="68" rx="22" ry="11" fill="#b5482a" opacity="0.85"/>'
                    '<ellipse cx="128" cy="70" rx="26" ry="12" fill="#b5482a" opacity="0.85"/>'
                    '<ellipse cx="172" cy="66" rx="16" ry="10" fill="#b5482a" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Ombra scura lungo la base",
                "carta": "umida",
                "colori": ["ombra_bruc", "oltremare"],
                "attrezzo": "Tondo n. 6",
                "testo": "Si appoggia lungo il piede della siepe una miscela scura di terra d'ombra bruciata e blu oltremare, per ancorarla al campo, e la si tampona con un pennello a setole corte e rigide.",
                "svg": svg_wrap(
                    '<rect x="16" y="86" width="188" height="36" rx="4" fill="#e8e2b8" opacity="0.6"/>'
                    '<rect x="24" y="52" width="172" height="36" rx="10" fill="#d98a26" opacity="0.88"/>'
                    '<ellipse cx="64" cy="68" rx="22" ry="11" fill="#b5482a" opacity="0.85"/>'
                    '<ellipse cx="128" cy="70" rx="26" ry="12" fill="#b5482a" opacity="0.85"/>'
                    '<path d="M26,84 Q70,90 110,85 Q155,90 194,84" stroke="#2e241f" stroke-width="7" fill="none" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A4-M2": {
        "titolo": "Infografica del video: fascia scura alla base e scioglimento a tratti verso il prato",
        "fasi": [
            {
                "titolo": "Corpo chiaro e toni medi",
                "carta": "asciutta",
                "colori": ["verde_oliva", "verde_chiaro"],
                "attrezzo": "Tondo piccolo (di lato)",
                "testo": "Si dipinge la sagoma della siepe con tocchi mossi, usando il lato del pennello, e si passa dal chiaro in alto al tono medio al centro.",
                "svg": svg_wrap(
                    '<rect x="26" y="46" width="168" height="40" rx="10" fill="#7cb356" opacity="0.82"/>'
                    '<rect x="28" y="60" width="164" height="24" rx="6" fill="#5c8a3c" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Fascia scura alla base",
                "carta": "umida",
                "colori": ["verde_bosco", "ombra_bruc"],
                "attrezzo": "Tondo piccolo",
                "testo": "Si appoggia un tono denso e scuro lungo la base della siepe per creare la rientranza d'ombra dove i rami toccano il terreno.",
                "svg": svg_wrap(
                    '<rect x="26" y="46" width="168" height="40" rx="10" fill="#6b9e48" opacity="0.85"/>'
                    '<rect x="28" y="76" width="164" height="10" rx="4" fill="#1e3d28"/>'
                ),
            },
            {
                "titolo": "Scioglimento a tratti col piatto umido",
                "carta": "umida",
                "colori": ["acqua"],
                "attrezzo": "Piatto medio-piccolo umido",
                "testo": "Subito, mentre lo scuro è umido, si passa un pennello piatto pulito e umido in 2-3 punti per scioglierlo dolcemente verso il prato davanti.",
                "svg": svg_wrap(
                    '<rect x="16" y="84" width="188" height="40" rx="4" fill="#dce8c8" opacity="0.65"/>'
                    '<rect x="26" y="46" width="168" height="40" rx="10" fill="#6b9e48" opacity="0.85"/>'
                    '<rect x="28" y="76" width="164" height="10" rx="4" fill="#1e3d28"/>'
                    '<ellipse cx="62" cy="90" rx="18" ry="7" fill="#1e3d28" opacity="0.45"/>'
                    '<ellipse cx="144" cy="90" rx="22" ry="7" fill="#1e3d28" opacity="0.45"/>'
                ),
            },
        ],
    },
    "A4-M3": {
        "titolo": "Infografica del video: cespuglio a cupola costruito per strati, dal chiaro allo scuro",
        "fasi": [
            {
                "titolo": "Prima macchia chiara al sole",
                "carta": "asciutta",
                "colori": ["giallo_limone", "oltremare"],
                "attrezzo": "Tondo n. 4-6",
                "testo": "Si imposta la forma raccolta a cupola partendo dal verde-giallo più chiaro, nella parte alta illuminata dal sole.",
                "svg": svg_wrap(
                    '<path d="M52,104 Q110,20 168,104 Z" fill="#a8c948" opacity="0.88"/>'
                ),
            },
            {
                "titolo": "Verdi medi per il volume",
                "carta": "umida",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo n. 4-6",
                "testo": "Si aggiunge nella zona centrale e bassa un verde medio più ricco di blu oltremare, lasciando scoperti i bordi superiori chiari.",
                "svg": svg_wrap(
                    '<path d="M52,104 Q110,20 168,104 Z" fill="#a8c948" opacity="0.88"/>'
                    '<path d="M56,104 Q110,44 164,104 Z" fill="#4e8742" opacity="0.9"/>'
                ),
            },
            {
                "titolo": "Ombre profonde spente col rosso",
                "carta": "umida",
                "colori": ["verde_bosco", "cremisi"],
                "attrezzo": "Tondo fine n. 2",
                "testo": "Si chiudono la base e gli incavi interni con un verde scurissimo spento con una punta di rosso, e si accennano piccoli tocchi sul contorno.",
                "svg": svg_wrap(
                    '<path d="M52,104 Q110,20 168,104 Z" fill="#a8c948" opacity="0.88"/>'
                    '<path d="M56,104 Q110,44 164,104 Z" fill="#4e8742" opacity="0.9"/>'
                    '<path d="M60,104 Q110,72 160,104 Z" fill="#1b3826"/>'
                    '<ellipse cx="96" cy="78" rx="14" ry="6" fill="#1b3826"/>'
                    '<ellipse cx="128" cy="82" rx="16" ry="7" fill="#1b3826"/>'
                ),
            },
        ],
    },
    "A4-M4": {
        "titolo": "Infografica del video: chiome chiare staccate con lo scuro dipinto dietro in negativo",
        "fasi": [
            {
                "titolo": "Chiome chiare dipinte prima",
                "carta": "asciutta",
                "colori": ["giallo_limone", "cadmio_arancio"],
                "attrezzo": "Calligrafico / tondo medio",
                "testo": "Si stendono liberamente le masse chiare (giallo limone, ocra e arancio) dove andranno i cespugli al sole, e si lasciano asciugare del tutto.",
                "svg": svg_wrap(
                    '<circle cx="78" cy="76" r="28" fill="#ebd834" opacity="0.88"/>'
                    '<circle cx="132" cy="72" r="32" fill="#e59a28" opacity="0.88"/>'
                ),
            },
            {
                "titolo": "Contorno in negativo col fondo scuro",
                "carta": "asciutta",
                "colori": ["oltremare", "verde_bosco", "indaco"],
                "attrezzo": "Calligrafico a punta tonda",
                "testo": "Con un tono scuro si dipinge lo sfondo, girando con la punta attorno al profilo frastagliato delle chiome chiare già asciutte.",
                "svg": svg_wrap(
                    '<rect x="18" y="18" width="95" height="90" rx="6" fill="#1f3b34"/>'
                    '<circle cx="78" cy="76" r="28" fill="#ebd834"/>'
                    '<circle cx="132" cy="72" r="32" fill="#e59a28"/>'
                ),
            },
            {
                "titolo": "Stacco completo e rami interni",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Tondo fine",
                "testo": "Si completa lo scuro tutto intorno, finché il cespuglio chiaro si stacca in avanti per contrasto, e si aggiungono pochi rametti sottili alla base.",
                "svg": svg_wrap(
                    '<rect x="18" y="18" width="184" height="92" rx="6" fill="#1f3b34"/>'
                    '<circle cx="78" cy="76" r="28" fill="#ebd834"/>'
                    '<circle cx="132" cy="72" r="32" fill="#e59a28"/>'
                    '<path d="M78,118 L78,86 M78,96 L68,84 M132,118 L132,82 M132,94 L144,80" stroke="#3b2d26" stroke-width="2.2" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A4-M5": {
        "titolo": "Infografica del video: passata leggera sul prato e striscia d'ombra fredda alla base",
        "fasi": [
            {
                "titolo": "Passata leggera sul prato",
                "carta": "asciutta",
                "colori": ["giallo_limone", "prussia"],
                "attrezzo": "Tondo grande",
                "testo": "Si imposta il prato in primo piano, sotto le siepi, con un velo leggerissimo e pulito, senza dettagli che attirino lo sguardo.",
                "svg": svg_wrap(
                    '<rect x="24" y="34" width="172" height="36" rx="8" fill="#6b8238"/>'
                    '<rect x="14" y="70" width="192" height="54" rx="4" fill="#d8e6b8" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Striscia d'ombra fredda alla base",
                "carta": "umida",
                "colori": ["oltremare", "lilla"],
                "attrezzo": "Tondo medio",
                "testo": "Mentre il prato è ancora umido, si appoggia subito sotto gli alberi e le siepi una striscia orizzontale di blu oltremare o grigio-lilla.",
                "svg": svg_wrap(
                    '<rect x="24" y="34" width="172" height="36" rx="8" fill="#6b8238"/>'
                    '<rect x="14" y="70" width="192" height="54" rx="4" fill="#d8e6b8" opacity="0.75"/>'
                    '<rect x="20" y="70" width="180" height="12" rx="4" fill="#5b6d99" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Bordo morbido e sentiero sobrio",
                "carta": "umida",
                "colori": ["ombra_bruc"],
                "attrezzo": "Tondo medio",
                "testo": "L'ombra fredda si lascia ammorbidire da sé nel prato umido; si aggiunge solo una traccia leggera per il terreno o il sentiero.",
                "svg": svg_wrap(
                    '<rect x="24" y="34" width="172" height="36" rx="8" fill="#6b8238"/>'
                    '<rect x="14" y="70" width="192" height="54" rx="4" fill="#d8e6b8" opacity="0.75"/>'
                    '<ellipse cx="110" cy="78" rx="88" ry="9" fill="#5b6d99" opacity="0.6"/>'
                    '<path d="M90,84 Q110,104 74,124 L126,124 Q134,104 114,84 Z" fill="#b89872" opacity="0.55"/>'
                ),
            },
        ],
    },

    # =========================================================================
    # A5 - ALBERI INVERNALI CON FUSTI CHIARI E BRINA (5 modalità)
    # =========================================================================
    "A5-M1": {
        "titolo": "Infografica dei video: fusti sottili col mascherante, rimozione e ombra su un lato",
        "fasi": [
            {
                "titolo": "Fusti tracciati col tiralinee",
                "carta": "asciutta",
                "colori": ["mascherante"],
                "attrezzo": "Tiralinee",
                "testo": "Sulla carta asciutta si intinge il tiralinee nel liquido mascherante e si tracciano fusti sottilissimi e biforcati a Y; si attende che asciughi del tutto.",
                "svg": svg_wrap(
                    '<path d="M76,128 L80,22 M78,68 L96,34 M142,128 L138,26 M140,72 L122,40" stroke="#5bc0de" stroke-width="3.2" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Rimozione del mascherante a secco",
                "carta": "asciutta",
                "colori": ["lilla", "oltremare"],
                "attrezzo": "Gomma crêpe",
                "testo": "Solo quando le velature di sfondo sono completamente asciutte si strofina la gomma crêpe, per scoprire i fusti bianchi e netti.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="112" rx="6" fill="#6c6486" opacity="0.75"/>'
                    '<path d="M76,128 L80,22 M78,68 L96,34" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                    '<path d="M142,128 L138,26 M140,72 L122,40" stroke="#5bc0de" stroke-width="3.5" stroke-linecap="round"/>'
                    '<rect x="124" y="56" width="32" height="20" rx="4" fill="#e6cfa3" stroke="#8c734b" stroke-width="1.5"/>'
                ),
            },
            {
                "titolo": "Ombra su un solo lato del fusto",
                "carta": "bagnata",
                "colori": ["lilla", "cobalto"],
                "attrezzo": "Tondo n. 12 scarico d'acqua",
                "testo": "Si stende acqua pulita sul fusto bianco, si scarica il pennello su un fazzoletto e si passa un filetto grigio-azzurro lungo un solo bordo, sfumandolo verso il centro per dare al fusto forma cilindrica.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="112" rx="6" fill="#6c6486" opacity="0.75"/>'
                    '<path d="M76,128 L80,22 M78,68 L96,34 M142,128 L138,26 M140,72 L122,40" stroke="#fcfaf4" stroke-width="4.5" stroke-linecap="round"/>'
                    '<path d="M78,128 L82,22 M144,128 L140,26" stroke="#3a4466" stroke-width="1.6" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A5-M2": {
        "titolo": "Infografica del video: tronchi dritti protetti col nastro e veli fusi sul bagnato",
        "fasi": [
            {
                "titolo": "Strisce sottili di nastro di carta",
                "carta": "asciutta",
                "colori": ["nastro"],
                "attrezzo": "Nastro di carta strappato",
                "testo": "Si tagliano o si strappano strisce sottili di nastro di carta e si fanno aderire bene sulla carta asciutta, per riservare i tronchi dritti.",
                "svg": svg_wrap(
                    '<rect x="64" y="16" width="10" height="110" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                    '<rect x="106" y="14" width="12" height="112" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                    '<rect x="150" y="20" width="9" height="106" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                ),
            },
            {
                "titolo": "Veli gialli e oro sul foglio bagnato",
                "carta": "bagnata",
                "colori": ["giallo_limone", "oro_chinacridone", "verde_oliva"],
                "attrezzo": "Tondo grande n. 14",
                "testo": "Si bagna il foglio passando sopra il nastro e si stendono bagnato su bagnato un velo giallo, macchie di oro chinacridone e tocchi di verde vescica.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="64" rx="6" fill="#ebd834" opacity="0.5"/>'
                    '<ellipse cx="70" cy="48" rx="42" ry="22" fill="#e59a28" opacity="0.55"/>'
                    '<ellipse cx="150" cy="46" rx="44" ry="22" fill="#7cb356" opacity="0.5"/>'
                    '<rect x="64" y="16" width="10" height="110" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                    '<rect x="106" y="14" width="12" height="112" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                    '<rect x="150" y="20" width="9" height="106" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                ),
            },
            {
                "titolo": "Blu-viola in basso e nastro rimosso",
                "carta": "bagnata",
                "colori": ["lilla", "turchese_cob", "siena_bruc"],
                "attrezzo": "Tondo n. 14 + tondo n. 2",
                "testo": "Si inseriscono i toni blu-viola, turchesi e ruggine in basso, lasciandoli fondere sopra i tronchi protetti; a carta asciutta si solleva il nastro.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="58" rx="6" fill="#e59a28" opacity="0.45"/>'
                    '<rect x="14" y="60" width="192" height="66" rx="6" fill="#7c729c" opacity="0.65"/>'
                    '<rect x="64" y="16" width="10" height="110" fill="#fcfaf4"/>'
                    '<rect x="106" y="14" width="12" height="112" fill="#fcfaf4"/>'
                    '<rect x="150" y="20" width="9" height="106" fill="#fcfaf4"/>'
                ),
            },
        ],
    },
    "A5-M3": {
        "titolo": "Infografica del video: la trama della brina col sale fino sparso sul colore umido",
        "fasi": [
            {
                "titolo": "Velo freddo invernale",
                "carta": "bagnata",
                "colori": ["indaco", "ombra_bruc"],
                "attrezzo": "Pennellessa piatta (hake)",
                "testo": "Si stende un velo morbido con grigio di Payne, indaco e un tocco di terra d'ombra bruciata, per l'atmosfera invernale delle chiome.",
                "svg": svg_wrap(
                    '<rect x="16" y="16" width="188" height="108" rx="8" fill="#5c687c" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Sale appena sparisce il lucido",
                "carta": "umida",
                "colori": ["sale"],
                "attrezzo": "Pizzico di sale da cucina",
                "testo": "Il sale non va gettato sull'acqua lucida (si scioglierebbe): si attende che la carta diventi opaca e umida, poi si sparge un pizzico di sale fino.",
                "svg": svg_wrap(
                    '<rect x="16" y="16" width="188" height="108" rx="8" fill="#5c687c" opacity="0.75"/>'
                    '<g fill="#ffffff">'
                    '<circle cx="62" cy="54" r="2.2"/><circle cx="88" cy="48" r="2"/><circle cx="116" cy="60" r="2.4"/>'
                    '<circle cx="74" cy="78" r="2.2"/><circle cx="104" cy="82" r="2"/><circle cx="138" cy="72" r="2.2"/>'
                    '<circle cx="154" cy="56" r="1.8"/><circle cx="128" cy="92" r="2"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Cristalli di brina e spazzolatura",
                "carta": "asciutta",
                "colori": ["indaco"],
                "attrezzo": "Mano asciutta",
                "testo": "Si lascia asciugare senza toccare finché il sale apre i cristalli chiari; solo a foglio completamente asciutto si spazzolano via i grani.",
                "svg": svg_wrap(
                    '<rect x="16" y="16" width="188" height="108" rx="8" fill="#5c687c" opacity="0.75"/>'
                    '<g fill="#eef3f8" opacity="0.9">'
                    '<circle cx="62" cy="54" r="7"/><circle cx="88" cy="48" r="6"/><circle cx="116" cy="60" r="8"/>'
                    '<circle cx="74" cy="78" r="7"/><circle cx="104" cy="82" r="6.5"/><circle cx="138" cy="72" r="7.5"/>'
                    '<circle cx="154" cy="56" r="5.5"/><circle cx="128" cy="92" r="6.5"/>'
                    '</g>'
                ),
            },
        ],
    },
    "A5-M4": {
        "titolo": "Infografica del video: massa scura dipinta in negativo dietro i rami e sfumata con acqua",
        "fasi": [
            {
                "titolo": "Scuro in negativo fra i rami",
                "carta": "asciutta",
                "colori": ["verde_bosco", "oltremare", "indaco"],
                "attrezzo": "Tondo fine a punta",
                "testo": "Con una miscela scura e fredda si dipingono gli spazi vuoti attorno ai fusti e ai rami chiari, per farli emergere per contrasto.",
                "svg": svg_wrap(
                    '<path d="M56,118 Q62,64 110,64 Q158,64 164,118 Z" fill="#1d3d3d"/>'
                    '<path d="M88,124 L90,34 M89,76 L72,50 M130,124 L128,38 M129,78 L146,52" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Bordo toccato con acqua pulita",
                "carta": "umida",
                "colori": ["acqua"],
                "attrezzo": "Tondo pulito con acqua",
                "testo": "Subito, prima che il contorno esterno della massa scura si asciughi, lo si sfiora con un pennello carico di sola acqua pulita.",
                "svg": svg_wrap(
                    '<path d="M48,72 Q110,42 172,72" stroke="#85bce8" stroke-width="8" fill="none" stroke-linecap="round" opacity="0.65"/>'
                    '<path d="M56,118 Q62,64 110,64 Q158,64 164,118 Z" fill="#1d3d3d"/>'
                    '<path d="M88,124 L90,34 M89,76 L72,50 M130,124 L128,38 M129,78 L146,52" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Bordo alto sfumato e interno netto",
                "carta": "umida",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo fine n. 2-4",
                "testo": "Il colore si espande nell'acqua e crea un passaggio sfumato verso l'alto, mentre il bordo contro i fusti bianchi resta netto.",
                "svg": svg_wrap(
                    '<path d="M42,118 Q54,40 110,44 Q166,40 178,118 Z" fill="#5c8a7e" opacity="0.45"/>'
                    '<path d="M56,118 Q62,68 110,68 Q158,68 164,118 Z" fill="#1d3d3d" opacity="0.9"/>'
                    '<path d="M88,124 L90,34 M89,76 L72,50 M130,124 L128,38 M129,78 L146,52" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A5-M5": {
        "titolo": "Infografica del video: trama leggera di rametti spogli col pennello a ventaglio",
        "fasi": [
            {
                "titolo": "Ventaglio quasi asciutto a pettine",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Pennello a ventaglio piccolo",
                "testo": "Si intinge il piccolo pennello a ventaglio nel seppia diluito e si scarica l'acqua, perché le setole restino ben separate a pettine.",
                "svg": svg_wrap(
                    '<path d="M110,96 L82,58 M110,96 L94,52 M110,96 L110,48 M110,96 L126,52 M110,96 L138,58" stroke="#2e241f" stroke-width="2" stroke-linecap="round"/>'
                    '<rect x="105" y="96" width="10" height="26" rx="2" fill="#8c6239"/>'
                ),
            },
            {
                "titolo": "Archi leggeri per i rametti fini",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Pennello a ventaglio piccolo",
                "testo": "Si sfiora la carta asciutta con movimenti rapidi ad arco, per creare in pochi secondi la trama fine dei rametti periferici.",
                "svg": svg_wrap(
                    '<g stroke="#2e241f" stroke-width="1.2" stroke-dasharray="3,2" fill="none">'
                    '<path d="M48,68 Q78,34 112,52"/><path d="M54,74 Q82,42 116,58"/>'
                    '<path d="M98,56 Q132,30 168,62"/><path d="M104,62 Q136,38 172,68"/>'
                    '<path d="M68,48 Q108,22 148,46"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Tronco e rami collegati col rigger",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Rigger sottile",
                "testo": "Con il rigger si tirano dal basso il tronco e i rami principali, fino a raccordarli dentro la trama leggera lasciata dal ventaglio.",
                "svg": svg_wrap(
                    '<g stroke="#2e241f" stroke-width="1.2" stroke-dasharray="3,2" fill="none">'
                    '<path d="M48,68 Q78,34 112,52"/><path d="M54,74 Q82,42 116,58"/>'
                    '<path d="M98,56 Q132,30 168,62"/><path d="M104,62 Q136,38 172,68"/>'
                    '<path d="M68,48 Q108,22 148,46"/>'
                    '</g>'
                    '<path d="M108,128 L108,68 M108,92 L78,56 M108,84 L138,54 M92,72 L106,42" stroke="#2e241f" stroke-width="2.6" stroke-linecap="round"/>'
                ),
            },
        ],
    },

    # =========================================================================
    # A6 - RAMI SOTTILI E FOGLIE BRINATE IN PRIMO PIANO (2 modalità)
    # =========================================================================
    "A6-M1": {
        "titolo": "Infografica del video: rami sottili tirati e intrecciati dal basso verso l'alto",
        "fasi": [
            {
                "titolo": "Rami principali dal basso in alto",
                "carta": "asciutta",
                "colori": ["ombra_bruc", "seppia"],
                "attrezzo": "Tondo a punta fine n. 6 o rigger",
                "testo": "Si appoggia il pennello alla base e si tirano i fusti principali verso l'alto, alleggerendo la pressione per assottigliare la linea.",
                "svg": svg_wrap(
                    '<path d="M58,128 Q78,78 96,24 M136,128 Q124,78 142,26" stroke="#4f3728" stroke-width="3" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Biforcazioni strette a V e Y",
                "carta": "asciutta",
                "colori": ["ombra_bruc"],
                "attrezzo": "Tondo a punta fine n. 6",
                "testo": "Dai rami principali si fanno partire biforcazioni strette a V e a Y, variando l'inclinazione e lo spessore a ogni snodo.",
                "svg": svg_wrap(
                    '<path d="M58,128 Q78,78 96,24 M136,128 Q124,78 142,26" stroke="#4f3728" stroke-width="3" fill="none" stroke-linecap="round"/>'
                    '<path d="M76,82 L54,42 M86,56 L112,28 M130,84 L110,44 M134,58 L162,32" stroke="#4f3728" stroke-width="2" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Incroci naturali e punte finissime",
                "carta": "asciutta",
                "colori": ["ombra_bruc"],
                "attrezzo": "Punta finissima del pennello",
                "testo": "Si aggiungono rami centrali che si incrociano e si sovrappongono agli altri (in natura i rami non si evitano), terminando le cime a filo.",
                "svg": svg_wrap(
                    '<path d="M58,128 Q78,78 96,24 M136,128 Q124,78 142,26" stroke="#4f3728" stroke-width="3" fill="none" stroke-linecap="round"/>'
                    '<path d="M76,82 L54,42 M86,56 L112,28 M130,84 L110,44 M134,58 L162,32" stroke="#4f3728" stroke-width="2" fill="none" stroke-linecap="round"/>'
                    '<path d="M98,128 Q106,76 74,30 M102,88 L148,40 M66,64 L122,48" stroke="#2e241f" stroke-width="1.5" fill="none" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A6-M2": {
        "titolo": "Infografica dei video: foglie scure col filo bianco di brina e bordo ammorbidito",
        "fasi": [
            {
                "titolo": "Risparmio del filo bianco sottile",
                "carta": "asciutta",
                "colori": ["siena_bruc", "prussia", "cremisi", "mascherante"],
                "attrezzo": "Tondo n. 4 (o tiralinee)",
                "testo": "Si dipinge la foglia un lobo alla volta, risparmiando un filo bianco sottilissimo tra i lobi o sul bordo alto (oppure lo si protegge prima col tiralinee).",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d9ecfa"/>'
                    '<path d="M44,116 Q98,74 166,34" stroke="#2e241f" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                    '<path d="M64,78 Q88,56 116,68 Q92,88 64,78 Z" fill="#4a2c24"/>'
                    '<path d="M112,52 Q136,32 162,44 Q140,64 112,52 Z" fill="#4a2c24"/>'
                    '<path d="M66,76 Q88,58 114,68 M114,50 Q136,34 160,44" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Accento scuro nella foglia umida",
                "carta": "umida",
                "colori": ["prussia"],
                "attrezzo": "Tondo a punta n. 4",
                "testo": "Mentre il lobo della foglia è ancora umido, si toccano il centro e la base con blu di Prussia denso per dare profondità, senza coprire il filo bianco.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d9ecfa"/>'
                    '<path d="M44,116 Q98,74 166,34" stroke="#2e241f" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                    '<path d="M64,78 Q88,56 116,68 Q92,88 64,78 Z" fill="#1b365d"/>'
                    '<path d="M112,52 Q136,32 162,44 Q140,64 112,52 Z" fill="#1b365d"/>'
                    '<path d="M66,76 Q88,58 114,68 M114,50 Q136,34 160,44" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Fili ammorbiditi col pennello umido",
                "carta": "asciutta",
                "colori": ["acqua"],
                "attrezzo": "Tondo pulito appena umido",
                "testo": "A foglia asciutta (e tolto l'eventuale mascherante) si sfiorano i fili bianchi con un pennello pulito e appena umido, per legare la brina alla foglia.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d9ecfa"/>'
                    '<path d="M44,116 Q98,74 166,34" stroke="#2e241f" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                    '<path d="M64,78 Q88,56 116,68 Q92,88 64,78 Z" fill="#1b365d"/>'
                    '<path d="M112,52 Q136,32 162,44 Q140,64 112,52 Z" fill="#1b365d"/>'
                    '<path d="M66,76 Q88,58 114,68 M114,50 Q136,34 160,44" stroke="#cbe4f7" stroke-width="3" fill="none" stroke-linecap="round"/>'
                    '<path d="M66,76 Q88,58 114,68 M114,50 Q136,34 160,44" stroke="#ffffff" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
                ),
            },
        ],
    },
}


def rendi_infografica_modalita(id_mod, e, pill):
    info = INFOGRAFICHE.get(id_mod)
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
    return (
        f'<div class="mod-info">'
        f'<div class="mod-info-tit">{e(info["titolo"])}</div>'
        f'<div class="fasi-grid tre">{"".join(carte)}</div>'
        f"</div>"
    )


def rendi_coda_albero(t, e):
    coda = []
    if t.get("controllo"):
        coda.append(f'<div class="info-check ok"><b>✓ Che cosa controllare sul foglietto:</b> {e(t["controllo"])}</div>')
    if t.get("attenzione"):
        att = " · ".join(e(x) for x in t["attenzione"])
        coda.append(f'<div class="info-check att"><b>⚠ Da evitare:</b> {att}</div>')
    if not coda:
        return ""
    return f'<div class="info-coda">{"".join(coda)}</div>'

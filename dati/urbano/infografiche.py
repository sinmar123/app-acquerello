#!/usr/bin/env python3
"""Infografiche SVG passo-passo per le 6 modalità del modulo S6 · Paesaggio urbano (U1-M1 .. U3-M2).
Ogni modalità ha 3 fasi illustrate (viewBox 220x140) con stato della carta, attrezzo, gettoni colore
senza nomi di marche commerciali e descrizione sintetica del passaggio."""

COLORI_HEX = {
    "ocra_gialla": ("#d8a63a", "ocra gialla (PY43)"),
    "siena_nat": ("#c98a2c", "terra di Siena naturale (PBr7)"),
    "siena_bruc": ("#9e4726", "terra di Siena bruciata (PR101)"),
    "ombra_nat": ("#7a6248", "terra d'ombra naturale (PBr7)"),
    "ombra_bruc": ("#4f3728", "terra d'ombra bruciata (PBr7)"),
    "rosso_terracotta": ("#b8432b", "rosso veneziano / ossido rosso (PR101)"),
    "rosso_cadmio": ("#d63b2f", "rosso chiaro / cadmio (PR108)"),
    "arancio": ("#e57c24", "arancio caldo (PO20)"),
    "cremisi": ("#8f2438", "cremisi / rosa chinacridone (PV19)"),
    "giallo_caldo": ("#ebd442", "giallo caldo (PY175 / PY35)"),
    "verde_chiaro": ("#7cb356", "verde chiaro (giallo + cobalto)"),
    "verde_scuro": ("#2d5e3e", "verde scuro per chiome"),
    "ceruleo": ("#3c88b8", "blu ceruleo (PB35)"),
    "cobalto": ("#3569a4", "blu cobalto (PB28)"),
    "oltremare": ("#2b4c8c", "blu oltremare (PB29)"),
    "viola_ombra": ("#5c4b7d", "viola minerale / diossazina (PV16 / PV23)"),
    "grigio_payne": ("#2f3b4c", "grigio di Payne / tinta neutra"),
    "acqua": ("#b8ddf5", "acqua pulita"),
}


def svg_wrap(inner, label=""):
    aria = f' aria-label="{label}"' if label else ""
    return (
        f'<svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg" role="img"{aria}>'
        '<rect x="2" y="2" width="216" height="136" rx="6" fill="#fcfaf4" stroke="#d5cfc0" stroke-width="1.5"/>'
        + inner
        + "</svg>"
    )


INFOGRAFICHE = {
    # =========================================================================
    # U1 - VICOLI, SCALINATE E MURI COLORATI (2 modalità)
    # =========================================================================
    "U1-M1": {
        "titolo": "Le tre fasi: luce risparmiata sui gradini, ombre a dente di sega e muri blu",
        "fasi": [
            {
                "titolo": "Parete al sole a pennello piatto scarico",
                "carta": "umida",
                "colori": ["ombra_nat", "ocra_gialla", "cobalto"],
                "attrezzo": "Piatto 12-18 mm",
                "testo": "Si lascia bianca la rampa centrale dei gradini; sul muro destro si passa il piatto poco carico d'acqua per suggerire l'intonaco, toccandolo a umido con poco cobalto.",
                "svg": svg_wrap(
                    # Cielo chiarissimo in cima al vicolo
                    '<rect x="78" y="8" width="56" height="22" fill="#cde3f5" opacity="0.65"/>'
                    # Traccia leggera dei muri e della scalinata centrale lasciata bianca
                    '<path d="M18,8 L78,8 L78,94 L18,132 Z" fill="#f7f4ec" stroke="#b9b09f" stroke-width="1"/>'
                    '<path d="M134,8 L202,8 L202,132 L134,94 Z" fill="#efe4c8" opacity="0.72" stroke="#b9b09f" stroke-width="1"/>'
                    # Effetto granulato / pennello scarico sul muro destro + tocchi cobalto a umido
                    '<path d="M142,16 L142,88 M154,14 L154,96 M168,18 L168,104 M184,14 L184,114" stroke="#c8ab73" stroke-width="5" stroke-dasharray="14,5,6,4" opacity="0.55"/>'
                    '<ellipse cx="158" cy="48" rx="14" ry="20" fill="#5a87b8" opacity="0.28"/>'
                    '<ellipse cx="182" cy="76" rx="12" ry="16" fill="#5a87b8" opacity="0.24"/>'
                    # Linee sottili dei gradini centrali risparmiati a carta bianca
                    '<path d="M78,72 L134,72 M74,82 L138,82 M68,93 L144,93 M60,106 L152,106 M50,120 L162,120" stroke="#b5ac9b" stroke-width="1"/>'
                ),
            },
            {
                "titolo": "Quinta scura e ombra a dente di sega",
                "carta": "asciutta",
                "colori": ["viola_ombra", "cobalto", "grigio_payne"],
                "attrezzo": "Piatto da 12 mm (di taglio)",
                "testo": "Con il muro sinistro in tono scuro freddo, si usa lo spigolo del pennello piatto per disegnare i denti d'ombra netti contro le alzate bianche dei gradini.",
                "svg": svg_wrap(
                    '<rect x="78" y="8" width="56" height="22" fill="#cde3f5" opacity="0.65"/>'
                    # Muro destro medio-chiaro
                    '<path d="M134,8 L202,8 L202,132 L134,94 Z" fill="#e8dab8" opacity="0.8"/>'
                    # Grande quinta scura a sinistra (forma a U semichiusa)
                    '<path d="M12,8 L78,8 L78,92 L46,132 L12,132 Z" fill="#51466b" opacity="0.82"/>'
                    # Ombra a dente di sega sui gradini (sawtooth shadow)
                    '<polygon points="78,72 108,72 102,82 116,82 108,93 124,93 114,106 132,106 118,120 50,120 68,93" fill="#463d61" opacity="0.88"/>'
                    # Pedate al sole che brillano per contrasto
                    '<path d="M108,72 L134,72 M116,82 L138,82 M124,93 L144,93 M132,106 L152,106" stroke="#fcfaf4" stroke-width="2.5"/>'
                ),
            },
            {
                "titolo": "Zoccolo blu saturo e contrappunto caldo",
                "carta": "umida",
                "colori": ["cobalto", "oltremare", "arancio"],
                "attrezzo": "Tondo medio e goccia",
                "testo": "Si ancora la parte bassa dei muri con blu cobalto e oltremare intensi, salvando un filo bianco sul corrimano, e si accende una nota arancio sopra la porta.",
                "svg": svg_wrap(
                    '<rect x="78" y="8" width="56" height="22" fill="#cde3f5" opacity="0.7"/>'
                    '<path d="M134,8 L202,8 L202,132 L134,94 Z" fill="#e6d7b4" opacity="0.82"/>'
                    '<path d="M12,8 L78,8 L78,92 L46,132 L12,132 Z" fill="#4f4569" opacity="0.82"/>'
                    # Zoccolo blu saturo di Chefchaouen a sinistra e a destra in basso
                    '<path d="M12,68 L78,58 L78,96 L48,132 L12,132 Z" fill="#2a62a8" opacity="0.86"/>'
                    '<path d="M134,62 L202,74 L202,132 L162,132 L134,94 Z" fill="#2e6cb5" opacity="0.82"/>'
                    # Filo bianco risparmiato del corrimano
                    '<line x1="134" y1="62" x2="176" y2="108" stroke="#fcfaf4" stroke-width="2.4" stroke-linecap="round"/>'
                    # Ombra a dente di sega e primo piano neutro sfumato
                    '<polygon points="78,72 108,72 102,82 116,82 108,93 124,93 114,106 132,106 118,120 50,120 68,93" fill="#3a3556" opacity="0.9"/>'
                    '<rect x="12" y="120" width="190" height="14" fill="#6d655e" opacity="0.45"/>'
                    # Accento caldo arancio e ombra viola sulla porticina
                    '<path d="M54,56 Q62,46 70,56 L70,82 L54,82 Z" fill="#24385c"/>'
                    '<rect x="52" y="45" width="20" height="5" rx="1.5" fill="#e57c24" opacity="0.9"/>'
                ),
            },
        ],
    },
    "U1-M2": {
        "titolo": "Le tre fasi: fondo caldo col sale, vasi con luce sollevata e ombre portate",
        "fasi": [
            {
                "titolo": "Velo caldo leggero e sale sul muro",
                "carta": "bagnata",
                "colori": ["ocra_gialla", "siena_bruc", "oltremare"],
                "attrezzo": "Tondo n. 10-12 e sale fino",
                "testo": "Si stende un velo al tè di ocra e Siena bruciata sui muri risparmiando il centro; sulla spalla destra in mattoni bagnata si lasciano cadere pochi grani di sale.",
                "svg": svg_wrap(
                    # Pareti del vicolo con velo caldo leggero
                    '<polygon points="10,8 82,8 82,104 10,132" fill="#edd8b0" opacity="0.65"/>'
                    '<polygon points="82,18 148,18 148,100 82,100" fill="#f7eed8" opacity="0.6"/>'
                    # Spalla destra in mattoni con terra di Siena bruciata + puntinatura chiara del sale
                    '<rect x="148" y="8" width="62" height="124" fill="#b8653b" opacity="0.72"/>'
                    '<circle cx="162" cy="30" r="2.2" fill="#fcfaf4" opacity="0.8"/>'
                    '<circle cx="176" cy="42" r="1.8" fill="#fcfaf4" opacity="0.8"/>'
                    '<circle cx="158" cy="64" r="2.5" fill="#fcfaf4" opacity="0.75"/>'
                    '<circle cx="172" cy="86" r="2.0" fill="#fcfaf4" opacity="0.8"/>'
                    '<circle cx="164" cy="108" r="2.2" fill="#fcfaf4" opacity="0.75"/>'
                    # Fascia blu della porta sulla destra
                    '<rect x="186" y="18" width="18" height="114" fill="#285580" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Piante a umido e vasi con luce sollevata",
                "carta": "umida",
                "colori": ["verde_chiaro", "verde_scuro", "rosso_terracotta"],
                "attrezzo": "Tondo n. 6 e pennello umido",
                "testo": "Si dipinge la chioma dal verde chiaro allo scuro a umido; si stendono i vasi in rosso terracotta e, prima che asciughino, si solleva una striscia di luce sul lato al sole.",
                "svg": svg_wrap(
                    '<polygon points="10,8 82,8 82,104 10,132" fill="#edd8b0" opacity="0.65"/>'
                    '<rect x="148" y="8" width="62" height="124" fill="#b8653b" opacity="0.68"/>'
                    '<rect x="186" y="18" width="18" height="114" fill="#285580" opacity="0.85"/>'
                    # Finestra rossa di fondo
                    '<rect x="96" y="34" width="16" height="22" fill="#9e3528"/>'
                    # Chioma rampicante verde chiaro -> verde scuro bagnato su bagnato
                    '<ellipse cx="132" cy="36" rx="26" ry="20" fill="#88be52" opacity="0.85"/>'
                    '<ellipse cx="140" cy="40" rx="18" ry="15" fill="#2d633b" opacity="0.85"/>'
                    '<ellipse cx="114" cy="76" rx="10" ry="18" fill="#5e9c45" opacity="0.85"/>'
                    # Vasi di terracotta con sollevamento chiaro a sinistra
                    '<path d="M74,104 L88,104 L85,122 L77,122 Z" fill="#bd432a"/>'
                    '<path d="M76,106 L80,106 L79,120 L77,120 Z" fill="#f3b69b" opacity="0.85"/>'
                    '<path d="M108,102 L124,102 L120,122 L112,122 Z" fill="#bd432a"/>'
                    '<path d="M110,104 L115,104 L114,120 L112,120 Z" fill="#f3b69b" opacity="0.85"/>'
                    '<path d="M132,104 L146,104 L143,124 L135,124 Z" fill="#a83520"/>'
                ),
            },
            {
                "titolo": "Velatura d'ombra viola-grigia obliqua",
                "carta": "asciutta",
                "colori": ["grigio_payne", "viola_ombra"],
                "attrezzo": "Tondo n. 10",
                "testo": "Su fondo ben asciutto si passano le ombre portate diagonali sui muri e sul selciato con una velatura trasparente di grigio di Payne e viola, lasciando intatta la luce centrale.",
                "svg": svg_wrap(
                    '<polygon points="10,8 82,8 82,104 10,132" fill="#edd8b0" opacity="0.7"/>'
                    '<rect x="96" y="34" width="16" height="22" fill="#9e3528"/>'
                    '<rect x="148" y="8" width="62" height="124" fill="#b8653b" opacity="0.72"/>'
                    # Giunti leggeri dei conci di pietra
                    '<path d="M148,34 L186,34 M148,58 L186,58 M148,84 L186,84 M148,108 L186,108" stroke="#6b3b22" stroke-width="1" opacity="0.65"/>'
                    '<rect x="186" y="18" width="18" height="114" fill="#285580" opacity="0.88"/>'
                    '<ellipse cx="132" cy="36" rx="26" ry="20" fill="#7cb356" opacity="0.9"/>'
                    '<ellipse cx="140" cy="40" rx="18" ry="15" fill="#285935" opacity="0.9"/>'
                    '<path d="M74,104 L88,104 L85,122 L77,122 Z" fill="#bd432a"/>'
                    '<path d="M108,102 L124,102 L120,122 L112,122 Z" fill="#bd432a"/>'
                    '<path d="M132,104 L146,104 L143,124 L135,124 Z" fill="#a83520"/>'
                    # Grandi ombre portate diagonali trasparenti a sinistra e a destra
                    '<polygon points="10,8 56,8 56,96 96,132 10,132" fill="#4a3e68" opacity="0.48"/>'
                    '<polygon points="148,46 210,28 210,132 126,132 148,112" fill="#4a3e68" opacity="0.52"/>'
                ),
            },
        ],
    },

    # =========================================================================
    # U2 - FACCIATE AL SOLE E GRANDE OMBRA PORTATA (2 modalità)
    # =========================================================================
    "U2-M1": {
        "titolo": "Le tre fasi: cielo scontornato sui tetti bianchi, quinte scure e ombre geometriche",
        "fasi": [
            {
                "titolo": "Cielo azzurro netto contro i muri bianchi",
                "carta": "asciutta",
                "colori": ["cobalto", "ceruleo"],
                "attrezzo": "Mop sintetico con buona punta",
                "testo": "Con metà cobalto e metà ceruleo si dipinge il cielo dall'alto verso il basso, girando con precisione attorno a comignoli e spigoli per conservare la carta bianca.",
                "svg": svg_wrap(
                    # Cielo azzurro intenso che ritaglia in negativo i tetti e il comignolo bianchi di Mykonos
                    '<path d="M72,8 L168,8 L148,74 L132,74 L118,42 L106,42 L106,24 L98,24 L98,42 L72,36 Z" fill="#2f86d4" opacity="0.88"/>'
                    # Profilo sottile a matita delle case lasciate a carta bianca pura
                    '<path d="M12,18 L72,36 L72,118 L12,132 Z" fill="#fcfaf4" stroke="#c8c0b0" stroke-width="1"/>'
                    '<path d="M72,36 L98,42 L98,24 L106,24 L106,42 L118,42 L132,74 L132,106 L72,106 Z" fill="#fcfaf4" stroke="#c8c0b0" stroke-width="1"/>'
                    '<path d="M168,8 L208,8 L208,132 L148,108 L148,74 Z" fill="#f7f2e7" stroke="#c8c0b0" stroke-width="1"/>'
                ),
            },
            {
                "titolo": "Quinta scura a destra e ombra sulla strada",
                "carta": "asciutta",
                "colori": ["oltremare", "siena_bruc", "cremisi"],
                "attrezzo": "Mop morbido in vajo",
                "testo": "A cielo asciutto si stende la facciata in ombra a destra variando rosso, blu e terra nel velo umido, e si trascina la stessa massa scura di traverso sul vicolo.",
                "svg": svg_wrap(
                    '<path d="M72,8 L168,8 L148,74 L132,74 L118,42 L106,42 L106,24 L98,24 L98,42 L72,36 Z" fill="#2f86d4" opacity="0.88"/>'
                    # Case bianche a sinistra con leggerissimo velo smorzato su un fianco
                    '<rect x="74" y="42" width="26" height="64" fill="#eae5dc" opacity="0.65"/>'
                    # Grande edificio in ombra a destra + ombra proiettata sulla strada
                    '<polygon points="168,8 208,8 208,132 108,132 132,106 148,74" fill="#5e5168" opacity="0.84"/>'
                    '<ellipse cx="182" cy="54" rx="18" ry="28" fill="#8b5d52" opacity="0.32"/>'
                    '<polygon points="148,86 208,98 208,132 108,132" fill="#3d4363" opacity="0.65"/>'
                ),
            },
            {
                "titolo": "Triangoli d'ombra obliqua sulla calce",
                "carta": "asciutta",
                "colori": ["oltremare", "siena_bruc", "arancio"],
                "attrezzo": "Mop in vajo e tondo medio",
                "testo": "In una sola passata decisa si tracciano le ombre geometriche dei balconi sul muro sinistro e si collegano alla sagoma scura del furgoncino, facendo splendere la calce.",
                "svg": svg_wrap(
                    '<path d="M72,8 L168,8 L148,74 L132,74 L118,42 L106,42 L106,24 L98,24 L98,42 L72,36 Z" fill="#2f86d4" opacity="0.88"/>'
                    '<rect x="74" y="42" width="26" height="64" fill="#ece7de" opacity="0.65"/>'
                    '<polygon points="168,8 208,8 208,132 108,132 132,106 148,74" fill="#5a4e66" opacity="0.86"/>'
                    # Ombra geometrica netta a denti obliqui sul muro bianco di sinistra
                    '<polygon points="12,18 58,34 42,50 72,60 58,74 86,84 72,94 34,82 34,132 12,132" fill="#584b66" opacity="0.86"/>'
                    # Furgoncino a tre ruote collegato all'ombra e lastre del selciato
                    '<rect x="52" y="88" width="38" height="24" rx="2" fill="#244854"/>'
                    '<polygon points="46,112 96,112 108,124 40,124" fill="#282d3c" opacity="0.88"/>'
                    '<path d="M56,128 L82,126 M92,128 L124,126" stroke="#7c756d" stroke-width="2" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "U2-M2": {
        "titolo": "Le tre fasi: verticali raddrizzate, lavaggio continuo e grande ombra in primo piano",
        "fasi": [
            {
                "titolo": "Verticali raddrizzate e gerarchia del segno",
                "carta": "asciutta",
                "colori": ["grigio_payne"],
                "attrezzo": "Penna impermeabile o matita",
                "testo": "Si corregge la deformazione del grandangolo riportando dritti gli spigoli verticali; si ispessiscono solo i profili degli edifici che stanno davanti per staccare i piani.",
                "svg": svg_wrap(
                    # Linee sottili degli edifici al centro e spigoli più forti in primo piano
                    '<line x1="12" y1="98" x2="208" y2="98" stroke="#cfc7b8" stroke-width="1" stroke-dasharray="4,3"/>'
                    # Quinta sinistra e destra in primo piano (tratto più deciso)
                    '<path d="M12,12 L48,24 L48,118 L12,128" fill="none" stroke="#2b2b2b" stroke-width="2.2"/>'
                    '<path d="M208,14 L166,28 L166,114 L208,126" fill="none" stroke="#2b2b2b" stroke-width="2.2"/>'
                    # Case di fondo con timpani a gradoni (tratto fine)
                    '<path d="M58,98 L58,52 L74,38 L90,52 L90,98 M90,56 L112,36 L132,54 L132,98 M132,58 L166,46" fill="none" stroke="#555" stroke-width="1.1"/>'
                    # Lampione a un terzo della larghezza
                    '<line x1="82" y1="62" x2="82" y2="108" stroke="#2b2b2b" stroke-width="1.6"/>'
                    '<circle cx="82" cy="60" r="3" fill="none" stroke="#2b2b2b" stroke-width="1.4"/>'
                ),
            },
            {
                "titolo": "Lavaggio unico: cielo, mattoni e selciato",
                "carta": "bagnata",
                "colori": ["cobalto", "siena_nat", "siena_bruc"],
                "attrezzo": "Mop medio (quill)",
                "testo": "Si stende un primo fondo continuo che unisce il cielo cobalto, il calore dei muri in mattoni (ossido rosso e Siena) e il selciato in Siena naturale smorzata col blu.",
                "svg": svg_wrap(
                    # Cielo cobalto mosso con bianchi risparmiati
                    '<path d="M44,10 L172,10 L166,46 L132,54 L112,36 L90,52 L74,38 L48,44 Z" fill="#4f82bd" opacity="0.62"/>'
                    # Toni caldi di base su case e quinte
                    '<polygon points="12,12 48,24 48,118 12,128" fill="#a88b73" opacity="0.55"/>'
                    '<rect x="74" y="44" width="38" height="54" fill="#c96e4b" opacity="0.58"/>'
                    '<rect x="112" y="44" width="34" height="54" fill="#ede4ce" opacity="0.7"/>'
                    '<polygon points="166,28 208,14 208,126 166,114" fill="#b87b5c" opacity="0.52"/>'
                    # Selciato in Siena naturale + punta di blu
                    '<polygon points="12,98 208,98 208,134 12,134" fill="#cab489" opacity="0.65"/>'
                    # Ripasso contorno principale
                    '<path d="M58,98 L58,52 L74,38 L90,52 L112,36 L132,54 L166,46" fill="none" stroke="#444" stroke-width="1"/>'
                ),
            },
            {
                "titolo": "Grande ombra collegata e poche finestre",
                "carta": "asciutta",
                "colori": ["oltremare", "ombra_bruc"],
                "attrezzo": "Pennello grande e tondo fine",
                "testo": "A foglio asciugato, un pennello grande carico di oltremare e bruno chiude in ombra le due quinte laterali e tutto il primo piano, isolando al centro le facciate colpite dal sole.",
                "svg": svg_wrap(
                    '<path d="M44,10 L172,10 L166,46 L132,54 L112,36 L90,52 L74,38 L48,44 Z" fill="#4f82bd" opacity="0.65"/>'
                    # Facciata centrale illuminata dal sole che spicca!
                    '<rect x="74" y="44" width="38" height="54" fill="#c96843" opacity="0.82"/>'
                    '<rect x="112" y="44" width="34" height="54" fill="#f7efda" opacity="0.92"/>'
                    # Grande massa d'ombra collegata: quinta sinistra + primo piano stradale + quinta destra
                    '<polygon points="12,12 56,26 56,102 146,102 146,50 166,46 166,28 208,14 208,134 12,134" fill="#3a4c70" opacity="0.76"/>'
                    # Pochi accenti scuri di finestre e lampione
                    '<rect x="82" y="58" width="6" height="11" fill="#2a2833"/>'
                    '<rect x="96" y="58" width="6" height="11" fill="#2a2833"/>'
                    '<rect x="120" y="58" width="6" height="11" fill="#3c4659"/>'
                    '<line x1="82" y1="62" x2="82" y2="112" stroke="#1f2430" stroke-width="1.8"/>'
                ),
            },
        ],
    },

    # =========================================================================
    # U3 - STRADE IN CITTA, RIFLESSI SUL BAGNATO E FIGURE IN SCALA (2 modalità)
    # =========================================================================
    "U3-M1": {
        "titolo": "Le tre fasi: goccia guida attorno ai fari, massa collegata e riflessi sul bagnato",
        "fasi": [
            {
                "titolo": "Orizzonte basso, goccia guida e luci bianche",
                "carta": "bagnata",
                "colori": ["ocra_gialla", "cremisi", "oltremare"],
                "attrezzo": "Mop grande su foglio inclinato",
                "testo": "Fissato l'orizzonte sotto metà foglio, si accompagna verso il basso il cordone d'acqua carico («goccia guida») in grigio morbido dai tre primari, girando attorno a tetti e fari delle auto.",
                "svg": svg_wrap(
                    # Orizzonte leggero sotto metà foglio (y=86)
                    '<line x1="10" y1="86" x2="210" y2="86" stroke="#b8b0a0" stroke-width="1" stroke-dasharray="4,3"/>'
                    # Grande lavaggio graduato atmosferico dall'alto fino alla goccia guida ("Mr Bead")
                    '<path d="M10,8 L210,8 L210,82 Q176,86 154,80 L142,80 L138,85 L112,85 L108,78 L90,78 L86,85 L10,83 Z" fill="#b7c2cc" opacity="0.72"/>'
                    # Cordone carico ("goccia guida") sul bordo inferiore del lavaggio
                    '<path d="M10,83 Q50,87 86,84 M112,85 Q125,88 138,85 M156,82 Q184,87 210,82" fill="none" stroke="#6f7e8f" stroke-width="3" stroke-linecap="round"/>'
                    # Sagome bianche risparmiate di auto e punti luce
                    '<rect x="88" y="78" width="20" height="10" rx="2" fill="#fcfaf4"/>'
                    '<rect x="140" y="80" width="16" height="8" rx="2" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Sagoma urbana unita, ombra d'ancoraggio e cavi",
                "carta": "umida",
                "colori": ["oltremare", "siena_bruc", "arancio"],
                "attrezzo": "Mop medio e pennello rigger",
                "testo": "Si legano in un'unica silhouette palazzi, alberi e traffico, si ancora ogni veicolo con l'ombra scura sotto il pianale, si toccano i fanali arancio a umido e si tirano i cavi col rigger.",
                "svg": svg_wrap(
                    '<rect x="10" y="8" width="200" height="78" fill="#cfd6dd" opacity="0.55"/>'
                    # Silhouette atmosferica di palazzi in secondo piano e quinte più scure ai lati
                    '<polygon points="82,22 114,22 114,84 82,84" fill="#8994a1" opacity="0.65"/>'
                    '<polygon points="10,12 58,28 58,86 10,86" fill="#464f5c" opacity="0.85"/>'
                    '<polygon points="154,26 210,14 210,86 154,86" fill="#4b5361" opacity="0.82"/>'
                    # Chioma scura a sinistra che abbraccia la strada
                    '<ellipse cx="44" cy="54" rx="26" ry="18" fill="#2f3d38" opacity="0.85"/>'
                    # Auto risparmiate con ombra scura sotto il pianale + fanali arancio/rossi
                    '<path d="M86,84 L110,84 L108,92 L88,92 Z" fill="#232830"/>'
                    '<rect x="89" y="77" width="18" height="8" rx="1.5" fill="#fcfaf4"/>'
                    '<circle cx="91" cy="84" r="2.2" fill="#ff9f1c"/>'
                    '<circle cx="105" cy="84" r="2.2" fill="#ff9f1c"/>'
                    '<path d="M138,84 L158,84 L156,90 L140,90 Z" fill="#232830"/>'
                    '<circle cx="142" cy="84" r="2" fill="#e63946"/>'
                    '<circle cx="154" cy="84" r="2" fill="#e63946"/>'
                    # Cavi sospesi del tram tirati col rigger
                    '<path d="M14,24 Q110,48 206,20 M28,42 Q118,58 206,38" fill="none" stroke="#363c45" stroke-width="0.9"/>'
                ),
            },
            {
                "titolo": "Asfalto ribagnato e riflessi verticali",
                "carta": "bagnata",
                "colori": ["acqua", "grigio_payne", "rosso_cadmio"],
                "attrezzo": "Piatto d'acqua e tondo medio",
                "testo": "Si bagna generosamente d'acqua pulita solo una fascia dell'asfalto lasciando strisce asciutte, e si calano pennellate verticali scure e calde sotto auto e fanali senza più toccarle.",
                "svg": svg_wrap(
                    '<rect x="10" y="8" width="200" height="78" fill="#cfd6dd" opacity="0.55"/>'
                    '<polygon points="82,22 114,22 114,84 82,84" fill="#8994a1" opacity="0.65"/>'
                    '<polygon points="10,12 58,28 58,86 10,86" fill="#464f5c" opacity="0.85"/>'
                    '<polygon points="154,26 210,14 210,86 154,86" fill="#4b5361" opacity="0.82"/>'
                    '<ellipse cx="44" cy="54" rx="26" ry="18" fill="#2f3d38" opacity="0.85"/>'
                    '<path d="M14,24 Q110,48 206,20" fill="none" stroke="#363c45" stroke-width="0.9"/>'
                    # Zona dell'asfalto bagnata con diagonale luminosa risparmiata
                    '<polygon points="10,86 210,86 210,134 10,134" fill="#dce4ec" opacity="0.55"/>'
                    '<polygon points="104,88 124,88 158,134 118,134" fill="#fcfaf4" opacity="0.9"/>'
                    # Riflessi verticali diffusi su bagnato sotto le auto e i fanali!
                    '<rect x="88" y="90" width="20" height="38" rx="4" fill="#3a4352" opacity="0.52"/>'
                    '<rect x="139" y="89" width="17" height="34" rx="4" fill="#3a4352" opacity="0.48"/>'
                    '<line x1="142" y1="88" x2="142" y2="116" stroke="#e63946" stroke-width="3.2" opacity="0.65" stroke-linecap="round"/>'
                    '<line x1="154" y1="88" x2="154" y2="114" stroke="#e63946" stroke-width="3.2" opacity="0.65" stroke-linecap="round"/>'
                    # Auto sopra
                    '<path d="M86,84 L110,84 L108,92 L88,92 Z" fill="#1e232b"/>'
                    '<rect x="89" y="77" width="18" height="8" rx="1.5" fill="#fcfaf4"/>'
                    '<path d="M138,84 L158,84 L156,90 L140,90 Z" fill="#1e232b"/>'
                ),
            },
        ],
    },
    "U3-M2": {
        "titolo": "Le tre fasi: sfondo urbano leggero, sagome «a carota» e teste sulla linea degli occhi",
        "fasi": [
            {
                "titolo": "Sfondo urbano chiaro e quota degli occhi",
                "carta": "umida",
                "colori": ["oltremare", "ombra_bruc", "verde_chiaro"],
                "attrezzo": "Tondo medio (n. 6-8)",
                "testo": "Si dipinge lo sfondo cittadino con un grigio molto diluito in modo che resti lontano e luminoso, e si fissa la fascia orizzontale all'altezza degli occhi dell'osservatore.",
                "svg": svg_wrap(
                    # Profilo pallido di edifici lontani (valore chiaro)
                    '<path d="M18,88 L18,54 L34,54 L34,38 L52,38 L52,60 L74,60 L74,32 L94,32 L94,56 L124,56 L124,44 L146,44 L146,64 L198,64 L198,88 Z" fill="#d5dce3" opacity="0.85"/>'
                    # Alberi semplici sul viale
                    '<ellipse cx="64" cy="70" rx="9" ry="12" fill="#7aa65a" opacity="0.8"/>'
                    '<line x1="64" y1="80" x2="64" y2="92" stroke="#4a3b30" stroke-width="1.6"/>'
                    '<ellipse cx="158" cy="60" rx="8" ry="18" fill="#649149" opacity="0.85"/>'
                    '<line x1="158" y1="76" x2="158" y2="92" stroke="#4a3b30" stroke-width="1.8"/>'
                    # Fascia del marciapiede e linea tratteggiata della quota occhi (y=74)
                    '<line x1="12" y1="92" x2="208" y2="92" stroke="#6d7468" stroke-width="2"/>'
                    '<line x1="12" y1="74" x2="208" y2="74" stroke="#c87a28" stroke-width="1.2" stroke-dasharray="4,3"/>'
                ),
            },
            {
                "titolo": "Il gesto in tre tocchi: testa, busto e gambe",
                "carta": "asciutta",
                "colori": ["oltremare", "ombra_bruc"],
                "attrezzo": "Tondo n. 4-6 a punta fine",
                "testo": "Con scuro denso (oltremare + ombra bruciata) si appoggia un puntino per la testa lasciando un filo di stacco sul collo, un busto a cuneo largo alle spalle e due tratti sottili per le gambe.",
                "svg": svg_wrap(
                    # Ingrandimento didattico delle 3 fasi della singola figura e di una coppia
                    # Passo A: puntino testa
                    '<circle cx="38" cy="36" r="4.5" fill="#252c38"/>'
                    '<text x="38" y="118" font-family="sans-serif" font-size="9.5" text-anchor="middle" fill="#555">1. testa</text>'
                    # Passo B: testa + busto "a carota" rastremato in basso
                    '<circle cx="98" cy="36" r="4.5" fill="#252c38"/>'
                    '<polygon points="89,43 107,43 102,74 94,74" fill="#252c38"/>'
                    '<text x="98" y="118" font-family="sans-serif" font-size="9.5" text-anchor="middle" fill="#555">2. busto</text>'
                    # Passo C: figura completa in passo + compagno accanto
                    '<circle cx="160" cy="36" r="4.5" fill="#252c38"/>'
                    '<polygon points="151,43 169,43 164,72 156,72" fill="#252c38"/>'
                    '<path d="M158,72 L154,100 M162,72 L167,98" stroke="#252c38" stroke-width="2.6" stroke-linecap="round"/>'
                    '<circle cx="182" cy="40" r="3.8" fill="#3a4556"/>'
                    '<polygon points="175,46 189,46 185,72 179,72" fill="#3a4556"/>'
                    '<path d="M181,72 L179,98 M184,72 L187,97" stroke="#3a4556" stroke-width="2.2" stroke-linecap="round"/>'
                    '<text x="171" y="118" font-family="sans-serif" font-size="9.5" text-anchor="middle" fill="#555">3. gambe</text>'
                ),
            },
            {
                "titolo": "Teste allineate, gruppi variati e ombre a terra",
                "carta": "asciutta",
                "colori": ["oltremare", "ombra_bruc", "grigio_payne"],
                "attrezzo": "Tondo n. 4 a punta fine",
                "testo": "In piano le teste degli adulti restano tutte vicine alla linea degli occhi, mentre i piedi scendono per chi è più vicino; un tocco d'ombra orizzontale sotto i piedi ancora le figure al suolo.",
                "svg": svg_wrap(
                    '<path d="M18,88 L18,54 L34,54 L34,38 L52,38 L52,60 L74,60 L74,32 L94,32 L94,56 L124,56 L124,44 L146,44 L146,64 L198,64 L198,88 Z" fill="#d5dce3" opacity="0.85"/>'
                    '<ellipse cx="64" cy="70" rx="9" ry="12" fill="#7aa65a" opacity="0.82"/>'
                    '<line x1="64" y1="80" x2="64" y2="92" stroke="#4a3b30" stroke-width="1.6"/>'
                    '<ellipse cx="158" cy="60" rx="8" ry="18" fill="#649149" opacity="0.85"/>'
                    '<line x1="158" y1="76" x2="158" y2="92" stroke="#4a3b30" stroke-width="1.8"/>'
                    '<rect x="12" y="92" width="196" height="10" fill="#8b9c78" opacity="0.55"/>'
                    '<line x1="12" y1="74" x2="208" y2="74" stroke="#c87a28" stroke-width="1" stroke-dasharray="3,3" opacity="0.7"/>'
                    # Figura vicina a sinistra (testa a y=73, piedi a y=110)
                    '<circle cx="34" cy="73" r="2.6" fill="#202733"/>'
                    '<polygon points="29,77 39,77 36,93 32,93" fill="#202733"/>'
                    '<path d="M33,93 L31,110 M35,93 L38,109" stroke="#202733" stroke-width="1.8" stroke-linecap="round"/>'
                    '<ellipse cx="42" cy="110" rx="10" ry="1.8" fill="#4f5b6b" opacity="0.55"/>'
                    # Figura lontana al centro (testa sempre a y=74, piedi più alti a y=91!)
                    '<circle cx="96" cy="74" r="1.7" fill="#424d5e"/>'
                    '<polygon points="93,77 99,77 97,85 95,85" fill="#424d5e"/>'
                    '<path d="M95,85 L94,92 M97,85 L98,92" stroke="#424d5e" stroke-width="1.2"/>'
                    '<ellipse cx="101" cy="92" rx="6" ry="1.2" fill="#4f5b6b" opacity="0.45"/>'
                    # Coppia media + bambino a destra (teste adulti a y=74, piedi a y=102)
                    '<circle cx="132" cy="74" r="2.2" fill="#252d3b"/>'
                    '<polygon points="128,77 136,77 134,90 130,90" fill="#252d3b"/>'
                    '<path d="M131,90 L129,102 M133,90 L135,102" stroke="#252d3b" stroke-width="1.5"/>'
                    '<circle cx="141" cy="75" r="2.1" fill="#2f394a"/>'
                    '<polygon points="137,78 145,78 143,90 139,90" fill="#2f394a"/>'
                    '<path d="M140,90 L139,102 M142,90 L144,101" stroke="#2f394a" stroke-width="1.5"/>'
                    '<circle cx="149" cy="82" r="1.6" fill="#252d3b"/>'
                    '<path d="M149,84 L149,101" stroke="#252d3b" stroke-width="2.2" stroke-linecap="round"/>'
                    '<ellipse cx="146" cy="102" rx="16" ry="1.8" fill="#4f5b6b" opacity="0.5"/>'
                ),
            },
        ],
    },
}


def rendi_infografica_modalita(id_mod, e, pill):
    info = INFOGRAFICHE.get(id_mod)
    if not info:
        raise ValueError(f"Infografica mancante per {id_mod}")
    if len(info["fasi"]) != 3:
        raise ValueError(f"{id_mod}: servono esattamente 3 fasi")
    carte = []
    for i, f in enumerate(info["fasi"], 1):
        if f["carta"] not in {"bagnata", "umida", "asciutta"}:
            raise ValueError(f"{id_mod} fase {i}: stato della carta non valido ({f['carta']})")
        chips = []
        for c_id in f.get("colori", []):
            if c_id not in COLORI_HEX:
                raise ValueError(f"{id_mod} fase {i}: colore sconosciuto {c_id}")
            col_hex, col_lab = COLORI_HEX[c_id]
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


def rendi_coda_esempio(t, e):
    coda = []
    if t.get("controllo"):
        coda.append(f'<div class="info-check ok"><b>✓ Che cosa controllare nella prova:</b> {e(t["controllo"])}</div>')
    if t.get("attenzione"):
        att = " · ".join(e(x) for x in t["attenzione"])
        coda.append(f'<div class="info-check att"><b>⚠ Da evitare:</b> {att}</div>')
    if not coda:
        return ""
    return f'<div class="info-coda">{"".join(coda)}</div>'

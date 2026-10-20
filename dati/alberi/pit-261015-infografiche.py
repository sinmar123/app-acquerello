# Tavole sinottiche SVG in 3 fasi dedicate a ciascuna delle 24 procedure video (A1-M1 .. A6-M2).
# Ogni scheda illustra visivamente la sequenza esecutiva:
# stato del supporto, pennello o strumento, pigmenti impiegati e azione pittorica.

COLORI_HEX = {
    "giallo_limone": ("#ebd834", "giallo limone / cadmio"),
    "verde_oro": ("#b8c93a", "verde oro"),
    "verde_chiaro": ("#7cb356", "verde chiaro"),
    "verde_oliva": ("#6b8238", "verde oliva / vescica"),
    "verde_bosco": ("#2b5b3c", "verde medio / scuro"),
    "turchese_cob": ("#38a3a5", "turchese di cobalto"),
    "blu_ftalo": ("#1b4965", "blu ftalo"),
    "cobalto": ("#3a6ea5", "blu cobalto / ceruleo"),
    "oltremare": ("#2b4c8c", "blu oltremare"),
    "prussia": ("#1b365d", "blu di Prussia"),
    "indaco": ("#263248", "indaco / grigio di Payne"),
    "lilla": ("#8f85a8", "grigio-malva / viola"),
    "cadmio_arancio": ("#e58728", "arancio / rosso chiaro"),
    "rosso_inglese": ("#b5482a", "rosso inglese / rame"),
    "cremisi": ("#8a2432", "cremisi / rosso scuro"),
    "siena_nat": ("#c98a2c", "terra di Siena naturale"),
    "siena_bruc": ("#9e4726", "terra di Siena bruciata"),
    "ombra_bruc": ("#4f3728", "terra d'ombra bruciata"),
    "seppia": ("#2e241f", "seppia / bruno scuro"),
    "acqua": ("#b8ddf5", "acqua pura"),
    "mascherante": ("#5bc0de", "fluido di mascheratura"),
    "nastro": ("#e2d9c5", "nastro di carta"),
    "sale": ("#d8d2c5", "cloruro di sodio (sale fino)"),
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
        "titolo": "Tavola sinottica: costruzione di punta o di fianco e stratificazione per piani",
        "fasi": [
            {
                "titolo": "Esemplare ravvicinato: asse e vertice a V",
                "carta": "asciutta",
                "colori": ["ombra_bruc", "verde_bosco"],
                "attrezzo": "Tondo n. 6 (di punta)",
                "testo": "Tracciare un asse direttore discontinuo, impostare l'apice con brevi tratti convergenti a V rivolti verso l'alto e discendere con tocchi minuti di punta.",
                "svg": svg_wrap(
                    '<line x1="110" y1="18" x2="110" y2="124" stroke="#7a5c43" stroke-width="1.5" stroke-dasharray="5,5"/>'
                    '<path d="M110,18 L105,11 M110,18 L115,11 M110,25 L103,18 M110,25 L117,18" stroke="#2b5b3c" stroke-width="2.2" stroke-linecap="round"/>'
                    '<path d="M110,33 L96,39 M110,35 L124,41 M110,44 L90,52 M110,46 L130,54 M110,56 L84,66 M110,58 L136,68 M110,70 L78,82 M110,72 L142,84" stroke="#2b5b3c" stroke-width="2.4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Media distanza: conduzione col fianco",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo n. 6 (di fianco)",
                "testo": "Discendere rapidamente dall'apice inclinando la ghiera e imprimendo col fianco della setola un andamento a zig-zag asimmetrico progressivamente più ampio.",
                "svg": svg_wrap(
                    '<line x1="110" y1="16" x2="110" y2="124" stroke="#7a5c43" stroke-width="1.4" stroke-dasharray="4,5"/>'
                    '<path d="M110,16 L106,10 M110,16 L114,10" stroke="#2b5b3c" stroke-width="2.2" stroke-linecap="round"/>'
                    '<path d="M108,24 L94,32 L122,40 L86,52 L130,62 L78,76 L138,88 L70,104 L146,114" fill="none" stroke="#2b5b3c" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>'
                ),
            },
            {
                "titolo": "Stratificazione: dal chiaro allo scuro",
                "carta": "asciutta",
                "colori": ["verde_chiaro", "verde_bosco", "seppia"],
                "attrezzo": "Tondo n. 6",
                "testo": "Stendere dapprima la schiera di fondo ad alta diluizione; a completa essiccazione sovrapporre i piani intermedi e gli esemplari scuri in primo piano.",
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
        "titolo": "Tavola sinottica: impostazione rapida del cono, sollevamento della luce e ombra propria",
        "fasi": [
            {
                "titolo": "Impostazione sintetica del cono",
                "carta": "asciutta",
                "colori": ["cobalto", "giallo_limone"],
                "attrezzo": "Tondo n. 12",
                "testo": "Tracciare l'asse centrale e definire in pochi secondi la massa conica in verde-azzurro, estraendo con la punta le espansioni laterali dei rami.",
                "svg": svg_wrap(
                    '<line x1="110" y1="14" x2="110" y2="122" stroke="#2f6f5e" stroke-width="2.5"/>'
                    '<path d="M110,14 L72,114 L148,114 Z" fill="#3b7a68" opacity="0.85"/>'
                    '<path d="M96,38 L82,42 M124,40 L138,44 M88,64 L72,70 M132,66 L148,72 M80,92 L62,98 M138,94 L156,100" stroke="#2f6f5e" stroke-width="3" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Asportazione della luce a sinistra (lifting)",
                "carta": "umida",
                "colori": ["acqua"],
                "attrezzo": "Pennello pulito e scaricato",
                "testo": "Con la campitura ancora umida, asciugare la setola su tessuto assorbente e rimuovere il pigmento lungo il fianco sinistro per restituire il volume illuminato.",
                "svg": svg_wrap(
                    '<circle cx="30" cy="26" r="10" fill="#f4d03f"/>'
                    '<path d="M110,14 L72,114 L148,114 Z" fill="#3b7a68" opacity="0.85"/>'
                    '<path d="M108,20 L76,108 L106,108 Z" fill="#dcebe4" opacity="0.78"/>'
                    '<path d="M62,56 L92,48" stroke="#85bce8" stroke-width="2" stroke-dasharray="3,3"/>'
                ),
            },
            {
                "titolo": "Ombra propria a destra e quinte lontane",
                "carta": "umida",
                "colori": ["indaco", "cobalto"],
                "attrezzo": "Tondo n. 12",
                "testo": "Introdurre per contatto una miscela profonda lungo il versante destro in ombra e completare lo sfondo con profili minori in grigio-azzurro diluito.",
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
        "titolo": "Tavola sinottica: fusione policroma in situ su supporto umido",
        "fasi": [
            {
                "titolo": "Impianto sciolto in turchese e ftalo",
                "carta": "asciutta",
                "colori": ["turchese_cob", "blu_ftalo"],
                "attrezzo": "Tondo in martora n. 7",
                "testo": "Impostare la cuspide e le fronde con pennellate centrifughe sciolte, alternando turchese di cobalto e blu ftalo.",
                "svg": svg_wrap(
                    '<path d="M110,14 L110,124" stroke="#1b4965" stroke-width="2"/>'
                    '<path d="M110,20 Q96,28 88,30 M110,24 Q124,32 132,34 M110,38 Q90,48 76,50 M110,42 Q128,52 142,54" stroke="#38a3a5" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
                    '<path d="M110,60 Q86,72 68,74 M110,64 Q134,76 150,78 M110,84 Q82,98 62,102 M110,88 Q138,102 156,106" stroke="#1b4965" stroke-width="5.5" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Innesto del verde oro a umido",
                "carta": "umida",
                "colori": ["verde_oro"],
                "attrezzo": "Tondo n. 7",
                "testo": "Finché i rami blu-verdi conservano l'umidità, depositare il verde oro lungo il versante illuminato lasciandolo espandere per capillarità.",
                "svg": svg_wrap(
                    '<path d="M110,14 L66,112 L154,112 Z" fill="#28666e" opacity="0.8"/>'
                    '<ellipse cx="94" cy="48" rx="16" ry="10" fill="#c5d63a" opacity="0.85"/>'
                    '<ellipse cx="86" cy="76" rx="20" ry="12" fill="#c5d63a" opacity="0.85"/>'
                    '<ellipse cx="118" cy="64" rx="14" ry="9" fill="#c5d63a" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Neutralizzazione sul fusto e sottorami",
                "carta": "umida",
                "colori": ["blu_ftalo", "cadmio_arancio"],
                "attrezzo": "Tondo n. 7",
                "testo": "Rafforzare l'intradosso dei rami con blu-verde denso e toccare l'asse del tronco con rosso/arancio di cadmio per generare bruni neutri in situ.",
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
        "titolo": "Tavola sinottica: inserimento discontinuo del fusto e dei rami entro i varchi",
        "fasi": [
            {
                "titolo": "Riserva dei varchi nella chioma",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo medio",
                "testo": "Nella stesura della massa fogliare risparmiare piccole aperture bianche irregolari tra i palchi, in particolare nel terzo medio e inferiore.",
                "svg": svg_wrap(
                    '<path d="M110,14 L64,108 L156,108 Z" fill="#2b5b3c"/>'
                    '<ellipse cx="108" cy="48" rx="9" ry="6" fill="#fcfaf4"/>'
                    '<ellipse cx="112" cy="76" rx="12" ry="7" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Tracciatura discontinua del fusto",
                "carta": "asciutta",
                "colori": ["siena_nat", "siena_bruc"],
                "attrezzo": "Tondo fine n. 2",
                "testo": "A chioma asciutta, definire il piede del tronco alla base e proseguire verso l'alto esclusivamente con brevi segmenti entro i varchi risparmiati.",
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
                "titolo": "Ombra propria del tronco e rami portanti",
                "carta": "asciutta",
                "colori": ["siena_bruc", "oltremare"],
                "attrezzo": "Tondo fine n. 2",
                "testo": "Scurire il margine destro dei segmenti di fusto con bruno neutro (Siena bruciata + Oltremare) e accennare brevi rami di raccordo.",
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
        "titolo": "Tavola sinottica: tamponatura preliminare dei palchi e raccordo a rigger",
        "fasi": [
            {
                "titolo": "Tamponatura dei palchi isolati",
                "carta": "umida",
                "colori": ["verde_bosco", "ombra_bruc"],
                "attrezzo": "Tondo medio",
                "testo": "Con miscela ad alta densità (miele) depositare per tamponatura masse orizzontali discontinue, progressivamente più ampie verso la base.",
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
                "titolo": "Conduzione del fusto e dei rami a rigger",
                "carta": "asciutta",
                "colori": ["ombra_bruc"],
                "attrezzo": "Rigger / liner sottile",
                "testo": "Ad asciugatura avvenuta, condurre il fusto dal basso verso l'alto rastremandolo fino al vertice e collegare lateralmente i singoli palchi.",
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
                "titolo": "Accenti d'ombra all'intradosso",
                "carta": "asciutta",
                "colori": ["verde_bosco", "indaco"],
                "attrezzo": "Tondo n. 6",
                "testo": "Rafforzare il valore scuro lungo il margine inferiore di ciascun ciuffo per conferire spessore plastico e ancorare il piede del fusto.",
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
        "titolo": "Tavola sinottica: impianto grafico su asciutto dal fusto ai rami singoli e agli aghi",
        "fasi": [
            {
                "titolo": "Tracciatura dell'asse del fusto",
                "carta": "asciutta",
                "colori": ["ombra_bruc", "verde_bosco"],
                "attrezzo": "Liner / tondo n. 0-1",
                "testo": "Su supporto asciutto condurre un tratto verticale capillare, mantenendo spoglio il terzo inferiore del fusto come nelle conifere d'alto fusto.",
                "svg": svg_wrap(
                    '<path d="M110,128 L110,14" stroke="#4f3728" stroke-width="2.4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Impostazione dei rami distanziati",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Liner / tondo n. 0-1",
                "testo": "Nella metà superiore tracciare linee singole ben spaziate, lievemente inflesse verso il basso e di estensione crescente.",
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
                "titolo": "Definizione degli aghi con tratti brevi",
                "carta": "asciutta",
                "colori": ["verde_bosco", "verde_chiaro"],
                "attrezzo": "Liner / tondo n. 0-1",
                "testo": "Rivestire ciascun ramo con brevi tocchi rapidi di punta, preservando ampie fasce di cielo libero tra un palco e il successivo.",
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
        "titolo": "Tavola sinottica: discesa rapida dalla cuspide per tocchi alternati a spinta",
        "fasi": [
            {
                "titolo": "Impostazione dell'apice sottile",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Piatto 3/8\" o tondo",
                "testo": "Iniziare dalla sommità con un tratto verticale minimo e discendere appoggiando lo spigolo della setola con brevi impronte disgiunte.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<path d="M110,14 L110,26 M106,28 L114,30 M100,38 L108,40 M112,42 L122,44" stroke="#2b5b3c" stroke-width="3.5" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Discesa cadenzata a spinta laterale",
                "carta": "asciutta",
                "colori": ["verde_bosco"],
                "attrezzo": "Piatto 3/8\" o tondo",
                "testo": "Appoggiare e spingere brevemente il pennello alternando sinistra e destra in modo asimmetrico, ampliando i palchi e risparmiando i varchi.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d8eaf7"/>'
                    '<g stroke="#2b5b3c" stroke-width="4.5" stroke-linecap="round">'
                    '<path d="M110,14 L110,24 M102,30 L118,32 M94,44 L110,46 M108,50 L128,53"/>'
                    '<path d="M84,64 L106,68 M112,70 L136,74 M76,86 L104,90 M110,92 L144,96 M70,108 L148,112"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Innesto a umido dell'ombra propria",
                "carta": "umida",
                "colori": ["oltremare", "ombra_bruc"],
                "attrezzo": "Piatto 3/8\" o tondo",
                "testo": "Finché il verde conserva l'umidità, introdurre lungo l'intradosso dei palchi una miscela neutra profonda (Oltremare + Terra d'ombra bruciata).",
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
        "titolo": "Tavola sinottica: conduzione circolare con la pancia del pennello dal centro al margine",
        "fasi": [
            {
                "titolo": "Impostazione centrale col ventre della setola",
                "carta": "asciutta",
                "colori": ["giallo_limone", "siena_nat"],
                "attrezzo": "Tondo grande n. 10",
                "testo": "Appoggiare la pancia del pennello ben carico al centro del lobo fogliare, evitando la picchiettatura verticale ripetitiva.",
                "svg": svg_wrap(
                    '<circle cx="110" cy="68" r="24" fill="#e59a28" opacity="0.88"/>'
                    '<path d="M98,68 A12,12 0 1,1 122,68" fill="none" stroke="#9e4726" stroke-width="2" stroke-dasharray="3,2"/>'
                ),
            },
            {
                "titolo": "Espansione rotatoria e margine frastagliato",
                "carta": "asciutta",
                "colori": ["siena_nat", "siena_bruc"],
                "attrezzo": "Tondo grande n. 10",
                "testo": "Condurre il pennello con moto circolare verso la periferia: lo scarico progressivo sulla grana genera spontaneamente un profilo frastagliato.",
                "svg": svg_wrap(
                    '<circle cx="84" cy="66" r="34" fill="#e59a28" opacity="0.85"/>'
                    '<circle cx="134" cy="64" r="36" fill="#d98224" opacity="0.85"/>'
                    '<circle cx="106" cy="58" r="5" fill="#fcfaf4"/>'
                    '<circle cx="122" cy="74" r="4" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Innesto del bruno d'ombra nei lobi inferiori",
                "carta": "umida",
                "colori": ["siena_bruc", "oltremare"],
                "attrezzo": "Tondo medio n. 6",
                "testo": "Sulla campitura ancora umida depositare lungo la fascia basale una miscela bruna profonda (Terra di Siena bruciata + Blu oltremare).",
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
        "titolo": "Tavola sinottica: fusione integrale bagnato su bagnato per immissione di gocce",
        "fasi": [
            {
                "titolo": "Stesura della base gialla ad alta umidità",
                "carta": "bagnata",
                "colori": ["giallo_limone"],
                "attrezzo": "Piatto medio o tondo",
                "testo": "Stendere una campitura lobata giallo-oro con abbondante veicolo acquoso, preservando sporadiche riserve bianche interne.",
                "svg": svg_wrap(
                    '<circle cx="86" cy="64" r="34" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="132" cy="62" r="36" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="108" cy="80" r="30" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="104" cy="56" r="5" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Immissione di arancio e Siena per gravità",
                "carta": "bagnata",
                "colori": ["cadmio_arancio", "siena_bruc"],
                "attrezzo": "Tondo medio",
                "testo": "Nel film ancora speculare lasciar cadere gocce di arancio e Terra di Siena bruciata nella fascia mediana, lasciandole diffondere senza spennellare.",
                "svg": svg_wrap(
                    '<circle cx="86" cy="64" r="34" fill="#ebd834" opacity="0.8"/>'
                    '<circle cx="132" cy="62" r="36" fill="#ebd834" opacity="0.8"/>'
                    '<ellipse cx="88" cy="70" rx="22" ry="16" fill="#e56b28" opacity="0.85"/>'
                    '<ellipse cx="132" cy="68" rx="24" ry="18" fill="#c4512d" opacity="0.85"/>'
                    '<circle cx="104" cy="56" r="5" fill="#fcfaf4"/>'
                ),
            },
            {
                "titolo": "Accento bruno-rosso basale e fusto in seppia",
                "carta": "umida",
                "colori": ["cremisi", "seppia"],
                "attrezzo": "Tondo fine n. 2",
                "testo": "Depositare per contatto il rosso profondo lungo il margine inferiore dei lobi e condurre al di sotto il fusto e i rami in seppia.",
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
        "titolo": "Tavola sinottica: testurizzazione con spugna marina e innesto degli scuri a pennello",
        "fasi": [
            {
                "titolo": "Tamponatura dell'arancio con spugna marina",
                "carta": "asciutta",
                "colori": ["cadmio_arancio"],
                "attrezzo": "Spugna marina naturale",
                "testo": "Inumidire e strizzare la spugna naturale, caricarla con arancio saturo e tamponare sul supporto per ottenere una trama alveolare ariosa.",
                "svg": svg_wrap(
                    '<g fill="#e58728" opacity="0.85">'
                    '<circle cx="78" cy="54" r="14"/><circle cx="98" cy="44" r="16"/><circle cx="124" cy="48" r="15"/>'
                    '<circle cx="68" cy="72" r="15"/><circle cx="94" cy="68" r="18"/><circle cx="122" cy="68" r="17"/><circle cx="144" cy="64" r="14"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Secondo passaggio a spugna in rosso medio",
                "carta": "umida",
                "colori": ["cremisi"],
                "attrezzo": "Spugna marina naturale",
                "testo": "Sull'arancio ancora umido tamponare con la spugna un rosso più profondo nella fascia inferiore e lungo il fianco destro in ombra.",
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
                "titolo": "Innesto a pennello dei massimi scuri (+15%)",
                "carta": "umida",
                "colori": ["ombra_bruc", "cremisi"],
                "attrezzo": "Tondo n. 12 + rigger n. 3",
                "testo": "Col tondo n. 12 immettere a umido i bruno-rossi ad alta densità (compensando lo schiarimento di essiccazione del 15%) e rifinire i margini.",
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
        "titolo": "Tavola sinottica: raccordo a umido tra chiome calde autunnali e quinte verdi",
        "fasi": [
            {
                "titolo": "Impostazione delle masse calde in Siena",
                "carta": "asciutta",
                "colori": ["siena_nat", "oltremare"],
                "attrezzo": "Tondo medio",
                "testo": "Stendere le chiome autunnali con Terra di Siena naturale temperata da una punta di Blu oltremare, orientando la luce da sinistra.",
                "svg": svg_wrap(
                    '<circle cx="68" cy="68" r="32" fill="#d48c2a" opacity="0.85"/>'
                    '<circle cx="104" cy="64" r="34" fill="#c97a26" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Accostamento a umido del verde profondo",
                "carta": "umida",
                "colori": ["verde_bosco", "oltremare"],
                "attrezzo": "Tondo medio",
                "testo": "Mentre il margine destro delle chiome calde è ancora umido, accostare il verde scuro (Siena + prevalenza di Oltremare) favorendone la fusione sul confine.",
                "svg": svg_wrap(
                    '<circle cx="68" cy="68" r="32" fill="#d48c2a" opacity="0.85"/>'
                    '<circle cx="104" cy="64" r="34" fill="#c97a26" opacity="0.85"/>'
                    '<circle cx="146" cy="66" r="34" fill="#2b5b3c" opacity="0.9"/>'
                    '<ellipse cx="124" cy="66" rx="12" ry="26" fill="#4d5e28" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Accenti di rosso inglese e frastagliatura",
                "carta": "umida",
                "colori": ["rosso_inglese", "verde_bosco"],
                "attrezzo": "Pennello sagomato / tondo",
                "testo": "Introdurre accenti di rosso inglese nella massa umida e articolare il perimetro esterno per preservare margini morbidi e frastagliati.",
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
        "titolo": "Tavola sinottica: incisione plastica dei rami nella campitura umida con tessera rigida",
        "fasi": [
            {
                "titolo": "Stesura della massa e messa in piano",
                "carta": "umida",
                "colori": ["siena_bruc", "indaco", "seppia"],
                "attrezzo": "Tondo grande",
                "testo": "Stendere i toni caldi e scuri della chioma e, stabilizzata la diffusione, riportare la tavola in posizione orizzontale per arrestare la colatura.",
                "svg": svg_wrap(
                    '<ellipse cx="110" cy="68" rx="68" ry="38" fill="#8c4a27" opacity="0.85"/>'
                    '<ellipse cx="122" cy="78" rx="52" ry="26" fill="#3b2d26" opacity="0.8"/>'
                ),
            },
            {
                "titolo": "Incisione rapida con lo spigolo della tessera",
                "carta": "umida",
                "colori": ["seppia"],
                "attrezzo": "Tessera polimerica rigida",
                "testo": "Impugnare una tessera rigida e trascinarne lo spigolo con tratti rapidi entro lo strato umido per generare la ramificazione interna.",
                "svg": svg_wrap(
                    '<ellipse cx="110" cy="68" rx="68" ry="38" fill="#8c4a27" opacity="0.85"/>'
                    '<ellipse cx="122" cy="78" rx="52" ry="26" fill="#3b2d26" opacity="0.8"/>'
                    '<polygon points="148,18 192,28 182,62 138,52" fill="#7ec8e3" stroke="#2b4c8c" stroke-width="1.5"/>'
                    '<path d="M84,96 L76,58 M112,98 L138,52" stroke="#fcfaf4" stroke-width="2" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Esito: solco scuro o riserva chiara",
                "carta": "umida",
                "colori": ["siena_bruc"],
                "attrezzo": "Tessera polimerica rigida",
                "testo": "Su film molto bagnato il solco drena il pigmento producendo rami scuri; nello stadio umido opaco asporta il colore aprendo fusti chiari.",
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
        "titolo": "Tavola sinottica: filare autunnale a umido con innesti di rosso inglese e base scura",
        "fasi": [
            {
                "titolo": "Impostazione in Giallo limone e Siena",
                "carta": "asciutta",
                "colori": ["giallo_limone", "siena_nat"],
                "attrezzo": "Tondo n. 6",
                "testo": "Con miscela calda di Giallo limone e Terra di Siena naturale (più concentrata rispetto al prato) impostare a tocchi la fascia della siepe.",
                "svg": svg_wrap(
                    '<rect x="24" y="52" width="172" height="36" rx="10" fill="#d98a26" opacity="0.88"/>'
                ),
            },
            {
                "titolo": "Innesti a umido di rosso inglese",
                "carta": "umida",
                "colori": ["rosso_inglese"],
                "attrezzo": "Tondo n. 6",
                "testo": "Finché la fascia della siepe conserva l'umidità, introdurre per contatto tocchi di rosso inglese per modulare la temperatura del fogliame.",
                "svg": svg_wrap(
                    '<rect x="24" y="52" width="172" height="36" rx="10" fill="#d98a26" opacity="0.88"/>'
                    '<ellipse cx="64" cy="68" rx="22" ry="11" fill="#b5482a" opacity="0.85"/>'
                    '<ellipse cx="128" cy="70" rx="26" ry="12" fill="#b5482a" opacity="0.85"/>'
                    '<ellipse cx="172" cy="66" rx="16" ry="10" fill="#b5482a" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Sottosquadro scuro lungo l'attacco a terra",
                "carta": "umida",
                "colori": ["ombra_bruc", "oltremare"],
                "attrezzo": "Tondo n. 6",
                "testo": "Depositare lungo il piede della siepe una miscela profonda di Terra d'ombra bruciata e Blu oltremare per ancorare la massa al suolo.",
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
        "titolo": "Tavola sinottica: fascia scura basale e sfumatura selettiva a tratti verso il prato",
        "fasi": [
            {
                "titolo": "Impostazione dei valori chiari e medi",
                "carta": "asciutta",
                "colori": ["verde_oliva", "verde_chiaro"],
                "attrezzo": "Tondo piccolo (di fianco)",
                "testo": "Costruire il profilo della siepe utilizzando il fianco del pennello, degradando dal tono chiaro superiore al tono medio centrale.",
                "svg": svg_wrap(
                    '<rect x="26" y="46" width="168" height="40" rx="10" fill="#7cb356" opacity="0.82"/>'
                    '<rect x="28" y="60" width="164" height="24" rx="6" fill="#5c8a3c" opacity="0.85"/>'
                ),
            },
            {
                "titolo": "Apposizione della fascia scura basale",
                "carta": "umida",
                "colori": ["verde_bosco", "ombra_bruc"],
                "attrezzo": "Tondo piccolo",
                "testo": "Depositare un tono denso e profondo lungo il margine inferiore della siepe per definire la cavità d'ombra al contatto col terreno.",
                "svg": svg_wrap(
                    '<rect x="26" y="46" width="168" height="40" rx="10" fill="#6b9e48" opacity="0.85"/>'
                    '<rect x="28" y="76" width="164" height="10" rx="4" fill="#1e3d28"/>'
                ),
            },
            {
                "titolo": "Sfumatura discontinua col pennello piatto umido",
                "carta": "umida",
                "colori": ["acqua"],
                "attrezzo": "Piatto medio-piccolo umido",
                "testo": "Mentre la fascia scura è ancora mobile, interromperla in 2-3 punti tirando il pigmento verso il prato con un pennello piatto pulito e umido.",
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
        "titolo": "Tavola sinottica: modellazione volumetrica del cespuglio a cupola per strati",
        "fasi": [
            {
                "titolo": "Prima campitura luminosa sulla calotta",
                "carta": "asciutta",
                "colori": ["giallo_limone", "oltremare"],
                "attrezzo": "Tondo n. 4-6",
                "testo": "Impostare la geometria emisferica partendo dal giallo-verde luminoso nella porzione superiore direttamente esposta alla luce.",
                "svg": svg_wrap(
                    '<path d="M52,104 Q110,20 168,104 Z" fill="#a8c948" opacity="0.88"/>'
                ),
            },
            {
                "titolo": "Sovrapposizione dei verdi medi",
                "carta": "umida",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo n. 4-6",
                "testo": "Introdurre nella fascia centrale e inferiore un verde medio più ricco di Blu oltremare, risparmiando i margini superiori chiari.",
                "svg": svg_wrap(
                    '<path d="M52,104 Q110,20 168,104 Z" fill="#a8c948" opacity="0.88"/>'
                    '<path d="M56,104 Q110,44 164,104 Z" fill="#4e8742" opacity="0.9"/>'
                ),
            },
            {
                "titolo": "Massimi scuri neutralizzati col rosso",
                "carta": "umida",
                "colori": ["verde_bosco", "cremisi"],
                "attrezzo": "Tondo fine n. 2",
                "testo": "Definire il piede e gli incavi interni con un verde profondo neutralizzato da una punta di rosso, articolando finemente il perimetro.",
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
        "titolo": "Tavola sinottica: isolamento di chiome luminose mediante fondo scuro in negativo",
        "fasi": [
            {
                "titolo": "Stesura preliminare delle masse chiare",
                "carta": "asciutta",
                "colori": ["giallo_limone", "cadmio_arancio"],
                "attrezzo": "Calligrafico / tondo medio",
                "testo": "Stendere liberamente le campiture luminose (giallo limone, ocra e arancio) dei cespugli in primo piano e attenderne la completa essiccazione.",
                "svg": svg_wrap(
                    '<circle cx="78" cy="76" r="28" fill="#ebd834" opacity="0.88"/>'
                    '<circle cx="132" cy="72" r="32" fill="#e59a28" opacity="0.88"/>'
                ),
            },
            {
                "titolo": "Profilatura esterna in negativo",
                "carta": "asciutta",
                "colori": ["oltremare", "verde_bosco", "indaco"],
                "attrezzo": "Calligrafico a punta tonda",
                "testo": "Con una miscela profonda dipingere la quinta retrostante profilando dall'esterno il margine frastagliato delle chiome chiare asciutte.",
                "svg": svg_wrap(
                    '<rect x="18" y="18" width="95" height="90" rx="6" fill="#1f3b34"/>'
                    '<circle cx="78" cy="76" r="28" fill="#ebd834"/>'
                    '<circle cx="132" cy="72" r="32" fill="#e59a28"/>'
                ),
            },
            {
                "titolo": "Chiusura del fondo e ramificazioni basali",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Tondo fine",
                "testo": "Completare la campitura scura circostante per far emergere il cespuglio per contrasto simultaneo e inserire sottili fusti alla base.",
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
        "titolo": "Tavola sinottica: velatura sintetica sul prato e ombra portata fredda alla base",
        "fasi": [
            {
                "titolo": "Velatura trasparente sul piano erboso",
                "carta": "asciutta",
                "colori": ["giallo_limone", "prussia"],
                "attrezzo": "Tondo grande",
                "testo": "Impostare il prato antistante alle siepi con un lavaggio unico ad alta diluizione, privo di dettagli grafici che disperdano l'attenzione.",
                "svg": svg_wrap(
                    '<rect x="24" y="34" width="172" height="36" rx="8" fill="#6b8238"/>'
                    '<rect x="14" y="70" width="192" height="54" rx="4" fill="#d8e6b8" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Innesto a umido dell'ombra portata fredda",
                "carta": "umida",
                "colori": ["oltremare", "lilla"],
                "attrezzo": "Tondo medio",
                "testo": "Mentre la velatura del prato è ancora umida, depositare immediatamente al piede della siepe una fascia orizzontale di Blu oltremare o grigio-malva.",
                "svg": svg_wrap(
                    '<rect x="24" y="34" width="172" height="36" rx="8" fill="#6b8238"/>'
                    '<rect x="14" y="70" width="192" height="54" rx="4" fill="#d8e6b8" opacity="0.75"/>'
                    '<rect x="20" y="70" width="180" height="12" rx="4" fill="#5b6d99" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Fusione spontanea e accenno del sentiero",
                "carta": "umida",
                "colori": ["ombra_bruc"],
                "attrezzo": "Tondo medio",
                "testo": "Lasciare che l'ombra fredda si espanda morbidamente nel velo umido del prato e aggiungere soltanto una traccia sobria per il sentiero.",
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
        "titolo": "Tavola sinottica: riserva dei fusti col tiralinee, rimozione a secco e modellazione cilindrica",
        "fasi": [
            {
                "titolo": "Tracciatura dei fusti col tiralinee",
                "carta": "asciutta",
                "colori": ["mascherante"],
                "attrezzo": "Tiralinee (ruling pen)",
                "testo": "Su supporto asciutto caricare il tiralinee con fluido di mascheratura e tracciare fusti capillari biforcati a Y; attendere la completa polimerizzazione.",
                "svg": svg_wrap(
                    '<path d="M76,128 L80,22 M78,68 L96,34 M142,128 L138,26 M140,72 L122,40" stroke="#5bc0de" stroke-width="3.2" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Asportazione a secco con gomma crêpe",
                "carta": "asciutta",
                "colori": ["lilla", "oltremare"],
                "attrezzo": "Gomma crêpe",
                "testo": "Solo a completa essiccazione delle lavature di sfondo, frizionare delicatamente con la gomma crêpe per scoprire le riserve bianche.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="112" rx="6" fill="#6c6486" opacity="0.75"/>'
                    '<path d="M76,128 L80,22 M78,68 L96,34" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                    '<path d="M142,128 L138,26 M140,72 L122,40" stroke="#5bc0de" stroke-width="3.5" stroke-linecap="round"/>'
                    '<rect x="124" y="56" width="32" height="20" rx="4" fill="#e6cfa3" stroke="#8c734b" stroke-width="1.5"/>'
                ),
            },
            {
                "titolo": "Ombra propria unilaterale sul fusto",
                "carta": "asciutta",
                "colori": ["lilla", "cobalto"],
                "attrezzo": "Tondo n. 8 scarico d'acqua",
                "testo": "Scaricare il pennello su tessuto assorbente e condurre un filetto grigio-azzurro lungo un solo margine del fusto bianco per restituirne la rotondità.",
                "svg": svg_wrap(
                    '<rect x="14" y="14" width="192" height="112" rx="6" fill="#6c6486" opacity="0.75"/>'
                    '<path d="M76,128 L80,22 M78,68 L96,34 M142,128 L138,26 M140,72 L122,40" stroke="#fcfaf4" stroke-width="4.5" stroke-linecap="round"/>'
                    '<path d="M78,128 L82,22 M144,128 L140,26" stroke="#3a4466" stroke-width="1.6" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A5-M2": {
        "titolo": "Tavola sinottica: schermatura dei tronchi con nastro di carta e velature sul bagnato",
        "fasi": [
            {
                "titolo": "Applicazione dei listelli di nastro",
                "carta": "asciutta",
                "colori": ["nastro"],
                "attrezzo": "Nastro di carta",
                "testo": "Sezionare o strappare listelli sottili di nastro di carta e farli aderire saldamente al supporto asciutto per schermare i fusti rettilinei.",
                "svg": svg_wrap(
                    '<rect x="64" y="16" width="10" height="110" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                    '<rect x="106" y="14" width="12" height="112" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                    '<rect x="150" y="20" width="9" height="106" fill="#e2d9c5" stroke="#b5a88c" stroke-width="1"/>'
                ),
            },
            {
                "titolo": "Velature calde su supporto bagnato",
                "carta": "bagnata",
                "colori": ["giallo_limone", "verde_oro", "verde_oliva"],
                "attrezzo": "Tondo grande n. 14",
                "testo": "Inumidire il foglio passando sopra il nastro e stendere bagnato su bagnato le velature di giallo, oro chinacridone e verde vescica.",
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
                "titolo": "Toni freddi basali e rimozione del nastro",
                "carta": "bagnata",
                "colori": ["lilla", "turchese_cob", "siena_bruc"],
                "attrezzo": "Tondo n. 14 + tondo n. 2",
                "testo": "Introdurre i toni blu-viola, turchesi e ruggine nella fascia inferiore lasciandoli fondere sopra le schermature; a carta asciutta rimuovere il nastro.",
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
        "titolo": "Tavola sinottica: induzione della trama cristallina di brina mediante cloruro di sodio",
        "fasi": [
            {
                "titolo": "Stesura della campitura atmosferica fredda",
                "carta": "bagnata",
                "colori": ["indaco", "ombra_bruc"],
                "attrezzo": "Pennellessa piatta (hake)",
                "testo": "Stendere una lavatura omogenea con grigio di Payne, indaco e una frazione di Terra d'ombra bruciata per il fondo invernale delle chiome.",
                "svg": svg_wrap(
                    '<rect x="16" y="16" width="188" height="108" rx="8" fill="#5c687c" opacity="0.75"/>'
                ),
            },
            {
                "titolo": "Applicazione del sale nello stadio umido opaco",
                "carta": "umida",
                "colori": ["sale"],
                "attrezzo": "Cloruro di sodio a grana fine",
                "testo": "Non applicare il sale sul velo liquido speculare: attendere che la superficie diventi umida opaca, quindi distribuire pochi cristalli distanziati.",
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
                "titolo": "Formazione dei cristalli e rimozione a secco",
                "carta": "asciutta",
                "colori": ["indaco"],
                "attrezzo": "Rimozione meccanica a secco",
                "testo": "Lasciare agire per igroscopia fino a completa essiccazione; rimuovere i grani residui esclusivamente a supporto perfettamente asciutto.",
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
        "titolo": "Tavola sinottica: definizione dei rami per campitura scura in negativo sfumata all'esterno",
        "fasi": [
            {
                "titolo": "Campitura in negativo negli interstizi",
                "carta": "asciutta",
                "colori": ["verde_bosco", "oltremare", "indaco"],
                "attrezzo": "Tondo n. 6 a punta",
                "testo": "Con una miscela profonda e fredda riempire gli spazi interstiziali attorno ai fusti e ai rami per isolarli in bianco per contrasto.",
                "svg": svg_wrap(
                    '<path d="M56,118 Q62,64 110,64 Q158,64 164,118 Z" fill="#1d3d3d"/>'
                    '<path d="M88,124 L90,34 M89,76 L72,50 M130,124 L128,38 M129,78 L146,52" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Sfumatura del perimetro esterno con acqua",
                "carta": "umida",
                "colori": ["acqua"],
                "attrezzo": "Tondo pulito con acqua pura",
                "testo": "Prima che il contorno esterno della campitura scura secchi, sfiorarlo con un pennello carico d'acqua pura per avviarne la dissolvenza.",
                "svg": svg_wrap(
                    '<path d="M48,72 Q110,42 172,72" stroke="#85bce8" stroke-width="8" fill="none" stroke-linecap="round" opacity="0.65"/>'
                    '<path d="M56,118 Q62,64 110,64 Q158,64 164,118 Z" fill="#1d3d3d"/>'
                    '<path d="M88,124 L90,34 M89,76 L72,50 M130,124 L128,38 M129,78 L146,52" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Dissolvenza esterna e margine interno netto",
                "carta": "umida",
                "colori": ["verde_bosco"],
                "attrezzo": "Tondo fine n. 2-4",
                "testo": "Il pigmento si espande nell'acqua creando una transizione atmosferica verso l'alto, mentre il contatto contro i fusti bianchi rimane nitido.",
                "svg": svg_wrap(
                    '<path d="M42,118 Q54,40 110,44 Q166,40 178,118 Z" fill="#5c8a7e" opacity="0.45"/>'
                    '<path d="M56,118 Q62,68 110,68 Q158,68 164,118 Z" fill="#1d3d3d" opacity="0.9"/>'
                    '<path d="M88,124 L90,34 M89,76 L72,50 M130,124 L128,38 M129,78 L146,52" stroke="#fcfaf4" stroke-width="4" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A5-M5": {
        "titolo": "Tavola sinottica: tessitura di ramificazioni spoglie periferiche col pennello a ventaglio",
        "fasi": [
            {
                "titolo": "Separazione a pettine delle setole",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Pennello a ventaglio piccolo",
                "testo": "Caricare il pennello a ventaglio con seppia denso e scaricare l'eccesso idrico affinché le setole si dispongano in ciuffi separati a pettine.",
                "svg": svg_wrap(
                    '<path d="M110,96 L82,58 M110,96 L94,52 M110,96 L110,48 M110,96 L126,52 M110,96 L138,58" stroke="#2e241f" stroke-width="2" stroke-linecap="round"/>'
                    '<rect x="105" y="96" width="10" height="26" rx="2" fill="#8c6239"/>'
                ),
            },
            {
                "titolo": "Sfioramento ad arco per la chioma spoglia",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Pennello a ventaglio piccolo",
                "testo": "Sfiorare il supporto asciutto con rapidi movimenti ad arco incrociati per generare la trama leggera dei rametti terminali.",
                "svg": svg_wrap(
                    '<g stroke="#2e241f" stroke-width="1.2" stroke-dasharray="3,2" fill="none">'
                    '<path d="M48,68 Q78,34 112,52"/><path d="M54,74 Q82,42 116,58"/>'
                    '<path d="M98,56 Q132,30 168,62"/><path d="M104,62 Q136,38 172,68"/>'
                    '<path d="M68,48 Q108,22 148,46"/>'
                    '</g>'
                ),
            },
            {
                "titolo": "Raccordo strutturale dal basso col rigger",
                "carta": "asciutta",
                "colori": ["seppia"],
                "attrezzo": "Rigger sottile",
                "testo": "Con il rigger condurre dal basso il fusto e i rami portanti, innestandoli all'interno della tessitura fine tracciata dal ventaglio.",
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
        "titolo": "Tavola sinottica: conduzione ascendente e sovrapposizione naturale dei tralci sottili",
        "fasi": [
            {
                "titolo": "Conduzione dal basso dei fusti principali",
                "carta": "asciutta",
                "colori": ["ombra_bruc", "seppia"],
                "attrezzo": "Tondo a punta fine n. 6 o rigger",
                "testo": "Appoggiare il pennello alla base e tirare i fusti verso l'alto, riducendo progressivamente la pressione per rastremare la linea.",
                "svg": svg_wrap(
                    '<path d="M58,128 Q78,78 96,24 M136,128 Q124,78 142,26" stroke="#4f3728" stroke-width="3" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Impostazione delle biforcazioni a V e Y",
                "carta": "asciutta",
                "colori": ["ombra_bruc"],
                "attrezzo": "Tondo a punta fine n. 6",
                "testo": "Innesto dei rami secondari ad angolo acuto (a V e a Y), differenziando l'inclinazione e il calibro a ogni nodo.",
                "svg": svg_wrap(
                    '<path d="M58,128 Q78,78 96,24 M136,128 Q124,78 142,26" stroke="#4f3728" stroke-width="3" fill="none" stroke-linecap="round"/>'
                    '<path d="M76,82 L54,42 M86,56 L112,28 M130,84 L110,44 M134,58 L162,32" stroke="#4f3728" stroke-width="2" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Intersezioni spaziali e apici capillari",
                "carta": "asciutta",
                "colori": ["ombra_bruc"],
                "attrezzo": "Estrema punta della setola",
                "testo": "Aggiungere tralci centrali che intersecano e sovrappongono i rami adiacenti, assottigliando i tratti terminali a spessore capillare.",
                "svg": svg_wrap(
                    '<path d="M58,128 Q78,78 96,24 M136,128 Q124,78 142,26" stroke="#4f3728" stroke-width="3" fill="none" stroke-linecap="round"/>'
                    '<path d="M76,82 L54,42 M86,56 L112,28 M130,84 L110,44 M134,58 L162,32" stroke="#4f3728" stroke-width="2" fill="none" stroke-linecap="round"/>'
                    '<path d="M98,128 Q106,76 74,30 M102,88 L148,40 M66,64 L122,48" stroke="#2e241f" stroke-width="1.5" fill="none" stroke-linecap="round"/>'
                ),
            },
        ],
    },
    "A6-M2": {
        "titolo": "Tavola sinottica: foglie scure con riserva capillare di brina e sfumatura a secco",
        "fasi": [
            {
                "titolo": "Riserva capillare del filetto bianco",
                "carta": "asciutta",
                "colori": ["siena_bruc", "prussia", "mascherante"],
                "attrezzo": "Tondo n. 4 (o tiralinee)",
                "testo": "Dipingere la lamina fogliare lobo per lobo risparmiando a mano libera un filetto bianco sub-millimetrico (oppure proteggerlo prima col tiralinee).",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d9ecfa"/>'
                    '<path d="M44,116 Q98,74 166,34" stroke="#2e241f" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                    '<path d="M64,78 Q88,56 116,68 Q92,88 64,78 Z" fill="#4a2c24"/>'
                    '<path d="M112,52 Q136,32 162,44 Q140,64 112,52 Z" fill="#4a2c24"/>'
                    '<path d="M66,76 Q88,58 114,68 M114,50 Q136,34 160,44" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Innesto a umido del Blu di Prussia",
                "carta": "umida",
                "colori": ["prussia", "cremisi"],
                "attrezzo": "Tondo a punta n. 4",
                "testo": "Finché il lobo fogliare è umido, depositare al centro e alla base Blu di Prussia ad alta densità per massimizzare il contrasto senza invadere la riserva.",
                "svg": svg_wrap(
                    '<rect x="6" y="6" width="208" height="128" rx="4" fill="#d9ecfa"/>'
                    '<path d="M44,116 Q98,74 166,34" stroke="#2e241f" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                    '<path d="M64,78 Q88,56 116,68 Q92,88 64,78 Z" fill="#1b365d"/>'
                    '<path d="M112,52 Q136,32 162,44 Q140,64 112,52 Z" fill="#1b365d"/>'
                    '<path d="M66,76 Q88,58 114,68 M114,50 Q136,34 160,44" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
                ),
            },
            {
                "titolo": "Attenuazione a secco con pennello umido",
                "carta": "asciutta",
                "colori": ["acqua"],
                "attrezzo": "Tondo pulito lievemente umido",
                "testo": "A foglia asciutta (e rimosso l'eventuale mascherante), sfiorare i filetti bianchi con un pennello pulito e appena umido per fondere la brina nella lamina.",
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
        coda.append(f'<div class="info-check ok"><b>✓ Criteri di verifica sul campione:</b> {e(t["controllo"])}</div>')
    if t.get("attenzione"):
        att = " · ".join(e(x) for x in t["attenzione"])
        coda.append(f'<div class="info-check att"><b>⚠ Errori ricorrenti da prevenire:</b> {att}</div>')
    if not coda:
        return ""
    return f'<div class="info-coda">{"".join(coda)}</div>'

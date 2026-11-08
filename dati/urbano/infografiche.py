"""Schemi vettoriali autonomi per gli esercizi di paesaggio urbano, non fotogrammi."""
from html import escape


def pol(punti, colore, stroke="none", width=1):
    return f'<polygon points="{punti}" fill="{colore}" stroke="{stroke}" stroke-width="{width}"/>'


def linea(x1, y1, x2, y2, colore="#56616a", width=1):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colore}" stroke-width="{width}"/>'


def rect(x, y, w, h, colore, stroke="none"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{colore}" stroke="{stroke}"/>'


def disegna(schema, fase, ident, titolo):
    if schema not in {"vicolo", "case", "strada", "veduta"} or fase not in {1, 2, 3}:
        raise ValueError("Schema o fase non validi")
    b = [rect(0, 0, 240, 210, "#fffdf7")]
    bordo = "#687a88"
    if schema == "vicolo":
        b += [pol("0,0 96,46 96,120 0,210", "#d8e6ee" if fase > 1 else "#fffdf7", bordo),
              pol("240,0 146,46 146,120 240,210", "#b8cfe0" if fase > 1 else "#fffdf7", bordo),
              pol("0,210 96,120 146,120 240,210", "#d7e1eb" if fase > 1 else "#fffdf7", bordo),
              rect(98, 68, 46, 48, "#fffdf7", bordo)]
        for x1, x2, y in [(95,147,124), (88,154,134), (75,168,149), (56,190,171), (29,217,199)]:
            if fase == 3:
                b.append(pol(f"{x1},{y} {x2},{y} {x2+3},{y+5} {x1-3},{y+5}", "#496b9d"))
            b.append(linea(x1,y,x2,y,bordo,1.3))
        if fase == 3:
            b += [pol("174,56 213,26 213,141 174,117", "#3d5480"),
                  pol("27,46 53,63 53,126 27,144", "#6d90b8"),
                  rect(111,88,17,28,"#526884"),
                  pol("14,177 33,177 30,195 18,195","#ad754b"),
                  pol("191,142 205,142 203,156 194,156","#929b60")]
            b += [linea(24,178,19,162,"#3e6a51",3),linea(199,145,205,131,"#3e6a51",3)]
    elif schema == "case":
        b += [pol("0,210 0,113 102,85 132,118 172,123 240,178 240,210", "#d8dfdf" if fase > 1 else "#fffdf7", bordo),
              pol("138,0 240,0 240,178 172,123 132,118", "#d8b893" if fase > 1 else "#fffdf7", bordo),
              pol("0,0 138,0 132,118 102,85 0,113", "#b9cfdd" if fase > 1 else "#fffdf7", bordo),
              pol("0,126 101,96 123,129 166,135 240,194 240,205 158,153 112,145 94,113 0,146", "#fffdf7", bordo)]
        if fase == 3:
            b += [pol("0,210 0,153 91,123 111,153 154,160 216,210", "#4b5065"),
                  pol("157,20 177,31 177,92 157,83", "#5c5665"),
                  pol("198,59 215,69 215,133 198,122", "#5c5665")]
            for x,y in [(110,118),(124,133),(168,145)]:
                b += [linea(x,y,x,y+7,"#3b4351",2),f'<circle cx="{x}" cy="{y-2}" r="2" fill="#3b4351"/>']
    elif schema == "strada":
        b += [rect(0,0,240,90,"#e8e7e1"),pol("0,210 100,91 143,91 240,210","#eeebe0"),
              pol("0,30 79,48 103,91 0,151", "#4b596d" if fase > 1 else "#d7d9d7"),
              pol("240,13 164,38 140,91 240,155", "#667485" if fase > 1 else "#d7d9d7")]
        for x,y,ww,hh in [(104,80,17,26),(65,118,25,16),(145,107,21,14)]:
            b += [rect(x,y,ww,hh,"#fffdf7",bordo)]
            if fase > 1:
                b += [rect(x,y+hh-4,ww,4,"#394b5d")]
        if fase == 3:
            for x,y,ww,hh in [(68,139,18,55),(147,124,13,48),(108,109,10,52)]:
                b.append(pol(f"{x},{y} {x+ww},{y} {x+ww+4},{y+hh} {x-3},{y+hh}","#bac6d1"))
            b += [linea(30,209,102,104,"#fffdf7",3),linea(205,209,144,102,"#fffdf7",3)]
    else:
        b += [rect(0,0,240,116,"#d9e7ed"),rect(0,116,240,94,"#d5e4e7"),
              pol("8,120 8,80 40,80 40,63 66,63 66,90 108,90 108,76 138,76 138,93 181,93 181,82 225,82 225,120", "#ead9b4")]
        if fase > 1:
            for x,y,ww,hh in [(10,81,28,39),(44,65,21,55),(71,92,34,28),(112,78,25,42),(144,95,34,25),(185,85,38,35)]:
                b += [rect(x,y,ww,hh,"#d8bb96",bordo),rect(x+ww-7,y,7,hh,"#a9a6a3")]
            b += [rect(89,40,10,80,"#b3a99a"),pol("86,40 94,23 102,40","#778390")]
        if fase == 3:
            for x,y in [(20,94),(49,86),(76,101),(120,90),(151,105),(194,97),(210,97)]:
                b.append(rect(x,y,4,6,"#5c6269"))
            b += [pol("33,164 90,164 81,176 44,176","#a56255"),pol("36,164 48,156 81,156 89,164","#fffdf7",bordo),
                  linea(21,186,108,186,"#829ba9",2),linea(130,146,192,146,"#829ba9",2),linea(167,171,224,171,"#829ba9",2)]
    did = escape(ident + "-disegno")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 210" role="img" aria-labelledby="{did}">'
            f'<title id="{did}">{escape(titolo)}. Schema della prova proposta, fase {fase}.</title>' + "".join(b) + '</svg>')

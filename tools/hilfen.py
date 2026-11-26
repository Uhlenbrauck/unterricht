#!/usr/bin/env python3
"""Erzeugt Hilfekarten-Seiten und QR-Codes aus den Quellen in hilfen/.

Jede Quelldatei hilfen/*.md enthält oben gemeinsame Angaben und darunter
beliebig viele Karten. Jede Karte wird eine eigene Seite h/<kennung>/
mit eigenem QR-Code in qr/<kennung>.png und .svg.

Aufbau einer Quelldatei:

    ---
    fach: Chemie
    klasse: 7
    ab: AB 06
    thema: Aggregatzustände im Teilchenmodell
    ---

    # c7-agg-1b-1
    aufgabe: 1b
    art: Hilfekarte 1

    Text der Karte in Markdown. Formeln: $x^2$ oder $$...$$,
    Reaktionsgleichungen: $\\ce{H2O + HCl -> H3O+ + Cl-}$.
    Bilder liegen in hilfen/bilder/ und werden als ![](bilder/name.png) eingebunden.

art ist "Hilfekarte <n>", "Lösung" oder "Info".

Aufruf:  python3 tools/hilfen.py
Benötigt: pip install markdown segno pillow

QR-Codes bekommen in der Mitte ein Etikett (Aufgabe, Kartennummer).
Vorhandene QR-Codes werden nie überschrieben, weil sie schon gedruckt sein können.
"""

import html
import re
import shutil
from pathlib import Path

import markdown
import segno

# Adresse, unter der GitHub Pages das Repo ausliefert
BASIS = "https://uhlenbrauck.github.io/unterricht"

ROOT = Path(__file__).resolve().parent.parent
QUELLEN = ROOT / "hilfen"
ZIEL = ROOT / "h"
QR = ROOT / "qr"

KATEX = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/mhchem.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {delimiters: [
    {left: '$$', right: '$$', display: true},
    {left: '$', right: '$', display: false}]})"></script>"""

SEITE = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex">
<title>{titel}</title>
<link rel="stylesheet" href="../../assets/hilfe.css">{katex}
</head>
<body>
<main class="karte{klasse}">
  <div class="kopf">
    <span>{herkunft}</span>
    <span class="art">{art}</span>
  </div>
  <div class="inhalt">
{inhalt}
  </div>
</main>
</body>
</html>
"""


def lies_quelle(pfad):
    text = pfad.read_text(encoding="utf-8")
    kopf, rumpf = {}, text
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        kopf = dict(z.split(":", 1) for z in m.group(1).splitlines() if ":" in z)
        kopf = {k.strip(): v.strip() for k, v in kopf.items()}
        rumpf = text[m.end():]

    karten = []
    for block in re.split(r"^# ", rumpf, flags=re.M)[1:]:
        zeilen = block.splitlines()
        karte = {"kennung": zeilen[0].strip()}
        i = 1
        while i < len(zeilen) and re.match(r"^\w+:", zeilen[i]):
            k, v = zeilen[i].split(":", 1)
            karte[k.strip()] = v.strip()
            i += 1
        karte["text"] = "\n".join(zeilen[i:]).strip()
        karten.append(karte)
    return kopf, karten


def markdown_mit_formeln(text):
    """Formeln vor Markdown schützen, damit _ und \\ erhalten bleiben."""
    formeln = []

    def merke(m):
        formeln.append(m.group(0))
        return f"\x00{len(formeln) - 1}\x00"

    geschuetzt = re.sub(r"\$\$.+?\$\$|\$[^$\n]+?\$", merke, text, flags=re.S)
    ergebnis = markdown.markdown(geschuetzt, extensions=["tables", "md_in_html", "attr_list"])
    ergebnis = re.sub(r"\x00(\d+)\x00", lambda m: html.escape(formeln[int(m.group(1))], quote=False), ergebnis)
    return ergebnis, bool(formeln) or "\\ce{" in text


def art_html(art):
    m = re.match(r"(.*?)\s*(\d+)$", art)
    if m:
        return f'{html.escape(m.group(1).upper())} <span class="nr">{m.group(2)}</span>'
    return html.escape(art.upper())


SCHRIFTEN = [  # fett, serifenlos; die erste vorhandene wird benutzt
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",        # macOS
    "C:/Windows/Fonts/arialbd.ttf",                              # Windows
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",      # Linux
]
BLAU, BLAU_TEXT = "#9dc3e6", "#1f3f63"       # wie das Nummernkästchen der Karten
GRUEN, GRUEN_TEXT = "#e8f0eb", "#2d5a3d"     # wie Lösungskarten


def etikett(aufgabe, art):
    """Beschriftung für die Mitte des QR-Codes: oben z. B. A1c, darunter Kästchen."""
    # Aufgabennummern (1c) bekommen ein A davor, Gruppenbuchstaben (A, B, C) nicht
    oben = (f"A{aufgabe}" if aufgabe[:1].isdigit() else aufgabe) if aufgabe else ""
    m = re.search(r"(\d+)$", art)
    if m:
        return oben, m.group(1), BLAU, BLAU_TEXT
    if art.lower().startswith("lösung"):
        return oben, "L", GRUEN, GRUEN_TEXT
    return oben, "i", BLAU, BLAU_TEXT


def schreibe_qr(url, kennung, aufgabe, art, scale=10, rand=2):
    """QR-Code als PNG und SVG, mit Etikett (Aufgabe, Kartennummer) in der Mitte.

    Fehlerkorrektur H verkraftet bis zu 30 % verdeckte Fläche; das Etikett
    belegt mit 30 % der Seitenlänge rund 9 %.
    """
    import io
    from PIL import Image, ImageDraw, ImageFont

    code = segno.make(url, error="h")
    module = code.symbol_size(scale=1, border=0)[0]
    seite = int(module * 0.30) * scale
    oben, nr, farbe, farbe_text = etikett(aufgabe, art)

    breite = (module + 2 * rand) * scale
    x0 = (breite - seite) / 2
    pad = scale / 2
    # Lage der Elemente relativ zum Etikett
    y_oben = x0 + seite * 0.25
    kw, kh = seite * 0.62, seite * 0.44
    kx = (breite - kw) / 2
    ky = x0 + (seite * 0.50 if oben else (seite - kh) / 2)

    schrift = next((s for s in SCHRIFTEN if Path(s).exists()), None)

    def font(groesse, text, max_breite):
        if schrift is None:
            return ImageFont.load_default(groesse)
        f = ImageFont.truetype(schrift, groesse)
        while groesse > 8 and f.getlength(text) > max_breite:
            groesse -= 1
            f = ImageFont.truetype(schrift, groesse)
        return f

    # PNG
    buf = io.BytesIO()
    code.save(buf, kind="png", scale=scale, border=rand)
    buf.seek(0)
    bild = Image.open(buf).convert("RGB")
    d = ImageDraw.Draw(bild)
    d.rounded_rectangle([x0 - pad, x0 - pad, x0 + seite + pad, x0 + seite + pad],
                        radius=scale, fill="white")
    if oben:
        d.text((breite / 2, y_oben), oben, fill="black", anchor="mm",
               font=font(int(seite * 0.30), oben, seite * 0.9))
    d.rectangle([kx, ky, kx + kw, ky + kh], fill=farbe)
    d.text((breite / 2, ky + kh / 2), nr, fill=farbe_text, anchor="mm",
           font=font(int(seite * 0.36), nr, kw * 0.9))
    bild.save(QR / f"{kennung}.png")

    # SVG
    buf = io.BytesIO()
    code.save(buf, kind="svg", scale=scale, border=rand, light="#fff")
    svg = buf.getvalue().decode("utf-8")
    schrift_svg = 'font-family="Arial, Helvetica, sans-serif" font-weight="bold" text-anchor="middle" dominant-baseline="central"'
    zusatz = (f'<rect x="{x0 - pad}" y="{x0 - pad}" width="{seite + 2 * pad}" height="{seite + 2 * pad}" '
              f'rx="{scale}" fill="#fff"/>')
    if oben:
        zusatz += (f'<text x="{breite / 2}" y="{y_oben}" font-size="{seite * 0.30}" '
                   f'textLength="{seite * 0.9}" lengthAdjust="spacingAndGlyphs" {schrift_svg}>'
                   f'{html.escape(oben)}</text>' if len(oben) > 3 else
                   f'<text x="{breite / 2}" y="{y_oben}" font-size="{seite * 0.30}" {schrift_svg}>'
                   f'{html.escape(oben)}</text>')
    zusatz += (f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" fill="{farbe}"/>'
               f'<text x="{breite / 2}" y="{ky + kh / 2}" font-size="{seite * 0.36}" fill="{farbe_text}" '
               f'{schrift_svg}>{html.escape(nr)}</text>')
    (QR / f"{kennung}.svg").write_text(svg.replace("</svg>", zusatz + "</svg>"), encoding="utf-8")


def main():
    kennungen = set()
    uebersicht = []

    if (QUELLEN / "bilder").is_dir():
        shutil.copytree(QUELLEN / "bilder", ZIEL / "_bilder", dirs_exist_ok=True)
    QR.mkdir(exist_ok=True)

    for quelle in sorted(QUELLEN.glob("*.md")):
        if quelle.name == "UEBERSICHT.md":   # wird von diesem Skript erzeugt
            continue
        kopf, karten = lies_quelle(quelle)
        for k in karten:
            kennung = k["kennung"]
            if not re.fullmatch(r"[a-z0-9-]+", kennung):
                raise SystemExit(f"{quelle.name}: ungültige Kennung {kennung!r} (nur a-z, 0-9, -)")
            if kennung in kennungen:
                raise SystemExit(f"{quelle.name}: Kennung {kennung} doppelt vergeben")
            kennungen.add(kennung)

            art = k.get("art", "Hilfekarte")
            text = k["text"].replace("](bilder/", "](../_bilder/")
            inhalt, mit_formeln = markdown_mit_formeln(text)
            herkunft = " · ".join(x for x in [
                f"{kopf.get('fach', '')} {kopf.get('klasse', '')}".strip(),
                kopf.get("ab", ""),
                f"Aufgabe {k['aufgabe']}" if k.get("aufgabe") else "",
            ] if x)

            ordner = ZIEL / kennung
            ordner.mkdir(parents=True, exist_ok=True)
            (ordner / "index.html").write_text(SEITE.format(
                titel=html.escape(f"{art} – {herkunft}"),
                katex=KATEX if mit_formeln else "",
                klasse=" loesung" if art.lower().startswith("lösung") else "",
                herkunft=html.escape(herkunft),
                art=art_html(art),
                inhalt=inhalt,
            ), encoding="utf-8")

            url = f"{BASIS}/h/{kennung}/"
            # Vorhandene QR-Codes nie überschreiben: sie können schon gedruckt sein.
            if not (QR / f"{kennung}.png").exists():
                schreibe_qr(url, kennung, k.get("aufgabe", ""), art)
            uebersicht.append((kennung, kopf.get("ab", ""), k.get("aufgabe", ""), art, url))

    zeilen = ["# Übersicht der Hilfekarten", "",
              "Erzeugt von `tools/hilfen.py`. Nicht von Hand bearbeiten.", "",
              "| Kennung | AB | Aufgabe | Art | Adresse | QR-Code |",
              "|---|---|---|---|---|---|"]
    for kennung, ab, aufgabe, art, url in uebersicht:
        zeilen.append(f"| {kennung} | {ab} | {aufgabe} | {art} | {url} | [PNG](../qr/{kennung}.png) |")
    (QUELLEN / "UEBERSICHT.md").write_text("\n".join(zeilen) + "\n", encoding="utf-8")
    print(f"{len(uebersicht)} Karten erzeugt.")


if __name__ == "__main__":
    main()

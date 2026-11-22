# Arbeitsweise in diesem Repo

Unterrichtsmaterial von Kai Uhlenbrauck (Mathe und Chemie, Gymnasium, NRW).
Aufbau des Repos: siehe `README.md`.

## Zusammenarbeit

- Ansprache: duzen. Antworten auf Deutsch.
- **Erst planen, dann bauen.** Bei neuen Materialien zuerst Konzept vorschlagen
  (Bildschirmaufbau, Bedienelemente, offene Entscheidungen) und Rückmeldung abwarten.
- Arbeitsblätter, Präsentationen und Hilfekarten, die hochgeladen werden, vollständig lesen
  (docx/pptx z. B. mit LibreOffice zu PDF/PNG rendern), bevor etwas vorgeschlagen wird.
- Fremde Medien (Videos, Simulationen) wenn möglich herunterladen und über Einzelbilder
  ansehen (ffmpeg). Ehrlich sagen, was man davon beurteilen kann und was nicht.
- Die Arbeitsblätter überarbeitet Kai selbst. Claude liefert Texte und Aufgaben zum Einfügen,
  Rückmeldungen und Durchsichten.
- Aufgaben zu einem Tool stehen entweder auf dem Arbeitsblatt **oder** auf einer Erarbeitungsseite
  im Repo (`<thema>-erarbeitung.html`, Aufgaben neben dem eingebetteten Tool mit `?eingebettet`).
  Die Erarbeitungsseite bietet sich an, wenn die S direkt mit Diagrammen oder Simulationen arbeiten.
  Vorbild: `mathe/q2/binomialverteilung-erarbeitung.html`.
- Zu einer Erarbeitungsseite kann es auf Kais Wunsch eine **Lösungsseite** geben
  (`<thema>-loesungen.html`): Lösungen in Schülersprache, pro Teilaufgabe eingeklappt, Sprungziele
  `#aufgabe1` … wie auf der Erarbeitungsseite. **Nicht verlinkt** (weder Startseite noch Erarbeitungsseite),
  bis Kai das anders entscheidet (z. B. zur Wiederholung). QR-Codes der Sprungziele in `qr/loesungen/`,
  auf der Seite im Lehrermodus `?lehrer`. Vorbild: `mathe/q2/binomialverteilung-loesungen.html`.
- Aufgaben mit NRW-Operatoren formulieren (nenne, beschreibe, vergleiche, erkläre, erläutere …).
- Fachliche Aussagen prüfen. Didaktische Reduktionen ausdrücklich benennen.

## Git und Veröffentlichung

- Jede Änderung auf einem eigenen Branch, dann Pull Request und Merge in `main`.
  **Mergen in `main` ist ausdrücklich erlaubt**, wenn die Änderung getestet ist.
- `main` wird über GitHub Pages veröffentlicht: `https://uhlenbrauck.github.io/unterricht/`.
  Nach einem Merge dauert es etwa eine Minute, bis die Seiten aktualisiert sind.
- Die Datei `.nojekyll` im Hauptordner muss bleiben. Ohne sie verarbeitet GitHub Pages das Repo
  mit Jekyll, und Ordner mit `_` am Anfang (z. B. `h/_bilder/`) würden nicht ausgeliefert.
- **Veröffentlichte Adressen nicht mehr ändern.** QR-Codes und Links auf gedruckten
  Arbeitsblättern hängen daran. Das gilt für Repo-Name, Ordner, Dateinamen und Hash-Anker.
  Muss doch etwas verschoben werden, eine Weiterleitungsseite unter der alten Adresse anlegen.
- Das Repo ist **öffentlich**: keine Schülerdaten, keine Noten, kein fremdes Material
  (Schulbuchseiten, Verlagsabbildungen). Lösungen, die Schüler:innen nicht vorab finden sollen,
  gehören nicht ins Repo (z. B. Erwartungshorizonte). Ausnahmen: Lösungskontrollen in interaktiven
  Seiten (siehe unten), deren Lösungen im Quelltext stehen, und Lösungsseiten zu Erarbeitungsseiten
  (siehe oben), wenn Kai sie will.

## Interaktive Materialien (Animationen, Simulationen)

- Eine einzelne HTML-Datei ohne externe Abhängigkeiten, offline lauffähig.
- Zielgerät: **iPad, Bedienung durch die Schüler:innen selbst**, Safari, quer und hochkant.
  Große Bedienelemente (mind. 44 px), keine Hover-Funktionen.
- **Nicht überfrachten:** nur die Bedienelemente, die der Arbeitsauftrag braucht.
- **Keine Lösungstexte in der Animation.** Erklärungen und Aufgaben stehen auf dem Arbeitsblatt
  oder auf der Erarbeitungsseite, nie im Tool selbst.
  Ausnahme **Lösungskontrollen**, wenn Kai sie für eine Aufgabe will: Die S antworten zuerst,
  dann gibt es ✓/✗ (ohne die richtige Antwort zu verraten); eine Begründung oder Auflösung erst danach
  oder nach einer Wartezeit. Die Lösungen dafür dürfen im Quelltext der Seite stehen.
  Auf dem Bildschirm nur neutrale Beschriftungen (z. B. „Stoffebene“, „Teilchenebene“, „fest“).
- **Schätzen aus Diagrammen:** Sollen die S Wahrscheinlichkeiten oder Werte aus einem Diagramm ablesen
  oder schätzen, dürfen die genauen Werte nicht beim Antippen erscheinen oder im Diagramm stehen
  (hat in der Histogramm-Umgebung vom Schätzen abgelenkt). Werte nur zeigen, wenn damit gerechnet werden soll.
- Mehrere Teile einer Animation über Reiter, jeder Teil direkt verlinkbar über einen Hash-Anker
  (z. B. `#zustaende`), damit das AB pro Aufgabe einen eigenen QR-Code haben kann.
- Lehrermodus über `?lehrer`: Feineinstellung der Parameter, „Werte kopieren“.
- Vor jedem Merge im Browser testen (Playwright mit Chromium, Screenshots quer und hochkant,
  keine JavaScript-Fehler). Bekannte Falle: Der erste `requestAnimationFrame`-Zeitstempel kann
  vor `performance.now()` liegen. Zeitschritte deshalb nie negativ werden lassen.

### Darstellung im Teilchenmodell (Regeln von den Arbeitsblättern)

- Teilchen eines Stoffes haben immer dieselbe Form und Farbe. Teilchen verschiedener Stoffe
  unterscheiden sich in Form oder Farbe.
- **Teilchen nie als Kugeln**, außer Atome und Ionen (die kommen erst in Klasse 9).
- Beispiele vom AB: Wasser = **ausgefülltes blaues Dreieck** (`#5b5ef4`),
  Sauerstoff = rote Raute, Kohlenstoffdioxid = graues Sechseck.
- Lieber wenige, große Teilchen als viele kleine.
- Hintergrund der Lupe **weiß**: Zwischen den Teilchen ist nichts.
- Makro- und Teilchenebene wie auf den Arbeitsblättern: Becherglas (Rand beidseitig leicht
  gewölbt) mit Lupenkreis, der über zwei Linien mit einem Punkt im Glas verbunden ist.
  Eis als gestapelte Eiswürfel, Wasser hellblau, Gas als kleine Kreise.

## Versuchsvorschriften

- Versuchsvorschriften auf Seiten im Repo im **Design von Kais Arbeitsblättern**
  (Vorbild: AB 04.7 „Veranschaulichung des pH-Wertes“, Station 7): `assets/versuch.css`,
  Vorlage zum Kopieren `assets/versuch-vorlage.html`.
- Aufbau: dicker Rahmen um alles; Titelkasten mit Gebotszeichen rechts (Schutzbrille `assets/schutzbrille.svg`);
  zwei Kästen nebeneinander **Chemikalien** (Kästchen zum Abhaken, GHS-Piktogramme rechts in eigener Spalte,
  `assets/ghs/`) und **Material** (Kästchen); Kasten **Durchführung** mit fett gesetzter **Vorbereitung**,
  nummerierten Schritten und Versuchsskizze rechts; Beobachtungs- und Messaufträge *kursiv*
  („Vergleiche …“, „Notiere …“); Kasten **Entsorgung** mit Überschrift links und Kästchen rechts.
  Schrift serif (wie Times New Roman auf dem AB).
- Nur GHS-Piktogramme, keine H-Sätze im Kasten. Stoffe ohne Gefahrstoffkennzeichnung ohne Piktogramm.
- Versuchsskizzen als eigenes SVG (Strichzeichnung, Flüssigkeiten farbig), keine fremden Abbildungen.
- Mengen, die noch nicht erprobt sind, in der Reihen-Notiz kennzeichnen.

## Hilfekarten

- **Eine Seite pro Karte**, jede mit eigenem QR-Code. Karten verlinken nicht aufeinander,
  damit die Verlockung kleiner ist, gleich alle anzusehen.
- Arten: `Hilfekarte <n>` (gestufte Impulse), `Lösung` (grün abgesetzt), `Info` (Wissen, Anleitung).
- Stil wie Kais bisherige Karten: Kopfzeile mit Fach, Jahrgang, AB und Aufgabe,
  rechts „HILFEKARTE“ mit blauem Nummernkästchen.
- Kennung: `<fach><jahrgang>-<thema>-<aufgabe>-<nr>`, z. B. `c7-agg-1b-1`
  (`c` Chemie, `m` Mathe; Jahrgang `7`, `9`, `ef`, `q1`, `gk`, `lk` …).
  **Eine Kennung nie umbenennen und nie neu vergeben.**
- Quellen in `hilfen/<thema>.md`, erzeugt mit `python3 tools/hilfen.py`
  (`pip install markdown segno pillow`). Das Skript schreibt `h/<kennung>/index.html`, `qr/<kennung>.png/.svg`
  und `hilfen/UEBERSICHT.md`. Die erzeugten Dateien nicht von Hand bearbeiten.
- Formeln als Text mit KaTeX (`$…$`, `$$…$$`), Reaktionsgleichungen mit mhchem (`\ce{…}`),
  nicht als Bild.
- Hilfen geben Denkanstöße, Leitfragen oder Wortspeicher, keine fertigen Antworten
  (außer auf Karten der Art `Lösung`).
- Nach dem Erzeugen die QR-Codes als PNG an Kai schicken.
- Bisherige Hilfekarten liegen auf OneDrive und bleiben dort. Umgestellt wird erst,
  wenn das jeweilige AB ohnehin überarbeitet wird.

## Unterrichtsreihen

- Chemie 7, Aggregatzustände: `chemie/7/aggregatzustaende-reihe.md`
- Chemie 10, Säuren und Basen (Plan 2, Helicobacter): `chemie/10/saeuren-basen-reihe.md`
- Mathe GK Q2, Binomialverteilung: `mathe/q2/binomialverteilung-reihe.md`

# Chemie 10 – Säuren und Basen (Plan 2: So schützt sich Helicobacter pylori)

Absprachen zur Reihe und zu den Materialien in `chemie/10/`.

## Rahmen

- Die S arbeiten die Arbeitspläne **im eigenen Tempo** ab. Versuche deshalb als Schülerversuche,
  nicht als Lehrerversuche (sonst müsste Kai sie mehrfach vorführen).
- **Keine konzentrierte Ammoniak-Lösung** in diesen Schülerversuchen. Auch verdünnte Lösungen
  (1–2 mol/L) sind je nach Hersteller als ätzend (H314) gekennzeichnet.
- Jede Erarbeitung muss auch **ohne Versuch** funktionieren (Animation als Ersatz).

## Plan 2 und Materialien

| Auftrag | Material | Repo |
|---|---|---|
| 1 | Film „So schützt sich H. pylori“ (Quarks & Co.) | – |
| 2–6 | Ammoniak, Magnetmodell, Reaktion mit Wasser, Brønsted, Leitfähigkeit | – (Link in Auftrag 4 fehlt im AB) |
| 7 | **Material 5** (ersetzt AB 19 mit Ammoniak-Schaumstoff-Versuch) | `helicobacter-erarbeitung.html` + `helicobacter.html` |
| 8 | Diagnosetest 2 (**muss überarbeitet werden**, siehe „Offen“) | – |
| 9 | **Material 6** „Die Rolle des Wassers“ (Zusatz) | `rolle-des-wassers.html` |

## Links

- Material 5 (Erarbeitungsseite): https://uhlenbrauck.github.io/unterricht/chemie/10/helicobacter-erarbeitung.html
  (Sprungziele `#versuch`, `#aufgabe1` … `#aufgabe5`)
- Lösungsseite (nicht verlinkt): https://uhlenbrauck.github.io/unterricht/chemie/10/helicobacter-loesungen.html
  (Sprungziele `#aufgabe1` … `#aufgabe5`, QR-Codes in `qr/loesungen/helicobacter-aufgabeN.png/.svg`,
  auf der Seite mit `?lehrer`)
- Animation: https://uhlenbrauck.github.io/unterricht/chemie/10/helicobacter.html mit `#modell`, `#teilchen`
- Lehrermodus: `…/helicobacter.html?lehrer#modell`
- Material 6: https://uhlenbrauck.github.io/unterricht/chemie/10/rolle-des-wassers.html
  (Sprungziele `#versuch`, `#info`, `#aufgaben`). Der **Erwartungshorizont** zu M6 liegt nicht im Repo
  (öffentlich), sondern in Kais Doc.

## Material 5: Versuch mit Urease-Alginatkugeln

**Noch nicht erprobt.** Mengen sind abgeschätzt und werden mit den S getestet.
Die Erarbeitungsseite ist so gebaut, dass sie auch ohne Versuch nur mit der Animation funktioniert.
Die Versuchsvorschrift für die S steht auf der Erarbeitungsseite im Design der Arbeitsblätter (`assets/versuch.css`).

### Vorbereitung durch die Lehrkraft

Lösung „Magensäure“ (500 mL, reicht für etwa 10 Gruppen):
- 5 mL Salzsäure (c = 0,1 mol/L) mit dest. Wasser auf 500 mL auffüllen → c = 0,001 mol/L, pH 3
- 10 g Harnstoff darin lösen (2 %)
- Universalindikator-Lösung zugeben, bis die Lösung in 0,5 cm Schichtdicke deutlich orange-rot ist

Alginatkugeln:
- 2 g Natriumalginat in 100 mL warmem dest. Wasser lösen (kräftig rühren), abkühlen lassen
- **Gefäß A:** 50 mL Alginatlösung mit Urease verrühren (etwa 0,1–0,2 g Urease;
  ersatzweise 2–3 g fein gemahlenes Sojabohnenmehl)
- **Gefäß B:** 50 mL Alginatlösung ohne Urease (Kontrolle)
- Jeweils mit Einwegspritze oder Pipette in Calciumchlorid-Lösung tropfen (5 g CaCl₂ wasserfrei bzw.
  6,6 g CaCl₂ · 2 H₂O in 500 mL, etwa 1 %), 10 min härten lassen, abgießen, mit Wasser spülen,
  in wenig Wasser aufbewahren. Die Calcium-Ionen vernetzen die Alginat-Ketten, die Tropfen werden zu Gelkugeln.
- Ersatz für Calciumchlorid: Calciumlactat (kein Gefahrstoff), für dieselbe Calcium-Konzentration
  etwa 14 g Calciumlactat-Pentahydrat in 500 mL.
- Am besten am Versuchstag herstellen. Haltbarkeit im Kühlschrank ungetestet.
- Kugeln **nicht** in phosphat- oder citrathaltigen Lösungen aufbewahren: Diese binden Calcium, die Kugeln lösen sich auf.
- Gefahrstoffe: Calciumchlorid GHS07 (H319). Alle übrigen Stoffe in diesen Konzentrationen kein Gefahrstoff;
  Universalindikator laut Etikett (enthält meist Ethanol).

Schnelltest, ob die Urease aktiv ist: Harnstofflösung + Urease + 1 Tropfen Phenolphthalein → rosa.

### Mögliche Probleme

- Urease aus Soja- oder Jackbohnen arbeitet in stark saurer Lösung kaum. Deshalb pH 3 statt pH 1–2 wie im Magen
  (für die Modellkritik in Aufgabe 2 b). Bleibt der Hof aus: Säure weiter verdünnen (0,0005 mol/L) oder mehr Urease.
- Die Kugeln ohne Urease müssen orange-rot bleiben. Sonst Alginat- oder Calciumchlorid-Reste prüfen
  (Kugeln gründlich spülen).

## Auftrag 6: Leitfähigkeit der Ammoniak-Lösung

**Ammoniak-Lösung c = 0,1 mol/L** (≈ 0,17 % NH₃). Ansetzen einmal für alle unter dem Abzug:
7,5 mL Ammoniak-Lösung 25 % mit dest. Wasser auf 1 L auffüllen. Unter 1 % NH₃ in der Regel nicht
kennzeichnungspflichtig (CLP-Grenzwerte); mit der eigenen Gefährdungsbeurteilung abgleichen.

**Nachweis über Strommessung, nicht über Lampe oder LED** (Erfahrung im Unterricht):
- Die kleine Glühbirne leuchtet bei **keiner** Ammoniak-Konzentration. Ammoniak ist eine schwache Base,
  die Leitfähigkeit bleibt auch bei hoher Konzentration bei höchstens wenigen mS/cm.
  Eine höhere Konzentration bringt also nichts außer mehr Gefährdung.
- Die LED mit Spannungswandler leuchtet schon bei wenigen µA, also auch bei VE-Wasser. Sie unterscheidet
  Wasser und Ammoniak-Lösung nicht.
- Stattdessen: Elektroden (Abstand etwa 1 cm), Gleichspannung etwa 6 V, Amperemeter (Multimeter im mA-Bereich)
  in Reihe. Abgeschätzte Stromstärken (aus Literaturdaten berechnet, nicht gemessen; hängen von Elektroden
  und Eintauchtiefe ab):

| Lösung | Leitfähigkeit | Stromstärke bei 6 V |
|---|---|---|
| VE-Wasser | ≈ 0,005 mS/cm | ≈ 0,03 mA |
| Ammoniak-Lösung 0,1 mol/L | ≈ 0,35 mS/cm | ≈ 2 mA |
| Ammoniak-Lösung 1 mol/L | ≈ 1,1 mS/cm | ≈ 7 mA |
| Salzsäure 0,1 mol/L | ≈ 39 mS/cm | ≈ 230 mA (Glühbirne leuchtet) |

- Zum Vergleich bietet sich Salzsäure 0,1 mol/L an: gleiche Konzentration, aber etwa 100-mal mehr Strom.
  Daran sehen die S, dass Ammoniak mit Wasser nur wenige Ionen bildet (Anknüpfung an M6, Aufgabe 5).

## Animation: getroffene Entscheidungen

**Teil 1 – Modellversuch (`#modell`):** Petrischale von oben, eine Alginatkugel mit Urease in der Mitte,
Farbskala des Universalindikators (pH 1–11) daneben. Bedienung: Start/Pause, Neu, Schalter „Harnstoff“
und „Urease“ (jedes Umschalten startet neu). Zeitanzeige in Minuten. Keine pH-Zahlen in der Schale
(die S lesen an der Skala ab, Aufgabe 1 b).

Modell dahinter: Reaktions-Diffusions-Rechnung auf einem 0,5-mm-Gitter. Die Kugel (Radius 3 mm) bildet
Ammoniak (1·10⁻⁴ mol/(L·s)), wenn Harnstoff **und** Urease eingeschaltet sind. Der pH-Wert folgt aus der
Ladungsbilanz mit pKs(NH₄⁺) = 9,25 und c(HCl) = 0,001 mol/L. Zeitraffer ×30, Dauer 15 min.
Ergebnis: Hof (pH ≥ 6) nach 1 min etwa 4 mm, nach 5 min etwa 7,5 mm, nach 10 min etwa 10,5 mm Radius,
an der Kugel pH ≈ 10,5. Ohne Harnstoff oder ohne Urease bleibt überall pH 3.

**Teil 2 – Teilchenebene (`#teilchen`):** Kleine Petrischale (Zustand nach 8 min) mit Punkt am Kugelrand,
zwei Linien zur Lupe. In der Lupe unten die Kugel mit drei Urease-Enzymen, darüber die Lösung.
Bedienung: Pause, Zeitlupe, Neu.
- Moleküle als **Lewis-Formeln** (NH₃, NH₄⁺, H₂O, H₃O⁺), wo der Protonenübergang die Struktur braucht;
  Harnstoff und CO₂ als **Summenformeln** (Kärtchen bzw. graues Sechseck wie CO₂ in Kl. 7).
  Ionen mit Kreis und Ladung. Farben: Ammoniak/Ammonium petrol, Oxonium rot, Wasser `#5b5ef4`, Chlorid grün.
- Protonenübergang: Das H₃O⁺ dreht ein H zum freien Elektronenpaar des N; das Proton (orange) wandert;
  am O entsteht das zweite freie Elektronenpaar, die Ionenhülle wechselt vom H₃O⁺ zum NH₄⁺.
- Oxonium-Ionen kommen anfangs nach (höchstens 25 s, solange kein Ammoniak übrig ist), danach nicht mehr.
  Findet ein Paar Ammoniak/Oxonium-Ion länger nicht zueinander, bewegen sich die beiden nächsten aufeinander zu.
  Nach 20–40 s ist in der Lupe kein H₃O⁺ mehr, Ammoniak bleibt übrig (Aufgabe 3 c).
- Nachschub an Harnstoff vom Lupenrand; überzählige Produkte wandern aus der Lupe ab.

### Didaktische Reduktionen (bewusst so entschieden)

- **Teil 1:** Alle Teilchen diffundieren gleich schnell, und der effektive Diffusionskoeffizient (0,03 mm²/s)
  ist etwa 20-mal größer als die freie Diffusion von Ammoniak in Wasser. So wächst der Hof in einer
  Unterrichtsminute sichtbar. Nach der Erprobung im Lehrermodus an den Realversuch anpassen.
- **Teil 1:** CO₂ aus der Harnstoffspaltung wird für den pH-Wert nicht berücksichtigt (würde den pH-Wert im Hof
  etwas senken). Die Urease arbeitet unabhängig vom pH-Wert gleich schnell.
- **Teil 2:** Wasser-Moleküle als Lösungsmittel sind nicht dargestellt (nur die entstehenden). Die Harnstoffspaltung
  wird ohne das mitreagierende Wasser-Molekül gezeigt; die Erarbeitungsseite weist bei Aufgabe 3 a darauf hin.
- **Teil 2:** Die Reaktion des überschüssigen Ammoniaks mit Wasser (OH⁻-Bildung) ist nicht dargestellt.
  Die alkalische Färbung erklären die S mit Auftrag 4 des Plans (Lösungsseite 3 c).
- **Teil 2:** Die Urease sitzt an der Kugeloberfläche (im Realversuch im ganzen Gel verteilt).

### Bewusst nicht enthalten

Erklärtexte und Reaktionsgleichungen im Tool, pH-Zahlen in der Schale, Antippen von Teilchen.

## Offen

- **Diagnosetest 2 überarbeiten.**

- Versuch erproben (mit den S), danach Mengen hier und auf der Erarbeitungsseite anpassen.
- Ggf. Lehrermodus-Werte für Teil 1 (Diffusion, Rate) an die beobachtete Hofgröße anpassen.

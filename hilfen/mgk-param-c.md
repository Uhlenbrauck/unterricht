---
fach: Mathe
klasse: Q2 GK
ab: AB 42C
thema: Parameter der Binomialverteilung bestimmen
---

# mgk-param-c-1
aufgabe: C
art: Hilfekarte 1

Gegeben sind die Anzahl der Tickets $n = 55$ und die Anzahl der Sitzplätze. Die Plätze reichen, wenn höchstens 50 Personen erscheinen.

Gesucht ist die Wahrscheinlichkeit, dass eine Person erscheint.

Welcher Buchstabe ist also unbekannt?

# mgk-param-c-2
aufgabe: C
art: Hilfekarte 2

Die Unbekannte steht im Ansatz an derselben Stelle wie das $x$ in `binomCdf`:

`f(x):=binomCdf(55,x,0,50)`

$x$ ist jetzt eine Wahrscheinlichkeit, also eine Zahl zwischen $0$ und $1$.

# mgk-param-c-3
aufgabe: C
art: Hilfekarte 3

**Erste Tabelle:** Start $0$, Schritt $0{,}1$. Die Werte fallen zwischen $0{,}8$ und $0{,}9$ unter $0{,}95$.

**Zweite Tabelle:** Start $0{,}8$, Schritt $0{,}01$. Suche jetzt genau die Stelle, an der die Werte unter $0{,}95$ fallen.

# Roboterprogramm

## Problembeschreibung

Ein Roboter erhält ein kurzes Programm als Zeichenkette. Vor dem eigentlichen Programm steht die verfügbare Treibstoffmenge. Die Treibstoffmenge wird in Unärdarstellung angegeben.

**Beispiel:**

~~~text
1111#FFRFL
~~~

Bedeutung:

~~~text
1111    Treibstoffmenge 4
#       Trennzeichen
FFRFL   Roboterprogramm
~~~

Die Befehle des Roboters sind:

~~~text
F       einen Schritt vorwärts fahren
L       nach links drehen
R       nach rechts drehen
~~~

Ein Befehl `F` verbraucht genau eine Einheit Treibstoff. Die Befehle `L` und `R` verbrauchen keinen Treibstoff.

Ihre Aufgabe ist es, mit Python und automata-lib eine zweistufige Prüfung für solche Roboterprogramme umzusetzen.


## Aufgabenstellung

Implementieren Sie ein Python-Programm, das Eingaben der folgenden Form verarbeitet:

~~~text
1+#(F|L|R)*
~~~

Das bedeutet:

- Vor dem Zeichen `#` steht mindestens eine `1`.
- Nach dem Zeichen `#` stehen beliebig viele Befehle aus der Menge `{F, L, R}`.
- Andere Zeichen sind nicht erlaubt.
- Das Zeichen `#` darf genau einmal vorkommen.

Beispiele für syntaktisch gültige Eingaben:

~~~text
1#
1#F
111#FFR
1111#RRLL
11111#FFRFL
~~~

Beispiele für syntaktisch ungültige Eingaben:

~~~text
#
#FFR
111
111FFR
111#FX
11##FF
~~~

## Teil 1: Deterministischer endlicher Automat

Erstellen Sie mit automata-lib einen deterministischen endlichen Automaten, der genau die syntaktisch gültigen Eingaben akzeptiert.

Der Automat soll folgende Sprache erkennen:

~~~text
1+#(F|L|R)*
~~~

Der Automat prüft nur die äußere Form der Eingabe. Er prüft noch nicht, ob der Treibstoff für das Roboterprogramm ausreicht.

Ihr Automat soll mindestens folgende Fälle korrekt behandeln:

~~~text
111#FFR      akzeptieren
1#           akzeptieren
#FF          verwerfen
111FFR       verwerfen
111#FX       verwerfen
11##FF       verwerfen
~~~

## Teil 2: Turingmaschine

Erstellen Sie mit automata-lib eine Turingmaschine, die prüft, ob die vorhandene Treibstoffmenge für das Roboterprogramm ausreicht.

Die Turingmaschine erhält nur Eingaben, die bereits vom endlichen Automaten akzeptiert wurden.

Die Turingmaschine soll folgende Idee umsetzen:

- Für jeden noch nicht verarbeiteten Befehl `F` wird eine Treibstoffeinheit verbraucht.
- Eine Treibstoffeinheit ist eine `1` links vom Zeichen `#`.
- Verbrauchte Treibstoffeinheiten dürfen auf dem Band markiert werden.
- Verarbeitete `F`-Befehle dürfen ebenfalls markiert werden.
- Wenn alle `F`-Befehle verarbeitet wurden, soll die Turingmaschine akzeptieren.
- Wenn ein `F`-Befehl gefunden wird, aber keine unverbrauchte Treibstoffeinheit mehr vorhanden ist, soll die Turingmaschine verwerfen.

Die Befehle `L` und `R` verbrauchen keinen Treibstoff.

Beispiele:

~~~text
111#FFR      akzeptieren
11#FFR       akzeptieren
1#FFR        verwerfen
111#RRLL     akzeptieren
111#FFF      akzeptieren
11#FFF       verwerfen
~~~

## Teil 3: Graphische Darstellung

Erstellen Sie für beide Modelle eine graphische Darstellung.

- Erstellen Sie eine graphische Darstellung für den deterministischen endlichen Automaten.
- Erstellen Sie eine graphische Darstellung für die Turingmaschine.
- Die Darstellungen sollen als Bilddateien gespeichert werden, zum Beispiel als PNG oder SVG.
- Die Dateien sollen im Projektordner abgelegt werden.

Mögliche Dateinamen:

~~~text
dfa.png
tm.png
~~~

Die graphische Darstellung muss in der Dokumentation verwendet werden.

Falls die direkte Visualisierung mit automata-lib in Ihrer Umgebung nicht funktioniert, erzeugen Sie alternativ eine Graphviz-DOT-Datei und daraus eine PNG- oder SVG-Datei.

## Teil 4: Testfälle

Erstellen Sie eine Testdatei oder einen Testabschnitt in Ihrem Programm.

Testen Sie mindestens zehn Eingaben.

Die Testfälle müssen sowohl akzeptierte als auch verworfene Eingaben enthalten.

Für jeden Testfall soll angegeben werden:

~~~text
Eingabe
Erwartetes Ergebnis des DFA
Erwartetes Ergebnis der Turingmaschine, falls der DFA akzeptiert
Tatsächliches Ergebnis
~~~

Beispiel:

~~~text
Eingabe: 111#FFR
DFA: akzeptiert
TM: akzeptiert
Begründung: 3 Einheiten Treibstoff, 2 F-Befehle
~~~

Ein anderes Beispiel:

~~~text
Eingabe: 1#FFR
DFA: akzeptiert
TM: verworfen
Begründung: 1 Einheit Treibstoff, 2 F-Befehle
~~~

## Teil 5: Dokumentation

Erstellen Sie eine kurze Dokumentation im Projektordner.

Die Dokumentation soll folgende Punkte enthalten:

- Name und kurze Beschreibung der Aufgabe.
- Beschreibung der Eingabesprache.
- Erklärung des deterministischen endlichen Automaten.
- Graphische Darstellung des deterministischen endlichen Automaten.
- Erklärung der Turingmaschine.
- Graphische Darstellung der Turingmaschine.
- Beschreibung der verwendeten Bandzeichen und Markierungen.
- Tabelle mit Testfällen.
- Kurze Erklärung, warum der DFA allein für die Treibstoffprüfung nicht ausreicht.

## Vorschlag für die Projektstruktur

~~~text
roboter_automat/
│
├── automata/
│   ├── dfa.py
│   └── tm.py
├── img/
│   ├── dfa.png
│   └── tm.png
├── tests/
│   ├── tests.md
│   ├── test_dfa.py
│   └── test_tm.py
│
├── main.py
└── README.md
~~~

Die genaue Struktur darf angepasst werden, muss aber nachvollziehbar sein.

## Hinweise zur Modellierung des DFA

Der DFA kann mit wenigen Zuständen erstellt werden.

Ein möglicher Gedanke ist:

- Am Anfang müssen eine oder mehrere Einsen gelesen werden.
- Danach muss genau ein `#` gelesen werden.
- Danach dürfen nur noch die Befehle `F`, `L` und `R` gelesen werden.
- Sobald ein unerlaubtes Zeichen oder ein zweites `#` gelesen wird, muss die Eingabe verworfen werden.

## Hinweise zur Modellierung der Turingmaschine

Die Turingmaschine kann mit Markierungen arbeiten.

Eine mögliche Markierung ist:

~~~text
1       noch verfügbare Treibstoffeinheit
X       verbrauchte Treibstoffeinheit
F       noch nicht verarbeiteter Fahrbefehl
Y       bereits verarbeiteter Fahrbefehl
L       Linksdrehung
R       Rechtsdrehung
#       Trennzeichen
~~~

Eine mögliche Arbeitsweise ist:

- Suche rechts vom `#` nach einem noch nicht verarbeiteten `F`.
- Markiere dieses `F` als verarbeitet.
- Gehe nach links zum Treibstoffbereich.
- Suche dort eine noch nicht verbrauchte `1`.
- Markiere diese `1` als verbraucht.
- Gehe wieder zurück in den Programmbereich.
- Wiederhole diesen Ablauf.
- Wenn kein unverarbeitetes `F` mehr gefunden wird, akzeptiere die Eingabe.
- Wenn ein `F` gefunden wurde, aber keine unverbrauchte `1` mehr vorhanden ist, verwerfe die Eingabe.

## Abgabe

Geben Sie den vollständigen Projektordner ab.

Die Abgabe muss enthalten:

- Den Python-Code.
- Die graphischen Darstellungen des DFA und der Turingmaschine.
- Die Dokumentation.
- Die Testfälle mit Ergebnissen.
- Eine kurze Anleitung zur Ausführung.

## Erweiterungsmöglichkeiten

- **Erweiterung 1:**<br>
  Der Befehl `F` kostet zwei Einheiten Treibstoff.

- **Erweiterung 2:**<br>
  Auch die Befehle `L` und `R` verbrauchen jeweils eine Einheit Treibstoff.

- **Erweiterung 3:**<br>
  Das Roboterprogramm darf leer sein, aber die Treibstoffangabe muss weiterhin vorhanden sein.

- **Erweiterung 4:**<br>
  Es wird zusätzlich ein weiterer Befehl `B` für einen Schritt rückwärts eingeführt.

- **Erweiterung 5:**<br>
  Es wird eine Klammerstruktur eingeführt, zum Beispiel:

~~~text
11111#[FFR]
11111#[F[FR]L]
~~~

In diesem Fall kann zusätzlich ein Kellerautomat (Eigenrecherche) verwendet werden, um korrekt geschachtelte Klammern zu prüfen.

## Ziele der Übung

Nach Abschluss der Übung sollen Sie Folgendes können:

- Sie können einen deterministischen endlichen Automaten zur Erkennung einer einfachen Sprache erstellen.
- Sie können erklären, welche Eigenschaften einer Eingabe durch einen endlichen Automaten geprüft werden können.
- Sie können eine Turingmaschine zur Verarbeitung und Veränderung eines Bandinhalts modellieren.
- Sie können den Unterschied zwischen syntaktischer Prüfung und semantischer Prüfung erklären.
- Sie können Automaten und Turingmaschinen mit Python und automata-lib implementieren.
- Sie können die erstellten Automaten graphisch darstellen und die Darstellung in die Dokumentation aufnehmen.
- Sie können geeignete Testfälle formulieren und deren erwartetes Ergebnis begründen.

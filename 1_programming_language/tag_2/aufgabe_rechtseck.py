"""
Aufgabe:
Berechne die Fläche eines Rechtecks mit den Seiten a und b
Die Seitenlängen sollen durch User-input erhoben werden.
Die eingebenen Werte sollen Integer sein (Ganzzahlen).

Berechne die Fläche und print das Ergebnis auf stdout.

EVA
Eingabe - Vearbeitung - Ausgabe
"""
a = int(input("Bitte Seitenlänge a eingeben: "))  # Rückgabe String
b = int(input("Bitte Seitenlänge b eingeben: "))
# a_int = int(a)
# print("Seitenlänge a:", a, type(a))
# print("Seitenlänge a:", a_int, type(a_int))

result = a * b

print("Die Fläche ist", result, "m2")
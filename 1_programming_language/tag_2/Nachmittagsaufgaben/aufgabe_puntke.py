"""
Berechne die Distanz zweier Punkte p1(x1, y1) p2(x2, y2)
die Koordinaten sollen über Userinput eingegeben werden
nutze dazu das math-Modul (für die Squareroot-Methode)
runde das Ergebnis auf 3 Nachkommastellen
"""
import math

x1 = float(input("Bitte gebe die x Koordinate des ersten Punktes ein: "))
y1 = float(input("Bitte gebe die y Koordinate des ersten Punktes ein: "))
x2 = float(input("Bitte gebe die x Koordinate des zweiten Punktes ein: "))
y2 = float(input("Bitte gebe die y Koordinate des zweiten Punktes ein: "))

# Berechne Distanz
d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("Die Distanz beträgt:", round(d, 3))

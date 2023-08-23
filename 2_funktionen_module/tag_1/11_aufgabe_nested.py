"""
Aufgabe: Erstelle eine Funktion circle, die einen Parameter hat: radius

diese Funktion soll drei innere Funktionen haben, die die Berechnungen
durchführen:
- area, Rückgabwert der Flächeninhalt eines Kreises,
- circumference, Rückgabewert der Kreisumfang,
- diameter, Rückgabewert der Durchmesser

=> keine dieser inneren Funktionen hat einen Parameter.
=> circle soll uns drei Werte zurück (als tuple): Fläche, Umfang, Diameter

Beispiel des Funktionsaufrufs:

area, circumference, diameter = circle(5)

"""
import math


def circle(radius):

    def area():
        return math.pi * radius**2

    def circumference():
        return 2 * math.pi * radius

    def diameter():
        return radius * 2

    return area(), circumference(), diameter()


area, circumference, diameter = circle(5)
print((f"Fläche: {round(area)}, "
       f"Umfang: {round(circumference)}, "
       f"Durchmesser: {round(diameter)}")
      )
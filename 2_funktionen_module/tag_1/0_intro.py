""" 
Einführung zum Thema Funktionen

"""


def hello_world(name, lastname):
    # Parameter name
    print(f"Hello World: {name} {lastname}")


hello_world("Fritz", "the Cat")  # call mit Argument


def berechne_rauminhalt(a, b, c):
    rauminhalt = a * b * c
    if a < 0:
        return 0
    # print(f"Rauminhalt: {rauminhalt}")
    return rauminhalt


result = berechne_rauminhalt(10, 10, 10)
print(f"Rauminhalt: {result}")

""" 
Aufgabe:
1.) Es soll eine Funktion area definiert werden (a, b), die eine Fläche berechnet.
Wenn a ODER b kleinergleich 0 ist, dann soll die Funktion 0 zurückgeben.

2.) Für jedes Element der Liste lengths_widths soll die definierte Funktion aufgerufen 
werden und als Element einer neuen Liste gespeichert werden (optional mit List comprehensions)
"""
lengths_widths = [(22, 24.3), (-1, 34), (0.2, 0.2), (0, 23)]


def area(a, b):
    if a <= 0 or b <= 0:
        return 0
    else:
        area = a * b
        return area


def areashort(a, b):
    if a <= 0 or b <= 0:
        return 0
    return a * b


# klassisch
areas = []
for a, b in lengths_widths:
    areas.append(area(a, b))
print(areas)

# List Comprehension
areas = [area(a, b) for a, b in lengths_widths]
print(areas)
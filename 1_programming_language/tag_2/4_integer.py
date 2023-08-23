""" 
Ganzzahl (Integer)
-unendlich bis plus unendlich
"""
x = 3
print("Datentyp von x:", x)

# arithmetische Operatoren

# Addition
a = 3
b = 4
print("Addition:", a + b)

result_multiply = a * b
print("Multiplikation:", result_multiply)

result_subtraction = a - b
print("Subtraktion:", result_subtraction)

# Truediv! Ergebnis ist immer ein float
result_division = 4 / 2
print("True Division:", result_division)

# Floordiv / Integerdivision
result_division = 5 // 2
print("Floor Division:", result_division)  # Ergebnis ist immer ein Int

# Exponentation (Potenz)
a = 20
volume = a**3


"""
Aufgabe:
Ein Raum fasst maximal 10 Personen. Zur Zeit befinden sich eine
gewisse Anzahl an Personen in diesem Raum.
Wieviele Personen können den Raum noch betreten?
Lege passende Variablen/Konstanten an und führe die Berechnung durch.

Singular und Plural sowie negative Anzahl an Personen im Ergebnis
sind zu ignorieren.

5 Minuten
"""
MAX_PERSONS = 10
current_persons = 3

persons = MAX_PERSONS - current_persons
print("es passen noch", persons, "Personen in den Raum")

a = 1
b = 2
c = 3

# Operatoren-Präzedenz
z = a / b + c
z = (a / b) + c

p = (-2)**2
print("result von p:", p)

# Gruppieren
amount = 100000000
amount = 100_000_000
print("amount:", amount)

price = 10_000

# Division und Modulo
print("divison 3 / 4: ", 3 / 4)  # Division (Truediv)
print("divison 5 // 4: ", 5 // 4)  # Integerdivision
print("modulo 8 % 3:", 8 % 3)  # Rechnen mit Rest
print("modulo 4 % 2:", 4 % 2)  # Rechnen mit Rest


# Beispiel: 5 Minuten Zeit (Happy Coding)
"""
Wieviele Baumstämme passen der Länge nach in die Halle.
Wieviele Meter sind danach noch übrig?

Baumstamm-Länge 4, Hallenlänge 19
"""
HALL_LENGTH = 19
tree_length = 4

total_trees = HALL_LENGTH // tree_length
total_rest = HALL_LENGTH % tree_length

print("Es passen", total_trees, "Bäume in die Halle. Es sind noch", total_rest, "Meter übrig")

timer = 14999
print("aktuelle Uhrzeit:", timer % 12)

# Datentypen konvertieren (type-casting)
# USERINPUT IS EVIL
nummer = "1"  # str
nummer_int = int(nummer)  # nach Integer casten
nummer_str = str(nummer_int)  # nach String zurück casten

print("Typ nummer:", type(nummer))
print("Typ nummer_int:", type(nummer_int))
print("Typ nummer_str:", type(nummer_str))

# User Input
user_input = input("Bitte gebe eine Zahl ein: ")  # Blockierender I/O, Enter drücken!
print("Der Userinput war:", user_input, type(user_input))


# Division erzeugt Float
zahl_1 = 10
zahl_2 = 5
print("divison 10 / 5: ", zahl_1 / zahl_2)  # Division (Truediv)
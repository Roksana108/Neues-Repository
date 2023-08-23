from pprint import pprint
""" 
Sortieren von Collections mithilfe lambda-Funktionen
"""
# unsortierte Liste
liste = [3, 5, 1, 9, 2]

# aufsteigende Sortierung
print("aufsteigend sortiert:", sorted(liste))

# absteigende Sortierung
print("absteigend sortiert:", sorted(liste, reverse=True))

# A ist kleiner als a
chars = ["A", "a", "f", "b", "B", "A", "d", "e"]
print("aufsteigend sortiert chars:", sorted(chars))
print("absteigend sortiert  chars:", sorted(chars, reverse=True))

def char_upper(e):
    return e.upper()


chars = ["A", "a", "f", "b", "B", "A", "d", "e"]
print("aufsteigend sortiert lower:", sorted(chars, key=lambda e: e.lower()))
print("aufsteigend sortiert upper:", sorted(chars, key=char_upper))

ids = ["id5", "idx3", "id2", "id4", "id3"]
print("sorted ids:", sorted(ids, key=lambda e: e[-1]))

# Aufgabe: String aufsteigend sortieren (caseinsensitive)
# Ergebnis muss ein (sortierter) String sein
chars = "zoiocuszUuOcioAAieAABb"
chars = "".join(sorted(chars, key=lambda e: e.lower()))
print(chars)

# -------------------------------------------------------------
# Dict sortieren
# -------------------------------------------------------------
snacks = {'Milka': 3.30, 'Kekse': 5.20, 'Snickers': 1.50}
# snack_iterator = iter(snacks)
# print(next(snack_iterator))
print("Sortierte Dict-Keys:", sorted(snacks))
# snack_iterator = iter(snacks)
# for d in snacks:
#     print(d)

# -------------------------------------------------------------
# snacks aufsteigend nach preis sortieren
# -------------------------------------------------------------
snacks = {'Milka': 3.30, 'Kekse': 5.20, 'Snickers': 1.50}
# snacks.items() erzeugt Liste mit Tupeln. Und jedes Tupel ist Argument e von lambda
print("Snacks nach Preis aufs. sortiert:", sorted(snacks.items(), key=lambda e: e[1]))

# Namen der Snacks nach Preis sortiert
print("Snacks nach Preis aufs. sortiert (nur Namen):", sorted(snacks, key=lambda e: snacks[e]))

# -------------------------------------------------------------
# Städte nach Einwohnerzahl sortieren
# -------------------------------------------------------------

cities = {
    'Köln': 1_200_000,
    'Berlin': 3_400_000,
    'New York': 8_800_000,
    'München': 1_500_000,
    "Dresden": 900_000
}

print("Städte Einwohner:", sorted(cities.items(), key=lambda e: e[-1], reverse=True))

# -------------------------------------------------------------
# Snack Automat
# -------------------------------------------------------------

snacks = {
    1: {'name': 'Erdnüsse', 'price': 200, 'amount': 50, 'pos': {'x': 70}},
    2: {'name': 'Milka', 'price': 400, 'amount': 20, 'pos': {'x': 30}},
    3: {'name': 'Snickers', 'price': 100, 'amount': 10, 'pos': {'x': 50}},
}

# nach Preis (price) sortiert
print("Sortierte Snacks nach price:",
      sorted(snacks.items(), key=lambda e: e[1]["price"])
)

# Aufgabe: nach x sortieren 
print("Sortierte Snacks nach x:",
      sorted(snacks.items(), key=lambda e: e[1]["pos"]["x"])
)

# -------------------------------------------------------------------
# Aufgabe: nach Stringlänge sortieren
# -------------------------------------------------------------------
monty_crew = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print("Sortiere Crew:", sorted(monty_crew, key=lambda e: len(e)))

# -------------------------------------------------------------------
# nach zwei Kriterien sortieren
# -------------------------------------------------------------------
# Usernamen nach Namen und Alter sortieren

def name_age(e):
    """Key-Funktion bei längeren Ausdrücken"""
    return e[1]["name"], e[1]["age"]

user = {
    1: {'name': 'Ali', 'age': 13, 'city': 'New York'},
    2: {'name': 'Ali', 'age': 33, 'city': 'Paris'},
    3: {'name': 'Ali', 'age': 19, 'city': 'Istanbul'},
    4: {'name': 'Ali', 'age': 43, 'city': 'Kairo'},
    5: {'name': 'Ali', 'age': 8, 'city': 'Dortmund'},
    6: {'name': 'Alex', 'age': 2, 'city': 'Berlin'},
    7: {'name': 'Alex', 'age': 12, 'city': 'Hamburg'},
}
# print(user.items())
print("sortierte user:", sorted(user.items(), key=lambda e: (e[1]["name"], e[1]["age"])))
print("sortierte user:", sorted(user.items(), key=name_age))
import sys
from copy import deepcopy

""" 
List Operatoren und Co.
"""
gewichte = [1, 2.2, 0.2, 3]
fruits = ["apple", "banana", "cherry", "pineapple"]


# Zugriff auf einzelne Elemente der Liste mit dem Index-Operator
print("Banane:", fruits[1])

# Herausfinden, an welchem Index ein Objekt liegt
index_von_cherry = fruits.index("cherry")
print("Cherry liegt an index:", index_von_cherry)
print("Cherry wiegt:", gewichte[index_von_cherry])  # lookup

# Hinzufügen eines Elements an eine Liste von hinten
fruits.append("melon")
print(fruits)

# Fügt ein und verdrängt Listeelemente
fruits.insert(1, "lemon")
print(fruits)

# Ersetzt Element an Index 1
fruits[1] = "citron"


# Listen addieren
exotic_fruits = ["passonfruit", "dragonfruit"]
print("fruits vor Addition:", id(fruits))
fruits = fruits + exotic_fruits  # HIER ensteht neue ID für fruits

fruits_copy = deepcopy(fruits) # eine ECHTE, vollständige Kopie der Liste erstellen
fruits_shallow_copy = fruits.copy()  # eine shallow Kopie anlegen
fruits_shallow_copy = fruits[:]  # per Slicing eine shallow Kopie anlegen

frucht_kopie = fruits  # Referenz (beide haben die selbe ID)

print("fruits nach Addition:", id(fruits))
print(fruits)

# extend: Liste addieren ohne neue Liste zu erzeugen
berries = ["strawberry", "cranberry"]
fruits.extend(berries)
print("fruits vor extend:", id(fruits))
print(fruits)

# Auf ein Listenelement zugreifen
print("letztes Element der Liste: ", fruits[-1])
print("Pop-Methode poppt das letzte Element raus und löscht es:", fruits.pop())
print(fruits)

the_first_fruit = fruits.pop(0)
print("Pop-Methode poppt das Element an Index 0 raus und löscht es:", the_first_fruit)

# print("es zeigen folgende Bezeichner auf die Liste:", sys.getrefcount(fruits))

print("fruits: ", fruits)
print("fruits copy: ", fruits_copy)
# reine Theorie
print("es zeigen folgende Bezeichner auf die Liste:", sys.getrefcount(fruits))

"""
Aufgabe:
- Lege eien neue leere Liste cities an
- füge mit append jeweiels drei Städte hinzu (berlin, paris, hamburg)
- ermittle den Index an dem  hamburg liegt mit der index-methode
- lösche hamburg aus der liste mit pop(index)
10 Minuten zeit
"""
cities = []
cities.append("Berlin")
cities.append("Paris")
cities.append("Hamburg")
index_hh = cities.index("Hamburg")
cities.pop(index_hh)

# Matrix (mehrdimenionalen Listen)
M = [
    [1, 2],
    [3, 4],
]

print(M[0][1])

# Numerische Sortierung
zahlen = [3, 2, 99, 191, 4]
zahlen.sort()  # Sortiert die Liste (verändert die liste, inplace Sortierung)
print(zahlen)


if frucht_kopie is fruits:
    print("die frucht_kopie ist die fruits")
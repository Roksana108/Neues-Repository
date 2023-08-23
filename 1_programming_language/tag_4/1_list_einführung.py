""" 
List Operatoren und Co.
"""
fruits = ["apple", "banana", "cherry", "pineapple"]
fruits2 = ["apple", "banana", "cherry", "pineapple"]

# Operatoren: IN-Operator (Membership operator)
if "apple" in fruits:
    print("ja, in der Liste ist ein Apfel")

if fruits == fruits2:
    print("die Listen haben die gleichen Elemente in der selben Reihenfolge")

if [1, 2] == [2, 1]:
    print("sind diese Listen gleich? nein")


# IDENTITY
a = 100_000_000
print(hex(id(a)))  # Speicherort

b = 100_000_000
print(hex(id(b)))

# Listen (bzw. alle veränderlichen Datentypen) haben
# IMMER eine unterschiedliche ID
print("ID fruits:", id(fruits))
print("ID fruits2:", id(fruits2))


# True, False, None (Singleton implementiert)
a = True
b = True
c = None

print(id(a) == id(b))

# IS OPERATOR (vergleicht die Identität zweier Objekte)
fruits_copy = fruits   # Es wird NICHT die Liste kopiert, sondern nur die Referenz
print("id vergleich: ", id(fruits_copy) == id(fruits))
print("is vergleich: ", fruits is fruits_copy)

if fruits_copy is not fruits:
    print("Verweisen nicht auf das gleiche Objekt")

# Die Anzahl der elemente einer Liste
print("Es befinden sich", len(fruits), "in der Liste")

# Prüfen, ob Elemente in einer Liste sind
if fruits:
    print("Es befinden sich Elemente in der Liste")

# bad practice
if len(fruits):
    print("Es befinden sich Elemente in der Liste")

if not fruits:
    print("Es befinden sich KEINE Elemente in der Liste")

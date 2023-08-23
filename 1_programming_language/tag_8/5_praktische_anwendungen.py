""" 
Praktische Beispiele
"""

# Prüfen, ob zwei Listen mindestens ein gemeinsames Element haben
a = [1, 2, 3, 4]
b = [33, 44, 3]

if set(a) & set(b):
    print("haben ein gemeinsames Element")
    print(set(a) & set(b))


# Prüfen, ob alle Elemente einer Liste in einer anderen enthalten sind
a = [1, 2]
b = [2, 1, 4, 6]

if set(a) <= set(b):
    print("Alle Elemente a sind in b enthalten")
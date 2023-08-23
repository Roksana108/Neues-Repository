""" 
Vereinigungsmenge
https://mathepedia.de/Vereinigung.html

Die Vereinigung zweier Mengen ist die Menge, die diejenigen Elemente enthält, 
die wenigstens in einer der beiden Mengen enthalten ist, 
sie umfasst also die Elemente beider Mengen.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print("A U B", x.union(y))
print("A U B", y.union(x))
print("A U B", x | y)

# Menge updaten
y |= {"Yahoo", "Booking"}
print(y)
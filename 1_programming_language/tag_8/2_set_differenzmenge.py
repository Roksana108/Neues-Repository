""" 
Differenzmenge
https://mathepedia.de/Differenz.html

Die Differenzmenge zweier Mengen enthält alle Elemente, 
die in der ersten Menge enthalten sind und nicht in der zweiten.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)
print(x - y)  # Minus-Operator
print(y - x)  # (nicht kommutativ, anderes Ergebnis)
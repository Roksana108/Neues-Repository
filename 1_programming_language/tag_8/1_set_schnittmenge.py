""" 
Schnittmenge
https://mathepedia.de/Durchschnitt.html

A∩B:={x ∣ x∈A ∧ x∈B}
kommutative Operation
"""
a = {"a", "b", "c", "d"}
b = {"a", "d", "e"}

print(f"{a=} & {b=}")
print(a & b)
print(b & a)
print(a.intersection(b))
print(b.intersection(a))

if not a.isdisjoint(b):
    print("die Mengen a und b enthalten ein gleiches Element")

# ----------------------------------
# isdisjoint(): Prüfen, ob keine Elemente in der jeweils anderen Menge enthalten sind
# ----------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

if x.isdisjoint(y):
    print("die Mengen enthalten kein gleiches Element")
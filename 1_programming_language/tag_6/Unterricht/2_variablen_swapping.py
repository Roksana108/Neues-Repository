""" 
Variablentausch (Swapping)
"""
a = 1
b = 2

print(f"before swapping {a=}, {b=}")

# Classic (C)
temp = a
a = b 
b = temp 

print(f"after swapping {a=}, {b=}")

# pythonic, mit Tupel
a, b = (b, a)   # (b, a) => Tupel
print(f"after swapping {a=}, {b=}")

# Erzeugen einer Namensliste
name_1 = "Dirk"
name_2 = "Otto"

namensliste = [name_1, name_2]
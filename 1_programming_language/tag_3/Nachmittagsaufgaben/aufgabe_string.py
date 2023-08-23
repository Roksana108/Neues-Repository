import random

# 1. Gegeben sind zwei Strings. Verkette sie zu einem:
a = "A"
b = "C"
c = a + b
print(c)

a = "Banana"
b = "rama"
c = a + b
print(c)


# 2. Gegeben sind zwei Strings. Prüfe, ob b in a vorkommt
a = "Bellavista"
b = "vis"
if b in a:
    print(f"{b} kommt in {a} vor")

a = "Rom"
b = "Rome"
if b in a:
    print(f"{b} kommt in {a} vor")

# 3. String Ersetzung
a = "Bellavista"
b = "Bella"
c = "Buena"
d = a.replace(b, c)
print(d)

a = "Nordpol"
b = "pol"
c = "kap"
d = a.replace(b, c)
print(d)

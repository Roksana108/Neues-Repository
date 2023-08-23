"""
 "Always code as if the guy who ends up maintaining your code will be a 
 violent psychopath who knows where you live"
― John Woods

Tupel als Rückgabewert von Funktionen
"""
def fn():
    return 2, 3


# Aufrufen der Funktion print()
rueckgabewert = fn()
print(rueckgabewert)
a = rueckgabewert[0]
b = rueckgabewert[1]

a, b = fn()

# Tupel Unpacking (Variablen und Werte müssen übereinstimmen)
x, y, z = 1, 2, 3

# Tupel ungleicher Länge entpacken mit Sternchenoperatoren
x, y, *z = 1, 2, 3, 4, 5
print(f"{x=} {y=} {z=}")
print("Typ von x: ", type(x))  # Typ von x:  <class 'int'>

# Vorne liste, hinten x und y
*x, y, z = 1, 2, 3, 4, 5
print(f"{x=} {y=} {z=}")
print("Typ von *x: ", type(x))  # Typ von *x:  <class 'list'>

# sternchenoperator in der Mitte
x, *y, z = 1, 2, 3, 4, 5
print(f"{x=} {y=} {z=}")

# Underline Varialbnenname, wenn diese Variable nicht weiter verwendet wird
_, y, *z = "a3", 2, 3, 4, 5


# Underline als Variablenname, wenn sie nicht weiter verwendet wird
for _ in range(4):
    print("Hello world!")
"""
 "Always code as if the guy who ends up maintaining your code will be a 
 violent psychopath who knows where you live"
― John Woods

Tupel als Rückgabewert von Funktionen
"""
def fn():
    return 2, 3


# Aufrufen der Funktion print()
rueckgabewert = fn()
print(rueckgabewert)
a = rueckgabewert[0]
b = rueckgabewert[1]

a, b = fn()

# Tupel Unpacking (Variablen und Werte müssen übereinstimmen)
x, y, z = 1, 2, 3

# Tupel ungleicher Länge entpacken mit Sternchenoperatoren
x, y, *z = 1, 2, 3, 4, 5
print(f"{x=} {y=} {z=}")
print("Typ von x: ", type(x))  # Typ von x:  <class 'int'>

# Vorne liste, hinten x und y
*x, y, z = 1, 2, 3, 4, 5
print(f"{x=} {y=} {z=}")
print("Typ von *x: ", type(x))  # Typ von *x:  <class 'list'>

# sternchenoperator in der Mitte
x, *y, z = 1, 2, 3, 4, 5
print(f"{x=} {y=} {z=}")

# Underline Varialbnenname, wenn diese Variable nicht weiter verwendet wird
_, y, *z = "a3", 2, 3, 4, 5


# Underline als Variablenname, wenn sie nicht weiter verwendet wird
for _ in range(4):
    print("Hello world!")

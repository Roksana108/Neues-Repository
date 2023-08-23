""" 
Entpacken von Sequenzen
"""
coords = [1, 2, 3]

# unpythonische Weg
x = coords[0]
y = coords[1]
z = coords[2]

# pythonic 
x, y, z = coords
print(x, y, z)

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

# --------------------------------------------------------
# Entpacken bei Funktionsaufruf (üblich sequentiellen Datentypen)
# --------------------------------------------------------
def summe(a: int, b: int) -> int:
    return a + b

values = (2, 3)
a, b = values

summe(a, b)   # pythonischer
summe(values[0], values[1])   # unpythonisch

values = (2, 3)
summe(*values)  # Entpacken bei Aufruf

numbers = set([1, 2])
summe(*numbers)

# --------------------------------------------------------
# Entpacken bei Funktionsaufruf Liste von dicts
# --------------------------------------------------------
def check(a: dict, b: dict) -> None:
    print("check: ", a, b)

values2 = [
    {"a": 1, "b": 2},
    {"a": 3, "b": 4},
]

check(*values2)   # better
check(values2[0], values2[1])  # nicht optimal

def filter_sizes(gender: list, weights: list, heights: list):
    ...

humans = [
    ["m", "f", "f"],
    [78, 64, 62],
    [188, 178, 176]
]

filter_sizes(*humans)

# --------------------------------------------------------
# Entpacken bei Funktionsaufruf: Dictionary
# --------------------------------------------------------
def check2(filename: str, bytesize: int):
    print(f"check2: {filename=}, {bytesize=}")


d = {
    "bytesize": 1200,
    "filename": "products.csv",
}

# unpythonisch
# check2(d["filename"], d["bytesize"])
# check2(*d.values())  # ["products.csv", 1200]
check2(**d)   # check2(bytesize=1200, filename=products.csv)

""" 
Aufgabe:
Schreibe eine Funktion print_movie.
Diese Funktion soll ihr übergebene Werte ausdrucken, und zwar in der Form
title - director - year - producer

Beispiel:
The Matrix - Wachowski - 1999
The Terminator - James Cameron - 1984 - Gale Anne Hurd
"""
def print_movie(*args):
    print(" - ".join(str(el) for el in args))

def print_movie2(title, director, year, producer=""):
    result = " - ".join(
        str(value) for value in [title, director, year, producer] if value
    )
    print(result)


movies = [
    {
        "title": "The Matrix", 
        "director": "Wachowski",
        "year": 1999
    },
    {
        "title": "The Terminator",
        "director": "James Cameron",
        "year": 1984,
        "producer": "Gale Anne Hurd",
    },
]


print_movie(*movies[0].values())
print_movie2(**movies[0])
print_movie2(**movies[1])
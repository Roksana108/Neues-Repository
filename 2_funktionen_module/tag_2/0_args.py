""" 
Positionelle Argumente
"""


def volume(a, b, c):
    print(f"positionelle Parameter: {a=}, {b=}, {c=}")


volume(1, 2, 3)

# ----------------------------------------------------
# Default Parameter
# ----------------------------------------------------


def area(a, b=10):
    print(f"{a=}, Default Paramter {b=}")


area(5, 3)
area(5)  # hier wird b nicht als Argument übergeben

print(max(3, 4, 5, 1, 9))  # unbestimmte Anzahl an Argumenten ODER Iterable
sum([2, 3, 4, 5])   # MUSS Iterable

# ----------------------------------------------------
# args: Unbestimmte Anzahl an Argumenten
# ----------------------------------------------------


def values(*args):
    # *args ist eine unbestimmte Anzahl an Argumenten
    print(f"Der Funktion wurden folgende Werte übergeben: {args}, {type(args)}")


values(1, 9, 3, 78, 42, 12)
values()  # ohne Argument aufrufen

# ----------------------------------------------------
# fixed  Unbestimmte Anzahl an Argumenten und zwei zwingende
# Paramter
# ----------------------------------------------------


def fixed(a, b, *args):
    # *args ist eine unbestimmte Anzahl an Argumenten
    print(f"Der Funktion wurden folgende Werte übergeben: {a=}, {b=}, {args=}")


fixed(1, 9, 3, 78, 42, 12)

# ----------------------------------------------------
# default parameter mit *args
# ----------------------------------------------------


def fixed2(a, b, default=10, *args):
    # *args ist eine unbestimmte Anzahl an Argumenten
    print(f"{a=}, {b=}, {default=} {args=}")


fixed2(1, 9, 3, 78, 42, 12)  # a=1, b=9, default=3 args=(78, 42, 12)
fixed2(1, 9)                 # a=1, b=9, default=10 args=()
fixed2(1, 9, 42)             # a=1, b=9, default=42 args=()

# ----------------------------------------------------
# Funktion mit positionellen Argumenten erzwingen
# positional-only mit /, alles was links davor steht
# ----------------------------------------------------


def numbers(a, /, b):
    print(f"{a=}, {b=}")


# numbers(a=1, b=2)
numbers(1, b=2)
numbers(1, 2)
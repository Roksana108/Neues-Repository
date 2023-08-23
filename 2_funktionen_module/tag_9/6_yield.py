""" 
yield-Funktionen (erzeugen einen Iterator)
"""
from typing import Generator

gen_ex = (x for x in range(10))

def normale_funktion():
    return 1


wert = normale_funktion()

# yield Funktion
def infinite_counter() -> Generator:
    """uendlicher counter, der hochzählt."""
    x = 0
    while True:
        yield x  # yield = ernten
        x += 1


counter = infinite_counter()  # counter ist jetzt ein Iterator
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
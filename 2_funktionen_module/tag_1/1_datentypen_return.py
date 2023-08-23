""" 
Datentypen der Rückgabewerte
idealerweise bei meheren returns immer den selben Datentypen verwenden
"""


def area(a, b):
    if a < 0:
        return "not possible"  # bad practice
    return a * b


area_1 = area(-1, 4)
print(area_1 ** 3)
""" 
Type-Hinting

f: A -> B
"""

def summe(a, b):
    return a + b


def better_summe(a: float, b: float) -> float:
    return a + b


def concatenate_lists(a: list, b: list) -> tuple:
    return tuple(a + b)


# # a, b = input("Bitte Zahlen eingeben a,b").split(",")
# a, b = ["3"], ["3"]
# print(summe(a, b))
summe("a", "b")
better_summe(1, "a")


concatenate_lists([3, 3], 3)
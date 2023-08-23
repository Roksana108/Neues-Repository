"""
Sideeffect: Anhängen von Elementen aus einer globalen Liste in einer Funktion
Egal ob mit oder ohne Parameterzuweisung

"""

fruits = ["apple"]
print(id(fruits))


def fn(fruits):
    fruits.extend(["strawberry"])  # klassischer Seiteneffekt
    print("locals:", locals())
    print(id(fruits))


def gn():
    fruits.extend(["strawberry2"])  # klassischer Seiteneffekt


fn(fruits)
gn()
print(fruits)
# print(globals())
print(id(fruits))

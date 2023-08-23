"""
Filter 

SCHEMA: 
[e] for el in sequnece if predicate]

vs 
filter(predicate, seq)

wenn Bedingung war ist, gebe Element zurück

"""
def greater_than_100(el):
    """gibt True zurück, wenn el > 100"""
    return el > 100


numbers = [200, 30, 100, 99, 101]
 
# als List comprehension
print( [el for el in numbers if greater_than_100(el)])

# als Filetr 
filter_object = filter( greater_than_100, numbers)
print(list(filter_object))

# map und filter kombiniert 
# montey_up = map (str.title, montey)
# Filtere alle elemente, die mehr as 4 zeichen haben 
def greater_four(e):
    return len(e) > 4


monty = ["eggs", "spam whomp", "cheese", "ham"]
def greater_four(e):
    return len(e) > 4

monty = ["eggs", "spam whomp", "cheese", "ham"]
result = map(str.title, filter(greater_four, monty))
print(list(result))

# -------------------------------------------------------------
# map und filter kombiniert, Aufgabe
# Ausgangsliste number auf gerade Zahlen filtern und das Ergebnis
# davon jeweils durch 3 teilen
# -------------------------------------------------------------
numbers = [200, 33, 101, 100, 102, 5]


def div_3(el):
    return el / 3


result = map(div_3, filter(lamada el: el numbers % 2 == 0), numbers)
print(list(result))

def result(e):
    return result(e) / 3


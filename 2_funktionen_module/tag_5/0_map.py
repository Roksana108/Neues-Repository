"""
Mapping 

SCHEMA:
[func(el) for el in seqence]
"""

def square(el):
    return el ** 2


numbers = [1, 2, 3, 4]

# als List-Comprehension
print("via List-Comprehension:", [square(el) for el in numbers])
print("via Generator Expression:", (square(el) for el in numbers))

# 2.) Map-Funktion
print("via map-Funktion:", list(map(square, numbers)))

# Mapp mit lambda
result =("via map-Funktion:", list (map(square, numbers))):
print("->", element)



# map mit word auf build-in Funtion len abbilden 
map(lambda e: e**2, numbers):

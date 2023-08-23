"""
Annonyme Funtionen
Lambda Funktionen (Lammbda Ausdruck)

Weg Werfern Funktionen 
"""
# klassiche Funktion
def fn(x, y):
    return x + y

# Lamabda Ausdruck (immer einzeilig)
f = lambda x, y : x +y

# Dog Poo Syntax (eine Lambda funtion direkt aufrufen)
print((lambda x, y, : x +y)(1, 2))


print(f(3, 4))
print(fn)

# --------------------------------------------------
#  Funktionsreferenz
# --------------------------------------------------

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,

}

userprint_operator = "?"
a, b = 3, 5

result = operations.get(userprint_operator, lambda x, y: 0)(a, b)
print("Ergebis:", result)

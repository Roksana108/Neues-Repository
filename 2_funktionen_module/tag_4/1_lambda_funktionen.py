""" 
Anonyme Funktionen
Lambda Funktionen (Lambda Ausdruck)

Wegwerf-Funktionen
"""

# klasssische Funktion
def fn(x, y):
    return x + y


# Lambda Ausdruck (immer einzeilig)
f = lambda x, y: x + y

# ----------------------------------------------------------
# Dog Poo Syntax (eine Lambda funktion direkt aufrufen)
# Immediately invoked function expression
# ----------------------------------------------------------
print((lambda x, y: x + y)(1, 2))


print(f(3, 4))
print(fn)

# ----------------------------------------------------------
# Funktionsreferenzen im Dict
# ----------------------------------------------------------

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

userinput_operator = "?"
a, b = 3, 5


result = operations.get(userinput_operator, lambda x, y: 0)(a, b)
print("Ergebnis:", result)

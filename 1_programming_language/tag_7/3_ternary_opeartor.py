""" 
Ternärer Operator
? wahrheitszweig : unwahr

b = 1 if a > 0 else 2

"""

y = 0
a = 3

# klasssiche Schreibweise
if a > 0:
    y = 100
else:
    y = 200

print(f"{y=}")

# Ternary operator
y = 100 if a > 0 else 200

print(f"{y=}")
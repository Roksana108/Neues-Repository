# 1. Iteration über Liste
fruits = ["Banane", "Apfel", "Kirsche"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 2. Filtern einer Liste 1
fruits = ["Banane", "Apfel", "Kirsche", "Birne"]
filtered_fruits = []
for fruit in fruits:
    if fruit.startswith("B"):
        filtered_fruits.append(fruit)
print(filtered_fruits)

# 3. Filtern einer Liste 2
numbers = [1, 4, 5, 2, 42, 200, 1, 99, 23, 323]
filtered_numbers = []
for number in numbers:
    if number > 5 and number < 100:
        filtered_numbers.append(number)
print(sorted(filtered_numbers))


# 5. das letzte Element
symbols = ["B", "C"]
if symbols:
    print("das letzte Element in der Liste: ", symbols[0])


# 6. erlaubte Werte
a = [50, 100, 40, 20, 200, 50, 100, 10]
allowed_values = [50, 100, 200]
c = []
for el in a:
    if el in allowed_values:
        c.append(el)
print(c)


# 7. Bereiningen der Liste
a = ["x_x", "alpha_beta", "_"]
c = []
for el in a:
    el = el.replace('_', '')
    if el:
        c.append(el)
print(c)

# 8. Bereiningen der Liste von Steuerzeichen und x
a = ["haxlt ", "\nandx", "\tcatch ", " xfire "]
c = []
for el in a:
    el = el.strip().replace("x", "")
    if el:
        c.append(el)
print("8: ", c)


# 9. Zusammenführen von zwei Listen
a = ["A", "B", "C", "D", "E", "F"]
b = [1, 2, 3, 4, 5]
c = []

for i, element in enumerate(a):
    if i >= len(b):
        break
    c.append(f"{element}{b[i]}")

print(c)

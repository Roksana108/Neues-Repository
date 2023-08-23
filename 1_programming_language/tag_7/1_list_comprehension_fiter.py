"""
Listen Abstraktion Filter
"""
names = ["Armin", "Jürgen", "Serap", "Brice", "andrea", "Roksana"]

# Alle Namen, die mit A anfangen
names_with_a = []
for name in names:
    if name.startswith("A"):
        names_with_a.append(name)
print(names_with_a)


# Filter mit List-Comprehension
names_with_a = [name for name in names if name.startswith("A")]
print(names_with_a)

# übungsaufabe: filtere alle Zahlen aus der Liste, die durch 2 teilbar sind
numbers = [1, 2, 3, 4, 9, 11, 24, 10, 7]
even_numbers = [number for number in numbers if number % 2 == 0]
even_numbers_2_version = [number for number in numbers if not number % 2]
print(even_numbers_2_version)
print(even_numbers)
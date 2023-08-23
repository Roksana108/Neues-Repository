""" 
Dict Methoden
https://www.w3schools.com/python/python_ref_dictionary.asp
"""

population = {
    'Berlin': 3748148,
    'Hamburg': 1822445,
    'München': 1471508,
    'Cologne': 1085664,
    'Frankfurt': 753056
}

# Printe alle keys
for key in population.keys():
    print(key)

# Printe alle keys (ohne keys-Methode)
for key in population:
    print(key)

print("*" * 30)

# Printe alle values
for value in population.values():
    print(value)

print("*" * 30)

# ---------------------------------------------------------
# Printe key, value paare
# ---------------------------------------------------------
for key, value in population.items():
    print(key, value)

# ---------------------------------------------------------
# Wert setzen
# ---------------------------------------------------------
population["Berlin"] = 4_000_000

# Wert entfernen
del population["Berlin"]
print(population)

# ---------------------------------------------------------
# Dict updaten
# ---------------------------------------------------------
population.update({"Berlin": 3, "Dresden": 800_000})
print(population)
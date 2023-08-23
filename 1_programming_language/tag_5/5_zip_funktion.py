""" 
zip
aus zwei Listen (all. Sequenzen) ein Dict erstellen.
"""
countries = ["Argentinien", "Türkei", "USA", "Russland", "Spanien"]
food = ["Alfajores", "Pilav", "Hamburger", "Pelmeni", "Empanada"]

d = {}
for i, country in enumerate(countries):
    d[country] = food[i]

print(d)

world_foods = zip(countries, food)  # erzeugt zip-Objekt
# print(list(world_foods))
world_foods_dict = dict(world_foods)
print(world_foods_dict)

# kurze schreibweise (Anmerkung: itertools zip_longest)
countries = ["Argentinien", "Türkei", "USA", "Russland", "Spanien", "Portugal"]  # Portugal wird ignoriert
food = ["Alfajores", "Pilav", "Hamburger", "Pelmeni", "Empanada"]
foods = dict(zip(countries, food))

# ----------------------------------------------
# dict aus einer 2D-Liste erstellen
# ----------------------------------------------
liste = [
    ["a", [1, 2]],
    ["b", 2],
    ["c", 3],
]
liste_dict = dict(liste)
print(liste_dict)
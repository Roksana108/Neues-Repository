""" 
Datentyp dict (key value speicher)
Key: nur unverändliche Datentypen
Value: alle Datentypen
"""
from pprint import pprint

d = {}
print(f"Datentyp von d: {type(d)}")
d["a"] = 1  # Zuweisung
print(f"Wert von key a: {d['a']}")  # Zugriff, konstante Zeitkomplexitit O(1)

# Dict-Literal
player = {
    "name": "Bob",
    "age": 120,
    "weapons": ["gun", "shuriken"],
    "address": {
        "zip": "382A",
        "city": "Mars"
    }
}
# pprint(player, sort_dicts=False)
print(player)
print("Name des Players:", player["name"])

# Prüfen, ob ein Key vorhanden ist
numbers = {
    1: "alfa",
    2: "beta"
}
if 1 in numbers:
    print(numbers[1])


# Wörterbuch DE EN
de_en = {
    "katze": "cat",
    "hund": "dog"
}

if "katze" in de_en:
    print(f"Katze heisst auf englisch: {de_en['katze']}")
else:
    print("Das Wort befindet sich leider nicht im Wörterbuch")

capitals = {
    "Hessen": "Wiesbaden",
    "Saarland": "Saarbrücken",
}

""" 
get Methode: Gibt den Value eines Keys zurück oder Defaultwert, wenn key 
nicht vorhanden
"""
wort = de_en.get("schildkröte", "Defaulttier")
print(wort)
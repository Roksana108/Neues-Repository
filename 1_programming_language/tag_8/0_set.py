""" 
Datentyp set
veränderlich, unsortiert (nicht indexierbar), Collection
darf nur unveränderliche Werte enthalten

https://www.w3schools.com/python/python_sets_methods.asp
"""

# Set definieren
x = {} # vorsicht, leeres Dict!
y = set()
z = {1, 2, 3, 4}  # Set Literal

print(f"Set: {z}, {type(z)}")

# Ein Set aus einer Liste erstellen
z = set([1, 2, 3, 4])
print(f"Set: {z}, {type(z)}")

# praktische Anwendung: Liste von doppelten Elementen entfernen
numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 1]
unique_numbers = list(set(numbers))
print(unique_numbers)

# ---------------------------------------------------------
# add-Methode: ein Element zur Menge hinzufügen
# Mengenelemente bleiben eindeutig (unique)
# ---------------------------------------------------------
z.add(5)
z.add("5")
print(f"Set: {z}, {type(z)}")

# ---------------------------------------------------------
# nur unverändlicher Datentypen als Elemente nutzen
# Liste ist ein verändlicher Datentyp und darf nicht als 
# Element eines sets genutzt werden
# ---------------------------------------------------------
# z.add([1, 2])  # TypeError: unhashable type: 'list'

# ---------------------------------------------------------
# Pop: ein willkürliches Element der Menge rausgreifen
# ---------------------------------------------------------
print(z.pop())
print(f"Set nach pop: {z}")
print(z.pop())
print(f"Set nach pop: {z}")

# ---------------------------------------------------------
# Zugriff per Index auf ein Set GEHT NICHT!
# ---------------------------------------------------------
# print(z[0])

# ---------------------------------------------------------
# Element aus Set löschen (mit remove)
# ---------------------------------------------------------
z.remove('5')
print(f"pop: {z}")
# z.remove('5') resultiert in KeyError, da kein Element '5' 
# enthalten ist

# ---------------------------------------------------------
# Element aus Set löschen (mit discard), kein KeyError 
# wenn Element nicht enthalten ist
# ---------------------------------------------------------
z.discard('5')
print(f"pop: {z}")

# ---------------------------------------------------------
# Prüfen, ob ein Element im Set: IN-Operator
# ---------------------------------------------------------
if 3 in z:
    print("3 ist im Set z enthalten")


# ---------------------------------------------------------
# Länge eines Set
# ---------------------------------------------------------
print("Es befinden sich aktuell folgende Elemente im SEt:", len(z))

# ---------------------------------------------------------
# Iteration über ein Set
# ---------------------------------------------------------
for element in z:
    print(element)


# ---------------------------------------------------------
# Update eines Set
# ---------------------------------------------------------
z.update([1, 22, 33, 44], [7, 8, "9"])
print(z)
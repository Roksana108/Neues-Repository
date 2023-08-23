""" 
Iteration

Iteration beschreibt allgemein einen Prozess mehrfachen Wiederholens
https://de.wikipedia.org/wiki/Iteration

Sammlungskontrollierte Schleife: der for-Loop
"""

# über eine Zahl kann man nicht iterieren
# TypeError: 'int' object is not iterable
# x = 3
# for zahl in x:
#     print(zahl)

# -------------------------------------------
# Iteation über einen String (Sequenz)
# -------------------------------------------
first_name = "Alf"
for char in first_name:
    print("=>", char)


fruits = ["apple", "banana", "cherry", "pineapple"]
for fruit in fruits:
    print(fruit)

# -------------------------------------------
# Zahlenliste von 1 - 10
# -------------------------------------------
for number in range(1, 11):
    print(number, end=" ")

# -------------------------------------------
# Filter
# -------------------------------------------
names = ["Andrea", "Lennart", "Anja", "Armin"]
filtered_names = []

for name in names:
    if name.startswith("An"):
        filtered_names.append(name)

print()
print(filtered_names)

# -------------------------------------------
# Enumeration (falscher Weg)
# -------------------------------------------
zahlen = [2, 4, 8, 10]
i = 0
for zahl in zahlen:
    print("index:", i, "Wert", zahl)
    i = i + 1

print("*" * 50)

# -------------------------------------------
# pythonische Variante der Enumeration
# -------------------------------------------
zahlen = [2, 4, 8, 10]
for index, value in enumerate(zahlen):
    print("index:", index, "Wert", value)


# -------------------------------------------
# Elemente in der Liste ändern
# wir wollen jedes element in der Liste mit 2 multiplizieren
# -------------------------------------------
zahlen = [2, 4, 8, 10]
for index, value in enumerate(zahlen):
    zahlen[index] = value * 2

print(zahlen)


# -------------------------------------------
# Liste aus einem String erzeugen (default trenner von split ist space)
# -------------------------------------------
satz = "the quick brown fox jumps over the lazy dog"
wort_liste = satz.split()
print(wort_liste)

# -------------------------------------------
# Liste aus einem String erzeugen und Integer erzeugen
# -------------------------------------------
user_input = input("Bitte Koordinaten und Radius eingeben (x, y, r): ")
user_input_liste = user_input.split(",")  # ['3', '3', '10']
int_liste = []

for zahl in user_input_liste:
    int_liste.append(int(zahl))

print(int_liste)

# -------------------------------------------
# Suchen (Loop mit break verlassen)
# -------------------------------------------
names = ["Anja", "Armin", "Jürgen", "Ewald"]
for name in names:
    if name == "Jürgen":
        print("Name Jürgen ist gefunden")
        break


# -------------------------------------------
# mit continue die aktuelle Iteration abbrechen und 
# zum nächsten Iterationsschritt gehen
# Beispiel: Gerade Zahlen verdoppeln
# Hinweis: 4 % 2 == 0, 5 % 2 == 1
# -------------------------------------------
zahlen = [2, 3, 4, 8, 9, 10]
for zahl in zahlen:
    # wenn die zahl ungerade ist, nächster Iterationsschritt (continue)
    if zahl % 2 != 0:
        continue
    print(zahl, zahl * 2)

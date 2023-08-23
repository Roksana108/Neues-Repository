""" 
Formatieren von Strings

https://realpython.com/python-formatted-output/
"""

player = 3
zombies = 100
print("Aktuell befinden sich", player, "im Spiel und", zombies, "kriechen durch die Gassen")

""" 
format-Methode: String-Methode
Template-String

Die Anzahl der Platzhalter {} muss der Anzahl der Argumente der format-Methode entpsrechen
"""
string = "Aktuell befinden sich {} im Spiel und {} kriechen durch die  Gassen".format(player, zombies)
print(string)


"""
f-String (Format String)
"""
string = f"Aktuell befinden sich {player} im Spiel und {zombies} kriechen durch die Gassen"
print(string)

"""
Float formatieren
"""
z = 1 / 3
print(f"{z:.2f}")
print(f"{2 / 3:.2f}")

""" 
Integer Repräsentation
"""
y = 42
print(f"int: {y:d}, hex: {y:#x}, bin: {y:#b}")

""" 
Prozentuales Verhältnis
"""
points = 19
total  = 25
gesamt = points / total
print(f"{gesamt:.2f}, {gesamt:.1%}")

x = 1
y = 3
print(f"x={x} und y={y}")  # x=1 und y=3
print(f"{x=} und {y=}")  # x=1 und y=3


""" 
Tausender Trennzeichen
"""
number = 100_000_000
print(f"{number:,}")  # 100,000,000
print(f"{number:_}")  # 100_000_000

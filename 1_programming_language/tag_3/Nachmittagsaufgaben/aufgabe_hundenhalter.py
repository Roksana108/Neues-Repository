"""
Allgemein rechnet man Hundejahre in Menschenjahre um, indem man das Alter des Hundes mit 7 multipliziert. Je nach
Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus, z.B.:

- Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
- 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
- Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger Methode berechnet, welchem Alter in Menschenjahren das entspricht.
Beachte, dass ein Hund mindestens 1 Jahr alt sein muss!
"""
age = int(input("Bitte geben Sie das Alter des Hundes ein: "))

if age < 1:
    print("Ein Hund darf nicht jünger als 1 Jahr sein!")
else:
    if age == 1:
        dog_age = 14
    elif age == 2:
        dog_age = 22
    else:
        dog_age = 22 + ((age - 2) * 5)

    print("Der Hund ist", dog_age, "Jahre alt")

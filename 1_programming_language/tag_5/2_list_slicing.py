""" 
Subliste (Slicing-Operator)

Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String

"""
planeten = [
    "Merkur",
    "Venus",
    "Erde",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptun",  
    "Pluto",  # good practice: komma an den letzten Eintrag hängen
]

liste_mit_strings = [
    "eins"
    "zwei"
    "drei"
]   # "einszweidrei"

numbers = [1, 2, 3]


print("planeten:", planeten[0:3])
planeten_kopie = planeten[:]   # flache Kopie

print(planeten)
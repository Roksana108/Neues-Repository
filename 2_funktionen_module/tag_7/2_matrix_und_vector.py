""" 
Vektor erstellen
"""
from pprint import pprint

# v = [0, 0, 0], v = [1, 2, 3]
v = [0] * 10
print(f"Vektor {v=}")

"""
Matrix: 3 x 4 (3 Zeilen, 4 Spalten)
m = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
"""
M = [[0 for i in range(4)] for j in range(3)]
M[0][0] = 1
print(M)

""" 
Transponieren

m = [
    [1, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
mT = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
"""
print("*" * 40)
M = [
    [1, 2, 3],
    [4, 5, 6]
]
pprint(M, width=20)

print("Matrix transponiert:")
mT = [x for x in zip(*M)]
pprint(mT, width=20)

""" 
Übungsaufgabe: Diagonale
"""
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for index, valuelist in enumerate(M):
    print(valuelist[index])

# Lösung mit range
MD = [M[i][i] for i in range(len(M))]
print(MD)

# Lösung mit enjmerate
diag = [row[i] for i, row in enumerate(M)]
pprint(f"diagonal: {diag}")

# Lösung für umgekehret Diagonale
diag = [row[-i - 1] for i, row in enumerate(M)]
pprint(f"diagonal: {diag}")
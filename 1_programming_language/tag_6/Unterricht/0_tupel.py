""" 
Tupel: unverändlich, sequentiell
"""

# Tupel definiert man so
x = (1, 2, 3, 4)  # x = [1, 2]
y = 1, 2    # x = [1, 2]
z = (1,)
falscher_tupel = (1)  # das ist ein Integer!
z2 = 1,
leer_tuple = ()
print("Leerer Tupel:", type(leer_tuple))

# per Index addressieren
print("Tupel y an Index 0:", y[0])

# Slicing von Tupel erzeugt neuen Tupel
print("x[0:2]", x[:2], type(x[:2]))

# tupel als Key von Dict
m = {(0, 3): 1, (2, 1): 1, (2, 2): 1, (2, 3): 1, (4, 0): 1, (4, 6): 1}

# Tupel erstellen
literal = (2, 2, 4)

s = [1, 2, 3]
ts = tuple(s)
print("Tupel ts:", ts, type(ts))

# Tupel aus String
string = "king kong"
tupel_king = tuple(string)
print("Tupel tupel_king:", tupel_king, type(tupel_king))

# List aus String
string = "king kong"
string_king = list(string)
print("Tupel tupel_king:", string_king, type(string_king))
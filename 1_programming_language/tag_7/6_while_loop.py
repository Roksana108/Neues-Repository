""" 
While Loop: läuft solange, wie eine Bedinung wahr ist

while <BEDINGUNG_WAHR>:
    mach was

Endlosloop anhalten mit STRG+C
"""

if True:
    print("das ist wahr")

while False:
    print("das ist aber nicht wahr!")

while True:
    # das würde ohne break endlos laufen
    print("....")
    break

print("*" * 50)

counter = 1
THRESHOLD = 10

while counter <= THRESHOLD:
    print(f"{counter=}")
    counter += 1  # counter = counter + 1 / (in java: counter++)

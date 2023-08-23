import random

random_number = random.randint(1, 8)

# Aufgabe: in welchen Wertebereich fällt die Zahl
# a) 6-8
# b) 3-5
# c) 1-2

if random_number >= 6:
    print("die Zahl", random_number, "ist im Wertebereich a")
elif random_number >= 3:
    print("die Zahl", random_number, "ist im wertebereich b")
else:
    print("die Zahl", random_number, "ist im Wertebereich c")

# fstring
if random_number >= 6:
    print(f"die Zahl {random_number} ist im Wertebereich a")
elif random_number >= 3:
    print(f"die Zahl {random_number} ist im wertebereich b")
else:
    print(f"die Zahl {random_number} ist im Wertebereich c")

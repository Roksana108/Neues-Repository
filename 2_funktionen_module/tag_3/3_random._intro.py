"""
Pseudozufallszahlen mit random
Generator: https://de.wikipedia.org/wiki/Mersenne-Twister
"""

import random
import matplotlib.pyplot as plt

random.seed(42)  # default Startwert ist (meistens) der aktuelle Zeitstempel 
# INTEGER Zufalsszahl
print(f"Zufällige Ganzzahl zwischen 1 und 6: {random.randint(1, 6)}")
print(f"Zufällige Ganzzahl zwischen 1 und 6: {random.randint(1, 6)}")


# INTEGER Zufalsszahl (halboffenses Intervall) (7 ist exclusive)
print(f"Zufällige Ganzzahl zwischen 1 und 6: {random.randint(1, 7)}")
print(f"Zufällige Ganzzahl zwischen 1 und 6: {random.randint(1, 7)}")

# gerade Zahl zwischen 0 und 100
print(f"gerade Zahl zwischen 0 und 100: {random.randrange(0, 101, 2)}")

#  Liste von 100 geraden Zufallszahlen zwischen 0 und 100
numbers = [random.randrange(0, 101, 2) for _ in range(100)]
print(numbers)

# Häfigkeitswerte
plt.hist(numbers, bins=20)
plt.title = "Histogramm der Zufallszahlen"
plt.show()

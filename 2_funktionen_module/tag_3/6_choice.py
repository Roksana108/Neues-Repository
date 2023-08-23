"""
Zufälliger Zugriff auf eine Seqenz, mit Zurücklegen
"""

import random
from collections import Counter

random.seed(42)

rabbits = [
    "fiver",
    "hazel",
    "bigwig",
    "blackberry",
]

print("Zufälliges Kaninichen:", random.choice(rabbits))

# ---------------------------------------------------------
# Zufällige, gewichtete Kaninchen mit Zurücklegen
# ---------------------------------------------------------
weights = [10, 10, 40, 40]
weighted_elements = random.choices(rabbits, weights, k=1000)
c = Counter(weighted_elements)
print(c)
print("Die zwei häfigesten Kaninichen:",  c.most_common(2))
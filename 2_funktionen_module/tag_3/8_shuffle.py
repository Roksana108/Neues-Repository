"""
shuffle: Elemente durschmischen 
"""

import random


random.seed(42)

rabbits = [
    "fiver",
    "hazel",
    "bigwig",
    "blackberry",
]

x = random.shuffle(rabbits)  # Zuweisung von shuffle ist None
print(rabbits)
print(x)  # None
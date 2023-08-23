import random

A = [(a, True) if a % 2 == 0 else (a, False) for a in range(0, 100)]
print(A)
print("*" * 50)

# kartesische Produkt (Kreuzprodukt)
a = [1, 2]
b = [3, 4]

cart = []
for el_a in a:
    for el_b in b:
        cart.append((el_a, el_b))


# 
cart_prod = [(el_a, el_b) for el_a in a for el_b in b]
print(cart_prod)

# 3 x 3 Null-Matrix erzeugen OHNE list compri
p = 3
q = 3
result = [[0] * p] * q  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(result)

# 3 x 3 Null-Matrix erzeugen Mit list compri
result = [[0] * p for a in range(3)]
print(result)


# Spielkarten
colors = ["♠", "♥", "♣", "♦"]
values = ["K", "Q", "A", "J"]

french_deck = [(color, value) for color in colors for value in values]
print(french_deck)
random.shuffle(french_deck)
print(french_deck)

# eine Karte vom Stapel nehmen
card = french_deck.pop()
print(card)

# 5 Karten rauspoppen
cards = [french_deck.pop() for _ in range(5)]
print(cards)

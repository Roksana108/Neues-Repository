"""
Counter mit und ohne global
Besser als global ist expliziter Return und Zuweisung an neuen Wert
"""
c = 0


def counter():
    global c
    c += 1


def better_counter(n):
    n += 1
    return n


# global
counter()
counter()
counter()
print(c)


# ohne global
c = better_counter(c)
c = better_counter(c)
c = better_counter(c)
print(c)
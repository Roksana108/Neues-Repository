"""
Scope: global und lokal
"""
MAX_VAL = 43
x = 1  # global
y = 3  # global

# Alle globalen Variablen ausgeben
# print(globals())


def g():
    local_p = 43
    print("locals von g():", locals())


def fn():
    print(f"zugriff vom lokalen Scope auf {x=} {y=} aus globalem Scope")
    local_p = 42
    print("locals von fn():", locals())


fn()
g()
# print(f"Local_p aus einem lokalen Scope: {local_p}")

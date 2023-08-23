# Eingänge
A = False
B = False


"""
Implementiere das XOR-Gatter
# XOR Gatter: XOR ist wahr, wenn exklusiv A oder B wahr ist
#
A   B   A XOR B
0   0   0
0   1   1
1   0   1
1   1   0
"""
if A is not B:
    print("XOR true")
else:
    print("XOR false")

if A != B:
    print("XOR True")
else:
    print("XOR false")

"""
Ein NAND-Gatter gibt am Ausgang 0 aus, wenn alle Eingänge 1 sind.
In allen anderen Fällen, d. h., wenn mindestens ein Eingang 0 ist,
wird eine 1 ausgegeben.

A   B   A NAND B
0   0   1
0   1   1
1   0   1
1   1   0
"""
if not (A and B):
    print("NAND: 0")
else:
    print("NAND: 1")

# nor
# https://de.wikipedia.org/wiki/NOR-Gatter
"""
Ein NOR-Gatter gibt am Ausgang 1 aus, w
enn alle Eingänge 0 sind. In allen anderen Fällen,
d. h. wenn mindestens ein Eingang 1 ist, wird eine 0 ausgegeben.

A   B   A NOR B
0   0   1
0   1   0
1   0   0
1   1   0
"""

if not (A or B):
    print("nor(A, B) => True")
else:
    print("NOR ist False")

"""
Implementiere das XNOR-Gatter (exklusive not or) mit zwei Eingängen
https://de.wikipedia.org/wiki/XNOR-Gatter
Gibt eine 1 aus, wenn beide Eingänge entweder False oder beide Eingänge True
sind.

A   B   A XNOR B
0   0   1
0   1   0
1   0   0
1   1   1
"""

if A and B or (not A and not B):
    print("XNOR ist true")

if A and B or not (A or B):
    print("XNOR ist true")

if not (A ^ B):
    print("XNOR ist true")

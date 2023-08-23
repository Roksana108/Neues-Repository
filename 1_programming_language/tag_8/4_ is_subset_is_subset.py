""" 
issubset(): Prüfen, ob eine menge a eine Submenge von b ist.
"""
a = {"apple", "facebook"}
c = {"apple", "facebook"}
b = {"google", "microsoft", "apple", "facebook"}


if a.issubset(b):
    print("a ist eine Untermenge von b")

if a < b:
    print("a ist eine ECHTE Untermenge von b")

if a < c:
    print("a ist eine echte Untermenge von c (trifft nicht zu)")

if a <= c:
    print("a ist eine Untermenge von c (aber keine echte)")

print("*" * 40)

""" 
issuperset(): Prüfen, ob eine menge a eine Supermenge von b ist.
"""
a = {"apple", "facebook"}
c = {"apple", "facebook"}
b = {"google", "microsoft", "apple", "facebook"}

if b.issuperset(a):
    print("b ist eine Übermenge von a")

if b > a:
    print("b ist eine echte Übermenge von a")

if b >= a:
    print("b ist eine Übermenge von a")

if a > c:
    print("a ist eine echte Übermenge von c (trifft nicht zu)")

if a >= c:
    print("a ist eine Übermenge von c (trifft zu)")
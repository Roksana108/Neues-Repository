""" 
Darstellung von Zeichen und interne Speicherung
"""

string = "a"
print(f"Unicode Codepoint von a: {ord(string)}")

string = "ö"
print(f"Unicode Codepoint von ö: {ord(string)}")

if "a" < "ö":
    print("a ist kleiner als ö")

print(f"Unicode Codepoint von r: {ord('r')}")

word = "hallo"
print("Bytes von word:", list(bytes(word, encoding="ascii")))  # b'hallo'
# x = word.encode(encoding="ascii")

print("Bytes von Möwe:", list(bytes("Mowe", encoding="ascii")))
print("Bytes von Möwe:", list(bytes("Möwe", encoding="iso-8859-1")))  # [77, 246, 119, 101]
print("Bytes von Möwe:", list(bytes("Möwe", encoding="cp1252")))

# UTF-8 (konkrete Implementierung von Unicode)
oe = list(bytes("ö", encoding="utf-8"))
print("oe:", oe)

a = list(bytes("a", encoding="utf-8"))
print("a:", a)
""" 
Bitwise operators

Operatoren auf Bit-Ebene
& Bitwise AND
| Bitwise OR
^ Bitwise XOR
~ Bitwise NOT
>> right shift
<< left shift
"""
a = 8
print(f"8: {a:08b}")  # 1 Byte 00001000

for number in range(8 + 1):
    print(f"{number:08b}")

# -------------------------------------------------------------
# left shift
# -------------------------------------------------------------
x = 1  # 00000001
print(x << 1)  # 00000010
print(2 << 1)  # 00000100
print(4 << 1)  # 000001000
print(8 << 1)  # 000010000

p = 2
print("left shift:", p << 1)  # Bit um eine Stelle nach links verschieben: verdoppeln
print("mal 2:", p * 2)

# -------------------------------------------------------------
# right shift (Bits nach rechts verschieben)
# -------------------------------------------------------------
print("Zahl durch 2:", 24 // 2)  # Zahl durch zwei Teilen
print("Zahl durch 2:", 24 >> 1)  # Zahl durch zwei Teilen

# -------------------------------------------------------------
# & -> bitwise AND
# 00000101
# 11101111
# 00000101
# -------------------------------------------------------------
a = 8
b = 4
print(f"a & b: {a & b}")

# Ist eine Zahl eine Zweierpotenz? 2 ** x
n = 2 ** 9
print(f"n:    {n:016b}")
print(f"n-1:  {n-1:016b}")
print(f"n & (n-1): {n & (n-1)}")


if n & (n - 1) == 0:
    print("Zahl ist Zweierpotenz")

# 192.168.178.56
# Subnetz-Maske: 255.255.255.0
ip = 3232281144
subnet = 4294967040

print(f"IP Addresse:  {ip:032b}")
print(f"Subnetz-Maske: {subnet:032b}")
print(f"Netzwerk-Teil: {ip & subnet:032b}")
print(f"HOST-Teil: {ip & ~subnet:032b}")


# -------------------------------------------------------------
# | -> bitwise OR
# 00000101
# 11101111
# 11101111
# -------------------------------------------------------------
a = 17
b = 3
print(f"a | b: {a | b}")

# -------------------------------------------------------------
# ^ -> bitwise XOR
# 00000101
# 11101111
# 11101010
# -------------------------------------------------------------
a = 17
b = 3
print(f"a ^ b: {a ^ b}")

# -------------------------------------------------------------
# ~ -> bitwise not (unärer Operator)
# 00000101
# 11101111
# 11101111
# -------------------------------------------------------------
a = 8
print(f"~8: {~8:08b}")
print(~8)
""" 
Substrings (Slicing-Operator)

Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String

"""
string = "Teststring"
print("string[0:3] =>", string[0:3])  # Tes
print("string[:3] =>", string[:3])  # Tes
print("string[3:6] =>", string[3:6])  # tst
print("string[3:] =>", string[3:])  # tstring
print("string[:-1] =>", string[:-1])  # Teststrin
print("string[:-2] =>", string[:-2])  # Teststri

# --------------------------------------------
# 1. Argument: Start-Index
# 2. Argument: End-Index (exclusive)
# --------------------------------------------

"""
# Übung
# Schneide jeweils alle A aus den Strings
AAAAB => AAAA
"""
test = "AAAAB"
print(test[:-1])

"""
BBAAABBB => AAA
"""
test = "BBAAABBB"
print(test[2:5])

"""
AAAABBBB => AAAA
"""
test = "AAAABBBB"
print(test[:-4])

"""
BBAABBBB => AA
"""
test = "BBAABBBB"
print(test[2:-4])

print("*" * 40)

# --------------------------------------------
# Step Argument (Schrittweite angeben)
# --------------------------------------------
"""
ABABAB = AAA
"""
test = "ABABABABAB"
print(test[2:5:2])

# Aufgabe: schneide gerade zahlen aus der Reihen: 2468
numbers = "123456789"
print(numbers[1::2])

# --------------------------------------------
# negative Schrittweite
# --------------------------------------------
numbers = "123456789"
print(numbers[::-1])  # 987654321

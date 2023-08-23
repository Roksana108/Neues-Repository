"""
Eine als String (Text) dargestellte Binärzahl (0 und 1) soll dahingehend geprüft werden,
ob sie maximal eine Folge von Einsen enthält. Die Länge der Folge ist beliebig, sie kann also auch nur einem Element bestehen.
Dabei kann die Binärzahl auch vorangestellte Nullen enthalten.

Beispiele:
b = "1100"
Lösung: wahr => 1100 (1 Folge)

b = "1010"
Lösung: falsch => 1010 (2 Folgen)

b = "00111000"
Lösung: wahr => 00111000 (1 Folge)

b = "10000001"
Lösung: falsch => 10000001 (2 Folgen)

b = "1100011001"
Lösung: falsch => 1100011001 (3 Folgen)

die Binärzahl soll als input übergeben werden.
"""

b = "011101"

first_index = b.find("1")
if first_index >= 0 and b.find("01", first_index) >= 0:
    print("leider falsch")
else:
    print("wahr")

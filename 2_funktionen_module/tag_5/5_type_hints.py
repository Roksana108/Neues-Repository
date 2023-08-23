""" 
Listen von Elementen: Typehints von verschachtelten Elementen / Collections

weitere Datentypen finden sich im typing-Modul, zb. Final

list[int] => Liste von Integern
Final => Konstanten definieren
"""
from typing import Final

MAX: Final = 3
MAX += 3   # Konstante MAX verändert (Final meckert)

def my_dict(d: dict[str, list[int]]) -> int:
    """
    Key muss String sein
    Value muss Liste aus Ints sein
    """
    return 1


# Funktion soll integerliste sortieren
def sort_integers(seq: list[int]):
    ...


sort_integers([1, 2, 3])

# falsches Dict übergeben, da als Value eine Int-Liste erwartet wird,
# und kein int
d = {
    "a": 3
}
my_dict(d)
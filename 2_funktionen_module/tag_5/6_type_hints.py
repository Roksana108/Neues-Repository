""" 
Default Parameter mit Typehints. 
Verschiedene Datentypen als Return- oder Parameterwert mit |
"""
from typing import Optional

NUMBER_SET = set[int]
MATRIX = list[list[int]]


def num_set(n: NUMBER_SET):
    ...


n = set([1, 2, 3, "a"])
num_set(n)


def sum(a: int, b: int) -> int:
    return a + b


def caesar_decrypt(name: str, number: int = 1) -> Optional[str]:
    """number hat den default wert 1"""
    return 1.2


def caesar_decrypt(name: str, number: int = 1) -> str | None:
    """seit python 3.10 ist str | None möglich, Optional[str] nicht mehr."""
    return 1.2


caesar_decrypt("pete")
caesar_decrypt("pete", 1.2)  # Error, muss int sein

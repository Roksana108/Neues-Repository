"""
to iterate is human, to recurse divine.
Peter Deutsch (Ghostscript)
"""
import sys
import math

print(f"das aktuelle Rekursionslimit ist: {sys.getrecursionlimit()}")
# print(math.factorial(1))

def factorial(n: int) -> int:
    """Recursiv implementierte Fakultätsfunktion."""
    print(f"Factorial mit WErt: {n}")
    if n < 0:
        raise ValueError("negative Zahlen sind nicht erlaubt")
    elif n == 1 or n == 0:  # n in [0, 1]
        return 1
    else:
        result = n * factorial(n - 1)
        return result
    
    
def factorial2(n: int) -> int:
    """Recursiv implementierte Fakultätsfunktion."""
    if n < 0:
        raise ValueError("negative Zahlen sind nicht erlaubt")
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)


print(f"Ergebnis der Fakultät: {factorial2(3)}")
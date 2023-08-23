"""
Error "erheben", Fehler werfen
"""
import math

def ellipse_area(a: float, b: float) -> float:
    """Calculate area of ellipse.

    Args:
        a: (float): große Halbachse
        b: (float): kleine Halbachse
    
    Raises:
        ValueError if b > a

    Returns:
        area (float)
    """
    if b > a:
        raise ValueError(("Die kleine Halbachse darf nicht größer sein"
                          " als die große Halbachse."))

    return a * b * math.pi


a = 8
b = 4
try:
    area = ellipse_area(a=a, b=b)
    print(f"Die Fläche der Ellipse ist: {area:.2f}")
except ValueError:
    print("Nicht berechnbar")
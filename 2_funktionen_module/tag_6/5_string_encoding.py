import sys 

x = 3

try:
    y / 0
except ZeroDivisionError as e:
    print(f"Error-Objekt: {e}")
except (ValueError, NameError) as e:
    print(f"Value-Error oder Name-Error: {e}")
finally:
    print("finally wird immer ausgeführt")
    print("Guter Ort für Clean-Up Arbeiten")

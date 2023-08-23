"""
System-specific parameters and functions
argv = Argument Vector (liste der Argumente)

Ausführen mit:

python 3_sys_argv.py 42
"""
import sys

eingabewerte = sys.argv
print(f"{eingabewerte}", type(sys.argv))

print("Name des Programms:", sys.argv[0])
print("Ein Wert:", sys.argv[1])

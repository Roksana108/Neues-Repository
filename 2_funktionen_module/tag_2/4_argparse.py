""" 
Argparse: Parser for command-line options, arguments and sub-commands

python 4_argparse.py --help
python 4_argparse.py --name Otto  --age 23

Docs:
https://docs.python.org/3/library/argparse.html

gentle introduction:
https://docs.python.org/3/howto/argparse.html#argparse-tutorial
"""
import argparse

# 1. Parser instantiieren
parser = argparse.ArgumentParser()
parser.description = "Generiere ein Personenobjekt"

# 2. Definieren der Argumente
parser.add_argument(
    "--name", "-N", type=str, required=True, help="Vorname der Person" 
)

parser.add_argument(
    "--age", "-A", type=int, required=True, help="Alter der Person"
)

parser.epilog = "Usage Example: python 4_argparse.py --name Otto --age 12"

# 3. Argumente auslesen
args = parser.parse_args()


# Zugriff auf die Arugmente per args.VALUE
print("Der Name der Person:", args.name)  # --name
print("Das Alter der Person:", args.age)  # --age
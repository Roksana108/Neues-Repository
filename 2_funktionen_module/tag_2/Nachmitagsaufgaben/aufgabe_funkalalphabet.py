"""
Gruppenaufgabe: Funkalphabet Übersetzer

Worte sollen in ein Funk-Alphabet übersetzt werden. zum Beipiel das deutsche
Funkalphabet:
Hans
Heinrich – Anton – Nordpol - Samuel

https://de.wikipedia.org/wiki/Buchstabiertafel
https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

Natoformat
Julia
Juliett Uniform Lima India Alfa

Aufgabe:
Es soll ein Programm geschrieben werden, welches verschiedene Funk-Alphabete (deutsch, nato) einlesen kann. Der User kann während des Betriebs wählen, welches Funkalphabet er nutzen möchte. Die Alphabete liegen als txt-Dateien
in folgendem Format vor:

D Delta
E Echo
F Foxtrot
[..]

Nach Wahl des Funkalphabets kann der User Worte eingeben, die in
das gewählte Alphabet übersetzt werden.

Das Programm bzw. der Userinput läuft in einem while-Loop und terminiert erst bei Eingabe des Wortes _q bzw. _quit


folgende Funktionen sollen implementiert werden:
------------------------------------------------

def load_data_from_file(filename): => Daten aus der txt-Datei einlesen und
als geeignete Datenstruktur, zb. Dictionary als Returnwert zur Verfügung
stellen.

def translate(word, alphabet) => ein Wort in Abhängigkeit des gewählten
Alphabets (deutsch/nato/...) übersetzen und als String zurückgeben.

def choose_alphabet() => ein Sub-Programm zum wählen eines Alphabetes.
Rückgabewert ist das gewählte und geladene Alphabet (zum Beispiel als Dict.)

def main() => das Hauptprogramm

Bitte beachten!
Beispielhafter Ablauf:

Welcome to the phonetic alphabet Translator
Choose alphabet with _c or quit translator with _q
Please choose an alphabet from list to proceed:
D: Deutsches Funkalphabet
N: Nato Funkalphabet
Please choose Alphabet: D

you have chosen: Deutsches Funkalphabet
Enter: hans
Heinrich Anton Nordpol Samuel
Enter: _c
Please choose an alphabet from list to proceed:
D: Deutsches Funkalphabet
N: Nato Funkalphabet
Please choose Alphabet: N
you have chosen: Nato Funkalphabet
Enter: Julia
Juliet Uniform Lima India Alfa
Enter: _q
Goodbye
"""


from pathlib import Path


ALPHABETS = {
    "D": {
        "file": "deutsch.txt",
        "name": "Deutsches Funkalphabet",
    },
    "N": {
        "file": "nato.txt",
        "name": "Nato Funkalphabet",
    },
}
ALPHABETS_DIR = "alphabets"

REPLACEMENTS = {
    " ": " - ",
}

EXIT_WORDS = ["_q", "_quit"]
WORD_DELIMITER = " "
WELCOME_MSG = "Welcome to the Phonetic Alphabet Translator"


def load_data_from_file(filename):
    """Load data from file and build phonetic dict."""

    with open(
        Path(__file__).parent / ALPHABETS_DIR / filename, encoding="utf-8"
    ) as f:
        return dict([row.split() for row in f])


def translate(word, alphabet, replacements=REPLACEMENTS):
    """Translate word to phonetic alphabet.

    Args:
        word (str): Word to translate
        alphabet (dict): phonetic alphabet
        replacments (dict): optional replacement dict

    Returns:
        str: translated phonetic string

    Examples:
    >> translate('hn', {'h': 'Heinrich', 'n':'Nordpol'})
    Heinrich Nordpol
    """
    result = []
    alphabet |= replacements
    for char in word.upper():
        if char in alphabet:
            result.append(alphabet[char])

    return WORD_DELIMITER.join(result)


def choose_alphabet():
    """User Interface Function to choose an alphabet."""
    print("Please choose an alphabet from list to proceed:")
    print_alphabet_infos()
    while True:
        user_input = input("Please choose Alphabet: ").upper()
        if user_input in ALPHABETS:
            print(f"you have choosen: {ALPHABETS[user_input]['name']}")
            return load_data_from_file(ALPHABETS[user_input]["file"])
        print(f"Alphabet {user_input} not found, please try again!")


def print_alphabet_infos():
    output = []
    for key, value in ALPHABETS.items():
        output.append(f"{key}: {value['name']}")
    print("\n".join(output))


def main():
    print(WELCOME_MSG)
    print("Choose alphabet with _c or quit translator with _q")
    alphabet = choose_alphabet()

    while (user_input := input("Enter: ")) not in EXIT_WORDS:
        if user_input in ["_c", "_choose"]:
            alphabet = choose_alphabet()
            continue

        result = translate(user_input, alphabet)
        if result:
            print(result)
    else:
        print("Goodbye!")


main()

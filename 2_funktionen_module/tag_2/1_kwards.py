""" 
kwargs: keyword arguments
"""

# ----------------------------------------------------
# Funktion mit Keyword-Argumenten aufgerufen
# ----------------------------------------------------


def load_csv(filename, encoding):
    print(f"{filename=}, {encoding=}")


load_csv(filename="test.txt", encoding="iso-8859-1")
load_csv(encoding="iso-8859-1", filename="test.txt")

# ----------------------------------------------------
# kwargs: Unbestimmte Anzahl an Keywort-Argumenten
# ----------------------------------------------------


def values(**kwargs):
    # *args ist eine unbestimmte Anzahl an Argumenten
    print(f"Der Funktion wurden folgende Werte übergeben: {kwargs}, {type(kwargs)}")


values(encoding="utf-8", filename="test.txt")


# ----------------------------------------------------
# Keyword-Argumente erzwingen
# kewword-only mit *, alles was rechts vom * steht
# ----------------------------------------------------
def connect_to_database(*, username, password, database):
    print(f"{username=}, {password=}, {database=}")


connect_to_database(database="password",
                    username="fritzcat",
                    password="secret123")
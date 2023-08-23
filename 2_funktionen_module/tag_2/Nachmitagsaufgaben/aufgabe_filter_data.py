from pathlib import Path

FILE_IN = "log.txt"
FILE_OUT = "log_clean.txt"


def read_data(filename):
    """Einlesen der Datei und Auslesen der Daten. Es sollen Daten zurückgegeben
    werden.
    """
    with open(Path(__file__).parent / filename) as f:
        content = f.readlines()
        return content


def write_data(filename, data):
    """Die Daten sollen zeilenweise in eine Datei geschrieben werden."""

    data_linebreaks = [f"{line}\n" for line in data]
    with open(Path(__file__).parent / filename, mode="w") as f:
        f.writelines(data_linebreaks)


def filter_data(data):
    """Filter die Daten und befreie sie von unzulässigen Zeichen."""
    return [line.strip("#=*\n ") for line in data if line.strip()]


def main():
    """Hauptprogramm."""
    content = read_data(FILE_IN)
    cleaned_content = filter_data(content)
    write_data(FILE_OUT, cleaned_content)


main()

# Mit Hilfe des connectors ist es möglich, dass Sie mit einem
# Pythonprogramm eine Tabelle in einer Datenbank erstellen

import mysql.connector 


connection = mysql.connector.connect(
    host="localhost",
    database="my_database",
    user="root",
    password="12345"
)

print(connection)

query = """
CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    release_year INT
)
"""


def create_tabel(connection, query):  # Funktionsdefinition von der Zeile 26-35
    try:
        cursor = connection.cursor()
        cursor.execute(query)  # Es wird ein Zeiger auf die Datenbankverbindung gesetzt (cursor())
        connection.commit()
        print("Tabelle 'movies' wurde erfolgreich erstellt.")
    except Exception as e:
        print("Fehler beim Erstellen der Tabelle:", str(e))
    finally:
        cursor.close()
create_tabel(connection, query)  # Funktionsaufruf  

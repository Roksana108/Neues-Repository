# Schritt 2: Importieren der Variable connection aus my_sql_connection

# from my_sql_connection import connection

import mysql.connector

# Schritt 3: Definieren des SQL-Statements
query = "INSERT INTO movies (title, release_year, genre) VALUES (%s, %s, %s)"

# Schritt 4: Einträge für die Tabelle movies
movie_entries = [
    ("Movie 1", 2020, "Action"),
    ("Movie 2", 2018, "Comedy"),
    ("Movie 3", 2021, "Drama"),
    ("Movie 4", 2019, "Sci-Fi"),
    ("Movie 5", 2022, "Adventure")
]

# Schritt 5: Definieren der Funktion insert_data
def insert_data(connection, query, data):
    try:
        with connection.cursor() as cursor:
            cursor.executemany(query, data)
            connection.commit()
            print("Daten wurden erfolgreich eingefügt.")
    except Exception as e:
        print("Fehler beim Einfügen der Daten:", e)

# Schritt 6: Aufruf der Funktion insert_data
insert_data(connection, query, movie_entries)



# Schritt 7: Überprüfen der eingefügten Werte in der MySQL-Datenbank
# Hierzu können Sie SELECT-Statements verwenden, um die Daten aus der Tabelle movies abzufragen.
# Zum Beispiel:
# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM movies")
#     result = cursor.fetchall()
#     for row in result:
#         print(row)

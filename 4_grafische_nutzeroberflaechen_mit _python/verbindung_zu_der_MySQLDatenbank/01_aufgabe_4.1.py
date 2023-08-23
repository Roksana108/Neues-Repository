"""Aufgabe mysql_connection"""
# mysql_connection.py. Bei valider Verbindung wird der Speicherort der Verbindung ausgegeben hier:
# object at 0x0000024FA34C39D0>

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    database="my_database",
    user="root",
    password="12345"
)

print(connection)
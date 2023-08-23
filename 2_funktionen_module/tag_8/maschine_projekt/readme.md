# Projekt Machine Projekt

Wie man Module und Packages importiert, was Module und Packages sind.

Module:
--------
- jede Python-Datei ist ein Modul


Package
-----------
- ein Verzeichnis mit einem oder mehr Python-Modulen
- optional aber empfohlen eine __init__.py als Initialisierungdatei für das Package

Imports
---------
Beim Importieren gilt folgende Such-Reihenfolge:
- erst wird in sys.modules gesucht (u.U. vorgeladene Module)
- danach wird im sys.path nachgeguckt

Modul Importieren
==================
- import check
    check.checker()
    check.petname("otto")
- from check import checker
- from check import checker as checkeralias
- from check import * => keine gute Practice!
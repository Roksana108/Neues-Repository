""" QFormLayout
QFormLayout liefert das Layout für ein Formular, 
das für Eingabedialoge wie Registrierung | Login |Datenbankoperationen geeignet ist
Die Anzahl der Spalte ist bei dem QFormLayout auf zwei Spalten eingeschränkt
Das Layout kann mit anderen Layouts kombiniert werden
"""
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QApplication, QPushButton, QGridLayout, QWidget, QLabel, QFormLayout QLineEdit

class Window(QMainWindow):
    def __init__(self) ->None:
        super().__init__()
        self.setWindowTitle("QFormLayout Exmaple")
        self.setFixedSize(300, 100)
        
        self.container = QWidget()
        self.main_layout = QFormLayout()
        self.emailLabel = QLabel("E-Mail:")
        
        self.main_layout.addRow("Name", QLineEdit())
        self.main_layout.addRow(self.emailLabel, QLineEdit())
        
        self.container.setLayout(self.main_layout)
        self.set
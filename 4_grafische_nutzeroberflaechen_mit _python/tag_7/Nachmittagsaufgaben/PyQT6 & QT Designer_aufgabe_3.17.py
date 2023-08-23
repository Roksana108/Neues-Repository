#  Importieren von Klassen incl. impotiren das Modul load_ui aus PyQt6.uic

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


# Programmieren von Klasse MainWindow. QMainWindow ist Kindklasse von MainWindow
class MainWindow(QMainWindow):
    # Konstruktor
    def __init__(self) -> None:
        super(). __init__()
        # Methode loadUi() aufrufen und speichern in das Objektattribut ui
        self.ui = uic.load_ui.loadUi("aufhabe_3.15.ui", self)
        # Programmieren Objektattribut self.ui.buttonOk das Signal clicked mit dem Methodenobjekt action als Slot programmieren
        # Methode action programmieren
        self.ui.button_ok.clicked.connect(self.action)
        
    def action(self) -> None:
        print(self.ui.input_name.text())
        
        
# Erstellen des Objekts von Qapplication. Erzeugung eines grafischen Fensters mit PyQt6 
app = QApplication([])
# Erstellen des Objekt window der Klasse MainWindow
window = MainWindow()
# Methoden .show() und exec() aufrufen
window.show()
app.exec()
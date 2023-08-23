'''
PyQT6 & QT Designer
'''

# Klassen importieren incl. importieren der Klasse Ui_MainWindow aus dem Modul Login

from PyQt6.QtWidgets import QMainWindow, QApplication
from Login import Ui_MainWindow
#  from aufhabe_3.15 import Ui_MainWindow 

# Programmieren der Kalsse MainWindow
# MainWindow is eine Kindklasse von QMainWindow und Ui_MainWindow#


class MainWindow(QMainWindow, Ui_MainWindow):
    # Konstruktor
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)     # Aufrufen der Methode setUi()
        self.button_ok.clicked.connect(self.action)  # Methodenobjekt action als Slot. Objektattribut button_ok das Signal  
      
    def action(self, event) -> None:
        print(self.input_name.text())
     
     
# Erstellen des Objekts von Qapplication 
app = QApplication([])
# Erstellen des Objekt window der Klasse MainWindow
window = MainWindow()
# Methoden .show() und exec() aufrufen
window.show()
app.exec()
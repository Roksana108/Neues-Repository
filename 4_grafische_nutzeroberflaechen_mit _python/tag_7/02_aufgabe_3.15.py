# Klassen importieren incl. importieren der Kalsse Ui_MainWindow aus dem Modul Login

from PyQt6.QtWidgets import QMainWindow, QApplication
from Login import Ui_MainWindow
from aufhabe_3.15 import Ui_MainWindow 

# Programmieren der Kalsse MainWindow
# MainWindow is eine Kindklasse von QMainWindow und Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.button_ok.clicked.connect(self.action)
      
        def action(self, event):
            print(self.input_name.text())
     

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
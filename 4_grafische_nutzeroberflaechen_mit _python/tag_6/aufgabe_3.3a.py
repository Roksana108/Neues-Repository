"""OOP und PyQt6"""

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

# Erstellen der Klasse MainWindow. MainWindow is Kindklasse der Klasse QMainWindow
class MainWindow(QMainWindow):
    # Konstruktor
    def __init__(self) -> None:
        super().__init__()
        # Setzen den Titel der GUI "Meditation"
        self.setWindowTitle("Meditation")
        # Initialisieren von Objektattribut pushbutton der Klasse QPushButton mit dem Argument „Click me“
        self.pushbutton = QPushButton("Click me")
        # Setzen von MainWindow mit der Methode setCentralWidget() das Objektattribut pushbutton als zentrales Widget
        self.setCentralWidget(self.pushbutton)
        
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec() 
        
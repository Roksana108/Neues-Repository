"""OOP und PyQt6"""

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit

# Erstellen der Klasse MainWindow. MainWindow is Kindklasse der Klasse QMainWindow
class MainWindow(QMainWindow):
    # Konstruktor
    def __init__(self) -> None:
        super().__init__()
        # Setzen den Titel der GUI "Meditation"
        self.setWindowTitle("Meditation")
        # Ersetzen Sie das Objektattribut label durch das Objektattribut label der Klasse QLabel 
        self.label = QLineEdit("Click me")
        # Setzen von MainWindow mit der Methode setCentralWidget() das Objektattribut label als zentrales Widget
        self.setCentralWidget(self.label)
        
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec() 
        
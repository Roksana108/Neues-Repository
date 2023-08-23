"""QGridLayout"""

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QLabel, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.container = QWidget()
        self.main_layout = QGridLayout()
        
        self.label = QLabel("Label")
        self.button = QPushButton("Click just here")
        self.entry = QLineEdit()
        self.main_layout.addWidget(self.label, 0, 0)
        self.main_layout.addWidget(self.button, 0, 1)
        self.main_layout.addWidget(self.entry, 0, 2)
        
        self.container.setLayout(self.main_layout)
        self.setCentralWidget(self.container)
        
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.container = QWidget()
        self.main_layout = QVBoxLayout()
        
        self.label = QLabel("Label")
        self.button = QPushButton("Click")
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button)
        
        self.container.setLayout(self.main_layout)
        self.setCentralWidget(self.container)
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec() 
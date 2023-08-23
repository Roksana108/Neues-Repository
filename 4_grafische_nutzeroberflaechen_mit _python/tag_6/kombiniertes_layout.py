from turtle import width


from PyQt6.QtWidgets import (QApplication, QPushButton, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QGridLayout, QFormLayout, QLineEdit)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formular")
        self.setFixedSize(500, 300)

        self.container = QWidget()
        self.main_layout = QGridLayout()

        self.inner_widget1 = QWidget()
        self.inner_widget1_layout = QFormLayout()
        self.name = QLabel("Name")
        self.email = QLabel("E-Mail")
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.inner_widget1_layout.addRow(self.name, self.name_input)
        self.inner_widget1_layout.addRow(self.email, self.email_input)
        self.inner_widget1.setLayout(self.inner_widget1_layout)

        self.inner_widget2 = QWidget()
        self.inner_widget2_layout = QFormLayout()
        self.name = QLabel("Name")
        self.email = QLabel("E-Mail")
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.inner_widget2_layout.addRow(self.name, self.name_input)
        self.inner_widget2_layout.addRow(self.email, self.email_input)
        self.inner_widget2.setLayout(self.inner_widget2_layout)

        self.main_layout.addWidget(self.inner_widget1, 0, 0)
        self.main_layout.addWidget(self.inner_widget2, 0, 1)

        self.container.setLayout(self.main_layout)
        # WEITERE LAYOUTS
        self.setCentralWidget(self.container)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()

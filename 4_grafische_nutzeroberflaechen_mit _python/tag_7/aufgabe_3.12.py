
"""AUFGABE
    3.12
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QHBoxLayout, QWidget, QLabel


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog 3.12")
        self.button_type = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        
        # self.button_type1 = QPushButton("OK")
        # self.button_type2 = QPushButton("Cancel")

        self.button_box = QDialogButtonBox(self.button_type)
        self.main_layout = QHBoxLayout()

        self.main_layout.addWidget(self.button_box)
        self.setLayout(self.main_layout)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aufgabe 3.10")

        self.container = QWidget()
        self.main_layout = QHBoxLayout()

        self.button = QPushButton("Click!")
        self.label = QLabel("Content.")

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button)
        self.container.setLayout(self.main_layout)

        self.button.clicked.connect(self.on_click)
        self.setCentralWidget(self.container)

    def on_click(self):
        my_dialog = CustomDialog()
        my_dialog.setWindowTitle("New Dialog")
        result = my_dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            print("OK")
            self.label.setText("Clicked OK!")
        elif result == QDialog.DialogCode.Rejected:
            print("CANCEL")
            self.label.setText("Clicked Cancel!")
        self.button.setEnabled(False)
        


app = QApplication([])
window = MainWindow()
window.show()
app.exec()  
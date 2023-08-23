"""
QApplication & QWidget_    
"""

#  Importieren der Klassen QApplication und QWidget von Modul PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget

# Erstellen von dem Objekt der Klasse Qapplication mit leerem Array als Argument
app = QApplication([])
window = QWidget()  # Erstellen des Objekts window der Klasse QWidg
window.show()   # Aufrufen der Methode .show() des Objektes window 
app.exec()        # Aufrufen der Methode .exec() des Objektes app auf
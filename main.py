from PyQt5.QtWidgets import QApplication
from Window import Window
import sys

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())

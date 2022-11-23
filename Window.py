from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QMainWindow

from Speedometer import Speedometer
from Tachometer import Tachometer


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top= 150
        self.left= 150
        self.width = 1280
        self.height = 720
        self.InitWindow()
        self.speedometer = Speedometer(150)
        self.tachometer = Tachometer()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.speedometer.DrawSpeedometer(painter)
        self.speedometer.DrawArrow(painter)
        self.tachometer.DrawTachometer(painter)
        self.tachometer.DrawArrow(painter)

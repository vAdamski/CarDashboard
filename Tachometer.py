from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush

from ClockPointer import ClockPointer


class Tachometer:
    def __init__(self):
        self.engineRPM = 0
        self.centerX = 830
        self.centerY = 50
        self.size = 400

    def DrawTachometer(self, painter):
        painter.setPen(QPen(Qt.gray, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.drawEllipse(self.centerX, self.centerY, self.size, self.size)

    def DrawArrow(self, painter):
        arrow = ClockPointer(x = self.centerX, y = self.centerY, radius = (self.size / 2), painter = painter)
        arrow.DrawArrow(135)
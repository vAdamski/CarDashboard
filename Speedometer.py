import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush

from ClockPointer import ClockPointer


class Speedometer:
    def __init__(self, carSpeed):
        self.carSpeed = carSpeed
        self.centerX = 50
        self.centerY = 50
        self.size = 400

    def DrawSpeedometer(self, painter):
        #TODO: Create circle class to draw circle example Circle(x,y,r, painter) etc.
        painter.setPen(QPen(Qt.gray, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.drawEllipse(self.centerX, self.centerY, self.size, self.size)

    def DrawArrow(self, painter):
        arrow = ClockPointer(x = self.centerX, y = self.centerY, radius = (self.size / 2), painter = painter)
        arrow.DrawArrow(135)
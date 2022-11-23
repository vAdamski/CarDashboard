import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen


class ClockPointer:
    def __init__(self, x, y, radius, painter):
        self.centerX = x
        self.centerY = y
        self.radius = radius
        self.painter = painter

    def DrawArrow(self, angle):
        radian = (angle * math.pi) / 180
        arrowLenght = self.radius - 20
        startX, startY = self.centerX + self.radius, self.centerY + self.radius

        self.painter.setPen(QPen(Qt.red, 8, Qt.SolidLine))
        endPointX = self.centerX + self.radius + arrowLenght * math.cos(radian)
        endPointY = self.centerY + self.radius + arrowLenght * math.sin(radian)

        self.painter.drawLine(startX, startY, endPointX, endPointY)
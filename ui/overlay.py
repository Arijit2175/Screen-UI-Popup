from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap, QGuiApplication
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(350, 450)

        screen = QGuiApplication.primaryScreen().availableGeometry()

        x = screen.width() - self.width() - 20
        y = -self.height()           

        self.move(x, y)

        self.spiderman = QLabel(self)

        pixmap = QPixmap("assets/spidey.jpg")

        self.spiderman.setPixmap(
            pixmap.scaled(
                250,
                250,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self.spiderman.move(50, 0)

        self.animate_down()

    def animate_down(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()

        end_x = screen.width() - self.width() - 20
        end_y = 20

        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(1200)
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(QPoint(end_x, end_y))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        self.animation.start()
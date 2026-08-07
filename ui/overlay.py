from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(350, 450)
        self.move(100, 100)

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
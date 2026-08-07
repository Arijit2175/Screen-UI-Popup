from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spider Greeting")

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(350, 450)
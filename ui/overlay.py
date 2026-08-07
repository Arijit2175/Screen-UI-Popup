from PySide6.QtWidgets import QWidget, QLabel, QGraphicsOpacityEffect
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

        self.resize(520, 450)

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

        self.spiderman.move(250, 0)

        self.bubble = QLabel(self)

        bubble = QPixmap("assets/bubble.png")

        self.bubble.setPixmap(
            bubble.scaled(
                260,
                180,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self.bubble.move(130, 150)

        self.bubbleOpacity = QGraphicsOpacityEffect()
        self.bubble.setGraphicsEffect(self.bubbleOpacity)
        self.bubbleOpacity.setOpacity(0)

        self.greeting = QLabel(
            "What's up,\nArijit!",
            self.bubble
        )

        self.greeting.setAlignment(Qt.AlignCenter)
        self.greeting.setWordWrap(True)

        self.greeting.setStyleSheet("""
        QLabel{
            color:white;
            background:transparent;
            font-family:"Comic Sans MS";
            font-size:16px;
            font-weight:bold;
        }
        """)

        self.greeting.setGeometry(
            3,
            36,
            190,
            95
        )

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

        self.animation.finished.connect(self.showGreeting)

        self.animation.start()

    def showGreeting(self):

        self.bubbleFade = QPropertyAnimation(
            self.bubbleOpacity,
            b"opacity"
        )

        self.bubbleFade.setDuration(500)
        self.bubbleFade.setStartValue(0)
        self.bubbleFade.setEndValue(1)
        self.bubbleFade.setEasingCurve(QEasingCurve.OutQuad)

        self.bubbleFade.start()
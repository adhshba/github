import sys

from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAbstractButton, QRadioButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QMainWindow, QButtonGroup
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('untitled.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()


    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for _ in range(10):
            x = randint(0, 100)
            qp.drawEllipse(randint(0, 800), randint(0, 600), x, x)

    def paint(self):
        self.flag = True
        self.repaint()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
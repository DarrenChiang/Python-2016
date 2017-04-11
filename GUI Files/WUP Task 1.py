import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class TitleSwitcher(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title = 'No Button Pressed'

    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color:white;')
        self.setWindowTitle(self.title)

        self.btnA = QPushButton('Button A', self)
        self.btnA.clicked.connect(self.setTitleA)
        self.btnA.move(20,20)

        self.btnB = QPushButton('Button B', self)
        self.btnB.clicked.connect(self.setTitleB)
        self.btnB.move(20, 100)

        self.show()

    def setTitleA(self):
        self.setWindowTitle('Button A Pressed')

    def setTitleB(self):
        self.setWindowTitle('Button B Pressed')

app = QApplication(sys.argv)

w = TitleSwitcher()
w.init()

sys.exit(app.exec_())

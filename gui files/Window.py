import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Simple_Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color:white;')
        self.setWindowTitle('GUI')
        self.setWindowIcon(QIcon('DefaultIcon.png'))
        self.btn1 = QPushButton('Button', self)
        self.show()

app = QApplication(sys.argv)

w = Simple_Window()
w.init()

sys.exit(app.exec_())

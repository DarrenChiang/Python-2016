import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap

class LabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('gui demo')

        self.label1 = QLabel(self)
        self.label1.setText('text')
        self.label1.move(300, 40)

        self.label2 = QLabel(self)
        self.label2.setToolTip('http://goo.gl/p89kmb')
        self.label2.setText("<a href='http://goo.gl/p89kmb'>Surprise URL </a>")
        self.label2.move(390, 90)
        self.label2.setOpenExternalLinks(True)

        self.label3 = QLabel(self)
        self.label3.move(80, 130)
        self.label3.setPixmap(QPixmap('DefaultIcon.png'))

        self.show()

app = QApplication(sys.argv)
w = LabelDemo()
exit(app.exec_())

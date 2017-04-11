import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDockWidget, QPushButton

class DockTest(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.floating = True
        self.movable = True

    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color:white;')
        self.setWindowTitle('Dock Test')

        self.dock = QDockWidget('Dock Thing', self)
        self.dock.setFloating(self.floating)
        self.dock.move(20, 100)

        self.btn1 = QPushButton('Change Dock Float', self)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.changeFloat)

        self.btn2 = QPushButton('This is on the QDock', self)
        self.btn2.move(20, 20)
        self.dock.setWidget(self.btn2)

        self.show()

    def changeFloat(self):
        self.floating = not self.floating
        if not self.floating:
            self.dock.move(20, 100)
        self.dock.setFloating(self.floating)


app = QApplication(sys.argv)

w = DockTest()
w.init()

exit(app.exec_())

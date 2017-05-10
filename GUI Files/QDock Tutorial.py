import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDockWidget, QPushButton
import PyQt5.QtCore

class DockTest(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.floating = False
        self.closable = True

    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color:white;')
        self.setWindowTitle('Dock Test')

        self.dock = QDockWidget('Dock Thing', self)
        self.dock.setFloating(self.floating)
        self.dock.setFeatures(self.dock.DockWidgetClosable|self.dock.DockWidgetMovable)
        self.dock.move(20, 160)

        self.dock2 = QDockWidget('Second Dock', self)
        self.dock2.setFloating(True)
        self.dock2.move(20, 80)

        self.btn1 = QPushButton('Change Dock Closable', self)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.changeClosable)

        self.btn2 = QPushButton('This is on the QDock', self)
        self.btn2.move(20, 20)
        self.btn2.clicked.connect(self.changeFloat)
        self.dock.setWidget(self.btn2)

        self.show()

    def changeFloat(self):
        self.floating = not self.floating
        if not self.floating:
            self.dock.move(20, 160)
        self.dock.setFloating(self.floating)

    def changeClosable(self):
        self.closable = not self.closable
        if self.closable:
            self.dock.setFeatures(self.dock.DockWidgetClosable|self.dock.DockWidgetMovable)
            self.dock2.setFeatures(self.dock.DockWidgetClosable|self.dock.DockWidgetFloatable)
        else:
            self.dock.setFeatures(self.dock.DockWidgetMovable)
            self.dock2.setFeatures(self.dock.DockWidgetFloatable)

app = QApplication(sys.argv)

w = DockTest()
w.init()

exit(app.exec_())

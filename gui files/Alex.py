import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon

class CheckBoxDemo(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def init(self):
        self.setGeometry(400, 400, 450, 350)
        self.setWindowTitle('Default')

        self.cBox = QCheckBox('This is a checkbox', self)
        self.cBox.move(100, 100)
        self.cBox.resize(300, 100)
        self.cBox.stateChanged.connect(self.dosomething)
        self.cBox.setTristate(True) #allowing tristate
        self.cBox.setWindowIcon(QIcon('DefaultIcon.png'))

        self.btn1 = QPushButton('Button', self)
        self.btn1.move(20, 100)
        self.btn1.clicked.connect(self.reset)

        self.btn2 = QPushButton('Enable/Disable', self)
        self.btn2.move(20, 200)
        self.btn2.clicked.connect(self.able)

        self.show()

    def dosomething(self):
        '''
        if self.cBox.isChecked():
            self.setWindowTitle('Checked')
        else:
            self.setWindowTitle('Not Checked')
        '''
        state = self.cBox.checkState()
        if state == 0:
            self.setWindowTitle('0')
        elif state == 1:
            self.setWindowTitle('1')
        elif state == 2:
            self.setWindowTitle('2')

    def reset(self):
        self.cBox.setChecked(False)

    def able(self):
        if self.cBox.isEnabled():
            self.cBox.setEnabled(False)
        else:
            self.cBox.setEnabled(True)

app = QApplication(sys.argv)

w = CheckBoxDemo()
w.init()

exit(app.exec_())
        

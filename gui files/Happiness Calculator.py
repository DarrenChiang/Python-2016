import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDoubleSpinBox
from PyQt5.QtGui import QIcon
import math

class Simple_Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.hours_slept = 0
        self.happiness = 0

    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color:white;')
        self.setWindowTitle('Happiness Calculator')
        self.setWindowIcon(QIcon('DefaultIcon.png'))
        
        self.btn1 = QPushButton('Calculate Happiness', self)
        self.btn1.clicked.connect(self.calculate_happiness)
        self.btn1.move(20, 80)

        self.text1 = QDoubleSpinBox(self)
        self.text1.setSuffix(' hours slept')
        self.text1.setMinimum(0)
        self.text1.setDecimals(5)
        self.text1.move(20, 40)
        
        self.btn2 = QPushButton('Calculate Hours Slept', self)
        self.btn2.clicked.connect(self.calculate_hours_slept)
        self.btn2.move(20, 180)

        self.text2 = QDoubleSpinBox(self)
        self.text2.setSuffix(' happiness')
        self.text2.setMaximum(10)
        self.text2.setMinimum(0.0001)
        self.text2.setDecimals(5)
        self.text2.move(20, 140)
        
        self.show()

    def calculate_happiness(self):
        self.hours_slept = self.text1.value()
        self.happiness = 10 * 2 ** (-1 * abs(self.hours_slept - 7))
        self.text2.setValue(self.happiness)

    def calculate_hours_slept(self):
        self.happiness = self.text2.value()
        self.hours_slept = math.log(self.happiness / 10, 2) + 7
        self.text1.setValue(self.hours_slept)

app = QApplication(sys.argv)

w = Simple_Window()
w.init()

sys.exit(app.exec_())

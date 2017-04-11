import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

class GradeCalculator(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.numGrade = 100

    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color:white;')
        self.setWindowTitle('Grade Calculator')

        self.line = QLineEdit(self)
        self.line.setText(str(self.numGrade))
        self.line.move(20, 20)

        self.text = QPushButton('Calculate Grade', self)
        self.text.move(20, 100)
        self.text.clicked.connect(self.calculate)

        self.show()

    def calculate(self):
        grades = ['A+', 'A', 'B', 'C', 'D', 'F ', 'F ', 'F ', 'F ', 'F ', 'F ']
        var = ['-', '', '+']
        letter = ''
        self.numGrade = int(self.line.text())
        temp = int(self.numGrade / 10)
        letter += grades[10 - temp]
        temp = int(self.numGrade % 10)
        print(abs(int((temp - 1) / 3)))
        letter += var[abs(int((temp - 1) / 3))]
        self.text.setText(letter[0 : 2])
                
            

app = QApplication(sys.argv)

w = GradeCalculator()
w.init()

sys.exit(app.exec_())

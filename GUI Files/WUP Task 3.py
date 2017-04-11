import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QComboBox

class Scrollbar(QWidget):
    def __init__(self, filename):
        QWidget.__init__(self)
        self.file = open(filename, 'r')
        self.data = []

    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color:white;')
        self.setWindowTitle('Scrollbar Text Reader')

        self.output = QLineEdit(self)
        self.output.setText('1')
        self.output.move(20, 120)
        self.output.setReadOnly(True)

        self.input = QComboBox(self)
        self.input.move(20, 20)
        for line in self.file:
            self.data.append(line.split())
            self.input.addItem(line.split()[0])
            
        self.input.currentIndexChanged.connect(self.select)

        self.show()

    def select(self):
        a = self.input.currentText()
        b = ''
        for i in self.data:
            if i[0] == a:
                b = i[1]
                break
        self.output.setText(b)


app = QApplication(sys.argv)

w = Scrollbar('WUP Task 3 Text.txt')
w.init()

sys.exit(app.exec_())

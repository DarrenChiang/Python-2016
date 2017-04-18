import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate

class Calendar(QWidget):
    def __init__(self):
        super(Calendar, self).__init__()
        self.init()

    def init(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Calender Demo')

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.showDate)

        self.lab = QLabel(self)

        date = self.cal.selectedDate()
        self.lab.setText(date.toString())
        self.lab.move(20, 300)

        self.show()

    def showDate(self, date):
        self.lab.setText(date.toString())

app = QApplication(sys.argv)
w = Calendar()
exit(app.exec_())

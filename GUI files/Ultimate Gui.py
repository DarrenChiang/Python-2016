import sys
import time
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CountDown(QThread):
    set_max = pyqtSignal(int)
    update = pyqtSignal(int)
    
    def __init__(self, widget, text):
        super().__init__()
        self.deadline = None
        self.duration = None
        self.progress = None
        self.indicator = widget
        self.text = text

    def checkEarliest(self, earliest):
        if self.deadline != earliest:
            self.deadline = earliest
            self.start()

    def getDuration(self):
        current = datetime.datetime.now()

        f = self.deadline.date_numeral().split()
        final = datetime.datetime(int(f[2]), int(f[0]), int(f[1]))

        if final > current:
            dur = final - current
            return int(dur.days * 24 + dur.seconds / 3600)
        else:
            return 0

    def __del__(self):
        self.wait()

    def run(self):
        self.duration = self.getDuration()
        self.update.emit(self.duration)
        
        for i in range(1, 101):
            self.indicator.setText(self.text + ' ' + str(int(self.duration - i * 0.01 * self.duration)) + ' hours')
            self.progress = i
            self.update.emit(i)
            time.sleep(0.1)
        self.terminate()


class Deadline():
    month = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    def __init__(self, i, name, date, gui):
        self.name = name
        self.date = date
        self.id = i
        self.checkbox = QCheckBox(self.name + ' ' + self.date.toString(), gui)

    def date_numeral(self):
        num = self.date.toString().split()
        for i in range(len(self.month)):
            if num[1] == self.month[i]:
                return str(i) + ' ' + num[2] + ' ' + num[3]
        return None

class Ultimate_GUI(QTabWidget):
    def __init__(self):
        super().__init__()
        self.newDate = None
        self.deadlines = []
        self.dID = 1
        self.thread = None
        self.init()

    def init(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('MySchedule')

        self.tab1 = QWidget(self)
        self.addTab(self.tab1, 'Remaining Time')
        self.set_tab1()

        self.tab2 = QWidget(self)
        self.addTab(self.tab2, 'View Dates')
        self.set_tab2()

        self.show()

    def set_tab1(self):
        layout = QFormLayout()
        
        self.countDown = QLabel(self)
        self.text1 = 'Time until next deadline: '
        self.countDown.setText(self.text1)
        layout.addWidget(self.countDown)

        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)

        self.dock = QDockWidget('List', self)
        self.dock.setFloating(False)
        self.dock.setFeatures(self.dock.DockWidgetFloatable)
        self.setDock()
        layout.addWidget(self.dock)
        
        self.tab1.setLayout(layout)

    def set_tab2(self):
        layout = QFormLayout()
        
        self.cal = QCalendarWidget(self)
        self.cal.clicked[QDate].connect(self.chooseDate)
        layout.addWidget(self.cal)

        self.text2 = QLineEdit(self)
        self.text2.setPlaceholderText('Enter Description')
        layout.addWidget(self.text2)

        self.button1 = QPushButton('Create Deadline', self)
        self.button1.clicked.connect(self.createDeadline)
        layout.addWidget(self.button1)
        
        self.tab2.setLayout(layout)

    def setDock(self):
        self.dockWindow = QWidget(self)
        self.dockLayout = QFormLayout()
        
        self.button2 = QPushButton('Clear Checked', self)
        self.button2.clicked.connect(self.deleteDeadlines)
        self.dockLayout.addWidget(self.button2)
        
        
        self.dockWindow.setLayout(self.dockLayout)
        
        self.dock.setWidget(self.dockWindow)

    def chooseDate(self, date):
        self.newDate = date

    def createDeadline(self):
        if self.text2.text() != '' and self.newDate != None:
            self.deadlines.append(Deadline(self.dID, self.text2.text(), self.newDate, self))
            self.dockLayout.addWidget(self.findDeadline(self.dID).checkbox)
            self.setCountdown(self.findDeadline(self.dID))
            self.dID += 1
            self.text2.setText('')

    def findDeadline(self, iD):
        for d in self.deadlines:
            if d.id == iD:
                return d
        return None
                                  
    def deleteDeadlines(self):
        self.setDock()
        for i in range(len(self.deadlines) - 1, -1, -1):
            if self.deadlines[i].checkbox.checkState():
                self.deadlines.remove(self.deadlines[i])
            else:
                self.dockLayout.addWidget(self.deadlines[i].checkbox)

    def findEarliest(self):
        earliest = self.deadlines[0].date_numeral().split()
        deadline = self.deadlines[0]
        for d in self.deadlines:
            date = d.date_numeral().split()
            if date[0] < earliest[0]:
                earliest = date
                deadline = d
            elif date[0] == earliest[0] and date[1] < earliest[1]:
                earliest = date
                deadline = d
        return deadline

    def setCountdown(self, deadline):
        self.thread = CountDown(self.countDown, self.text1)
        self.thread.set_max.connect(self.progressBar.setMaximum)
        self.thread.update.connect(self.progressBar.setValue)
        self.thread.checkEarliest(deadline)


app = QApplication(sys.argv)
w = Ultimate_GUI()

exit(app.exec_())

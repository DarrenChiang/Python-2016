import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal

class ProgressBar(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.init()
        self.thread = Thread()
        self.thread.set_max.connect(self.set_max)
        self.thread.update.connect(self.set_value)

    def init(self):
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('ProgressBar')

        self.pb = QProgressBar(self)
        self.pb.move(50, 200)
        self.pb.resize(150, 10)

        self.btn1 = QPushButton('Start', self)
        self.btn1.resize(150, 40)
        self.btn1.move(50, 50)
        self.btn1.clicked.connect(self.start)

        self.btn2 = QPushButton('Stop', self)
        self.btn2.resize(150, 40)
        self.btn2.move(50, 100)
        self.btn2.clicked.connect(self.stop)

        self.show()

    def start(self):
        self.thread.start()

    def stop(self):
        self.thread.terminate()

    def set_max(self, data):
        self.pb.setMaximum(data)

    def set_value(self, data):
        self.pb.setValue(data)

class Thread(QThread):
    set_max = pyqtSignal(int)
    update = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        self.update.emit(100)
        for i in range(1, 101):
            self.update.emit(i)
            time.sleep(0.01)

app = QApplication(sys.argv)
w = ProgressBar()
exit(app.exec_())

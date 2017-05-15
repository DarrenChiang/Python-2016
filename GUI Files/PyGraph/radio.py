import sys
import math
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraphdev.pyqtgraph as pt
from pyqtgraphdev.pyqtgraph import PlotWidget
import numpy as np
import time

class TrigGraph(QDockWidget):
    def __init__(self, t, n, parent = None):
        super(TrigGraph, self).__init__(parent = parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName('Graph ' + str(n))
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.host.setMinimumSize(500, 200)

        self.setWindowTitle(str(t))

        self.graph = PlotWidget(self)
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName(t + ' Graph')
        self.graph.raise_()

        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), e.size().height())

class CosGraph(TrigGraph):
    def __init__(self):
        super(CosGraph, self).__init__('Cosine', 1)

    def plot(self, data):
        X = data['X']
        fm = data['fm']
        Y = [math.cos(2 * math.pi * fm * x) for x in X]
        self.graph.clear()
        self.graph.plot(X, Y, clear = True)

class SinGraph(TrigGraph):
    def __init__(self):
        super(SinGraph, self).__init__('Sine', 2)

    def plot(self, data):
        X = data['X']
        a = data['a']
        fc = data['fc']
        Y = [a * math.sin(2 * math.pi * fc * x) for x in X]
        self.graph.clear()
        self.graph.plot(X, Y, clear = True)

class RadioGraph(TrigGraph):
    def __init__(self):
        super(RadioGraph, self).__init__('Radio', 3)

    def plot(self, data):
        X = data['X']
        m = data['m']
        a = data['a']
        fc = data['fc']
        fm = data['fm']
        Y = [(1 + m * math.cos(2 * math.pi * fm * x)) * a * math.sin(2 * math.pi * fc * x) for x in X]
        self.graph.clear()
        self.graph.plot(X, Y, clear = True)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent = parent)
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.cosDock = CosGraph()
        self.sinDock = SinGraph()
        self.radioDock = RadioGraph()
        self.addDockWidget(Qt.RightDockWidgetArea, self.cosDock)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sinDock)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.radioDock)
        self.plot()

    def plot(self):
        data = {'fc': 1, 'fm': 0.1, 'a': 5, 'X': np.arange(0, 20, 0.01), 'm': 3}
        self.cosDock.plot(data)
        self.sinDock.plot(data)
        self.radioDock.plot(data)

class SandBoxApp(QtWidgets.QApplication):
    def __init__(self, *args, **kwargs):
        super(SandBoxApp, self).__init__(*args)
        self.mainwindow = MainWindow()
        self.mainwindow.setGeometry(50, 100, 1200, 600)
        self.mainwindow.show()

        self.mainwindow.setContextMenuPolicy(Qt.NoContextMenu)

def main():
    app = SandBoxApp(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

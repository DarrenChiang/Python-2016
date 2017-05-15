import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraphdev.pyqtgraph as pt
from pyqtgraphdev.pyqtgraph import PlotWidget
import numpy as np
import time

class HistGraph(QDockWidget):
    def __init__(self, parent = None):
        super(HistGraph, self).__init__(parent = parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName('Host Hist')
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.host.setMinimumSize(500, 200)

        self.graph = PlotWidget()
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName('hsplot')
        self.graph.raise_()

        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def plot(self, data):
        Y = data['Y']
        y, x = np.histogram(Y)
        self.graph.clear()
        self.graph.plot(x, y, stepMode = True, fillLevel = 0, brush = (0 , 0, 255, 255))

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), e.size().height())
        
class MainGraph(QDockWidget):
    def __init__(self, parent = None):
        super(MainGraph, self).__init__(parent = parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName('Host Graph')
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.host.setMinimumSize(500, 200)

        self.graph = PlotWidget(self)
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName('grplot')
        self.graph.raise_()

        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def plot(self, data):
        X = data['X']
        Y = data['Y']
        colorLine = data['pen']
        self.graph.plot(X, Y, pen = colorLine, clear = True)

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), e.size().height())

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent = parent)
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.dockGraph = MainGraph()
        self.dockHist = HistGraph()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockGraph)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockHist)
        self.update()

    def update(self):
        Npoints = 500
        X = np.arange(Npoints)
        Y = np.random.poisson(5.0, Npoints)
        C = pt.hsvColor(time.time() / 5 % 1, alpha = 0.5)

        pen = pt.mkPen(color = C, width = 2)
        data = {'X': X, 'Y': Y, 'pen': pen}
        self.dockGraph.plot(data)
        self.dockHist.plot(data)
        QtCore.QTimer.singleShot(100, self.update)

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

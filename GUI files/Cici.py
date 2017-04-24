import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTabWidget, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, QCheckBox

class Tab_Demo(QTabWidget):
    def __init__(self):
        super(Tab_Demo, self).__init__()
        self.init()

    def init(self):

        
        self.tab1 = QWidget(self)
        self.addTab(self.tab1, 'Contact Details')

        self.tab2 = QWidget(self)
        self.addTab(self.tab2, 'Personal Details')

        self.tab3 = QWidget(self)
        self.addTab(self.tab3, 'Educational Details')

        self.tab4 = QWidget(self)
        self.addTab(self.tab4, 'Family Details')

        self.tab_1()
        self.tab_2()
        self.tab_3()
        self.tab_4()

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

        self.show()

    def tab_1(self):
        layout = QFormLayout()
        layout.addRow('First Name', QLineEdit())
        self.tab1.setLayout(layout)

    def tab_2(self):
        layout = QFormLayout()
        gender = QHBoxLayout()
        gender.addWidget(QRadioButton('Male'))
        gender.addWidget(QRadioButton('Female'))
        layout.addRow(QLabel('Gender'), gender)
        self.tab2.setLayout(layout)

    def tab_3(self):
        layout = QFormLayout()
        layout.addWidget(QLabel('Majors'))
        layout.addWidget(QCheckBox('Engineering'))
        layout.addWidget(QCheckBox('Psychology'))
        layout.addWidget(QCheckBox('Others'))
        self.tab3.setLayout(layout)

    def tab_4(self):
        layout = QFormLayout()
        layout.addRow('Female Guardian', QLineEdit())
        layout.addRow('Male Guardian', QLineEdit())
        self.tab4.setLayout(layout)

    def closeTab(self, currentIndex):
        currentWidget = self.widget(currentIndex)
        currentWidget.deleteLater()
        self.removeTab(currentIndex)

    
app = QApplication(sys.argv)
w = Tab_Demo()
exit(app.exec_())

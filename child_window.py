import math
import sys

from child import Ui_Form
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChildWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.res = 0
        self.forge_link()


    def forge_link(self):

        week = self.week.value()
        self.ok_1.clicked.connect(self.finishinput1)
        self.ok_2.clicked.connect(self.finishinput2)
        self.ok_3.clicked.connect(self.finishinput3)
        self.Reset.clicked.connect(self.reset)

    def finishinput1(self):
        self.res += float(self.p_1.text())
        self.result.display(self.res)
    def finishinput2(self):
        self.res += float(self.p_2.text())
        self.result.display(self.res)
    def finishinput3(self):
        self.res += float(self.p_3.text())
        self.result.display(self.res)

    def reset(self):
        self.p_1.setText('0')
        self.p_2.setText('0')
        self.p_3.setText('0')
        self.week.setValue(0)
        self.result.display(0)
        self.res = 0

if __name__== '__main__':
    app = QApplication(sys.argv)

    childwindow = ChildWindow()
    childwindow.show()
    sys.exit(app.exec_())

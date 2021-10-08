# 养老金计算

from midlife import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import numpy as np
import sys

class MidlifeWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forge_link()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def forge_link(self):
        self.ok.clicked.connect(self.finishinput)
        self.reset.clicked.connect(self.Reset)
        self.close.clicked.connect(self.Close)

    def finishinput(self):
        if self.check_1.isChecked():
            month = 139
        else:
            month = 195

        salary = float(self.salary.text())
        avg = float(self.avg.text())
        year = float(self.year.text())
        sum = float(self.sum.text())

        result = salary*(1+avg)/2*year*0.01 + sum/month

        self.lcdNumber.display(result)

    def Reset(self):
        self.salary.setText('0')
        self.avg.setText('0')
        self.year.setText('0')
        self.sum.setText('0')
        self.lcdNumber.display(0)

    def Close(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    midlifewindow = MidlifeWindow()
    midlifewindow.show()
    sys.exit(app.exec_())

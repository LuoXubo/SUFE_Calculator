# 个税缴纳模块

import sys

from midlife2 import Ui_Form
from PyQt5.QtWidgets import *

class Midlife2Window(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forge_link()

    def forge_link(self):
        self.ok.clicked.connect(self.Finish)
        self.reset.clicked.connect(self.Reset)

    def Finish(self):
        money = [0, 3000, 12000, 25000, 35000, 55000, 80000]
        rate = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
        result = 0

        salary = float(self.salary.text())
        minus = float(self.minus.text())
        children = float(self.children.text())
        olds = float(self.olds.text())
        divide = float(self.divide.text())

        res = salary - minus - children*1000 - min(1000.0, 2000.0/(divide+1))*min(1,olds)
        if res<5000:
            result = 0
        else:
            for i in range(6):
                if res >= money[i]:
                    result += (min(res,money[i+1])-money[i]) * rate[i]
                else:
                    break
            result += min(res-money[6], 0) * rate[6]

        self.lcd.display(result)

    def Reset(self):
        self.lcd.display(0)
        self.salary.setText('0')
        self.minus.setText('0')
        self.children.setText('0')
        self.olds.setText('0')
        self.divide.setText('0')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mid2 = Midlife2Window()
    mid2.show()
    sys.exit(app.exec_())

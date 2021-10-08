from midlife3 import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class Midlife3Window(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forge_link()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def forge_link(self):
        self.ok.clicked.connect(self.Finish)
        self.reset.clicked.connect(self.Reset)
        self.close_2.clicked.connect(self.Close)

    def Finish(self):
        total = float(self.total.text())
        rate = float(self.rate.text())
        year = float(self.year.text())

        mrate = rate/12/100
        mcnt = year * 12

        mp = (total * mrate * (1+mrate) ** mcnt) / ((1+mrate)**mcnt - 1)
        sum = mp*mcnt - total
        self.lcd1.display(mp)
        self.lcd2.display(sum)

    def Reset(self):
        self.total.setText('0')
        self.rate.setText('0')
        self.year.setText('0')
        self.lcd1.display(0)
        self.lcd2.display(0)

    def Close(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mid3 = Midlife3Window()
    mid3.show()
    sys.exit(app.exec_())

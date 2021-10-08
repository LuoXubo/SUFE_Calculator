import math
import sys

from child import Ui_widget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ChildWindow(QMainWindow, Ui_widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forge_link()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, True)


    def forge_link(self):

        self.ok.clicked.connect(self.finishinput)
        self.Reset.clicked.connect(self.reset)
        self.close.clicked.connect(self.Close)

    def finishinput(self):

        bpd = float(self.p_1.text())
        ac = float(self.p_2.text())
        fl = float(self.p_3.text())
        res = 1.635 - 0.0034*ac*fl + 0.0316*bpd + 0.0457*ac + 0.05*fl - 0.000992*fl*ac
        self.result.display(res)

    def reset(self):
        self.p_1.setText('0')
        self.p_2.setText('0')
        self.p_3.setText('0')
        self.result.display(0)

    def Close(self):
        self.hide()

if __name__== '__main__':
    app = QApplication(sys.argv)

    childwindow = ChildWindow()
    childwindow.show()
    sys.exit(app.exec_())

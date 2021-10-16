import sys
import math

from PyQt5.QtWidgets import *
from calculator import Ui_Form

from child_window import ChildWindow
from youth_window import YouthWindow
from midlife_window import MidlifeWindow
from midlife2_window import Midlife2Window
from midlife3_window import Midlife3Window
from old_window import OldWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow, Ui_Form):

    lcdstring = ''
    operation = ''
    currentNum = 0
    previousNum = 0
    result = 0

    def __init__(self, parent=None):
        #parent = None代表此QWidget属于最上层的窗口,也就是MainWindows
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)

        self.setGraphicsEffect(effect)

        self.forge_link()
        self.child = ChildWindow()
        self.youth = YouthWindow()
        self.midlife1 = MidlifeWindow()
        self.midlife2 = Midlife2Window()
        self.midlife3 = Midlife3Window()
        self.old = OldWindow()

    def forge_link(self):
        self.b_0.clicked.connect(self.button_event)
        self.b_1.clicked.connect(self.button_event)
        self.b_2.clicked.connect(self.button_event)
        self.b_3.clicked.connect(self.button_event)
        self.b_4.clicked.connect(self.button_event)
        self.b_5.clicked.connect(self.button_event)
        self.b_6.clicked.connect(self.button_event)
        self.b_7.clicked.connect(self.button_event)
        self.b_8.clicked.connect(self.button_event)
        self.b_9.clicked.connect(self.button_event)
        self.b_dot.clicked.connect(self.button_event)

        self.b_plus.clicked.connect(self.opClicked)
        self.b_minus.clicked.connect(self.opClicked)
        self.b_divide.clicked.connect(self.opClicked)
        self.b_multiply.clicked.connect(self.opClicked)
        self.b_power.clicked.connect(self.opClicked)
        self.b_sin.clicked.connect(self.opClicked)
        self.b_cos.clicked.connect(self.opClicked)
        self.b_tan.clicked.connect(self.opClicked)
        self.b_log.clicked.connect(self.opClicked)

        self.b_reverse.clicked.connect(self.reverse_event)

        self.b_clear.clicked.connect(self.clear_event)
        self.b_delete.clicked.connect(self.delete_event)

        self.b_equal.clicked.connect(self.equal_event)

        self.b_child.clicked.connect(self.openchild)
        self.b_youth.clicked.connect(self.openyouth)
        self.b_mid1.clicked.connect(self.openmid1)
        self.b_mid2.clicked.connect(self.openmid2)
        self.b_mid3.clicked.connect(self.openmid3)
        self.b_old.clicked.connect(self.openold)

        self.close.clicked.connect(self.Close)
        self.min.clicked.connect(self.Min)

    def openchild(self):
        self.child.show()
    def openyouth(self):
        self.youth.show()
    def openmid1(self):
        self.midlife1.show()
    def openmid2(self):
        self.midlife2.show()
    def openmid3(self):
        self.midlife3.show()
    def openold(self):
        self.old.show()

    def button_event(self):
        self.lcdstring = self.lcdstring + self.sender().text()
        if str(self.lcdstring) == '.':
            self.lcdstring = '0.'
            self.lcd.display(self.lcdstring)
            self.currentNum = float(self.lcdstring)

        else:
            if str(self.lcdstring).count('.')>1:
                self.lcdstring = str(self.lcdstring)[:-1]
                self.lcd.display(self.lcdstring)
                self.currentNum = float(self.lcdstring)
            else:
                self.lcd.display(self.lcdstring)
                self.currentNum = float(self.lcdstring)

    def opClicked(self):
        if self.operation != '':
            self.equal_event()
            self.previousNum = self.currentNum
            self.currentNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()
        else:
            self.previousNum = self.currentNum
            self.currentNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()


    def equal_event(self):
        if self.operation == '+':
            self.result = self.previousNum + self.currentNum
            self.lcd.display(self.result)

        if self.operation == '-':
            self.result = self.previousNum - self.currentNum
            self.lcd.display(self.result)

        if self.operation == '*':
            self.result = self.previousNum * self.currentNum
            self.lcd.display(self.result)

        if self.operation == '/':
            if self.currentNum == 0:
                self.lcd.display('Error!')
                self.result = 0
                self.previousNum = 0
            else:
                self.result = self.previousNum / self.currentNum
                self.lcd.display(self.result)

        if self.operation == '^':
            self.result = self.previousNum ** self.currentNum
            self.lcd.display(self.result)

        if self.operation == 'sin':
            self.result = math.sin(self.currentNum)
            self.lcd.display(self.result)

        if self.operation == 'cos':
            self.result = math.cos(self.currentNum)
            self.lcd.display(self.result)

        if self.operation == 'tan':
            self.result = math.tan(self.currentNum)
            self.lcd.display(self.result)

        if self.operation == 'log':
            self.result = math.log2(self.currentNum)
            self.lcd.display(self.result)

        self.currentNum = self.result
        self.lcdstring = ''
        self.operation = ''

    def clear_event(self):
        self.lcdstring = ''
        self.operation = ''
        self.currentNum = 0
        self.previousNum = 0
        self.result = 0
        self.lcd.display(0)

    def delete_event(self):
        if len(self.lcdstring) > 1:
            self.lcdstring =  self.lcdstring[:-1]
        else:
            self.lcdstring = '0'
        self.lcd.display(self.lcdstring)
        self.currentNum = self.currentNum // 10

    def reverse_event(self):
        if self.currentNum < 0:
            self.lcdstring = self.lcdstring[1:]
        elif self.currentNum > 0:
            self.lcdstring = '-' + self.lcdstring

        # self.operation = ''
        self.currentNum = -self.currentNum
        self.lcd.display(self.lcdstring)

    def Close(self):
        app = QApplication.instance()
        app.quit()

    def Min(self):
        self.showMinimized()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
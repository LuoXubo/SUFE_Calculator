import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont
from calculator import Ui_Form
class MainWindow(QtWidgets.QMainWindow, Ui_Form):

    lcdstring = ''
    operation = ''
    currentNum = 0
    previousNum = 0
    result = 0

    def __init__(self, parent=None):
        #parent = None代表此QWidget属于最上层的窗口,也就是MainWindows
        super().__init__()
        self.setupUi(self)
        self.forge_link()

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

        self.b_clear.clicked.connect(self.clear_event)
        self.b_delete.clicked.connect(self.delete_event)
        # self.b_reverse.clicked.connect(self.button_enent)

        self.b_equal.clicked.connect(self.equal_event)
        # self.b_left.clicked.connect(self.button_event('('))
        # self.b_right.clicked.connect(self.button_event(')'))

        # self.b_child.clicked.connect()
        # self.b_youth.clicked.connect()
        # self.b_midlife.clicked.connect()
        # self.b_old.clicked.connect()

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
        

    def clear_event(self):
        self.lcdstring = ''
        self.operation = ''
        self.currentNum = 0
        self.previousNum = 0
        self.result = 0
        self.lcd.display(0)

    def delete_event(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
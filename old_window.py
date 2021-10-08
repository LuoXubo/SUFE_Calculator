from old import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class OldWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forge_link()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def forge_link(self):
        self.ok.clicked.connect(self.Finish)
        self.reset.clicked.connect(self.Reset)
        self.close.clicked.connect(self.Close)

    def Finish(self):
        height = float(self.height.text())
        weight = float(self.weight.text())

        bmi = weight / height ** 2

        self.lcd.display(bmi)

        str = ''
        if bmi<18.5:
            str = '体重过轻，建议补补身体'
        elif bmi>=18.5 and bmi<24:
            str = '恭喜，身体健康，继续保持'
        elif bmi>=24 and bmi<28:
            str = '稍有超重，请注意锻炼身体'
        else:
            str = '身体处于肥胖状态，请及时减重'

        self.analysis.setText(str)

    def Reset(self):
        self.height.setText('0')
        self.weight.setText('0')
        self.analysis.setText('')
        self.lcd.display(0)

    def Close(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    old = OldWindow()
    old.show()
    sys.exit(app.exec_())

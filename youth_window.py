from PyQt5.QtWidgets import *
from youth import Ui_Form
import sys
import numpy as np

class YouthWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forge_link()

    def forge_link(self):

        self.ok.clicked.connect(self.finishinput)

    def finishinput(self):
        grade = np.zeros(7)
        course = np.zeros(7)

        grade[0] = float(self.g_1.text())
        grade[1] = float(self.g_2.text())
        grade[2] = float(self.g_3.text())
        grade[3] = float(self.g_4.text())
        grade[4] = float(self.g_5.text())
        grade[5] = float(self.g_6.text())
        grade[6] = float(self.g_7.text())

        course[0] = float(self.c_1.text())
        course[1] = float(self.c_2.text())
        course[2] = float(self.c_3.text())
        course[3] = float(self.c_4.text())
        course[4] = float(self.c_5.text())
        course[5] = float(self.c_6.text())
        course[6] = float(self.c_7.text())

        final = 0.
        if course.sum() < 1:
            pass
        for i in range(7):
            final += grade[i] * course[i] / course.sum()

        self.final_grade.display(final)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    youthwindow = YouthWindow()
    youthwindow.show()
    sys.exit(app.exec_())

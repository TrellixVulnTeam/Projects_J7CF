import sys
import importlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

        # Global variable
firstNum = None

class MainWindow(QMainWindow):

        # Defining GUI
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):

        # Adding textbox

        self.label = QLineEdit(self)
        self.label.move(0, 0)
        self.label.setFixedSize(335, 30)
        self.label.setReadOnly(True)

        # Adding constructors

        self.button1 = QPushButton('7', self)
        self.button1.move(0, 40)
        self.button2 = QPushButton('8', self)
        self.button2.move(120, 40)
        self.button3 = QPushButton('9', self)
        self.button3.move(240, 40)
        self.button4 = QPushButton('4', self)
        self.button4.move(0, 80)
        self.button5 = QPushButton('5', self)
        self.button5.move(120, 80)
        self.button6 = QPushButton('6', self)
        self.button6.move(240, 80)
        self.button7 = QPushButton('1', self)
        self.button7.move(0, 120)
        self.button8 = QPushButton('2', self)
        self.button8.move(120, 120)
        self.button9 = QPushButton('3', self)
        self.button9.move(240, 120)
        self.button0 = QPushButton('0', self)
        self.button0.resize(220, 32)
        self.button0.move(0, 160)

        self.buttonDot = QPushButton('.', self)
        self.buttonDot.move(240, 160)
        self.buttonAdd = QPushButton('+', self)
        self.buttonAdd.move(360, 40)
        self.buttonSub = QPushButton('-', self)
        self.buttonSub.move(360, 80)
        self.buttonMulti = QPushButton('*', self)
        self.buttonMulti.move(360, 120)
        self.buttonDivide = QPushButton('/', self)
        self.buttonDivide.move(360, 160)

        self.buttonPlusMinus = QPushButton('+/-', self)
        self.buttonPlusMinus.move(240, 200)
        self.buttonClear = QPushButton('C', self)
        self.buttonClear.move(120, 200)
        self.buttonPrc = QPushButton('%', self)
        self.buttonPrc.move(360, 0)
        self.buttonEq = QPushButton('=', self)
        self.buttonEq.move(360, 200)

        self.ExButton = QPushButton('Exit', self)
        self.ExButton.move(0, 200)

        # Connecting buttons to functions 

        self.button1.clicked.connect(self.digit_pressed)
        self.button2.clicked.connect(self.digit_pressed)
        self.button3.clicked.connect(self.digit_pressed)
        self.button4.clicked.connect(self.digit_pressed)
        self.button5.clicked.connect(self.digit_pressed)
        self.button6.clicked.connect(self.digit_pressed)
        self.button7.clicked.connect(self.digit_pressed)
        self.button8.clicked.connect(self.digit_pressed)
        self.button9.clicked.connect(self.digit_pressed)
        self.button0.clicked.connect(self.digit_pressed)

        self.buttonDot.clicked.connect(self.dot_pressed)

        self.buttonPrc.clicked.connect(self.unary_operation)
        self.buttonPlusMinus.clicked.connect(self.unary_operation)

        self.buttonClear.clicked.connect(self.clear_pressed)

        self.buttonAdd.clicked.connect(self.binary_operation)
        self.buttonSub.clicked.connect(self.binary_operation)
        self.buttonMulti.clicked.connect(self.binary_operation)
        self.buttonDivide.clicked.connect(self.binary_operation)

        self.buttonAdd.setCheckable(True)
        self.buttonSub.setCheckable(True)
        self.buttonMulti.setCheckable(True)
        self.buttonDivide.setCheckable(True)

        self.buttonEq.clicked.connect(self.equal_pressed)
        self.ExButton.clicked.connect(self.exit_program())

    # Functions

    def exit_program(self):
        return sys.exit

    def digit_pressed(self):
        button = self.sender()
        newline = format(float(self.label.text() + button.text()), '.15g')
        self.label.setText(newline)

    def dot_pressed(self):

        tempstr = str(self.label.text())
        if (tempstr.count('.')) < 1:
            self.label.setText(self.label.text() + '.')

    def unary_operation(self):
        button = self.sender()
        linenumber = float(self.label.text())

        if button.text() == '%':
            linenumber = linenumber * 0.01
        else:
            linenumber = linenumber * -1

        newline = format(linenumber, '.15g')
        self.label.setText(newline)

    def clear_pressed(self):
        self.label.clear()

    def binary_operation(self):
        button = self.sender()
        self.firstNum = float(self.label.text())
        self.label.clear()

    def equal_pressed(self):
        secondNum = float(self.label.text())

        if self.buttonAdd.isChecked():
                linenumber = self.firstNum + secondNum
                linenumber = format(linenumber, '.15g')
                self.label.setText(linenumber)
                self.buttonAdd.setChecked(False)

        elif self.buttonSub.isChecked():
                linenumber = self.firstNum - secondNum
                linenumber = format(linenumber, '.15g')
                self.label.setText(linenumber)
                self.buttonSub.setChecked(False)

        elif self.buttonMulti.isChecked():
                linenumber = self.firstNum * secondNum
                linenumber = format(linenumber, '.15g')
                self.label.setText(linenumber)
                self.buttonMulti.setChecked(False)

        elif self.buttonDivide.isChecked():
                linenumber = self.firstNum / secondNum
                linenumber = format(linenumber, '.15g')
                self.label.setText(linenumber)
                self.buttonDivide.setChecked(False)



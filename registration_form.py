from PyQt5.QtWidgets import (QApplication, QPushButton,
                             QDesktopWidget, QMainWindow, 
                             QLabel,QLineEdit,
                             QTextEdit,QFrame
                             )
from PyQt5           import QtCore, QtWidgets, QtGui
from PyQt5.QtGui     import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore    import QCoreApplication, Qt,QBasicTimer, QPoint

import sys, os
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'logic'))

import scanqr
import fastlogin_form
import Login_form

from threading import Thread

class Registration(QMainWindow):
    numberToDetectChanges = 1
    def __init__(self):
        super().__init__()


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)


        #size
        self.setFixedSize(251, 401)
        self.center()
        self.setStyleSheet("border-radius: 10px;")


        #forms
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 251, 401))
        self.frame.setStyleSheet("* {\n"
                                 "    background: rgb(255,255,255);\n"
                                 "    border-radius: 7px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 140, 161, 41))
        self.lineEdit_2.setStyleSheet("border: 1px solid gray; qproperty-alignment: AlignCenter;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 211, 41))
        self.pushButton.setStyleSheet("*{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));\n"
                                      "    color: rgb(255, 255, 255)\n"
                                      "}\n"
                                      ":hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52,152,219, 255), stop:1 rgba(142,68,173, 255));\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("qproperty-alignment: AlignCenter;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 211, 41))
        self.lineEdit.setStyleSheet("border: 1px solid gray; qproperty-alignment: AlignCenter;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 190, 161, 41))
        self.lineEdit_3.setStyleSheet("border: 1px solid gray; qproperty-alignment: AlignCenter;")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 190, 41, 41))
        self.pushButton_2.setStyleSheet("*{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));\n"
                                        "}\n"
                                        ":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52,152,219, 255), stop:1 rgba(142,68,173, 255));\n"
                                        "}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 350, 211, 21))
        self.pushButton_3.setStyleSheet("*{color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));}\n"
                                        ":hover{color: rgb(0, 0, 0)}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 140, 41, 41))
        self.pushButton_4.setStyleSheet("*{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));\n"
                                        "}\n"
                                        ":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52,152,219, 255), stop:1 rgba(142,68,173, 255));\n"
                                        "}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(20, 240, 211, 21))
        self.checkBox.setStyleSheet("*{                                     \n"
                                    "    color: rgb(0, 0, 0);               \n"
                                    "}                                      \n"
                                    "QCheckBox::indicator{                  \n"
                                    "    border: 1px solid gray;            \n"
                                    "    border-radius: 6px;                \n"
                                    "}                                      \n"
                                    "QCheckBox::indicator:checked           \n"
                                    "{                                      \n"
                                    "    background-color: rgb(142,68,173); \n"
                                    "}                                      \n"
                                    "QCheckBox::indicator:unchecked         \n"
                                    "{                                      \n"
                                    "    background-color: rgb(255,255,255);\n"
                                    "}                                      \n"
                                    )

        self.checkBox.setObjectName("checkBox")




        self.checkBox.setText("Fast login")
        self.lineEdit_2.setText("Password")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton.setText("Go")
        self.pushButton_2.setIcon(QtGui.QIcon('static/qr.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_2.setToolTip("Show <b>QR code</b> to the camera")
        self.pushButton_3.setText("Quit")
        self.pushButton_4.setIcon(QtGui.QIcon('static/password_eye.png'))
        self.pushButton_4.setIconSize(QtCore.QSize(28, 28))
        self.label.setText("Registration")
        self.lineEdit.setText("Name Company")
        self.lineEdit_3.setText("Code")


        self.lineEdit_3.setReadOnly(True)
        self.pushButton_2.setToolTip("Show <b>QR code</b> to the camera")
        #actions
        #self.checkBox.toggled.connect(self.Print)
        self.pushButton_4.clicked.connect(self.WatchPassword)
        self.pushButton.clicked.connect(self.Go)
        self.pushButton_2.clicked.connect(self.ScanQR)
        self.pushButton_3.clicked.connect(self.quit)
        #/actions

        #/forms

        self.oldPos = self.pos()

        self.show()


    #defs
    def Print(self):
        print("I'm alive")

    def Go(self):
        if self.checkBox.isChecked():
            self.window = fastlogin_form.FastLogin()
            self.window.show()
            self.hide()
        else:
            self.window = Login_form.Login()
            self.window.show()
            self.hide()

    def ScanQR(self):
        self.lineEdit_3.clear()
        info = scanqr.QR.Scan()
        self.lineEdit_3.setText(str(info, 'utf-8'))

    def quit(self):
        sys.exit()

    def WatchPassword(self):
        if self.numberToDetectChanges%2 == 0:
            self.lineEdit_2.setEchoMode(QLineEdit.Password)
            self.numberToDetectChanges += 1
        else:
            self.lineEdit_2.setEchoMode(QLineEdit.Normal)
            self.numberToDetectChanges += 1
    #/defs

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

app = QApplication(sys.argv)

ex = Registration()
sys.exit(app.exec_())
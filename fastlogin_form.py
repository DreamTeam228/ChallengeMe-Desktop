from PyQt5.QtWidgets import (QApplication, QPushButton,
                             QDesktopWidget, QMainWindow, 
                             QLabel,QLineEdit,
                             QTextEdit,QFrame
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint

import sys, os
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'logic'))
import scanqr
import Registered_form

class FastLogin(QMainWindow):
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
                                 "    border-radius: 10px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 30, 211, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("qproperty-alignment: AlignCenter;")
        self.label.setObjectName("label")
        self.label.setText("Fast Login")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 350, 211, 21))
        self.pushButton_3.setStyleSheet("*{color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));}\n"
                                        ":hover{color: rgb(0, 0, 0)}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(105, 190, 41, 41))
        self.pushButton_2.setStyleSheet("*{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));\n"
                                        "}\n"
                                        ":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52,152,219, 255), stop:1 rgba(142,68,173, 255));\n"
                                        "}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        #actions
        #self.pushButton.setText("Read QR")
        self.pushButton_2.setIcon(QtGui.QIcon('static/qr.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_3.setText("Quit")
        #/actions


        #buttonsclicked
        self.pushButton_2.clicked.connect(self.ScanQR)
        self.pushButton_3.clicked.connect(self.quit)
        #/buttonsclicked

        #/forms

        self.oldPos = self.pos()

        self.show()

       #defs
    def ScanQR(self):
        #self.textEdit.clear()
        info = (str(scanqr.QR.Scan(), 'utf-8'))
        if info != '':
            #self.Print()
            self.window = Registered_form.Registered()
            self.window.show()
            self.hide()
        #self.textEdit.append(str(info, 'utf-8'))

    def quit(self):
        sys.exit()
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


def OpenWindowFastLogin():
    app = QApplication(sys.argv)

    ex = FastLogin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    OpenWindowFastLogin()
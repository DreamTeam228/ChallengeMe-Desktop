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
import base64
import encode_decode
import json

class Registered(QMainWindow):
    COUNTER = 0
    def __init__(self):
        super().__init__()


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)


        #size
        self.setFixedSize(651, 501)
        self.center()
        self.setStyleSheet("border-radius: 10px;")


        #forms
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 651, 501))
        self.frame.setStyleSheet("* {\n"
                                 "    background: rgb(255,255,255);\n"
                                 "    border-radius: 7px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 400, 211, 41))
        self.pushButton.setStyleSheet("*{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));\n"
                                      "    color: rgb(255, 255, 255)\n"
                                      "}\n"
                                      ":hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52,152,219, 255), stop:1 rgba(142,68,173, 255));\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 211, 301))
        self.textEdit.setStyleSheet("border: 1px solid gray; qproperty-alignment: AlignCenter;")
        
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 340, 211, 41))
        self.pushButton_2.setStyleSheet("*{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));\n"
                                        "    color: rgb(255, 255, 255)\n"
                                        "}\n"
                                        ":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52,152,219, 255), stop:1 rgba(142,68,173, 255));\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 460, 211, 21))
        self.pushButton_3.setStyleSheet("*{color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));}\n"
                                        ":hover{color: rgb(0, 0, 0)}")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.tableView = QtWidgets.QTableWidget(self.frame)
        self.tableView.setGeometry(QtCore.QRect(250, 20, 381, 461))
        self.tableView.setStyleSheet("QTableWidget{border: 1px solid gray; border-radius: 7px;}"
                                     "QHeaderView{"
                                     "    background: rgb(52,152,219);"
                                     "    border-top-left-radius: 6px;"
                                     "    border-top-right-radius: 6px;"
                                     "    color: rgb(255,255,255)"
                                     "}"
                                     "QHeaderView::section{"
                                     "    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142,68,173, 255), stop:1 rgba(52,152,219, 255));"
                                     "    border-top-left-radius: 6px;"
                                     "    border-top-right-radius: 6px;"
                                     "    color: rgb(255,255,255)"
                                     "}"
                                     ");")
        #self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(3)
        self.tableView.setRowCount(16)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)#ResizeToContents       
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)#Stretch
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)#ResizeToContents
        self.tableView.verticalHeader().hide()
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalHeaderLabels(['№','Фамилия и имя','Номер телефона'])
        self.tableView.resizeColumnsToContents()
        #self.tableView.setItem(0, 0, QtWidgets.QTableWidgetItem('Иванов Иван'))
        #self.tableView.setItem(0, 1, QtWidgets.QTableWidgetItem('+7(666)555-44-33'))

        self.pushButton.setText("Read QR")
        self.pushButton_2.setText("Save users info")
        self.pushButton_3.setText("Quit")


        #buttonsclicked
        self.pushButton.clicked.connect(self.ScanQR)
        self.pushButton_3.clicked.connect(self.quit)
        #/buttonsclicked

        #/forms

        self.oldPos = self.pos()

        self.show()

       #defs
    def ScanQR(self):
        self.textEdit.clear()
        if self.COUNTER >= 16:
            self.tableView.setRowCount(self.COUNTER + 1)

        self.tableView.setItem(self.COUNTER, 0, QtWidgets.QTableWidgetItem(str(self.COUNTER + 1)))
        self.tableView.setItem(self.COUNTER, 1, QtWidgets.QTableWidgetItem('Иванов Иван'))
        self.tableView.setItem(self.COUNTER, 2, QtWidgets.QTableWidgetItem('+7(666)555-44-33'))
        self.COUNTER += 1
        #scanned = scanqr.QR.Scan().decode("utf-8-sig").encode("utf-8")
        #print('-------------')
        #print(scanned)
        #print('-------------')
        #self.Parse(scanned)
        #self.textEdit.append(scanned)

    def quit(self):
        sys.exit()

    def Parse(self, string):
        parsed = json.loads(string, encoding='utf-8')
        print(parsed)
        print(type(parsed))
        try:
            print(parsed['first name'])
            print(parsed['second name'])
            print(parsed['phoneNumber'])
            print(parsed['code'])
        except Excrption:
            print('cant read')
        #print[parsed['code']]
        #pass
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


def OpenWindowRegistered():
    app = QApplication(sys.argv)

    ex = Registered()
    sys.exit(app.exec_())

if __name__ == '__main__':
    OpenWindowRegistered()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cont = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cont.setGeometry(QtCore.QRect(100, 650, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_cont.setFont(font)
        self.btn_cont.setObjectName("btn_cont")
        self.lbl_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(20, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_1.setFont(font)
        self.lbl_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_1.setObjectName("lbl_1")
        self.line_msg = QtWidgets.QLineEdit(self.centralwidget)
        self.line_msg.setGeometry(QtCore.QRect(300, 600, 691, 41))
        self.line_msg.setObjectName("line_msg")
        self.line_cont = QtWidgets.QLineEdit(self.centralwidget)
        self.line_cont.setGeometry(QtCore.QRect(20, 600, 261, 41))
        self.line_cont.setObjectName("line_cont")
        self.lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(300, 20, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_2.setFont(font)
        self.lbl_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_2.setObjectName("lbl_2")
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(810, 650, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_send.setFont(font)
        self.btn_send.setObjectName("btn_send")
        self.btn_conn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_conn.setGeometry(QtCore.QRect(810, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_conn.setFont(font)
        self.btn_conn.setObjectName("btn_conn")
        self.text_chat = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_chat.setGeometry(QtCore.QRect(300, 68, 691, 521))
        self.text_chat.setObjectName("text_chat")
        self.text_cont = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_cont.setGeometry(QtCore.QRect(20, 70, 261, 521))
        self.text_cont.setObjectName("text_cont")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat (Client)"))
        self.btn_cont.setText(_translate("MainWindow", "Add Contact"))
        self.lbl_1.setText(_translate("MainWindow", "Contact List"))
        self.lbl_2.setText(_translate("MainWindow", "Chat History"))
        self.btn_send.setText(_translate("MainWindow", "Send Message"))
        self.btn_conn.setText(_translate("MainWindow", "Connect"))
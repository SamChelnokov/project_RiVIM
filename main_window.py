# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_participants = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_participants.setGeometry(QtCore.QRect(20, 30, 621, 371))
        self.tableWidget_participants.setObjectName("tableWidget_participants")
        self.pushButton_add_participant = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_participant.setGeometry(QtCore.QRect(690, 30, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_add_participant.setFont(font)
        self.pushButton_add_participant.setObjectName("pushButton_add_participant")
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate.setGeometry(QtCore.QRect(690, 90, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_calculate.setFont(font)
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        #add button delete
        #///////////////////
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(690, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        # //////////////////
        #add button show
        #///////////////////
        self.pushButton_show = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show.setGeometry(QtCore.QRect(690, 210, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_show.setFont(font)
        self.pushButton_show.setObjectName("pushButton_show")
        # //////////////////
        self.label_view_participant = QtWidgets.QLabel(self.centralwidget)
        self.label_view_participant.setGeometry(QtCore.QRect(20, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_view_participant.setFont(font)
        self.label_view_participant.setObjectName("label_view_participant")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_add_participant.setText(_translate("MainWindow", "Add Participant"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))
        
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_show.setText(_translate("MainWindow", "Show"))
        

        self.label_view_participant.setText(_translate("MainWindow", "Список учасників:"))


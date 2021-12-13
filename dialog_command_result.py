# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_command_result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_command_result(object):
    def setupUi(self, Dialog_command_result):
        Dialog_command_result.setObjectName("Dialog_command_result")
        Dialog_command_result.resize(736, 404)
        self.tableWidget_comand_result = QtWidgets.QTableWidget(Dialog_command_result)
        self.tableWidget_comand_result.setGeometry(QtCore.QRect(20, 40, 691, 341))
        self.tableWidget_comand_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_comand_result.setObjectName("tableWidget_comand_result")
        self.tableWidget_comand_result.setColumnCount(0)
        self.tableWidget_comand_result.setRowCount(0)

        self.retranslateUi(Dialog_command_result)
        QtCore.QMetaObject.connectSlotsByName(Dialog_command_result)

    def retranslateUi(self, Dialog_command_result):
        _translate = QtCore.QCoreApplication.translate
        Dialog_command_result.setWindowTitle(_translate("Dialog_command_result", "Dialog"))


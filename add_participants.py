# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_participants.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 267)
        self.label_num_participant = QtWidgets.QLabel(Dialog)
        self.label_num_participant.setGeometry(QtCore.QRect(10, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_num_participant.setFont(font)
        self.label_num_participant.setObjectName("label_num_participant")
        self.label_name_participant = QtWidgets.QLabel(Dialog)
        self.label_name_participant.setGeometry(QtCore.QRect(10, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_participant.setFont(font)
        self.label_name_participant.setObjectName("label_name_participant")
        self.label_team_participant = QtWidgets.QLabel(Dialog)
        self.label_team_participant.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_team_participant.setFont(font)
        self.label_team_participant.setObjectName("label_team_participant")
        self.label_zone_participant = QtWidgets.QLabel(Dialog)
        self.label_zone_participant.setGeometry(QtCore.QRect(10, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_zone_participant.setFont(font)
        self.label_zone_participant.setObjectName("label_zone_participant")
        self.label_sector_participant = QtWidgets.QLabel(Dialog)
        self.label_sector_participant.setGeometry(QtCore.QRect(10, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sector_participant.setFont(font)
        self.label_sector_participant.setObjectName("label_sector_participant")
        self.label_weight_participant = QtWidgets.QLabel(Dialog)
        self.label_weight_participant.setGeometry(QtCore.QRect(10, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_weight_participant.setFont(font)
        self.label_weight_participant.setObjectName("label_weight_participant")
        self.lineEdit_num_participant = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_num_participant.setGeometry(QtCore.QRect(180, 30, 171, 21))
        self.lineEdit_num_participant.setObjectName("lineEdit_num_participant")
        self.lineEdit_name_participant = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name_participant.setGeometry(QtCore.QRect(180, 60, 171, 21))
        self.lineEdit_name_participant.setObjectName("lineEdit_name_participant")
        self.lineEdit_team_participant = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_team_participant.setGeometry(QtCore.QRect(180, 90, 171, 21))
        self.lineEdit_team_participant.setObjectName("lineEdit_team_participant")
        self.lineEdit_zone_participant = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_zone_participant.setGeometry(QtCore.QRect(180, 120, 171, 21))
        self.lineEdit_zone_participant.setObjectName("lineEdit_zone_participant")
        self.lineEdit_sector_participant = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_sector_participant.setGeometry(QtCore.QRect(180, 150, 171, 21))
        self.lineEdit_sector_participant.setObjectName("lineEdit_sector_participant")
        self.lineEdit_weight = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_weight.setGeometry(QtCore.QRect(180, 180, 171, 21))
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(370, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_num_participant.setText(_translate("Dialog", "Номер учасника"))
        self.label_name_participant.setText(_translate("Dialog", "ПІБ учасника"))
        self.label_team_participant.setText(_translate("Dialog", "Команда"))
        self.label_zone_participant.setText(_translate("Dialog", "Зона учасника"))
        self.label_sector_participant.setText(_translate("Dialog", "Сектор учасника"))
        self.label_weight_participant.setText(_translate("Dialog", "Вага"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))


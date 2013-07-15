# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_tipo.ui'
#
# Created: Tue Jul  2 19:39:19 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 241)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 60, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_nom = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.le_nom.setObjectName("le_nom")
        self.verticalLayout_2.addWidget(self.le_nom)
        self.sb_puertas = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.sb_puertas.setMinimum(1)
        self.sb_puertas.setMaximum(7)
        self.sb_puertas.setProperty("value", 3)
        self.sb_puertas.setObjectName("sb_puertas")
        self.verticalLayout_2.addWidget(self.sb_puertas)
        self.btn_cancel = QtGui.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(150, 170, 98, 27))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_ok = QtGui.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(260, 170, 98, 27))
        self.btn_ok.setObjectName("btn_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Formulario Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "N° de Puertas:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))


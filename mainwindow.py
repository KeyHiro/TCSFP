# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jun 28 13:18:25 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 455)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtGui.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(20, 10, 651, 391))
        self.tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab.setObjectName("tab")
        self.tab_ve = QtGui.QWidget()
        self.tab_ve.setObjectName("tab_ve")
        self.tabla_ve = QtGui.QTableWidget(self.tab_ve)
        self.tabla_ve.setGeometry(QtCore.QRect(20, 110, 611, 231))
        self.tabla_ve.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabla_ve.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabla_ve.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabla_ve.setAutoFillBackground(False)
        self.tabla_ve.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla_ve.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.tabla_ve.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_ve.setObjectName("tabla_ve")
        self.tabla_ve.setColumnCount(4)
        self.tabla_ve.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabla_ve.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabla_ve.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabla_ve.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabla_ve.setHorizontalHeaderItem(3, item)
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab_ve)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 611, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_filtro_ve = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.le_filtro_ve.setObjectName("le_filtro_ve")
        self.horizontalLayout.addWidget(self.le_filtro_ve)
        self.btn_nuevo_ve = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_nuevo_ve.setObjectName("btn_nuevo_ve")
        self.horizontalLayout.addWidget(self.btn_nuevo_ve)
        self.btn_editar_ve = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_editar_ve.setEnabled(False)
        self.btn_editar_ve.setAutoDefault(False)
        self.btn_editar_ve.setDefault(False)
        self.btn_editar_ve.setFlat(False)
        self.btn_editar_ve.setObjectName("btn_editar_ve")
        self.horizontalLayout.addWidget(self.btn_editar_ve)
        self.btn_eliminar_ve = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_eliminar_ve.setEnabled(False)
        self.btn_eliminar_ve.setObjectName("btn_eliminar_ve")
        self.horizontalLayout.addWidget(self.btn_eliminar_ve)
        self.tab.addTab(self.tab_ve, "")
        self.tab_ma = QtGui.QWidget()
        self.tab_ma.setObjectName("tab_ma")
        self.tabla_ma = QtGui.QTableWidget(self.tab_ma)
        self.tabla_ma.setGeometry(QtCore.QRect(20, 110, 611, 231))
        self.tabla_ma.setMinimumSize(QtCore.QSize(0, 0))
        self.tabla_ma.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla_ma.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.tabla_ma.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_ma.setObjectName("tabla_ma")
        self.tabla_ma.setColumnCount(4)
        self.tabla_ma.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabla_ma.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabla_ma.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabla_ma.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabla_ma.setHorizontalHeaderItem(3, item)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_ma)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 611, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_filtro_ma = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.le_filtro_ma.setObjectName("le_filtro_ma")
        self.horizontalLayout_2.addWidget(self.le_filtro_ma)
        self.btn_nuevo_ma = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_nuevo_ma.setObjectName("btn_nuevo_ma")
        self.horizontalLayout_2.addWidget(self.btn_nuevo_ma)
        self.btn_editar_ma = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_editar_ma.setEnabled(False)
        self.btn_editar_ma.setObjectName("btn_editar_ma")
        self.horizontalLayout_2.addWidget(self.btn_editar_ma)
        self.btn_eliminar_ma = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_eliminar_ma.setEnabled(False)
        self.btn_eliminar_ma.setObjectName("btn_eliminar_ma")
        self.horizontalLayout_2.addWidget(self.btn_eliminar_ma)
        self.tab.addTab(self.tab_ma, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 691, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Concesionaria", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ve.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "id_auto", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ve.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ve.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Año", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ve.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.le_filtro_ve.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "¿Qué desea buscar?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nuevo_ve.setText(QtGui.QApplication.translate("MainWindow", "Nuevo Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar_ve.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#e8d823;\">Presiona para editar una fila</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar_ve.setText(QtGui.QApplication.translate("MainWindow", "Editar Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar_ve.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#e8d823;\">Presione para eliminar una fila</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar_ve.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tab_ve), QtGui.QApplication.translate("MainWindow", "Vehículos", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ma.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "id_marca", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ma.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ma.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Pais", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla_ma.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Total de Autos", None, QtGui.QApplication.UnicodeUTF8))
        self.le_filtro_ma.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "¿Qué desea buscar?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nuevo_ma.setText(QtGui.QApplication.translate("MainWindow", "Nueva Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar_ma.setText(QtGui.QApplication.translate("MainWindow", "Editar Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar_ma.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tab_ma), QtGui.QApplication.translate("MainWindow", "Marcas", None, QtGui.QApplication.UnicodeUTF8))


#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from mainwindow import Ui_MainWindow

class Main (QtGui.QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		self.ui =  Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_signals()
		self.set_listeners()
		self.show()
	def set_signals(self):
		self.ui.btn_nuevo_ve.clicked.connect(self.nuevo_ve)
		self.ui.btn_editar_ve.clicked.connect(self.editar_ve)
		self.ui.btn_eliminar_ve.clicked.connect(self.eliminar_ve)

		self.ui.btn_nuevo_ma.clicked.connect(self.nuevo_ma)
		self.ui.btn_editar_ma.clicked.connect(self.editar_ma)
		self.ui.btn_eliminar_ma.clicked.connect(self.eliminar_ma)
	def nuevo_ve(self):
		print "Nuevo Vehiculo"
	def editar_ve(self):
		print "Editar Vehiculo"
	def eliminar_ve(self):
		print "Eliminar Vehiculo"
	
	def nuevo_ma(self):
		print "Nueva Marca"
	def editar_ma(self):
		print "Editar Marca"
	def eliminar_ma(self):
		print "Eliminar Marca"

	def set_listeners(self):
		self.ui.tab.currentChanged[int].connect(self.tab_cambio)
		self.ui.le_filtro_ve.textChanged[str].connect(self.cargar_vehiculo_por_busqueda)
		self.ui.le_filtro_ma.textChanged[str].connect(self.cargar_marca_por_busqueda)
	def cargar_vehiculo_por_busqueda(self):
		print "Buscar vehiculos"
	def cargar_marca_por_busqueda(self):
		print "Buscar marcas"
	def tab_cambio(self):
		if self.ui.tab.currentIndex()==0:
			self.ui.le_filtro_ve.setText("")
			self.ui.le_filtro_ma.setText("")
			print "tabla vehiculos"
		if self.ui.tab.currentIndex()==1:
			self.ui.le_filtro_ve.setText("")
			self.ui.le_filtro_ma.setText("")
			print "tabla marca"

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()

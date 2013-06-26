#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from mainwindow import Ui_MainWindow

class Main (QtGui.QMainWindow):
	
	headers_vehiculo = []
	headers_marca = []

	def __init__(self):
		super(Main, self).__init__()
		self.ui =  Ui_MainWindow()
		self.ui.setupUi(self)
		self.get_headers()
		self.set_signals()
		self.set_listeners()
		self.cargar_marca()
		self.cargar_vehiculo()
		self.show()
	def get_headers(self):
		for i in range(0,self.ui.tabla_ve.columnCount()):
			self.headers_vehiculo.append(self.ui.tabla_ve.horizontalHeaderItem(i).text())
		for i in range(0,self.ui.tabla_ma.columnCount()):
			self.headers_vehiculo.append(self.ui.tabla_ma.horizontalHeaderItem(i).text())
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
		self.ui.tabla_ve.itemSelectionChanged.connect(self.seleccion_ve)
		self.ui.tabla_ma.itemSelectionChanged.connect(self.seleccion_ma)
	
	def cargar_vehiculo_por_busqueda(self):
		print "Buscar vehiculos"
	def cargar_marca_por_busqueda(self):
		print "Buscar marcas"
	
	def tab_cambio(self):
		if self.ui.tab.currentIndex()==0:
			self.cargar_vehiculo()
			self.ui.le_filtro_ve.setText("")
			self.ui.le_filtro_ma.setText("")
			print "tabla vehiculos"
		if self.ui.tab.currentIndex()==1:
			self.cargar_marca()
			self.ui.le_filtro_ve.setText("")
			self.ui.le_filtro_ma.setText("")
			print "tabla marca"
	
	def cargar_vehiculo(self):
		productos = [[u"elantra", 1993, u"doble cabina"],
					[u"sali", 2010, "doble cabina"]
					]
		self.ui.tabla_ve.clear()
		self.set_headers()
		self.ui.tabla_ve.setRowCount(len(productos))
		r = 0
		for row in productos:
			item = QtGui.QTableWidgetItem(row[0])
			self.ui.tabla_ve.setItem(r,0,item)
			item = QtGui.QTableWidgetItem(str(row[1]))
			self.ui.tabla_ve.setItem(r,1,item)
			item = QtGui.QTableWidgetItem(row[2])
			self.ui.tabla_ve.setItem(r,2,item)
			r = r+1
	def cargar_marca(self):
		marcas = [[u"hyundai", u"Japon", 1],
				[u"chevrolet",u"USA",1]
				]
		self.ui.tabla_ma.clear()
		self.set_headers()
		self.ui.tabla_ma.setRowCount(len(marcas))
		r = 0
		for row in marcas:
			item = QtGui.QTableWidgetItem(row[0])
			self.ui.tabla_ma.setItem(r,0,item)
			item = QtGui.QTableWidgetItem(row[1])
			self.ui.tabla_ma.setItem(r,1,item)
			item = QtGui.QTableWidgetItem(str(row[2]))
			self.ui.tabla_ma.setItem(r,2,item)
			r = r+1
	def set_headers(self):
		self.ui.tabla_ve.setHorizontalHeaderLabels(self.headers_vehiculo)
		self.ui.tabla_ma.setHorizontalHeaderLabels(self.headers_marca)

	def seleccion_ve(self):
		sel_itms = self.ui.tabla_ve.selectedItems()
		enabled = True
		if len(sel_itms) == 0:
			enabled = False
		self.ui.btn_editar_ve.setEnabled(enabled)
		self.ui.btn_eliminar_ve.setEnabled(enabled)
	def seleccion_ma(self):
		sel_itms = self.ui.tabla_ma.selectedItems()
		enabled = True
		if len(sel_itms) == 0:
			enabled = False
		self.ui.btn_editar_ma.setEnabled(enabled)
		self.ui.btn_eliminar_ma.setEnabled(enabled)

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()

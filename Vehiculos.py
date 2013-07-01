#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from mainwindow import Ui_MainWindow
from forma_marca import FormMarca

class Main (QtGui.QMainWindow):
	
	headers_vehiculo = []
	headers_marca = []
	marcas = []
	vehiculos = []

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
			self.headers_marca.append(self.ui.tabla_ma.horizontalHeaderItem(i).text())
			
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
		
		dialog_marca = FormMarca(self)
		
		"""loop = QtCore.QEventLoop()
		dialog_marca.ui.btn_ok.clicked.connect(loop.quit)
		loop.exec_()"""
		if dialog_marca.result:
			print self.marcas
		print "Nueva Marca"
	def editar_ma(self):
		
		sel_itms = self.ui.tabla_ma.selectedItems()
		n_filas = len(sel_itms)/(self.ui.tabla_ma.columnCount())
		
		for fila in range(n_filas) :
			row = self.ui.tabla_ma.row(sel_itms[fila])
		
			self.marcas = [self.ui.tabla_ma.item(row, x).text() for x in range(1,self.ui.tabla_ma.columnCount()-1) ]
			print self.marcas

			dialog_marca = FormMarca(self, "Editar")
			if dialog_marca.result:
				print self.marcas
		print "Editar Marca"

	def eliminar_ma(self):

		sel_itms = self.ui.tabla_ma.selectedItems()
		n_filas = len(sel_itms)/(self.ui.tabla_ma.columnCount())

		msgBox = QtGui.QMessageBox()
		#msgBox.setWindowIconText("Eliminar marca(s)")
		msgBox.setText("Se ha(n) seleccionado "+str(n_filas)+" marca(s).")
		msgBox.setInformativeText("Seguro que quiere eliminar?")
		msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
		msgBox.setDefaultButton(QtGui.QMessageBox.Save)
		ret = msgBox.exec_()

		if ret == QtGui.QMessageBox.Save:
			# Save was clicked
			print "Guardar"
		elif ret == QtGui.QMessageBox.Discard:
			# Don't save was clicked
			print "Descartar"
		elif ret == QtGui.QMessageBox.Cancel:
			# cancel was clicked
			print "Cancelar"
		else:
		# should never be reached
			print "Error"
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
		productos = [[1, u"elantra", 1993, u"doble cabina"],
					[2, u"sail", 2010, "doble cabina"],
					[3, u"gallardo", 2013, "una cabina"]
					]
		self.ui.tabla_ve.clear()
		self.set_headers()
		self.ui.tabla_ve.setRowCount(len(productos))
		r = 0
		for row in productos:
			item = QtGui.QTableWidgetItem(str(row[0]))
			self.ui.tabla_ve.setItem(r,0,item)
			item = QtGui.QTableWidgetItem(row[1])
			self.ui.tabla_ve.setItem(r,1,item)
			item = QtGui.QTableWidgetItem(str(row[2]))
			self.ui.tabla_ve.setItem(r,2,item)
			item = QtGui.QTableWidgetItem(row[3])
			self.ui.tabla_ve.setItem(r,3,item)
			r = r+1
	def cargar_marca(self):
		marcas = [[1, u"hyundai", u"Japon", 1],
				[2, u"chevrolet",u"USA",1],
				[3, u"lamborghini", u"Italia", 1]
				]
		self.ui.tabla_ma.clear()
		self.set_headers()
		self.ui.tabla_ma.setRowCount(len(marcas))
		r = 0
		for row in marcas:
			item = QtGui.QTableWidgetItem(str(row[0]))
			self.ui.tabla_ma.setItem(r,0,item)
			item = QtGui.QTableWidgetItem(row[1])
			self.ui.tabla_ma.setItem(r,1,item)
			item = QtGui.QTableWidgetItem(row[2])
			self.ui.tabla_ma.setItem(r,2,item)
			item = QtGui.QTableWidgetItem(str(row[3]))
			self.ui.tabla_ma.setItem(r,3,item)
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

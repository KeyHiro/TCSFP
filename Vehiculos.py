#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from PySide import QtGui, QtCore
from mainwindow import Ui_MainWindow
from forma_marca import FormMarca
from forma_vehiculo import FormVehiculo
from controlador_autos import ejecutar as controlador

class Main (QtGui.QMainWindow):
	"""Esta es la clase principal que se encarga de mostrar y mantener los elementos gráficos.
		Importa dos formularios externos (para marcas y autos), y el 'controlador_autos' que
		administra el funcionamiento de la base de datos de los autos."""
	headers_vehiculo = []
	headers_marca = []
	marcas = []
	vehiculos = []
	dir = os.getcwd()

	def __init__(self):
		"""Se inicia el inicializarse la clase, y luego de llamar a la clase padre,
			y cargar la plantilla grafica, ejecuta los metodos necesarios
			para su uncionamiento. Al final llama al metodo 'show()' (que hereda de QMainWindow)
			que se encarga de dibujar los elementos gráficos en pantalla."""
		super(Main, self).__init__()
		self.create_folder()
		self.ui =  Ui_MainWindow()
		self.ui.setupUi(self)
		self.get_headers()
		self.set_signals()
		self.set_listeners()
		self.cargar_marca()
		self.cargar_vehiculo()
		self.show()

	def create_folder(self):
		"""EXTRA EXTRA
			Revisa si existe el directorio donde se guerdan los respaldos de las imagenes de 
			los autos. De no existir, la crea y lo reporta mediante un mensaje."""
		directorio = os.path.join(self.dir, '.Imagenes_Autos')
		if not os.path.isdir(directorio):
			os.mkdir(directorio)
			msgBox = QtGui.QMessageBox()
			msgBox.setWindowTitle('')
			msgBox.setIcon(QtGui.QMessageBox.Information)
			msgBox.setText("Se ha creado la carpeta 'Imagenes_Autos'.")
			msgBox.exec_()
		self.dir = directorio
	
	def get_headers(self):
		"""Guarda los nombres de las columnas de ambas tablas en variables de la clase 
			para posterior referecia."""
		for i in range(0,self.ui.tabla_ve.columnCount()):
			self.headers_vehiculo.append(self.ui.tabla_ve.horizontalHeaderItem(i).text())
		for i in range(0,self.ui.tabla_ma.columnCount()):
			self.headers_marca.append(self.ui.tabla_ma.horizontalHeaderItem(i).text())
			
	def set_signals(self):
		"""Establece las conecciones entre las señales emitidas al presionar un boton,
			con los metodos que deban reaccionar a estas."""
		self.ui.btn_nuevo_ve.clicked.connect(self.nuevo_ve)
		self.ui.btn_editar_ve.clicked.connect(self.editar_ve)
		self.ui.btn_eliminar_ve.clicked.connect(self.eliminar_ve)
		self.ui.btn_nuevo_ma.clicked.connect(self.nuevo_ma)
		self.ui.btn_editar_ma.clicked.connect(self.editar_ma)
		self.ui.btn_eliminar_ma.clicked.connect(self.eliminar_ma)

	def set_listeners(self):
		"""Establece los metodos que reaccionan ante el cambio de pestaña, la edición de texto
			en el buscador, la selección de items en los QComboBox, y el doble click en las tablas."""
		self.ui.tab.currentChanged[int].connect(self.tab_cambio)
		self.ui.le_filtro_ve.textChanged[str].connect(self.cargar_vehiculo_por_busqueda)
		self.ui.le_filtro_ma.textChanged[str].connect(self.cargar_marca_por_busqueda)
		self.ui.tabla_ve.itemSelectionChanged.connect(self.seleccion_ve)
		self.ui.tabla_ma.itemSelectionChanged.connect(self.seleccion_ma)
		self.ui.tabla_ve.cellDoubleClicked.connect(self.muestra_imagen)
	
	def nuevo_ve(self):
		"""Muestra un QDialog en respuesta al boton 'Nuevo Auto' de la pestaña Autos,
			en el cual aparecen los campos de texto necesarios para ingresar un nuevo auto,
			mostrando con QComboBox las marcas y tipos existentes, permitiendo agregar
			una nueva marca o un nuevo tipo. Tambien permite buscar la imagen del auto mediante
			un explorador de  carpetas."""
		dialog_vehiculo = FormVehiculo(self, 'Nuevo')
		if dialog_vehiculo.result:
			controlador('añadir auto', dialog_vehiculo.vehiculo)
		self.cargar_vehiculo()

	def editar_ve(self):
		"""Se ejecuta cuando se presiona el boton 'Editar Auto' de la pestaña Autos,
			solo si se han seleccionado elementos en la tabla. Muestra un QDialog con 
			los campos de texto necesarios para que se acutualicen los datos del auto, esto 
			por cada elemento seleccionado."""
		sel_itms = self.ui.tabla_ve.selectedItems()
		n_filas = len(sel_itms)/(self.ui.tabla_ve.columnCount()-1)
		for fila in range(n_filas) :
			row = self.ui.tabla_ve.row(sel_itms[fila])
			id_vehiculo = self.ui.tabla_ve.item(row, 0).text()
			self.vehiculos = controlador('obtener auto', id_vehiculo)[0]

			dialog_vehiculo = FormVehiculo(self, "Editar")
			if dialog_vehiculo.result:
				dialog_vehiculo.vehiculo.append(id_vehiculo)
				controlador('editar auto', dialog_vehiculo.vehiculo)
		self.cargar_vehiculo()
	
	def eliminar_ve(self):
		"""Se ejecuta cuando se presiona el boton 'Eliminar Auto' en la pestaña de autos
			cuando se ha seleccionado uno o más elementos de la tabla. Se Abre un QDialog
			que muestra la cantidad de filas seleccionadas que busca confirmar la desición de 
			elimiar el o los autos seleccionados en la tabla."""
		sel_itms = self.ui.tabla_ve.selectedItems()
		n_filas = (len(sel_itms))/(self.ui.tabla_ve.columnCount()-1)
		msgBox = QtGui.QMessageBox()
		msgBox.setWindowTitle('Eliminar Vehiculo(s)')
		msgBox.setIcon(QtGui.QMessageBox.Warning)
		msgBox.setText("Se ha(n) seleccionado "+str(n_filas)+" vehiculo(s).")
		msgBox.setInformativeText("Seguro que quiere eliminar?")
		msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
		msgBox.setDefaultButton(QtGui.QMessageBox.Save)
		ret = msgBox.exec_()
		if ret == QtGui.QMessageBox.Save:
			vehiculo = []
			for fila in range(n_filas) :
				row = self.ui.tabla_ve.row(sel_itms[fila])
				vehiculo.append(self.ui.tabla_ve.item(row, 0).text())
			for auto in vehiculo:
				controlador('eliminar auto', auto)
		elif ret == QtGui.QMessageBox.Cancel:
			pass
		else:
			print "Error"
		self.cargar_vehiculo()

	def nuevo_ma(self):
		"""Muestra un QDialog en respuesta al boton 'Nueva Marca' de la pestaña Marcas,
			en el cual aparecen los campos de texto necesarios para ingresar una nueva marca."""
		dialog_marca = FormMarca(self, "Nuevo")
		if dialog_marca.result:
			controlador('añadir marca', dialog_marca.marca)
		self.cargar_marca()

	def editar_ma(self):	
		"""Se ejecuta cuando se presiona el boton 'Editar Marca' de la pestaña Marcas,
			solo si se han seleccionado elementos en la tabla. Muestra un QDialog con 
			los campos de texto necesarios para que se acutualicen los datos de la marca, esto 
			por cada elemento seleccionado."""
		sel_itms = self.ui.tabla_ma.selectedItems()
		n_filas = (len(sel_itms)+1)/(self.ui.tabla_ma.columnCount()-1)
		for fila in range(n_filas) :
			row = self.ui.tabla_ma.row(sel_itms[fila])
			id_marca = self.ui.tabla_ma.item(row, 0).text()
			self.marcas = controlador('obtener marca', [id_marca])[0]
			dialog_marca = FormMarca(self, "Editar")
			if dialog_marca.result:
				dialog_marca.marca.append(id_marca)
				controlador('editar marca', dialog_marca.marca)
		self.cargar_marca()
	
	def eliminar_ma(self):
		"""Se ejecuta cuando se presiona el boton 'Eliminar en la pestaña de marcas
			cuando se ha seleccionado uno o más elementos de la tabla. Se Abre un QDialog
			que muestra la cantidad de filas seleccionadas que busca confirmar la desición de 
			elimiar la o las marcas seleccionadas en la tabla. Si existen autos de esa marca, 
			el proceso se interrumpe informando la cantidad de autos asiciados a 
			cada marca que no se pudo eliminar."""
		sel_itms = self.ui.tabla_ma.selectedItems()
		n_filas = (len(sel_itms))/(self.ui.tabla_ma.columnCount()-1)
		msgBox = QtGui.QMessageBox()
		msgBox.setWindowTitle('Eliminar Marca(s)')
		msgBox.setIcon(QtGui.QMessageBox.Warning)
		msgBox.setText("Se ha(n) seleccionado "+str(n_filas)+" marca(s).")
		msgBox.setInformativeText("Seguro que quiere eliminar?")
		msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
		msgBox.setDefaultButton(QtGui.QMessageBox.Save)
		ret = msgBox.exec_()
		if ret == QtGui.QMessageBox.Save:
			# Save was clicked
			marca = []
			for fila in range(n_filas):
				row = self.ui.tabla_ma.row(sel_itms[fila])
				id_marca = self.ui.tabla_ma.item(row, 0).text()
				num = controlador('contar autos', [id_marca])[0][0]
				if num == 0:
					marca.append(id_marca)
				else:
					msgBox = QtGui.QMessageBox()
					msgBox.setWindowTitle('Eliminar Marca')
					msgBox.setIcon(QtGui.QMessageBox.Information)
					msgBox.setText("No se pudo eliminar la marca: "+
									self.ui.tabla_ma.item(row, 1).text()+".")
					msgBox.setInformativeText("La marca tiene: "+str(num)
											+" vehiculo(s) asociado(s)")
					msgBox.exec_()
			for x in marca:
				controlador('eliminar marca', x)
		elif ret == QtGui.QMessageBox.Cancel:
			# cancel was clicked
			pass
		else:
			print "Error"
		self.cargar_marca()
		self.cargar_vehiculo()

	def muestra_imagen(self, row, column):
		"""Responde cuando se hace doble click en alguna celda de la tabla autos,
			desplagando en un QDialog la image del auto de la fila donde se encuentra la celda 
			clickeada"""
		id_vehiculo = self.ui.tabla_ve.item(row, 0).text()
		vehiculo = controlador('obtener auto', id_vehiculo)[0]
		ruta = os.path.join(self.dir, vehiculo[9])
		map=QtGui.QPixmap(ruta)
		if map.isNull() == False:
			msgBox = QtGui.QDialog()
			#layoutWidget = QtGui.QWidget(msgBox)
			#layoutWidget.setGeometry(QtCore.QRect(10, 10, 400, 600))
			graphicsView = QtGui.QGraphicsView(msgBox)
			height = 580
			width =  int(map.rect().height()*height/map.rect().width())
			msgBox.resize(height, width)
			#graphicsView.resize(height, width)
			scene = QtGui.QGraphicsScene(graphicsView)
			map=map.scaled(height-2, width-2)
			#msgBox.setIconPixmap(map)
			scene.addPixmap(map)
			graphicsView.setScene(scene)
			marca = controlador('obtener marca', [vehiculo[2]])[0]
			tipo = controlador('obtener tipo', [vehiculo[3]])[0]
			texto = "Modelo:\t"+vehiculo[1]+"\nMarca:\t"+marca[1]
			#texto = texto+"\nTipo:\t"+tipo[0]
			msgBox.setWindowTitle(marca[1]+" "+vehiculo[1])
			#msgBox.setDetailedText(texto)
		else:
			msgBox = QtGui.QMessageBox()
			msgBox.setWindowTitle('Visor de Imagen')
			msgBox.setIcon(QtGui.QMessageBox.Information)
			msgBox.setText("No se pudo cargar la imagen.")
		msgBox.exec_()

	def cargar_vehiculo_por_busqueda(self):
		"""Responde a la edicion de texto en el campo de busqueda de 
			la pestaña donde se muestra la tabla de autoss,
			desplagando en la misma las filas que contengan campos que coincidan 
			con el texto que se haya ingresado."""
		texto =  self.ui.le_filtro_ve.text()
		if not texto=="":
			id_vehiculo = controlador('buscar auto', texto)
			self.cargar_vehiculo(id_vehiculo)
		else:
			self.cargar_vehiculo()
	
	def cargar_marca_por_busqueda(self):
		"""Responde a la edicion de texto en el campo de busqueda de 
			la pestaña donde se muestra la tabla de marcas,
			desplagando en la misma las filas que contengan campos que coincidan 
			con el texto que se haya ingresado."""
		texto =  self.ui.le_filtro_ma.text()
		id_marca = controlador('buscar marca', texto)
		self.cargar_marca(id_marca)
	
	def tab_cambio(self):
		"""Modifica el comportamiento de las pestañas para que 
			actualicen sus contenidos cuando se navega entre ellas."""
		if self.ui.tab.currentIndex()==0:
			self.cargar_vehiculo()
			self.ui.le_filtro_ve.setText("")
			self.ui.le_filtro_ma.setText("")
		if self.ui.tab.currentIndex()==1:
			self.cargar_marca()
			self.ui.le_filtro_ve.setText("")
			self.ui.le_filtro_ma.setText("")
	
	def cargar_vehiculo(self, id_vehiculo = None):
		"""Administra las filas de la tabla autos. 
			Si el parámetro id_vehiculo es None, se trabajará con todos las autos, 
			de lo contrario, el método mismo, buscará los autos necesarias. 
		"""
		productos = []
		if id_vehiculo==None:
			productos = controlador('obtener autos', None)
		else:
			for i in id_vehiculo:
				#print controlador('obtener auto', i)[0]
				productos.append(controlador('obtener auto', i)[0])	
		self.ui.tabla_ve.clear()
		self.set_headers()
		self.ui.tabla_ve.setRowCount(len(productos))
		r = 0
		for row in productos:
			tipo = controlador('obtener tipo', [row[3]])[0][0]
			marca = controlador('obtener marca', [row[2]])[0][1]
			item = QtGui.QTableWidgetItem(str(row[0]))
			self.ui.tabla_ve.setItem(r,0,item)
			item = QtGui.QTableWidgetItem(row[1])
			self.ui.tabla_ve.setItem(r,1,item)
			item = QtGui.QTableWidgetItem(marca)
			self.ui.tabla_ve.setItem(r,2,item)
			item = QtGui.QTableWidgetItem(str(row[10]))
			self.ui.tabla_ve.setItem(r,3,item)
			item = QtGui.QTableWidgetItem(tipo)
			self.ui.tabla_ve.setItem(r,4,item)
			r = r+1
		self.ui.tabla_ve.setColumnHidden(0,True)
	
	def cargar_marca(self, id_marca = None):
		"""Administra las filas de la tabla marcas. 
			Si el parámetro id_marca es None, se trabajará con todas las marcas, 
			de lo contrario, el método mismo, buscará las marcas necesarias. 
		"""
		marcas = []
		if id_marca==None:
			marcas = controlador('obtener marcas', None)
		else:
			for i in id_marca:
				marcas.append(controlador('obtener marca', i)[0])
		self.ui.tabla_ma.clear()
		self.set_headers()
		self.ui.tabla_ma.setRowCount(len(marcas))
		r = 0
		for row in marcas:
			num_autos =  controlador('contar autos', [row[0]])[0][0]
			item = QtGui.QTableWidgetItem(str(row[0]))
			self.ui.tabla_ma.setItem(r,0,item)
			item = QtGui.QTableWidgetItem(row[1])
			self.ui.tabla_ma.setItem(r,1,item)
			item = QtGui.QTableWidgetItem(row[2])
			self.ui.tabla_ma.setItem(r,2,item)
			item = QtGui.QTableWidgetItem(str(num_autos))
			self.ui.tabla_ma.setItem(r,3,item)
			r = r+1
		self.ui.tabla_ma.setColumnHidden(0,True)
	
	def set_headers(self):
		"""Establece los nombres de las columnas de las tablas."""
		self.ui.tabla_ve.setHorizontalHeaderLabels(self.headers_vehiculo)
		self.ui.tabla_ma.setHorizontalHeaderLabels(self.headers_marca)

	def seleccion_ve(self):
		"""Habilita los botones 'eliminar' y 'editar' cuando se seleccionan
			uno o más elementos de la tabla autoss."""
		sel_itms = self.ui.tabla_ve.selectedItems()
		enabled = True
		if len(sel_itms) == 0:
			enabled = False
		self.ui.btn_editar_ve.setEnabled(enabled)
		self.ui.btn_eliminar_ve.setEnabled(enabled)
	
	def seleccion_ma(self):
		"""Habilita los botones 'eliminar' y 'editar' cuando se seleccionan
			uno o más elementos de la tabla marcas."""
		sel_itms = self.ui.tabla_ma.selectedItems()
		enabled = True
		if len(sel_itms) == 0:
			enabled = False
		self.ui.btn_editar_ma.setEnabled(enabled)
		self.ui.btn_eliminar_ma.setEnabled(enabled)

def run():
	"""Contiene los procesos necesarios para ejecutar el programa principal."""
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	"""Ejecuta el programa principal"""
	run()

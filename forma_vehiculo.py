#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
# Nombre archivo: view_form.py
import sys
import shutil
import os

from PySide import QtGui, QtCore

from dialog_vehiculo import Ui_Dialog

from forma_marca import FormMarca
from forma_tipo import FormTipo
from controlador_autos import ejecutar as controlador

class FormVehiculo(QtGui.QDialog):
	result = False
	trigger = None
	vehiculo = []
	archivo = []
	direccion = os.getcwd()
	def __init__(self, parent=None, trigger=None):
		QtGui.QDialog.__init__(self, parent)
		self.parent = parent
		self.trigger = trigger
		self.ui =  Ui_Dialog()
		self.ui.setupUi(self)

		marcas = controlador('obtener marcas', None)
		for marca in marcas:
			self.ui.cb_marca.addItem(marca[1], marca[0])
			print marca[0]
		
		tipos = controlador('obtener tipos', None)
		for tipo in tipos:
			self.ui.cb_tipo.addItem(tipo[1], tipo[0])

		if(trigger == "Nuevo"):
			 self.ui.btn_ok.setEnabled(False)
		if(trigger == "Editar"):
			
			self.ui.le_modelo.setText(parent.vehiculos[1])
			self.ui.le_color.setText(parent.vehiculos[4])
			self.ui.le_motor.setText(str(parent.vehiculos[5]))
			self.ui.le_peso.setText(str(parent.vehiculos[6]))
			self.ui.le_descripcion.setText(parent.vehiculos[7])
			self.ui.le_rendimiento.setText(str(parent.vehiculos[8]))
			

			self.ui.sb_fecha.setValue(self.ui.sb_fecha.valueFromText(str(parent.vehiculos[10])))
			print parent.vehiculos[2]
			print self.ui.cb_marca.findData(parent.vehiculos[2])
			self.ui.cb_marca.setCurrentIndex(self.ui.cb_marca.findData(parent.vehiculos[2]))
			self.ui.cb_tipo.setCurrentIndex(self.ui.cb_tipo.findData(parent.vehiculos[3]))
			
			ruta = os.path.join(parent.dir, parent.vehiculos[9])
			self.ui.le_imagen.setText(ruta)
			scene = QtGui.QGraphicsScene(self)
			map=QtGui.QPixmap(ruta)
			if map.isNull() == False:
				
				width =  170
				height = int(map.rect().width()*width/map.rect().height())
				map=map.scaled(height, width)
				scene.addPixmap(map)
				self.ui.graphicsView.setScene(scene)
			else:
				msgBox = QtGui.QMessageBox()
				msgBox.setWindowTitle('Error al cargar')
				msgBox.setIcon(QtGui.QMessageBox.Information)
				msgBox.setText("No se pudo cargar la imagen.")
				msgBox.exec_()
				self.ui.btn_ok.setEnabled(False)


		self.ui.btn_cancel.clicked.connect(self.cancel)
		self.ui.btn_ok.clicked.connect(self.ok)
		self.ui.btn_marca.clicked.connect(self.nuevo_marca)
		self.ui.btn_tipo.clicked.connect(self.nuevo_tipo)
		self.ui.btn_agregar.clicked.connect(self.nuevo_imagen)
		self.show()
		self.parent.setEnabled(False)
		self.setEnabled(True)
		self.exec_()

	def nuevo_imagen(self):
		dialog = QtGui.QFileDialog(self)
		dialog.setNameFilter(self.tr("Images (*.png *.xpm *.jpg)"))
		dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
		if dialog.exec_():
			fileNames = dialog.selectedFiles()
			fileName = fileNames[0]
			self.ui.le_imagen.setText(fileName)
			scene = QtGui.QGraphicsScene(self)
			map=QtGui.QPixmap(fileName)
			width =  170
			height = int(map.rect().width()*width/map.rect().height())
			map=map.scaled(height, width)
			scene.addPixmap(map)
			self.ui.graphicsView.setScene(scene)
			self.ui.btn_ok.setEnabled(True)
	
	def nuevo_tipo(self):
		dialog_tipo = FormTipo(self, "Nuevo")
		if dialog_tipo.result:
			controlador('añadir tipo', dialog_tipo.tipo)
		self.ui.cb_tipo.clear()
		tipos = controlador('obtener tipos', None)
		for tipo in tipos:
			self.ui.cb_tipo.addItem(tipo[1], tipo[0])

	def nuevo_marca(self):
		dialog_marca = FormMarca(self, "Nuevo")
		
		if dialog_marca.result:
			controlador('añadir marca', dialog_marca.marca)

		self.ui.cb_marca.clear()
		marcas = controlador('obtener marcas', None)
		for marca in marcas:
			self.ui.cb_marca.addItem(marca[1], marca[0])

	def cancel(self):
		self.reject()
		self.parent.setEnabled(True)
	
	def ok(self):

		nombre_archivo = os.path.basename(self.ui.le_imagen.text())
		fecha = self.ui.sb_fecha.textFromValue(self.ui.sb_fecha.value())
		id_marca = self.ui.cb_marca.itemData(self.ui.cb_marca.currentIndex())
		id_tipo = self.ui.cb_tipo.itemData(self.ui.cb_tipo.currentIndex())
		
		self.vehiculo = [self.ui.le_modelo.text(),
						id_marca,
						id_tipo,
						self.ui.le_color.text(),
						self.ui.le_motor.text(),
						self.ui.le_peso.text(),
						self.ui.le_descripcion.text(),
						self.ui.le_rendimiento.text(),
						nombre_archivo,
						fecha
						]
		if id_marca!=None and id_tipo!=None:
			#if self.trigger == "Nuevo":
			try:
				shutil.copy2(self.ui.le_imagen.text(), self.parent.dir)
			except Exception as e:
				print e.args[0]
			self.result = True
			self.parent.setEnabled(True)
			self.accept()
	
	def closeEvent(self, event):
		self.parent.setEnabled(True)
		self.reject()
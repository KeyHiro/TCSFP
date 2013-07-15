#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
# Nombre archivo: forma_marca.py
import sys
from PySide import QtGui, QtCore

#Importamos el constructor de la clase generada automáticamente
from dialog_marca import Ui_Dialog
class FormMarca(QtGui.QDialog):
	""""""
	result = False
	trigger = None
	marca = []
	def __init__(self, parent=None, trigger=None):
		QtGui.QDialog.__init__(self, parent)
		self.parent = parent
		self.trigger = trigger
		self.ui =  Ui_Dialog()
		self.ui.setupUi(self)
		if(trigger == "Editar"):
			self.ui.le_nom.setText(parent.marcas[1])
			self.ui.le_pais.setText(parent.marcas[2])
		self.ui.btn_ok.clicked.connect(self.ok)
		self.ui.btn_cancel.clicked.connect(self.cancel)
		self.show()
		self.parent.setEnabled(False)
		self.setEnabled(True)
		self.exec_()

	def cancel(self):
		self.reject()
		self.parent.setEnabled(True)

	def ok(self):
		"""Se almacenan los datos en una lista la cual sera agregada a la base de datos
		   posteriormente, asegurando que los datos no sean nulos"""
		self.marca = [self.ui.le_nom.text(),
					self.ui.le_pais.text()
					]

		if self.ui.le_nom.text() != "" and self.ui.le_pais.text() != "":
			self.result = True
			self.accept()
			self.parent.setEnabled(True)

	def closeEvent(self, event):
		self.parent.setEnabled(True)
		self.reject()
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from dialog_tipo import Ui_Dialog

class FormTipo(QtGui.QDialog):
	""" Esta es la clase que se encarga de crear el formulario para agregar 
		un tipo de auto"""
	result = False
	trigger = None
	tipo = []
	
	def __init__(self, parent=None, trigger=None):
		"""Contructor"""
		QtGui.QDialog.__init__(self, parent)
		self.parent = parent
		self.trigger = trigger
		self.ui =  Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.btn_ok.clicked.connect(self.ok)
		self.ui.btn_cancel.clicked.connect(self.cancel)

		self.show()
		self.parent.setEnabled(False)
		self.setEnabled(True)
		self.exec_()

	def cancel(self):

		"""Se detiene el loop cerrando la ventana"""

		self.reject()
		self.parent.setEnabled(True)
	
	def ok(self):
		"""Almacena en una lista los datos ingresados por el usuario"""
		if(self.trigger == "Nuevo"):
			self.tipo = [self.ui.le_nom.text(),
						self.ui.sb_puertas.textFromValue(self.ui.sb_puertas.value())]
		
		if self.ui.le_nom.text() != "" :
			self.result = True
			self.accept()
			self.parent.setEnabled(True)
	
	def closeEvent(self, event):
		"""Lo que se hace cuando se cierra la ventana"""
		self.parent.setEnabled(True)
		self.reject()
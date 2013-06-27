#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
# Nombre archivo: view_form.py
import sys
from PySide import QtGui, QtCore

#Importamos el constructor de la clase generada automáticamente
from dialog_marca import Ui_Dialog
class FormMarca(QtGui.QDialog):

	def __init__(self, parent=None, trigger=None):
		QtGui.QDialog.__init__(self, parent)
		self.parent = parent
		self.ui =  Ui_Dialog()
		self.ui.setupUi(self)
		if(trigger == "Editar"):
			self.ui.le_nom.setText(parent.marcas[0])
			self.ui.le_pais.setText(parent.marcas[1])
		self.ui.btn_ok.clicked.connect(self.ok)
		self.ui.btn_cancel.clicked.connect(self.cancel)
		self.show()

	def cancel(self):
		self.reject()

	def ok(self):

		self.parent.marcas = [
				self.ui.le_nom.text(),
				self.ui.le_pais.text()
				]
		self.accept()

	def closeEvent(self, event):
		self.parent.setEnabled(True)
		self.reject()
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
		self.show()

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()

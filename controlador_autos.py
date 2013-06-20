#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

def __crear_tablas():
	"""Crea las tablas del proyecto de no existir."""
	pass

def __anyadir_auto():
	"""Anyade un auto a la tabla autos"""
	pass

def __anyadir_marca():
	"""Anyade un marca a la tabla marcas"""
	pass

def __editar_auto():
	"""Actualiza los campos de un auto en la tabla autos"""
	pass

def __editar_marca():
	"""Actualiza los campos de una marca en la tabla marcas"""
	pass

def __eliminar_auto():
	"""Elimina un auto de la tabla autos"""
	pass

def __eliminar_marca():
	"""Elimina una marca de la tabla marcas"""
	pass

def ejecutar(): # cambiar el nombre
	"""Ejecuta alguna de las funciones, dependiendo de los parametros dados"""
	f = [
		__crear_tablas,
		__anyadir_auto,
		__anyadir_marca,
		__editar_auto,
		__editar_marca,
		__eliminar_auto,
		__eliminar_marca
		]
	pass
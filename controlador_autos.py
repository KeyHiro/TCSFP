#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as s

def __crear_tablas():
	"""Crea las tablas del proyecto de no existir."""
	query = """CREATE TABLE IF NOT EXIST """
	tablas = {
				'marcas':"""marcas (id_marca INT AUTOINCREMENT PRIMARY KEY, nombre TEXT, pais TEXT)""",
				'tipos':"""tipos (id_tipo INT AUTOINCREMENT PRIMARY KEY, nombre TEXT, puertas INT)""",
				'autos':"""autos (
								id_auto INT AUTOINCREMENT PRIMARY KEY, modelo TEXT,
								fk_id_marca INT, fk_id_tipo INT,
								color TEXT, motor TEXT, peso FLOAT,
								descripcion TEXT, rendimiento INT, 
								imagen TEXT, fecha_creacion DATE, 
								FOREIGN KEY (fk_id_marca) REFERENCES marcas (id_marca) 
														ON UPDATE CASCADE ON DELETE RESTRICT,
								FOREIGN KEY (fk_id_tipo) REFERENCES tipos (id_tipo)
														ON UPDATE CASCADE ON DELETE RESTRICT
								""" 
			}
	## El profe recomienda que cuando el usuario seleccione la imagen,
	## se copie a un directorio propio y sea esa la referencia que se guarde..
	exec_db(query + tablas['marcas']) #son mas lineas lo sé... pero me guta como se vé (me salió un verso sin esfuerzo)
	exec_db(query + tablas['tipos'])
	exec_db(query + tablas['autos'])

def __anyadir_auto(*args):
	"""
		Anyade un auto a la tabla autos.
		Se supodrá que args tendrá el siguiente formato:
			(modelo, color, motor, peso, descripcion, 
				rendimiento, imagen, fecha_creacion, marca, tipo)
	"""
	# SON 11 !!!
	query = """INSERT INTO autos VALUES(?, marcas.id_marca, tipos.id_tipo,?,?,?,?,?,?,?,?)
				WHERE marcas.nombre == ? AND tipos.nombre == ?""" 
	try:
		exec_db(query, list(args))
	except:
		print "buuuu"

def __anyadir_marca(*args):
	"""
		Anyade un marca a la tabla marcas.
		Se supodrá que args tendrá el siguiente formato:
			(nombre, pais)
	"""
	query = """INSERT INTO marcas (nombre, pais) VALUES(?, ?)"""
	exec_db(query, list(args))

def __editar_auto(*args):
	"""Actualiza los campos de un auto en la tabla autos"""
	pass

def __editar_marca(*args):
	"""Actualiza los campos de una marca en la tabla marcas"""
	pass

def __eliminar_auto(*args):
	"""Elimina un auto de la tabla autos"""
	pass

def __eliminar_marca(*args):
	"""Elimina una marca de la tabla marcas"""
	pass

def ejecutar(func, *args): # cambiar el nombre
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
	with s.connect("autos_db.db") as conn:
		cursor = conn.cusor()
		global exec_db = cursor.execute 
		f[0](c); f[func](args) 
	
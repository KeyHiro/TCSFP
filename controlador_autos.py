#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as s

def __crear_tablas():
	"""Crea las tablas del proyecto de no existir."""
	query = """CREATE TABLE IF NOT EXISTS """
	tablas = {
				'marcas':"""marcas (id_marca INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, pais TEXT)""",
				'tipos':"""tipos (id_tipo INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, puertas INT)""",
				'autos':"""autos (
								id_auto INTEGER PRIMARY KEY AUTOINCREMENT, modelo TEXT,
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
			(modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion, 
				rendimiento, imagen, fecha_creacion, marca, tipo)
	"""
	# SON 12 !!!
	query = """INSERT INTO autos (modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion, 
				rendimiento, imagen, fecha_creacion, marca, tipo) 
				VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""" 
	exec_db(query, list(args))

def __anyadir_marca(*args):
	"""
		Anyade un marca a la tabla marcas.
		Se supodrá que args tendrá el siguiente formato:
			(nombre, pais)
	"""
	query = """INSERT INTO marcas (nombre, pais) VALUES(?, ?)"""
	exec_db(query, list(args))

def __editar_auto(*args):
	"""
		Actualiza los campos de un auto en la tabla autos
		Se supodrá que args tendrá el siguiente formato:
			(modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion, 
				rendimiento, imagen, fecha_creacion, marca, tipo, id_auto)
	"""
	query = """UPDATE autos SET modelo = ?, fk_id_marca = ?, fk_id_tipo = ?, color = ?, 
								motor = ?, peso = ?, descripcion = ?, rendimiento = ?, 
								imagen = ?, fecha_creacion = ?, marca = ?, tipo = ? 
				WHERE id_auto = ?""" 
	exec_db(query, list(args))

def __editar_marca(*args):
	"""
		Actualiza los campos de un auto en la tabla autos
		Se supodrá que args tendrá el siguiente formato:
			(nombre, pais, id_marca)
	"""
	query = """UPDATE marcas SET nombre = ?, pais = ? WHERE id_marca = ?""" 
	exec_db(query, list(args))

def __eliminar_auto(*args):
	"""
		Elimina un auto de la tabla autos
		Se supodrá que args tendrá el siguiente formato:
			(id_auto)
	"""
	query = """DELETE FROM autos WHERE id_marca = ?"""
	exec_db(query, list(args))

def __eliminar_marca(*args):
	"""
		Elimina una marca de la tabla marcas
		Se supodrá que args tendrá el siguiente formato:
			(id_marca)
	"""
	query = """DELETE FROM marcas WHERE id_marca = ?"""
	exec_db(query, list(args))

def __obtener_marcas(*args):
	"""
		Retorna todas las marcas de la tabla marcas
		Se supodrá que args tendrá el siguiente formato:
			(NONE)
	"""
	query = """SELECT * FROM marcas"""
	exec_db(query)

def __obtener_autos(*args):
	"""
		Retorna todos las autos de la tabla autos
		Se supodrá que args tendrá el siguiente formato:
			(NONE)
	"""
	query = """SELECT * FROM autos"""
	exec_db(query)

def ejecutar(func, *args): # cambiar el nombre
	"""
		Ejecuta alguna de las funciones, dependiendo de los parametros dados.
		Ej:
			ejecuta('añadir auto', modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion, 
				rendimiento, imagen, fecha_creacion, marca, tipo)
	"""
	f = {
		'añadir auto':__anyadir_auto,
		'añadir marca':__anyadir_marca,
		'editar auto':__editar_auto,
		'editar marca':__editar_marca,
		'eliminar auto':__eliminar_auto,
		'eliminar marca':__eliminar_marca,
		'obtener marcas':__obtener_marcas,
		'obtener autos':__obtener_autos
		}
	with s.connect("autos_db.db") as conn:
		cursor = conn.cusor()
		global exec_db
		exec_db = cursor.execute
		try:
			__crear_tablas()
			f[func](args)
		except Exception as e:
			print e.text()
		finally:
			return cursor.fetchall()


	
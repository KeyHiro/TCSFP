#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as s

def __crear_tablas():
	"""Crea las tablas del proyecto de no existir."""
	query = """CREATE TABLE IF NOT EXIST """
	marcas = """marcas (id_marca INT PRIMARY KEY, nombre TEXT, pais TEXT)"""
	tipos = """tipos (id_tipo INT PRIMARY KEY, nombre TEXT, puertas INT)"""
	autos = """autos (
					id_auto INT PRIMARY KEY, modelo TEXT,
					fk_id_marca INT, fk_id_tipo INT,
					color TEXT, motor TEXT, peso FLOAT,
					descripcion TEXT, rendimiento INT, 
					imagen TEXT, fecha_creacion DATE, 
					FOREIGN KEY (fk_id_marca) REFERENCES marcas (id_marca),
					FOREIGN KEY (fk_id_tipo) REFERENCES tipos (id_tipo)
					""" 
	cur.execute(query + marcas)
	cur.execute(query + tipos)
	cur.execute(query + autos)

def __anyadir_auto(*args):
	"""Anyade un auto a la tabla autos"""
	pass

def __anyadir_marca(*args):
	"""Anyade un marca a la tabla marcas"""
	pass

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
		global c = conn.cusor()
		f[0](c); f[func](args) 
	
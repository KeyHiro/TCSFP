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
)
"""
}
## El profe recomienda que cuando el usuario seleccione la imagen,
## se copie a un directorio propio y sea esa la referencia que se guarde..
exec_db(query + tablas['marcas']) #son mas lineas lo sé... pero me guta como se vé (me salió un verso sin esfuerzo)
exec_db(query + tablas['tipos'])
exec_db(query + tablas['autos'])
def __buscar_auto(args):
"""
Busca en la tabla autos los que cumplan las condiciones
de similitud?.
Se supodrá que args tendrá el siguiente formato:
(palabra)
"""
query = """SELECT a.id_auto FROM autos a, marcas m, tipos t WHERE
a.fk_id_marca = m.id_marca AND
a.fk_id_tipo = t.id_tipo AND
(a.modelo LIKE '%'||?||'%' OR
a.color LIKE '%'||?||'%' OR
a.motor LIKE '%'||?||'%' OR
a.peso LIKE '%'||?||'%' OR
a.descripcion LIKE '%'||?||'%' OR
a.rendimiento LIKE '%'||?||'%' OR
a.fecha_creacion LIKE '%'||?||'%' OR
m.nombre LIKE '%'||?||'%' OR
t.nombre LIKE '%'||?||'%')
"""
exec_db(query, [args]*9)

def __buscar_marca(args):
"""
Busca en la tabla marcas las que cumplan las condiciones
de similitud?.
Se supodrá que args tendrá el siguiente formato:
(palabra)
"""
query = """SELECT m.id_marca FROM marcas m WHERE
m.nombre LIKE '%'||?||'%' OR
m.pais LIKE '%'||?||'%'
"""
exec_db(query, [args]*2)

def __anyadir_auto(args):
"""
Anyade un auto a la tabla autos.
Se supodrá que args tendrá el siguiente formato:
(modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion,
rendimiento, imagen, fecha_creacion)
"""
# SON 12 !!!
query = """INSERT INTO autos (modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion,
rendimiento, imagen, fecha_creacion)
VALUES(?,?,?,?,?,?,?,?,?,?)"""
exec_db(query, args)

def __anyadir_marca(args):
"""
Anyade un marca a la tabla marcas.
Se supodrá que args tendrá el siguiente formato:
(nombre, pais)
"""
query = """INSERT INTO marcas (nombre, pais) VALUES(?, ?)"""
exec_db(query, args)

def __anyadir_tipo(args):
"""
Anyade un tipo a la tabla tipos.
Se supodrá que args tendrá el siguiente formato:
(nombre, puertas)
"""
# SON 12 !!!
query = """INSERT INTO tipos (nombre, puertas)
VALUES(?, ?)"""
exec_db(query, args)

def __editar_auto(args):
"""
Actualiza los campos de un auto en la tabla autos
Se supodrá que args tendrá el siguiente formato:
(modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion,
rendimiento, imagen, fecha_creacion, id_auto)
"""
query = """UPDATE autos SET modelo = ?, fk_id_marca = ?, fk_id_tipo = ?, color = ?,
motor = ?, peso = ?, descripcion = ?, rendimiento = ?,
imagen = ?, fecha_creacion = ?
WHERE id_auto = ?"""
exec_db(query, args)

def __editar_marca(args):
"""
Actualiza los campos de un auto en la tabla autos
Se supodrá que args tendrá el siguiente formato:
(nombre, pais, id_marca)
"""
query = """UPDATE marcas SET nombre = ?, pais = ? WHERE id_marca = ?"""
exec_db(query, args)

def __eliminar_auto(args):
"""
Elimina un auto de la tabla autos
Se supodrá que args tendrá el siguiente formato:
(id_auto)
"""
query = """DELETE FROM autos WHERE id_auto = ?"""
exec_db(query, args)

def __eliminar_marca(args):
"""
Elimina una marca de la tabla marcas
Se supodrá que args tendrá el siguiente formato:
(id_marca)
"""
query = """DELETE FROM marcas WHERE id_marca = ?"""
exec_db(query, args)

def __obtener_marca(args):
"""
Retorna la marca de la tabla marcas cuya id_marca sea igual
al parámetro entregado.
Se supodrá que args tendrá el siguiente formato:
(id_marca)
"""
query = """SELECT * FROM marcas WHERE id_marca = ?"""

exec_db(query, args)


def __obtener_auto(args):
"""
Retorna el auto de la tabla autos cuyo id_auto sea igual
al parámetro entregado.
Se supodrá que args tendrá el siguiente formato:
(id_auto)
"""
query = """SELECT * FROM autos WHERE id_auto = ?"""
exec_db(query, args)

def __obtener_tipo(args):
"""
Retorna el tipo de la tabla tipos cuyo id_tipo sea igual
al parámetro entregado.
Se supodrá que args tendrá el siguiente formato:
(id_tipo)
"""
query = """SELECT nombre FROM tipos WHERE id_tipo = ?"""
exec_db(query, args)

def __obtener_marcas(args):
"""
Retorna todas las marcas de la tabla marcas
Se supodrá que args tendrá el siguiente formato:
(NONE)
"""
query = """SELECT * FROM marcas"""
exec_db(query)

def __obtener_autos(args):
"""
Retorna todos los autos de la tabla autos
Se supodrá que args tendrá el siguiente formato:
(NONE)
"""
query = """SELECT * FROM autos"""
exec_db(query)

def __obtener_tipos(args):
"""
Retorna todos las tipos de la tabla tipos
Se supodrá que args tendrá el siguiente formato:
(NONE)
"""
query = """SELECT * FROM tipos"""
exec_db(query)

def __contar_autos_por_marca(args):
"""
Cuenta la cantidad de autos de una determinada
marca.
Se supodrá que args tendrá el siguiente formato:
(id_marca)
"""
query = """SELECT COUNT(fk_id_marca) FROM autos WHERE fk_id_marca = ?"""
exec_db(query, args)

def ejecutar(func, args): # cambiar el nombre
"""
Ejecuta alguna de las funciones, dependiendo de los parametros dados.
Ej:
ejecuta('añadir auto', [modelo, fk_id_marca, fk_id_tipo, color, motor, peso, descripcion,
rendimiento, imagen, fecha_creacion, marca, tipo])
"""
f = {
'añadir auto':__anyadir_auto,
'añadir marca':__anyadir_marca,
'añadir tipo':__anyadir_tipo,
'editar auto':__editar_auto,
'editar marca':__editar_marca,
'eliminar auto':__eliminar_auto,
'eliminar marca':__eliminar_marca,
'obtener marcas':__obtener_marcas,
'obtener autos':__obtener_autos,
'obtener tipos':__obtener_tipos,
'obtener marca':__obtener_marca,
'obtener auto':__obtener_auto,
'obtener tipo':__obtener_tipo,
'contar autos':__contar_autos_por_marca,
'buscar marca':__buscar_marca,
'buscar auto':__buscar_auto
}
with s.connect("autos_db.db") as conn:
cursor = conn.cursor()
global exec_db
exec_db = cursor.execute
try:
__crear_tablas()
f[func](args)
except Exception as e:
print e.args[0]
finally:
resultado = cursor.fetchall()
return resultado


    Status
    API
    Training
    Shop
    Blog
    About

    © 2013 GitHub, Inc.
    Terms
    Privacy
    Security
    Contact


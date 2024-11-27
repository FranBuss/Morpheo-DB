import pyodbc

from config import DRIVER, SERVER, DATABASE
from src.models.Libro import Libro

class LibroRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")

    def crear(self, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
              cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        cursor = self.conexion.cursor()
        nombre = nombre.capitalize()
        try:
            query = '''INSERT INTO dbo.LIBROS(
                        NOMBRE, ESTADO, GENERO, AUTOR, EDITORIAL, 
                        FECHA_PUBLICACION, PAGINA_ACTUAL, CANT_PAGINAS,
                        DESCRIPCION, CLASIFICACION, PUNTUACION, WIKI, TIPO
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                      cant_paginas, descripcion, clasificacion, puntuacion, wiki, "LIBRO")
            cursor.execute(query, values)
            self.conexion.commit()
            print("Libro creado correctamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al crear el Libro: ", ex)

    def eliminar(self, id):
        cursor = self.conexion.cursor()
        try:
            query = '''DELETE FROM dbo.LIBROS WHERE ID_LIBRO = {}'''.format(id)
            cursor.execute(query)
            self.conexion.commit()
            print("el libro se ha borrado exitosamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al borrar el libro: ", ex)

    def actualizar(self, id, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        cursor = self.conexion.cursor()

        nombre = nombre.capitalize()

        try:
            query = '''UPDATE dbo.LIBROS SET NOMBRE = ?, ESTADO = ?, GENERO = ?, AUTOR = ?, EDITORIAL = ?, 
                               FECHA_PUBLICACION = ?, PAGINA_ACTUAL = ?, CANT_PAGINAS = ?, 
                               DESCRIPCION = ?, CLASIFICACION = ?, PUNTUACION = ?, WIKI = ? WHERE ID_LIBRO = ?'''
            values = (nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                cant_paginas, descripcion, clasificacion, puntuacion, wiki, id)

            cursor.execute(query, values)
            a = cursor.rowcount
            self.conexion.commit()
            print("el libro se ha actualizado exitosamente.")
            cursor.close()
            return a
        except pyodbc.Error as ex:
            print("Error al actualizar el libro: ", ex)

    def lista_libros(self):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM LIBROS'''
        cursor.execute(query)
        libros = cursor.fetchall()
        cursor.close()
        return libros

    def buscar_libro_id(self, id) -> Libro | None:
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM LIBROS WHERE ID_LIBRO = {}'''.format(id)
        cursor.execute(query)
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            libro = Libro(
                resultado[0],
                resultado[1],
                resultado[2],
                resultado[3],
                resultado[4],
                resultado[5],
                resultado[6],
                resultado[7],
                resultado[8],
                resultado[9],
                resultado[10],
                resultado[11],
                resultado[12],
            )
            return libro
        else:
            return None

    def buscar_por_estado(self, estado):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM LIBROS WHERE ESTADO = ?'''
        cursor.execute(query, estado)
        libros = cursor.fetchall()
        cursor.close()
        return libros

    def buscar_por_nombre(self, nombre):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM LIBROS WHERE NOMBRE LIKE ?'''
        parametro = f"%{nombre}%"
        cursor.execute(query, parametro)
        libros = cursor.fetchall()
        cursor.close()
        return libros
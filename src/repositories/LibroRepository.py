import pyodbc

from config import DRIVER, SERVER, DATABASE
from src.models.Libro import Libro

class LibroRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")

    def crear(self, id, nombre, estado, genero, editorial, fecha_publicacion, pagina_actual, 
                cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        cursor = self.conexion.cursor()
        try:
            query = '''INSERT INTO dbo.LIBROS(
                        NOMBRE, ESTADO, GENERO, EDITORIAL, 
                        FECHA_PUBLICACION, PAGINA_ACTUAL, CANT_PAGINAS,
                        DESCRIPCION, CLASIFICACION, PUNTUACION, WIKI
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (self, id, nombre, estado, genero, editorial, 
                      fecha_publicacion, pagina_actual, cant_paginas,
                    descripcion, clasificacion, puntuacion, wiki)
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

    def actualizar(self, id, nombre, estado, genero, editorial, fecha_publicacion, pagina_actual, 
                cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        cursor = self.conexion.cursor()
        try:

            # Revision de codigo
            libro = self.buscar_libro_id(id)
            nuevo_nombre = nombre if libro.nombre() != nombre else libro.nombre()
            nuevo_estado = estado if libro.estado() != estado else libro.estado()
            nuevo_genero = genero if libro.genero() != genero else libro.genero()
            nuevo_editorial = editorial if libro.editorial() != editorial else libro.editorial()
            nueva_fecha_publicacion = fecha_publicacion if libro.fecha_publicacion() != fecha_publicacion else libro.fecha_publicacion()
            nueva_pagina_actual = pagina_actual if libro.pagina_actual() != pagina_actual else libro.pagina_actual()
            nueva_cant_paginas = cant_paginas if libro.cant_paginas() != cant_paginas else libro.cant_paginas()
            nuevo_descripcion = descripcion if libro.descripcion() != descripcion else libro.descripcion()
            nuevo_clasificacion = clasificacion if libro.clasificacion() != clasificacion else libro.clasificacion()
            nuevo_puntuacion = puntuacion if libro.puntuacion() != puntuacion else libro.puntuacion()
            nuevo_wiki = wiki if libro.wiki() != wiki else libro.wiki()

            query = '''UPDATE dbo.LIBROS SET NOMBRE = '?',ESTADO = '?', GENERO = '?', EDITORIAL = '?', 
                        FECHA_PUBLICACION = '?', PAGINA_ACTUAL = '?', CANT_PAGINAS = '?',
                        DESCRIPCION = '?', CLASIFICACION = '?', PUNTUACION = '?', WIKI = '?'''
            values = (nuevo_nombre, nuevo_estado, nuevo_genero, nuevo_editorial,
                      nueva_fecha_publicacion, nueva_pagina_actual, nueva_cant_paginas,
                    nuevo_descripcion, nuevo_clasificacion, nuevo_puntuacion, nuevo_wiki)

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
                resultado[13]
            )
            return libro
        else:
            return None
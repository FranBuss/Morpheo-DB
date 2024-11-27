import pyodbc

from config import DRIVER, SERVER, DATABASE
from src.models.Pelicula import Pelicula

class PeliculaRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")

    def crear(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        cursor = self.conexion.cursor()

        nombre = nombre.capitalize()

        try:
            query = '''INSERT INTO dbo.PELICULAS(
                    NOMBRE, GENERO, FECHA_ESTRENO, DURACION, PAIS, ESTADO,
                    DIRECTOR, DISTRIBUIDOR, ESTUDIO, PLATAFORMA, DESCRIPCION,
                    COMENTARIO, PUNTUACION, CALIFICACION, WIKI, TIPO
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                nombre, genero, fecha_estreno, duracion, pais, estado,
                director, distribuidor, estudio, plataforma, descripcion,
                comentario, puntuacion, calificacion, wiki, "PELICULA"
            )
            cursor.execute(query, values)
            self.conexion.commit()
            print("Pelicula creado correctamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al crear la pelicula: ", ex)

    def eliminar(self, id):
        cursor = self.conexion.cursor()
        try:
            query = '''DELETE FROM dbo.PELICULAS WHERE ID_PELICULA = {}'''.format(id)
            cursor.execute(query)
            self.conexion.commit()
            print("la pelicula se ha borrado exitosamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al borrar la pelicula: ", ex)

    def actualizar(self, id, nombre, genero, fecha_estreno, duracion, pais, estado, director,
                distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        cursor = self.conexion.cursor()

        nombre = nombre.capitalize()

        try:
            query = '''
                    UPDATE dbo.PELICULAS 
                    SET NOMBRE = ?, GENERO = ?, FECHA_ESTRENO = ?, DURACION = ?, PAIS = ?, ESTADO = ?, 
                        DIRECTOR = ?, DISTRIBUIDOR = ?, ESTUDIO = ?, PLATAFORMA = ?, DESCRIPCION = ?, 
                        COMENTARIO = ?, CALIFICACION = ?, PUNTUACION = ?, WIKI = ?
                    WHERE ID_PELICULA = ?
                    '''
            values = (nombre, genero, fecha_estreno, duracion, pais, estado, director,
                distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki, id)
            
            cursor.execute(query, values)
            a = cursor.rowcount
            self.conexion.commit()
            print("la pelicula se ha actualizado exitosamente.")
            cursor.close()
            return a
        except pyodbc.Error as ex:
            print("Error al actualizar la pelicula: ", ex)

    def lista_peliculas(self):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM PELICULAS'''
        cursor.execute(query)
        peliculas = cursor.fetchall()
        return peliculas

    def buscar_pelicula_id(self, id) -> Pelicula:
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM PELICULAS WHERE ID_PELICULA = {}'''.format(id)
        cursor.execute(query)
        resultado = cursor.fetchone()

        if resultado:
            pelicula = Pelicula(
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
                resultado[13],
                resultado[14],
                resultado[15],
                resultado[16],
            )
            return pelicula
        else:
            return None

    def buscar_por_estado(self, estado):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM PELICULAS WHERE ESTADO = ?'''
        cursor.execute(query, estado)
        peliculas = cursor.fetchall()
        cursor.close()
        return peliculas

    def buscar_por_nombre(self, nombre):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM dbo.PELICULAS WHERE NOMBRE LIKE ?'''
        parametro = f"%{nombre}%"
        cursor.execute(query, parametro)
        peliculas = cursor.fetchall()
        cursor.close()
        return peliculas
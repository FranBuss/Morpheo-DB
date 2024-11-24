import pyodbc

from config import DRIVER, SERVER, DATABASE
from src.models.Pelicula import Pelicula

class PeliculaRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")

    def crear(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        cursor = self.conexion.cursor()
        try:
            query = '''INSERT INTO dbo.PELICULAS(
                    NOMBRE, GENERO, FECHA_ESTRENO, DURACION, PAIS, ESTADO,
                    DIRECTOR, DISTRIBUIDOR, ESTUDIO, PLATAFORMA, DESCRIPCION,
                    COMENTARIO, PUNTUACION, CALIFICACION, WIKI
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                nombre, genero, fecha_estreno, duracion, pais, estado,
                director, distribuidor, estudio, plataforma, descripcion,
                comentario, puntuacion, calificacion, wiki
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
        try:

            # Revision de codigo
            pelicula = self.buscar_pelicula_id(id)
            nuevo_nombre = nombre if pelicula.nombre() != nombre else pelicula.nombre()
            nuevo_genero = genero if pelicula.genero() != genero else pelicula.genero()
            nueva_fecha_estreno = fecha_estreno if pelicula.fecha_estreno() != fecha_estreno else pelicula.fecha_estreno()
            nuevo_duracion = duracion if pelicula.duracion() != duracion else pelicula.duracion()
            nuevo_pais = pais if pelicula.pais() != pais else pelicula.pais()
            nuevo_estado = estado if pelicula.estado() != estado else pelicula.estado()
            nuevo_director = director if pelicula.director() != director else pelicula.director()
            nuevo_distribuidor = distribuidor if pelicula.distribuidor() != distribuidor else pelicula.distribuidor()
            nuevo_estudio = estudio if pelicula.estudio() != estudio else pelicula.estudio()
            nuevo_plataforma = plataforma if pelicula.plataforma() != plataforma else pelicula.plataforma()
            nuevo_descripcion = descripcion if pelicula.descripcion() != descripcion else pelicula.descripcion()
            nuevo_comentario = comentario if pelicula.comentario() != comentario else pelicula.comentario()
            nuevo_puntuacion = puntuacion if pelicula.puntuacion() != puntuacion else pelicula.puntuacion()
            nuevo_calificacion = calificacion if pelicula.calificacion() != calificacion else pelicula.calificacion()
            nuevo_wiki = wiki if pelicula.wiki() != wiki else pelicula.wiki()

            query = '''UPDATE dbo.PELICULAS SET NOMBRE = '?', GENERO = '?', FECHA_ESTRENO = '?', 
                        DURACION = ?, PAIS = '?', ESTADO = ?, DIRECTOR = '?', DISTRIBUIDOR = '?', ESTUDIO = '?',
                        PLATAFORMA = ?, DESCRIPCION = '?', COMENTARIO = '?', CALIFICACION = ?, PUNTUACION = ?, WIKI = ?'''
            values = (nuevo_nombre, nuevo_genero, nueva_fecha_estreno, nuevo_duracion, nuevo_pais, nuevo_estado,
                    nuevo_director, nuevo_distribuidor, nuevo_estudio, nuevo_plataforma, nuevo_descripcion,
                    nuevo_comentario, nuevo_calificacion, nuevo_puntuacion, nuevo_wiki)
            
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
                resultado[13]
            )
            return pelicula
        else:
            return None
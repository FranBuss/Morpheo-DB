import pyodbc

from config import DRIVER, SERVER, DATABASE
from src.models.Juego import Juego

class JuegoRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")

    def crear(self, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
            modo_juego, descripcion, comentario, clasificacion, puntuacion):
        cursor = self.conexion.cursor()

        nombre = nombre.capitalize()

        try:
            query = '''INSERT INTO dbo.JUEGOS(
                            NOMBRE, GENERO, FECHA_SALIDA, ESTADO, DESARROLLADOR, 
                            DISTRIBUIDOR, PLATAFORMA, TEMATICA, MODO_JUEGO, DESCRIPCION, 
                            COMENTARIO, CLASIFICACION, PUNTUACION, TIPO
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                nombre, genero, fecha_salida, estado,
                desarrollador, distribuidor, plataforma,
                tematica, modo_juego, descripcion,
                comentario, clasificacion, puntuacion, "JUEGO"
            )
            cursor.execute(query, values)
            self.conexion.commit()
            print("Juego creado correctamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al crear el juego: ", ex)

    def eliminar(self, id):
        cursor = self.conexion.cursor()
        try:
            query = '''DELETE FROM dbo.JUEGOS WHERE ID_JUEGO = {}'''.format(id)
            cursor.execute(query)
            self.conexion.commit()
            print("el juego se ha borrado exitosamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al borrar el juego: ", ex)

    def actualizar(self, id, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
                   modo_juego, descripcion, comentario, clasificacion, puntuacion):
        cursor = self.conexion.cursor()

        try:
            query = '''UPDATE dbo.JUEGOS SET 
                        NOMBRE = ?, GENERO = ?, FECHA_SALIDA = ?, ESTADO = ?, 
                        DESARROLLADOR = ?, DISTRIBUIDOR = ?, PLATAFORMA = ?, TEMATICA = ?, 
                        MODO_JUEGO = ?, DESCRIPCION = ?, COMENTARIO = ?, CLASIFICACION = ?, 
                        PUNTUACION = ? WHERE ID_JUEGO = ?'''
            values = (nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
                      modo_juego, descripcion, comentario, clasificacion, puntuacion, id)

            cursor.execute(query, values)
            self.conexion.commit()
            a = cursor.rowcount
            print("El juego se ha actualizado exitosamente.")
            cursor.close()
            return a
        except pyodbc.Error as ex:
            print("Error al actualizar el juego: ", ex)

    def lista_juegos(self):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM JUEGOS'''
        cursor.execute(query)
        juegos = cursor.fetchall()
        cursor.close()
        return juegos

    def buscar_juego_id(self, id) -> Juego | None:
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM JUEGOS WHERE ID_JUEGO = {}'''.format(id)
        cursor.execute(query)
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            juego = Juego(
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
                resultado[14]
            )
            return juego
        else:
            return None

    def buscar_por_estado(self, estado):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM JUEGOS WHERE ESTADO = ?'''
        cursor.execute(query, estado)
        juegos = cursor.fetchall()
        cursor.close()
        return juegos

    def buscar_por_nombre(self, nombre):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM JUEGOS WHERE NOMBRE LIKE ?'''
        parametro = f"%{nombre}%"
        cursor.execute(query, parametro)
        juegos = cursor.fetchall()
        cursor.close()
        return juegos
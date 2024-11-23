import pyodbc

from config import DRIVER, SERVER, DATABASE
from src.models.Juego import Juego

class JuegoRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")

    def crear(self, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
            modo_juego, descripcion, comentario, clasificacion, puntuacion):
        cursor = self.conexion.cursor()
        try:
            query = '''INSERT INTO dbo.JUEGOS(
                            NOMBRE, GENERO, FECHA_SALIDA, ESTADO, DESARROLLADOR, 
                            DISTRIBUIDOR, PLATAFORMA, TEMATICA, MODO_JUEGO, DESCRIPCION, 
                            COMENTARIO, CLASIFICACION, PUNTUACION
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                nombre, genero, fecha_salida, estado,
                desarrollador, distribuidor, plataforma,
                tematica, modo_juego, descripcion,
                comentario, clasificacion, puntuacion
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

            # Revision de codigo
            juego = self.buscar_juego_id(id)
            nuevo_nombre = nombre if juego.nombre() != nombre else juego.nombre()
            nuevo_genero = genero if juego.genero() != genero else juego.genero()
            nueva_fecha_salida = fecha_salida if juego.fecha_salida() != fecha_salida else juego.fecha_salida()
            nuevo_estado = estado if juego.estado() != estado else juego.estado()
            nuevo_desarrollador = desarrollador if juego.desarrollador() != desarrollador else juego.desarrollador()
            nuevo_distribuidor = distribuidor if juego.distribuidor() != distribuidor else juego.distribuidor()
            nuevo_plataforma = plataforma if juego.plataforma() != plataforma else juego.plataforma()
            nuevo_tematica = tematica if juego.tematica() != tematica else juego.tematica()
            nuevo_modo_juego = modo_juego if juego.modo_juego() != modo_juego else juego.modo_juego()
            nuevo_descripcion = descripcion if juego.descripcion() != descripcion else juego.descripcion()
            nuevo_comentario = comentario if juego.comentario() != comentario else juego.comentario()
            nuevo_clasificacion = clasificacion if juego.clasificacion() != clasificacion else juego.clasificacion()
            nuevo_puntuacion = puntuacion if juego.puntuacion() != puntuacion else juego.puntuacion()

            query = '''UPDATE dbo.JUEGOS SET NOMBRE = '?', GENERO = '?', FECHA_SALIDA = '?', 
                        ESTADO = ?, DESARROLLADOR = '?', DISTRIBUIDOR = '?', PLATAFORMA = ?,
                        TEMATICA = '?', MODO_JUEGO = ?, DESCRIPCION = '?', COMENTARIO = '?',
                        CLASIFICACION = ?, PUNTUACION = ?'''
            values = (nuevo_nombre, nuevo_genero, nueva_fecha_salida, nuevo_estado, nuevo_desarrollador,
                      nuevo_distribuidor, nuevo_plataforma, nuevo_tematica, nuevo_modo_juego, nuevo_descripcion,
                      nuevo_comentario, nuevo_clasificacion, nuevo_puntuacion)

            cursor.execute(query, values)
            a = cursor.rowcount
            self.conexion.commit()
            print("el juego se ha actualizado exitosamente.")
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
                resultado[13]
            )
            return juego
        else:
            return None



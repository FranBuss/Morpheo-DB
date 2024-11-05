import pyodbc
from config import DRIVER, SERVER, DATABASE

class ServicioJuego:

    def __init__(self):
        #self.conexion = pyodbc.connect("DRIVER={SQL Server};SERVER=DESKTOP-1AMST2L\\SQLEXPRESS;DATABASE=MORPHEO-DB")
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")


    def crear(self, nombre, genero):
        cursor = self.conexion.cursor()
        try:
            query = '''INSERT INTO dbo.JUEGOS(NOMBRE, GENERO) VALUES ('{}','{}')'''.format(nombre, genero)
            cursor.execute(query)
            self.conexion.commit()
            print("Juego creado correctamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al crear el juego: ", ex)

    def eliminar(self, nombre):
        cursor = self.conexion.cursor()
        try:
            query = '''DELETE FROM dbo.JUEGOS WHERE NOMBRE = {}'''.format(nombre)
            cursor.execute(query)
            self.conexion.commit()
            print("el juego se ha borrado exitosamente.")
            cursor.close()
        except pyodbc.Error as ex:
            print("Error al borrar el juego: ", ex)

    def actualizar(self, id, nombre, genero):
        cursor = self.conexion.cursor()
        try:
            query = '''UPDATE dbo.JUEGOS SET NOMBRE = '{}', GENERO = '{}' WHERE ID_JUEGO = {}'''.format(nombre, genero,
                                                                                                        id)
            cursor.execute(query)
            a = cursor.rowcount
            self.conexion.commit()
            print("el juego se ha borrado exitosamente.")
            cursor.close()
            return a
        except pyodbc.Error as ex:
            print("Error al borrar el juego: ", ex)

    def lista_juegos(self):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM JUEGOS'''
        cursor.execute(query)
        juegos = cursor.fetchall()
        return juegos

    def buscar_juego_nombre(self, nombre):
        cursor = self.conexion.cursor()
        query = '''SELECT * FROM JUEGOS WHERE NOMBRE = {}'''.format(nombre)
        cursor.execute(query)
        juegos = cursor.fetchone()
        return juegos

nuevoServicio = ServicioJuego()
lista = nuevoServicio.lista_juegos()

for e in lista:
    print(e,"\n")

import pyodbc
from config import DRIVER, SERVER, DATABASE
from src.models.Juego import Juego


class ServicioJuego:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")


    def crear(self, nombre, genero):
        cursor = self.conexion.cursor()
        try:

            #Instancio nuevo juego
            juego = Juego(
                nombre= nombre.upper(),
                genero= genero.upper()
            )

            query = '''INSERT INTO dbo.JUEGOS(NOMBRE, GENERO) VALUES ('{}','{}')'''.format(juego.get_nombre(), juego.get_genero())
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

    def actualizar(self, nombre, genero):
        cursor = self.conexion.cursor()
        try:

            # Revision de codigo
            juego = self.buscar_juego_nombre(nombre)
            nuevo_nombre = nombre if juego.get_nombre() != nombre else juego.get_nombre()
            nuevo_genero = genero if juego.get_genero() != genero else juego.get_genero()

            query = '''UPDATE dbo.JUEGOS SET NOMBRE = '{}', GENERO = '{}' WHERE ID_JUEGO = {}'''.format(nuevo_nombre, nuevo_genero,                                                                                  id)
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
        resultado = cursor.fetchone()

        if resultado:
            juego = Juego(resultado[0], resultado[1])
            return juego
        else:
            return None

nuevoServicio = ServicioJuego()
lista = nuevoServicio.lista_juegos()

for e in lista:
    print(e,"\n")

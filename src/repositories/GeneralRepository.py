import pyodbc

from config import DRIVER, SERVER, DATABASE

class GeneralRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")


    def lista_todo(self):
        cursor = self.conexion.cursor()
        query = '''SELECT id_pelicula as id, nombre, estado, puntuacion, tipo FROM PELICULAS
                    UNION
                    SELECT id_juego, nombre, estado, puntuacion, tipo FROM JUEGOS
                    UNION
                    SELECT ID_LIBRO, nombre, estado, puntuacion, tipo FROM LIBROS'''
        cursor.execute(query)
        lista = cursor.fetchall()
        cursor.close()
        return lista

    def listar_por_puntuacion(self, puntuacion):
        cursor = self.conexion.cursor()
        query = '''SELECT id_pelicula as id, nombre, estado, puntuacion, tipo FROM PELICULAS where puntuacion >= {}
                    UNION
                    SELECT id_juego, nombre, estado, puntuacion, tipo FROM JUEGOS where puntuacion >= {}
                    UNION
                    SELECT ID_LIBRO, nombre, estado, puntuacion, tipo FROM LIBROS where puntuacion >= {}'''.format(puntuacion, puntuacion, puntuacion)
        cursor.execute(query)
        lista = cursor.fetchall()
        cursor.close()
        return lista

    def buscar_por_nombre(self, nombre):
        cursor = self.conexion.cursor()
        query = '''SELECT id_pelicula as id, nombre, estado, puntuacion, tipo FROM PELICULAS where nombre LIKE ?
                   UNION
                   SELECT id_juego, nombre, estado, puntuacion, tipo FROM JUEGOS where nombre LIKE ?
                   UNION
                   SELECT ID_LIBRO, nombre, estado, puntuacion, tipo FROM LIBROS where nombre LIKE ?'''
        # Usar % para realizar la búsqueda con comodín
        nombre_param = f"%{nombre}%"
        cursor.execute(query, (nombre_param, nombre_param, nombre_param))
        juegos = cursor.fetchall()
        cursor.close()
        return juegos

if __name__ == "__main__":
    repo = GeneralRepository()
    lista = repo.lista_todo()

    for e in lista:
        print(e[0], e[1], e[2], e[3], e[4])
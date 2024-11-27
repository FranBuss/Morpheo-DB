import pyodbc

from config import DRIVER, SERVER, DATABASE

class GeneralRepository:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")


    def lista_todo(self):
        cursor = self.conexion.cursor()
        query = '''SELECT id_pelicula as id, nombre, estado, puntuacion FROM PELICULAS
                    UNION
                    SELECT id_juego, nombre, estado, puntuacion FROM JUEGOS
                    UNION
                    SELECT ID_LIBRO, nombre, estado, puntuacion FROM LIBROS'''
        cursor.execute(query)
        lista = cursor.fetchall()
        cursor.close()
        return lista

if __name__ == "__main__":
    repo = GeneralRepository()
    lista = repo.lista_todo()

    for e in lista:
        print(e[0], e[1], e[2], e[3])
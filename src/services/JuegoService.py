import pyodbc
from src.repositories.JuegoRepository import  JuegoRepository
from src.models.Juego import Juego


class ServicioJuego:

    def __init__(self):
        self.juegoRepository = JuegoRepository()


    def crear(self, nombre, genero):
        self.juegoRepository.crear(nombre, genero)

    def eliminar(self, nombre):
        pass

    def actualizar(self, nombre, genero):
        pass

    def lista_juegos(self):
        pass

    def buscar_juego_id(self, id):
        pass


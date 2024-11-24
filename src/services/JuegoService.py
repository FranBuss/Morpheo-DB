import pyodbc
from src.repositories.JuegoRepository import  JuegoRepository
from src.models.Juego import Juego


class ServicioJuego:

    def __init__(self):
        self.juegoRepository = JuegoRepository()


    def crear(self, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
            modo_juego, descripcion, comentario, clasificacion, puntuacion):
        self.juegoRepository.crear(nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
            modo_juego, descripcion, comentario, clasificacion, puntuacion)

    def eliminar(self, id):
        self.juegoRepository.eliminar(id)

    def actualizar(self, id, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
              modo_juego, descripcion, comentario, clasificacion, puntuacion):
        self.juegoRepository.actualizar(id, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
              modo_juego, descripcion, comentario, clasificacion, puntuacion)

    def lista_juegos(self):
        return self.juegoRepository.lista_juegos()

    def buscar_juego_id(self, id):
        return self.juegoRepository.buscar_juego_id(id)


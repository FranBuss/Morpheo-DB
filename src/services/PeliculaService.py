import pyodbc
from src.repositories.PeliculaRepository import  PeliculaRepository
from src.models.Pelicula import Pelicula


class ServicioPelicula:

    def __init__(self):
        self.peliculaRepository = PeliculaRepository()


    def crear(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        self.PeliculaRepository.crear(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki)

    def eliminar(self, nombre):
        pass

    def actualizar(self, nombre, genero):
        pass

    def lista_peliculas(self):
        pass

    def buscar_pelicula_id(self, id):
        return self.peliculaRepository.buscar_pelicula_id(id)


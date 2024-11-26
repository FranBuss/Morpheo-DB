import pyodbc
from src.repositories.PeliculaRepository import  PeliculaRepository


class ServicioPelicula:

    def __init__(self):
        self.peliculaRepository = PeliculaRepository()


    def crear(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        self.peliculaRepository.crear(nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki)

    def eliminar(self, id):
        self.peliculaRepository.eliminar(id)

    def actualizar(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        self.peliculaRepository.actualizar(nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki)

    def lista_peliculas(self):
        return self.peliculaRepository.lista_peliculas()

    def buscar_pelicula_id(self, id):
        return self.peliculaRepository.buscar_pelicula_id(id)

    def buscar_por_estado(self, estado):
        return self.peliculaRepository.buscar_por_estado(estado)

    def buscar_por_nombre(self, nombre):
        return self.peliculaRepository.buscar_por_nombre(nombre)

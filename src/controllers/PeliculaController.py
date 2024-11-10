from src.services.PeliculaService import ServicioPelicula
from src.models.Pelicula import Pelicula


class PeliculaController:

    def __init__(self):
        self.servicioPelicula = ServicioPelicula()

    def create_movie(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        self.servicioJuego.crear(nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki)

    def buscar_pelicula_id(self, id):
        pelicula = self.servicioPelicula.buscar_pelicula_id(id)
        return pelicula


if __name__ == "__main__":

    PeliculaController().create_movie("SHREK")
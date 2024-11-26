from src.services.PeliculaService import ServicioPelicula


class PeliculaController:

    def __init__(self):
        self.servicioPelicula = ServicioPelicula()

    def create_movie(self, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        self.servicioPelicula.crear(nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki)

    def buscar_pelicula_id(self, id):
        pelicula = self.servicioPelicula.buscar_pelicula_id(id)
        return pelicula

    def listar_peliculas(self):
        return self.servicioPelicula.lista_peliculas()

    def eliminar(self, id):
        self.servicioPelicula.eliminar(id)

    def actualizar(self, id, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        self.servicioPelicula.actualizar(id, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki)

    def buscar_por_estado(self, estado):
        self.servicioPelicula.buscar_por_estado(estado)

    def buscar_por_nombre(self, nombre):
        self.servicioPelicula.buscar_por_nombre(nombre)
from src.services.JuegoService import ServicioJuego
from src.models.Juego import Juego


class JuegoController:

    def __init__(self):
        self.servicioJuego = ServicioJuego()

    def create_game(self, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
            modo_juego, descripcion, comentario, clasificacion, puntuacion):
        self.servicioJuego.crear(nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
            modo_juego, descripcion, comentario, clasificacion, puntuacion)

    def buscar_juego_id(self, id):
        juego = self.servicioJuego.buscar_juego_id(id)
        return juego


if __name__ == "__main__":

    JuegoController().create_game("HADES")
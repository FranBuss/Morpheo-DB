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

    def listar_juegos(self):
        juegos = self.servicioJuego.lista_juegos()
        return juegos

    def eliminar_juego(self, id):
        self.servicioJuego.eliminar(id)


if __name__ == "__main__":
    juegos = JuegoController().listar_juegos()
    for juego in juegos:
        print(juego)

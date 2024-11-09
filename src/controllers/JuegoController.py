from src.services.JuegoService import ServicioJuego


class JuegoController:

    def __init__(self):
        self.servicioJuego = ServicioJuego()

    def create_game(self, nombre, genero):
        self.servicioJuego.crear(nombre, genero)

    def buscar_juego_id(self, id):
        self.servicioJuego.buscar_juego_id(id)

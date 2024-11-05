from src.configurations.DatabaseManager import DatabaseManager
from src.services.JuegoService import ServicioJuego
from PyQt6.QtSql import *

class JuegoController:

    def __init__(self):
        pass

    @staticmethod
    def create_game() -> None:
        servicioJuego = ServicioJuego()
        juego = servicioJuego.crear()

JuegoController.getJuego(1)
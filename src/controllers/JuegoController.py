from src.configurations.DatabaseManager import DatabaseManager
from src.models.Juego import Juego
from PyQt6.QtSql import *

class JuegoController:

    def __init__(self):
        pass



    @staticmethod
    def getAllJuegos() -> None:
        db = DatabaseManager()
        juegos = db.select_data('SELECT * FROM JUEGOS')
        for juego in juegos:
            print(juego)

    @staticmethod
    def getJuego(id) -> None:
        db = DatabaseManager()
        juego = db.select_data(f'SELECT * FROM JUEGOS WHERE ID_JUEGO = {id}')
        print(juego)

JuegoController.getJuego(1)
from src.configurations.DatabaseManager import DatabaseManager

class JuegoController:

    def __init__(self):
        pass

    @staticmethod
    def getAllJuegos() -> None:
        db = DatabaseManager()
        juegos = db.select_data('SELECT * FROM JUEGOS')
        for juego in juegos:
            print(juego)
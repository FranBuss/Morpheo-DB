from src.configurations.DatabaseManager import DatabaseManager


class Juego:

    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def add_juego(self):
        db = DatabaseManager()
        db.insert_data('INSERT INTO dbo.JUEGOS(NOMBRE, GENERO) VALUES (? ,?)',
                       [f"{self.nombre}", f"{self.genero}"])



juego = Juego("DARK SOULS", "Soulslike")
juego.add_juego()


from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt6.QtWidgets import QWidget
from src.models.Juego import Juego

class VistaJuego(QMainWindow):

     def __init__(self):
        super(VistaJuego, self).__init__()
        loadUi('diseño.ui', self)

        self.database = Juego()
    
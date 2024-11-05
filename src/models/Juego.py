import json

import pyodbc

from src.configurations.DatabaseManager import DatabaseManager


class Juego:

    def __init__(self, nombre, genero):
        self.__nombre = nombre
        self.__genero = genero

    def get_nombre(self):
        return self.__nombre

    def get_genero(self):
        return self.__genero
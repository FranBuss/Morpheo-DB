import json

import pyodbc

from src.configurations.DatabaseManager import DatabaseManager


class Juego:

    def __init__(self, id, nombre, genero, fecha_salida, estado, desarrollador, distribuidor, plataforma, tematica,
                modo_juego, descripcion, comentario, clasificacion, puntuacion):
        self.__id = id
        self.__nombre = nombre
        self.__genero = genero
        self.__fecha_salida = fecha_salida
        self.__estado = estado
        self.__desarrollador = desarrollador
        self.__distribuidor = distribuidor
        self.__plataforma = plataforma
        self.__tematica = tematica
        self.__modo_juego = modo_juego
        self.__descripcion = descripcion
        self.__comentario = comentario
        self.__clasificacion = clasificacion
        self.__puntuacion = puntuacion

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, value):
        self.__genero = value

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, value):
        self.__fecha_salida = value

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, value):
        self.__estado = value

    @property
    def desarrollador(self):
        return self.__desarrollador

    @desarrollador.setter
    def desarrollador(self, value):
        self.__desarrollador = value

    @property
    def distribuidor(self):
        return self.__distribuidor

    @distribuidor.setter
    def distribuidor(self, value):
        self.__distribuidor = value

    @property
    def plataforma(self):
        return self.__plataforma

    @plataforma.setter
    def plataforma(self, value):
        self.__plataforma = value

    @property
    def tematica(self):
        return self.__tematica

    @tematica.setter
    def tematica(self, value):
        self.__tematica = value

    @property
    def modo_juego(self):
        return self.__modo_juego

    @modo_juego.setter
    def modo_juego(self, value):
        self.__modo_juego = value

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

    @property
    def comentario(self):
        return self.__comentario

    @comentario.setter
    def comentario(self, value):
        self.__comentario = value

    @property
    def clasificacion(self):
        return self.__clasificacion

    @clasificacion.setter
    def clasificacion(self, value):
        self.__clasificacion = value

    @property
    def puntuacion(self):
        return self.__puntuacion

    @puntuacion.setter
    def puntuacion(self, value):
        self.__puntuacion = value

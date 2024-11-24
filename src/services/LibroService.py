import pyodbc
from src.repositories.LibroRepository import  LibroRepository
from src.models.Libro import Libro

class ServicioLibro:

    def __init__(self):
        self.libroRepository = LibroRepository()


    def crear(self, id, nombre, estado, genero, editorial, fecha_publicacion, pagina_actual, 
                cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        self.libroRepository.crear(self, id, nombre, estado, genero, editorial, fecha_publicacion, pagina_actual, 
                cant_paginas, descripcion, clasificacion, puntuacion, wiki)

    def eliminar(self, id):
        self.libroRepository.eliminar(id)

    def actualizar(self, nombre, genero):
        pass

    def lista_libros(self):
        return self.libroRepository.lista_libros()

    def buscar_libro_id(self, id):
        return self.libroRepository.buscar_libro_id(id)
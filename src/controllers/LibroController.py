from src.services.LibroService import ServicioLibro
from src.models.Libro import Libro

class LibroController:

    def __init__(self):
        self.servicioLibro = ServicioLibro()

    def create_libro(self, id, nombre, estado, genero, editorial, fecha_publicacion, pagina_actual, 
                cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        self.serviciolibro.crear(self, id, nombre, estado, genero, editorial, fecha_publicacion, pagina_actual, 
                cant_paginas, descripcion, clasificacion, puntuacion, wiki)

    def buscar_libro_id(self, id):
        libro = self.servicioLibro.buscar_libro_id(id)
        return libro

    def listar_libros(self):
        libros = self.servicioLibro.lista_libros()
        return libros

    def eliminar_libro(self, id):
        self.servicioLibro.eliminar(id)


if __name__ == "__main__":
    libros = LibroController().listar_libros()
    for libro in libros:
        print(libro)

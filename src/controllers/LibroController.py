from src.services.LibroService import ServicioLibro
from src.models.Libro import Libro

class LibroController:

    def __init__(self):
        self.servicioLibro = ServicioLibro()

    def create_libro(self, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        self.serviciolibro.crear(self, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                cant_paginas, descripcion, clasificacion, puntuacion, wiki)

    def actualizar(self, id, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        self.servicioLibro.actualizar(id, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                cant_paginas, descripcion, clasificacion, puntuacion, wiki)

    def listar_libros(self):
        return self.servicioLibro.lista_libros()

    def eliminar_libro(self, id):
        self.servicioLibro.eliminar(id)

    def buscar_libro_id(self, id):
        return self.servicioLibro.buscar_libro_id(id)

    def buscar_por_estado(self, estado):
        return self.servicioLibro.buscar_por_estado(estado)

    def buscar_por_nombre(self, nombre):
        return self.servicioLibro.buscar_por_nombre(nombre)



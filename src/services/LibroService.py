from src.repositories.LibroRepository import LibroRepository

class ServicioLibro:

    def __init__(self):
        self.libroRepository = LibroRepository()

    def crear(self, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
              cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        self.libroRepository.crear(nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                                   cant_paginas, descripcion, clasificacion, puntuacion, wiki)

    def eliminar(self, id):
        self.libroRepository.eliminar(id)

    def actualizar(self, id, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                   cant_paginas, descripcion, clasificacion, puntuacion, wiki):
        self.libroRepository.actualizar(id, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                                        cant_paginas, descripcion, clasificacion, puntuacion, wiki)

    def lista_libros(self):
        return self.libroRepository.lista_libros()

    def buscar_libro_id(self, id):
        return self.libroRepository.buscar_libro_id(id)

    def buscar_por_estado(self, estado):
        return self.libroRepository.buscar_por_estado(estado)

    def buscar_por_nombre(self, nombre):
        return self.libroRepository.buscar_por_nombre(nombre)

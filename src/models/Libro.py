class Libro:

    def __init__(self, id, nombre, estado, genero, autor, editorial, fecha_publicacion, pagina_actual,
                cant_paginas, descripcion, clasificacion, puntuacion, wiki, tipo):
        self.__id = id
        self.__nombre = nombre
        self.__estado = estado
        self.__genero = genero
        self.__autor = autor
        self.__editorial = editorial
        self.__fecha_publicacion = fecha_publicacion
        self.__pagina_actual = pagina_actual
        self.__cant_paginas = cant_paginas
        self.__descripcion = descripcion
        self.__clasificacion = clasificacion
        self.__puntuacion = puntuacion
        self.__wiki = wiki
        self.__tipo = tipo

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
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, value):
        self.__estado = value

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, value):
        self.__genero = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def id(self, value):
        self.__autor = value

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, value):
        self.__editorial = value

    @property
    def fecha_publicacion(self):
        return self.__fecha_publicacion

    @fecha_publicacion.setter
    def fecha_publicacion(self, value):
        self.__fecha_publicacion = value

    @property
    def pagina_actual(self):
        return self.__pagina_actual

    @pagina_actual.setter
    def pagina_actual(self, value):
        self.__pagina_actual = value

    @property
    def cant_paginas(self):
        return self.__cant_paginas

    @cant_paginas.setter
    def cant_paginas(self, value):
        self.__cant_paginas = value
        
    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

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

    @property
    def wiki(self):
        return self.__wiki

    @wiki.setter
    def wiki(self, value):
        self.__wiki = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo= value
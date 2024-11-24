class Pelicula:

    def __init__(self, id, nombre, genero, fecha_estreno, duracion, pais, estado, director,
    distribuidor, estudio, plataforma, descripcion, comentario, puntuacion, calificacion, wiki):
        self.__id = id
        self.__nombre = nombre
        self.__genero = genero
        self.__fecha_estreno = fecha_estreno
        self.__duracion = duracion
        self.__pais = pais
        self.__estado = estado
        self.__director = director
        self.__distribuidor = distribuidor
        self.__estudio = estudio
        self.__plataforma = plataforma
        self.__descripcion = descripcion
        self.__comentario = comentario
        self.__puntuacion = puntuacion
        self.__calificacion = calificacion
        self.__wiki = wiki

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
        def fecha_estreno(self):
            return self.__fecha_estreno

        @fecha_estreno.setter
        def fecha_estreno(self, value):
            self.__fecha_estreno = value

        @property
        def duracion(self):
            return self.__duracion

        @duracion.setter
        def duracion(self, value):
            self.__duracion = value

        @property
        def pais(self):
            return self.__pais

        @pais.setter
        def pais(self, value):
            self.__pais = value

        @property
        def estado(self):
            return self.__estado

        @estado.setter
        def estado(self, value):
            self.__estado = value
        
        @property
        def director(self):
            return self.__director

        @director.setter
        def director(self, value):
            self.__director = value
        
        @property
        def distribuidor(self):
            return self.__distribuidor

        @distribuidor.setter
        def distribuidor(self, value):
            self.__distribuidor = value
        
        @property
        def estudio(self):
            return self.__estudio

        @estudio.setter
        def estudio(self, value):
            self.__estudio = value
        
        @property
        def plataforma(self):
            return self.__plataforma

        @plataforma.setter
        def plataforma(self, value):
            self.__plataforma = value

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
        def puntuacion(self):
            return self.__puntuacion

        @puntuacion.setter
        def puntuacion(self, value):
            self.__puntuacion = value

        @property
        def calificacion(self):
            return self.__calificacion

        @calificacion.setter
        def calificacion(self, value):
            self.__calificacion = value

        @property
        def wiki(self):
            return self.__wiki

        @wiki.setter
        def wiki(self, value):
            self.__wiki = value

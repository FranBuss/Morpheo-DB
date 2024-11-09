class Usuario:

    def __init__(self, usuario, contrasenia):
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        self.__usuario = value

    @property
    def contrasenia(self):
        return self.__contrasenia

    @contrasenia.setter
    def contrasenia(self, value):
        self.__contrasenia = value

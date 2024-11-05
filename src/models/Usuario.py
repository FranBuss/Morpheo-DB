class Usuario:

    def __init__(self, usuario, contrasenia):
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def get_usuario(self):
        return self.__usuario
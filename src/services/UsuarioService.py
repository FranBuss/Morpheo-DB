import pyodbc
from config import DRIVER, SERVER, DATABASE
from src.models.Usuario import  Usuario

class UsuarioService:

    def __init__(self):
        self.conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE}")

    def crear_usuario(self, nombre, contrasenia, contrasenia_rep):
        cursor = self.conexion.cursor()

        try:
            if nombre != self.buscar_usuario(nombre).get_usuario() and contrasenia == contrasenia_rep:
                query = '''INSERT INTO dbo.USUARIOS(NOMBRE, CONTRASENIA) VALUES ('{}','{}')'''.format(nombre, contrasenia)
                cursor.execute(query)
                self.conexion.commit()
                print("Usuario creado correctamente.")
                cursor.close()
            else:
                print("El usuario ya esta asociado a una cuenta")

        except pyodbc.Error as ex:
            print("ERROR: " + ex)

    def buscar_usuario(self, nombre_usuario):
        cursor = self.conexion.cursor()
        query = '''SELECT NOMBRE_USUARIO FROM USUARIOS WHERE NOMBRE = {}'''.format(nombre_usuario)
        cursor.execute(query)
        resultado = cursor.fetchone()

        if resultado:
            usuario = Usuario(resultado[0])
            return usuario
        else:
            return None
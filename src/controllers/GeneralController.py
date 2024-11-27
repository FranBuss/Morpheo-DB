from src.services.GeneralService import GeneralService

class GeneralController:

    def __init__(self):
        self.generalService = GeneralService()

    def listar_sin_filtro(self):
        return self.generalService.lista_sin_filtro()

    def buscar_por_nombre(self, nombre):
        return self.generalService.buscar_por_nombre(nombre)

    def buscar_por_puntuacion(self, puntuacion):
        return self.generalService.buscar_por_puntuacion(puntuacion)
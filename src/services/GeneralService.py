from src.repositories.GeneralRepository import GeneralRepository

class GeneralService:

    def __init__(self):
        self.generalRepository = GeneralRepository()

    def lista_sin_filtro(self):
        return self.generalRepository.lista_todo()

    def buscar_por_nombre(self, nombre):
        return self.generalRepository.buscar_por_nombre(nombre)
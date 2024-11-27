from src.services.GeneralService import GeneralService

class GeneralController:

    def __init__(self):
        self.generalService = GeneralService()

    def listar_sin_filtro(self):
        return self.generalService.lista_sin_filtro()



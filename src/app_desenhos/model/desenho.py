import pickle
from app_desenhos.model.figura import Figura

class Desenho:
    
    def __init__(self):
        self._figuras = []

    def adicionar_figura(self, figura: Figura):
        self._figuras.append(figura)

    def remover_figura(self, figura: Figura):
        if figura in self._figuras:
            self._figuras.remove(figura)

    def limpar(self):
        self._figuras.clear()

    def substituir_figuras(self, figuras):
        self._figuras = list(figuras)

    def obter_figuras(self):
        return tuple(self._figuras)

    def desenhar_todos(self, canvas):
        for figura in self._figuras:
            figura.desenhar(canvas)
    
    def salvar_em_arquivo(self, caminho_arquivo: str):

        with open(caminho_arquivo, 'wb') as arquivo:
            pickle.dump(self._figuras, arquivo)

    def carregar_de_arquivo(self, caminho_arquivo: str):

        with open(caminho_arquivo, 'rb') as arquivo:
            figuras = pickle.load(arquivo)

        if not isinstance(figuras, list) or not all(
            isinstance(figura, Figura) for figura in figuras
        ):
            raise ValueError("O arquivo não contém um desenho válido.")

        self.substituir_figuras(figuras)

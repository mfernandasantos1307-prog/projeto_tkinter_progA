from .figuras import Figura

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

    def obter_figuras(self):
        return tuple(self._figuras)

    def desenhar_todos(self, canvas):
        for figura in self._figuras:
            figura.desenhar(canvas)

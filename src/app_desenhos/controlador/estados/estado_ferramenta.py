from abc import ABC, abstractmethod

class EstadoFerramenta(ABC):

    @abstractmethod
    def ao_pressionar(self, controller, event):
        pass

    @abstractmethod
    def ao_arrastar(self, controller, event):
        pass

    @abstractmethod
    def ao_soltar(self, controller, event):
        pass

    @abstractmethod
    def ao_duplo_clique(self, controller, event):
        pass
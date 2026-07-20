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

    def ao_duplo_clique(self, controller, event):
        return None

    def ao_sair(self, controller):
        pass

    def cancelar(self, controller):
        self.ao_sair(controller)

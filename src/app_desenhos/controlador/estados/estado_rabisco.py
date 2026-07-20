from src.app_desenhos.controlador.estados.estado_ferramenta import EstadoFerramenta
from src.app_desenhos.model.rabisco import Rabisco

class EstadoRabisco(EstadoFerramenta):

    def __init__(self):
        self.pontos = []

    def ao_pressionar(self, controller, event):
        self.pontos = [(event.x, event.y)]

    def ao_arrastar(self, controller, event):
        self.pontos.append((event.x, event.y))

    def ao_soltar(self, controller, event):
        self.pontos.append((event.x, event.y))

        novo_rabisco = Rabisco(
            controller.cor_borda,
            controller.cor_preenchimento,
            self.pontos
        )

        controller.desenho.adicionar_figura(novo_rabisco)
        controller.atualizar_view()

    def ao_duplo_clique(self, controller, event):
        pass
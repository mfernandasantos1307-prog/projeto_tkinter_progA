import math
from src.app_desenhos.controlador.estados.estado_ferramenta import EstadoFerramenta
from src.app_desenhos.model.circulo import Circulo

class EstadoCirculo(EstadoFerramenta):

    def __init__(self):
        self.centro_x = 0
        self.centro_y = 0

    def ao_pressionar(self, controller, event):
        self.centro_x = event.x
        self.centro_y = event.y

    def ao_arrastar(self, controller, event):
        pass

    def ao_soltar(self, controller, event):
        fim_x = event.x
        fim_y = event.y

        raio = math.hypot(fim_x - self.centro_x, fim_y - self.centro_y)

        novo_circulo = Circulo(
            controller.cor_borda,
            controller.cor_preenchimento,
            self.centro_x,
            self.centro_y,
            raio
        )

        controller.desenho.adicionar_figura(novo_circulo)
        controller.atualizar_view()

    def ao_duplo_clique(self, controller, event):
        pass
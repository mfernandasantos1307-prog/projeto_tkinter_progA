import math
from app_desenhos.controlador.estados.estado_ferramenta import EstadoFerramenta
from app_desenhos.model.circulo import Circulo


class EstadoCirculo(EstadoFerramenta):

    def __init__(self):
        self.centro_x = None
        self.centro_y = None

    def ao_pressionar(self, controller, event):
        self.centro_x = event.x
        self.centro_y = event.y

    def ao_arrastar(self, controller, event):
        if self.centro_x is None:
            return

        circulo = self._criar_circulo(controller, event.x, event.y)
        controller.atualizar_view()
        controller.view.desenhar_previa(circulo)

    def ao_soltar(self, controller, event):
        if self.centro_x is None:
            return

        novo_circulo = self._criar_circulo(controller, event.x, event.y)
        if novo_circulo.raio > 0:
            controller.desenho.adicionar_figura(novo_circulo)

        self._limpar()
        controller.atualizar_view()

    def _criar_circulo(self, controller, fim_x, fim_y):
        raio = math.hypot(fim_x - self.centro_x, fim_y - self.centro_y)
        return Circulo(
            controller.cor_borda,
            controller.cor_preenchimento,
            self.centro_x,
            self.centro_y,
            raio
        )

    def ao_sair(self, controller):
        self._limpar()
        controller.atualizar_view()

    def _limpar(self):
        self.centro_x = None
        self.centro_y = None

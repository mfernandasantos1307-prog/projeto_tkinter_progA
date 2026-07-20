from app_desenhos.controlador.estados.estado_ferramenta import EstadoFerramenta
from app_desenhos.model.rabisco import Rabisco


class EstadoRabisco(EstadoFerramenta):

    def __init__(self):
        self.pontos = []

    def ao_pressionar(self, controller, event):
        self.pontos = [(event.x, event.y)]

    def ao_arrastar(self, controller, event):
        if not self.pontos:
            return

        self.pontos.append((event.x, event.y))
        controller.atualizar_view()
        controller.view.desenhar_previa(
            Rabisco(list(self.pontos), controller.cor_borda)
        )

    def ao_soltar(self, controller, event):
        if not self.pontos:
            return

        ponto_final = (event.x, event.y)
        if self.pontos[-1] != ponto_final:
            self.pontos.append(ponto_final)

        if len(self.pontos) > 1:
            controller.desenho.adicionar_figura(
                Rabisco(list(self.pontos), controller.cor_borda)
            )

        self.pontos = []
        controller.atualizar_view()

    def ao_sair(self, controller):
        self.pontos = []
        controller.atualizar_view()

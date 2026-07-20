from app_desenhos.controlador.estados.estado_ferramenta import EstadoFerramenta
from app_desenhos.model.poligono import Poligono


class EstadoPoligono(EstadoFerramenta):

    def __init__(self):
        self.pontos = []

    def ao_pressionar(self, controller, event):
        self.pontos.append((event.x, event.y))
        self._mostrar_previa(controller)

    def ao_arrastar(self, controller, event):
        pass

    def ao_soltar(self, controller, event):
        pass

    def ao_duplo_clique(self, controller, event):
        self._concluir(controller)
        return "break"

    def ao_sair(self, controller):
        self._concluir(controller)

    def cancelar(self, controller):
        self.pontos = []
        controller.atualizar_view()

    def _mostrar_previa(self, controller):
        controller.atualizar_view()
        if len(self.pontos) >= 2:
            controller.view.desenhar_previa(
                Poligono(list(self.pontos), controller.cor_borda, "")
            )

    def _concluir(self, controller):
        if len(self.pontos) >= 3:
            controller.desenho.adicionar_figura(
                Poligono(
                    list(self.pontos),
                    controller.cor_borda,
                    controller.cor_preenchimento,
                )
            )

        self.pontos = []
        controller.atualizar_view()

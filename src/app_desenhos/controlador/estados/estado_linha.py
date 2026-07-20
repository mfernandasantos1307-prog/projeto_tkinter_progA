from src.app_desenhos.controlador.estados.estado_ferramenta import EstadoFerramenta
from src.app_desenhos.model.linha import Linha

class EstadoLinha(EstadoFerramenta):

    def __init__(self):
        self.ini_x = 0
        self.ini_y = 0

    def ao_pressionar(self, controller, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def ao_arrastar(self, controller, event):
        pass

    def ao_soltar(self, controller, event):
        fim_y = event.y

        nova_linha = Linha(
            controller.cor_borda,
            controller.cor_preenchimento,
            self.ini_x,
            self.ini_y,
            fim_x,
            fim_y
        )

        controller.desenho.adicionar_figura(nova_linha)
        controller.atualizar_view()

    def ao_duplo_clique(self, controller, event):
        pass
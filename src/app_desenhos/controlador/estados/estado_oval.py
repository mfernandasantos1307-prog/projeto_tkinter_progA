from app_desenhos.controlador.estados.estado_ferramenta import EstadoFerramenta
from app_desenhos.model.oval import Oval


class EstadoOval(EstadoFerramenta):

    def __init__(self):
        self.ini_x = None
        self.ini_y = None

    def ao_pressionar(self, controller, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def ao_arrastar(self, controller, event):
        if self.ini_x is None:
            return

        oval = self._criar_oval(controller, event.x, event.y)
        controller.atualizar_view()
        controller.view.desenhar_previa(oval)

    def ao_soltar(self, controller, event):
        if self.ini_x is None:
            return

        if (self.ini_x, self.ini_y) != (event.x, event.y):
            controller.desenho.adicionar_figura(
                self._criar_oval(controller, event.x, event.y)
            )

        self._limpar()
        controller.atualizar_view()

    def _criar_oval(self, controller, fim_x, fim_y):
        return Oval(
            controller.cor_borda,
            controller.cor_preenchimento,
            self.ini_x,
            self.ini_y,
            fim_x,
            fim_y
        )

    def ao_sair(self, controller):
        self._limpar()
        controller.atualizar_view()

    def _limpar(self):
        self.ini_x = None
        self.ini_y = None

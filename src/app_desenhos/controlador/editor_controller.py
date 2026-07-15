from ..model.figuras import (
    Circulo,
    Linha,
    Oval,
    Poligono,
    Rabisco,
    Retangulo,
)


class EditorController:
    def __init__(self, desenho, view):
        self.desenho = desenho
        self.view = view

        self.ferramenta_atual = "circulo"
        self.figura_nova = None
        self.pontos_poligono = []

        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None

    def selecionar_ferramenta(self, ferramenta):
        self.ferramenta_atual = ferramenta
        self.view.destacar_ferramenta(ferramenta)

    def iniciar_figura(self, event):
        pass

    def atualizar_figura(self, event):
        pass

    def finalizar_figura(self, event):
        pass

    def finalizar_poligono(self, event):
        pass
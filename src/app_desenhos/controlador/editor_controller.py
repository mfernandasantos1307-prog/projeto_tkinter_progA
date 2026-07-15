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
        if self.ferramenta_atual == "circulo":
            self.iniciar_circulo(event)

    def atualizar_figura(self, event):
        if self.ferramenta_atual == "circulo":
            self.atualizar_circulo(event)

    def finalizar_figura(self, event):
        if self.ferramenta_atual == "circulo":
            self.finalizar_circulo(event)

    def finalizar_poligono(self, event):
        pass

    # ==========================================
    # CÍRCULO
    # ==========================================

    def iniciar_circulo(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def atualizar_circulo(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

        circulo = self.criar_circulo(self.fim_x, self.fim_y)
        self.view.redesenhar(self.desenho.obter_figuras())
        self.view.desenhar_previa(circulo)

    def finalizar_circulo(self, event):
        circulo = self.criar_circulo(event.x, event.y)
        self.desenho.adicionar_figura(circulo)
        self.view.redesenhar(self.desenho.obter_figuras())

    def criar_circulo(self, fim_x, fim_y):
        raio = self.calcular_raio(fim_x, fim_y)

        return Circulo(
            self.view.obter_cor_borda(),
            self.view.obter_cor_preenchimento(),
            self.ini_x,
            self.ini_y,
            raio
        )

    def calcular_raio(self, fim_x, fim_y):
        return (
            (self.ini_x - fim_x) ** 2
            + (self.ini_y - fim_y) ** 2
        ) ** 0.5

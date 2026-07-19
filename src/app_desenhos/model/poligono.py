from src.app_desenhos.model.figura import Figura

class Poligono(Figura):

    def __init__(self, pontos, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.pontos = pontos

    def desenhar(self, canvas):
        canvas.create_polygon(
            self.pontos,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )

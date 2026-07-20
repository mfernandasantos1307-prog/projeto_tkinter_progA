from app_desenhos.model.figura import Figura

class Rabisco(Figura):

    def __init__ (self, pontos, cor_borda):

        super().__init__(cor_borda, None)

        self.pontos = pontos
    
    def desenhar(self, canvas):
        canvas.create_line(
            self.pontos,
            fill=self.cor_borda,
        )

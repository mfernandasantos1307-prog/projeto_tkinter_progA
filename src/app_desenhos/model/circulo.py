from src.app_desenhos.model.figura import Figura

class Circulo(Figura):
    
    def __init__(self, cor_borda, cor_preenchimento, x, y, raio):

        super().__init__(cor_borda, cor_preenchimento)
        
        self.x = x
        self.y = y
        self.raio = raio
    
    def desenhar(self, canvas):
        
        canvas.create_oval(
            self.x - self.raio,
            self.y - self.raio,
            self.x + self.raio,
            self.y + self.raio,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )
from app_desenhos.model.figura import Figura

class Linha(Figura):

    def __init__ (self, cor_borda, cor_preenchimento, ini_x, ini_y, fim_x, fim_y):

        super().__init__(cor_borda, None)

        self.ini_x = ini_x
        self.ini_y = ini_y
        self.fim_x = fim_x
        self.fim_y = fim_y
    
    def desenhar(self, canvas):
        canvas.create_line(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            fill=self.cor_borda,
        )

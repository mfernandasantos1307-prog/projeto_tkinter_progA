class Figura:
    
    def __init__(self, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
    
    def desenhar(self, canvas):
        pass

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

class Retangulo(Figura):
    
    def __init__(self, cor_borda, cor_preenchimento, ini_x, ini_y, fim_x, fim_y):

        super().__init__(cor_borda, cor_preenchimento)
        
        self.ini_x = ini_x
        self.ini_y = ini_y
        self.fim_x = fim_x
        self.fim_y = fim_y

    def desenhar(self, canvas):
        canvas.create_rectangle(
            self.ini_x, self.ini_y,
            self.fim_x, self.fim_y,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )


class Oval(Figura):
    
    def __init__(self, cor_borda, cor_preenchimento, ini_x, ini_y, fim_x, fim_y):

        super().__init__(cor_borda, cor_preenchimento)
        
        self.ini_x = ini_x
        self.ini_y = ini_y
        self.fim_x = fim_x
        self.fim_y = fim_y

    def desenhar(self, canvas):
        canvas.create_oval(
            self.ini_x, self.ini_y,
            self.fim_x, self.fim_y,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )

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

class Rabisco(Figura):

    def __init__ (self, pontos, cor_borda):

        super().__init__(cor_borda, None)

        self.pontos = pontos
    
    def desenhar(self, canvas):
        canvas.create_line(
            self.pontos,
            fill=self.cor_borda,
        )


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

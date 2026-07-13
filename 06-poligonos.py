from tkinter import * 
from tkinter import colorchooser

import cores

# Criei a classe figura de forma provisória
# Assim que a classe figura de verdade for criada essa aqui precisa ser apagada 

class Figura:
    def __init__(self, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

# ***** CLASSE POLIGONO ***** 

class Poligono(Figura):
    def __init__(self, lista_de_pontos, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.pontos = lista_de_pontos

    def desenhar(self, canvas):
        canvas.create_polygon(
            self.pontos,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )

#lista que vai acumular os cliques no mouse 
pontos_atual = []
figuras = []

def adicionar_ponto(event):
    global pontos_atual
    pontos_atual.append(event.x)
    pontos_atual.append(event.y)
    desenhar_tudo()

def finalizar_poligono(event):
    global pontos_atual, figuras

    if len(pontos_atual) >= 2:
        pontos_atual = pontos_atual[:-2]

    if len(pontos_atual) >= 6:

        novo_poligono = Poligono(list(pontos_atual), cores.cor_borda_atual, cores.cor_preenchimento_atual)
        figuras.append(novo_poligono)

    pontos_atual = []

    desenhar_tudo()

def desenhar_tudo():
    canvas.delete('all')
    
    for fig in figuras:
        fig.desenhar(canvas)

    if len(pontos_atual) >= 4:
        canvas.create_polygon(pontos_atual, outline=cores.cor_borda_atual, fill='')

    # vai marcar cada ponto já clicado pelo usuário, para ele entender onde colocou cada vertice 
    for i in range(0, len(pontos_atual), 2):
        x = pontos_atual[i]
        y = pontos_atual[i + 1]
        canvas.create_oval(x - 3, y - 3, x + 3, y +3, fill='red', outline='red')


# criar janela de teste 
janela = Tk()
janela.title('polígono')
janela.geometry('600x600')

# barra de ferramentas com as cores 
frame_ferramentas = Frame(janela)
frame_ferramentas.pack(side='top', fill='x')
cores.criar_paleta(frame_ferramentas)

canvas = Canvas(janela, bg='white')
canvas.pack(fill=BOTH, expand=True)

canvas.bind('<Button-1>', adicionar_ponto)
canvas.bind('<Double-Button-1>', finalizar_poligono)

janela.mainloop()

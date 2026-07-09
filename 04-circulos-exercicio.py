# Exercício: desenhar círculos.
#  O centro é a posição onde o mouse foi clicado
#  O raio é definido pela distância entre o centro e a posição atual do mouse

from tkinter import *

# Quando o mouse é pressionado
def inicia_linha(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

# Quando o mouse é movido com o botão pressionado
def atualiza_linha(event):
    global fim_x, fim_y, raio
    global cor_borda_atual, cor_preenchimento_atual
    
    fim_x = event.x
    fim_y = event.y
    desenhar()
    raio = ( (ini_x - fim_x)**2 + (ini_y - fim_y)**2 ) ** 0.5
    canvas.create_oval(ini_x-raio, ini_y-raio, ini_x+raio, ini_y+raio, outline=cor_borda_atual, fill=cor_preenchimento_atual))

# Quando o mouse é solto
def incluir_linha(event):
    global cor_borda_atual, cor_preenchimento_atual # adicionei essa linha para a implementação das cores, essas variaveis ainda não estão nesse codigo
    circulos.append((ini_x, ini_y, raio, cor_borda_atual, cor_prenchimento_atual))

def desenhar():
    canvas.delete("all")
    for circulo in circulos:
        x, y, r, cor_b, cor_p = circulo
        canvas.create_oval(x-r, y-r, x+r, y+r, outline=cor_b, fill=cor_p)



#******* MAIN *******#

# Todas os círuculos desenhados são armazenados aqui
circulos = []
raio = None

root = Tk()

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()

ini_x = None
ini_y = None
fim_x = None
fim_y = None
canvas.bind('<ButtonPress-1>', inicia_linha)
canvas.bind('<B1-Motion>', atualiza_linha)
canvas.bind('<ButtonRelease-1>', incluir_linha)

root.mainloop()

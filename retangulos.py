from tkinter import *

#definir a posição inicial 
def inicia_retangulo(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

# acompanha o movimento do mouse
def atualiza_retangulo(event):
    global fim_x, fim_y
    fim_x = event.x
    fim_y = event.y
    desenhar()
    canvas.create_rectangle(ini_x, ini_y, fim_x, fim_y)

# Quando o usuário soltar o botão
def incluir_retangulo(event):
    global ini_x, ini_y, fim_x, fim_y
    retangulos.append((ini_x, ini_y, fim_x, fim_y))

def desenhar():
    canvas.delete("all")
    for retangulo in retangulos:
        x_ini, y_ini, x_fim, y_fim = retangulo
        canvas.create_rectangle(x_ini, y_ini, x_fim, y_fim)

# ******* MAIN *******#

# onde armazeno os retângulos desenhados
retangulos = []
#criando a janela
root = Tk()
canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()

#guardam a posição do mouse
ini_x = None
ini_y = None 
fim_x = None 
fim_y = None 
canvas.bind('<ButtonPress-1>', inicia_retangulo)
canvas.bind('<B1-Motion>', atualiza_retangulo)
canvas.bind('<ButtonRelease-1>', incluir_retangulo)

root.mainloop()

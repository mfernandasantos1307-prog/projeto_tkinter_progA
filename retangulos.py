from tkinter import *
from tkinter import colorchooser

#******* variaveis de cor *******#

cor_borda_atual = 'black'
cor_preenchimento_atual = ''
modo_cor = 'preenchimento'

def selecionar_cor(cor_escolhida):
    global cor_preenchimento_atual, cor_borda_atual, modo_cor
    if modo_cor == 'preenchimento':
        cor_preenchimento_atual = cor_escolhida
    elif modo_cor == 'borda':
        cor_borda_atual = cor_escolhida

def ativar_modo_borda():
    global modo_cor
    modo_cor = 'borda'

def ativar_modo_preenchimento():
    global modo_cor
    modo_cor = 'preenchimento'

def escolher_cor_extra():
    global cor_preenchimento_atual
    global cor_borda_atual
    global modo_cor

    cor = colorchooser.askcolor(title='Outras cores')
    if modo_cor == 'preenchimento':
        if cor[1]:
            cor_preenchimento_atual = cor[1]
            return cor_preenchimento_atual
        
    elif modo_cor == 'borda':
        if cor[1]:
            cor_borda_atual = cor[1]
            return cor_borda_atual
            
# ******* funções do desenho *******#

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
    canvas.create_rectangle(ini_x, ini_y, fim_x, fim_y,
                            outline = cor_borda_atual, fill = cor_preenchimento_atual)

# Quando o usuário soltar o botão
def incluir_retangulo(event):
    global ini_x, ini_y, fim_x, fim_y
    retangulos.append((ini_x, ini_y, fim_x, fim_y,
                       cor_borda_atual, cor_preenchimento_atual))

def desenhar():
    canvas.delete("all")
    for retangulo in retangulos:
        x_ini, y_ini, x_fim, y_fim, borda, preench = retangulo
        canvas.create_rectangle(x_ini, y_ini, x_fim, y_fim,
                                outline=borda, fill=preench)

# ******* MAIN *******#

# onde armazeno os retângulos desenhados
retangulos = []
#criando a janela
root = Tk()

frame = Frame(root)
frame.pack()

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

#******* botões de cor *******#
selecionar_borda = Button(frame, text='Borda', command=ativar_modo_borda)
selecionar_preenchimento = Button(frame, text='Preenchimento', command=ativar_modo_preenchimento)
selecionar_mais_cores = Button(frame, text='Mais cores', command=escolher_cor_extra)

#Quadrinhos das cores 
botao_preto = Button(frame, bg='black', width=2, command=lambda: selecionar_cor('black'))
botao_branco = Button(frame, bg='white', width=2, command=lambda: selecionar_cor('white'))
botao_vermelho = Button(frame, bg='red', width=2, command=lambda:selecionar_cor('red'))
botao_verde = Button(frame, bg='green', width=2, command=lambda: selecionar_cor('green'))
botao_azul = Button(frame, bg='blue', width=2, command=lambda: selecionar_cor('blue'))
botao_amarelo = Button(frame, bg='yellow', width=2, command=lambda:selecionar_cor('yellow'))
botao_rosa = Button(frame, bg='pink', width=2, command=lambda: selecionar_cor('pink'))
botao_roxo = Button(frame, bg='purple', width=2, command=lambda: selecionar_cor('purple'))
botao_marrom = Button(frame, bg='brown', width=2, command=lambda: selecionar_cor('brown'))
botao_cinza = Button(frame, bg='gray', width=2, command=lambda: selecionar_cor('gray'))
botao_transparente = Button(frame, text='X', bg='lightgray', width=2, command=lambda: selecionar_cor(''))
botao_laranja = Button(frame, bg='orange', width=2, command=lambda: selecionar_cor('orange'))

#organizar a grade de cores dentro do frame
selecionar_borda.grid(row=0, column=0, padx=5, pady=2, sticky=W)
selecionar_preenchimento.grid(row=1, column=0, padx=5, pady=2, sticky=W)

# cores - Fileira de cima (Linha 2)
botao_preto.grid(row=2, column=1, padx=2, pady=2)
botao_vermelho.grid(row=2, column=2, padx=2, pady=2)
botao_azul.grid(row=2, column=3, padx=2, pady=2)
botao_rosa.grid(row=2, column=4, padx=2, pady=2)
botao_marrom.grid(row=2, column=5, padx=2, pady=2)
botao_laranja.grid(row=2, column=6, padx=2, pady=2)

# cores - Fileira de baixo (Linha 3)
botao_transparente.grid(row=3, column=1, padx=2, pady=2)
botao_branco.grid(row=3, column=2, padx=2, pady=2)
botao_verde.grid(row=3, column=3, padx=2, pady=2)
botao_amarelo.grid(row=3, column=4, padx=2, pady=2)
botao_roxo.grid(row=3, column=5, padx=2, pady=2)
botao_cinza.grid(row=3, column=6, padx=2, pady=2)

selecionar_mais_cores.grid(row=2, column=7, rowspan=2, padx=5, pady=2)

root.mainloop()
from tkinter import *
from tkinter import colorchooser

# ==========================================
# PARTE 1: LOGICA DE CORES
# ==========================================

# Variáveis globais para armazenar o estado atual das cores
cor_borda_atual = 'black'
cor_preenchimento_atual = ''
modo_cor = 'preenchimento'  # Começa definindo o preenchimento por padrão

# Função que os quadradinhos da tabela vão chamar
def selecionar_cor(cor_escolhida):
    global cor_preenchimento_atual
    global cor_borda_atual
    global modo_cor
    
    if modo_cor == 'preenchimento':
        cor_preenchimento_atual = cor_escolhida
        return cor_preenchimento_atual
    elif modo_cor == 'borda':
        cor_borda_atual = cor_escolhida
        return cor_borda_atual 

# Funções para alternar o modo
def ativar_modo_borda():
    global modo_cor
    modo_cor = 'borda'
    return modo_cor

def ativar_modo_preenchimento():
    global modo_cor
    modo_cor = 'preenchimento'
    return modo_cor

# Função para selecionar cores personalizadas (Mais cores)
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

# ==========================================
# PARTE 2: LÓGICA DE DESENHO           
# ==========================================

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
    canvas.create_oval(ini_x-raio, ini_y-raio, ini_x+raio, ini_y+raio, 
                       outline=cor_borda_atual, fill=cor_preenchimento_atual)

# Quando o mouse é solto
def incluir_linha(event):
    global cor_borda_atual, cor_preenchimento_atual
    circulos.append((ini_x, ini_y, raio, cor_borda_atual, cor_preenchimento_atual))

def desenhar():
    canvas.delete("all")
    for circulo in circulos:
        x, y, r, cor_b, cor_p = circulo
        canvas.create_oval(x-r, y-r, x+r, y+r, outline=cor_b, fill=cor_p)


#******* MAIN *******#

# Todos os círculos desenhados são armazenados aqui
circulos = []
raio = None
ini_x = None
ini_y = None
fim_x = None
fim_y = None

root = Tk()
root.title("Paint de Círculos")

# Cria uma área (Frame) dedicada para a barra de ferramentas
frame_ferramentas = Frame(root)
frame_ferramentas.pack(side="top", fill="x", padx=5, pady=5)

# Área de desenho (Canvas) posicionada logo abaixo da barra de ferramentas
canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack(side="bottom")

# ==========================================
# PARTE 3: CRIAÇÃO E POSICIONAMENTO DA PALETA
# ==========================================

# Botões seletores de modo e mais cores inseridos no frame_ferramentas
selecionar_borda = Button(frame_ferramentas, text="Borda", command=ativar_modo_borda)
selecionar_preenchimento = Button(frame_ferramentas, text='Preenchimento', command=ativar_modo_preenchimento)
selecionar_mais_cores = Button(frame_ferramentas, text="Mais cores", command=escolher_cor_extra)

# Quadradinhos da Paleta de Cores inseridos no frame_ferramentas
botao_preto = Button(frame_ferramentas, bg="black", width=2, command=lambda: selecionar_cor("black"))
botao_branco = Button(frame_ferramentas, bg="white", width=2, command=lambda: selecionar_cor("white"))
botao_vermelho = Button(frame_ferramentas, bg="red", width=2, command=lambda: selecionar_cor("red"))
botao_verde = Button(frame_ferramentas, bg="green", width=2, command=lambda: selecionar_cor("green"))
botao_azul = Button(frame_ferramentas, bg="blue", width=2, command=lambda: selecionar_cor("blue"))
botao_amarelo = Button(frame_ferramentas, bg="yellow", width=2, command=lambda: selecionar_cor("yellow"))
botao_rosa = Button(frame_ferramentas, bg="pink", width=2, command=lambda: selecionar_cor("pink"))
botao_roxo = Button(frame_ferramentas, bg="purple", width=2, command=lambda: selecionar_cor("purple"))
botao_marrom = Button(frame_ferramentas, bg="brown", width=2, command=lambda: selecionar_cor("brown"))
botao_cinza = Button(frame_ferramentas, bg="gray", width=2, command=lambda: selecionar_cor("gray"))
botao_transparente = Button(frame_ferramentas, text="X", bg="lightgray", width=2, command=lambda: selecionar_cor(""))
botao_laranja = Button(frame_ferramentas, bg="orange", width=2, command=lambda: selecionar_cor("orange"))

# Organização usando Grid dentro do frame_ferramentas
selecionar_borda.grid(row=0, column=0, padx=5, pady=2, sticky=W)
selecionar_preenchimento.grid(row=1, column=0, padx=5, pady=2, sticky=W)

# Linha de cima de cores
botao_preto.grid(row=2, column=1, padx=2, pady=2)
botao_vermelho.grid(row=2, column=2, padx=2, pady=2)
botao_azul.grid(row=2, column=3, padx=2, pady=2)
botao_rosa.grid(row=2, column=4, padx=2, pady=2)
botao_marrom.grid(row=2, column=5, padx=2, pady=2)
botao_laranja.grid(row=2, column=6, padx=2, pady=2)

# Debaixo das cores
botao_transparente.grid(row=3, column=1, padx=2, pady=2)
botao_branco.grid(row=3, column=2, padx=2, pady=2)
botao_verde.grid(row=3, column=3, padx=2, pady=2)
botao_amarelo.grid(row=3, column=4, padx=2, pady=2)
botao_roxo.grid(row=3, column=5, padx=2, pady=2)
botao_cinza.grid(row=3, column=6, padx=2, pady=2)

selecionar_mais_cores.grid(row=2, column=7, rowspan=2, padx=5, pady=2)

# Vinculando os eventos do mouse ao canvas
canvas.bind('<ButtonPress-1>', inicia_linha)
canvas.bind('<B1-Motion>', atualiza_linha)
canvas.bind('<ButtonRelease-1>', incluir_linha)

root.mainloop()

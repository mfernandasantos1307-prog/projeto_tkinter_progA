from tkinter import *

import cores

# ==========================================
#SELETOR DE FERRAMENTAS
# ==========================================

ferramenta_atual = "circulo"

def selecionar_circulo():
    global ferramenta_atual
    ferramenta_atual = "circulo"

    botao_circulo.config(relief=SUNKEN)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)


def selecionar_retangulo():
    global ferramenta_atual
    ferramenta_atual = "retangulo"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=SUNKEN)
    botao_oval.config(relief=RAISED)


def selecionar_oval():
    global ferramenta_atual
    ferramenta_atual = "oval"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=SUNKEN)


# ==========================================
# LÓGICA DO CÍRCULO
# ==========================================

# Quando o mouse é pressionado para iniciar um círculo
def iniciar_circulo(event):
    global ini_x, ini_y

    ini_x = event.x
    ini_y = event.y


# Quando o mouse é movido com o botão pressionado
def atualizar_circulo(event):
    global fim_x, fim_y, raio

    fim_x = event.x
    fim_y = event.y

    # Redesenha todas as figuras já finalizadas
    desenhar_figuras()

    # Calcula a distância entre o centro e o mouse
    raio = (
        (ini_x - fim_x) ** 2
        + (ini_y - fim_y) ** 2
    ) ** 0.5

    # Mostra o círculo atual enquanto o mouse é arrastado
    canvas.create_oval(
        ini_x - raio,
        ini_y - raio,
        ini_x + raio,
        ini_y + raio,
        outline=cores.cor_borda_atual,
        fill=cores.cor_preenchimento_atual
    )


# Quando o mouse é solto, salva o círculo
def finalizar_circulo(event):
    fim_x = event.x
    fim_y = event.y

    raio_final = (
        (ini_x - fim_x) ** 2
        + (ini_y - fim_y) ** 2
    ) ** 0.5

    figuras.append(
        (
            'circulo',
            ini_x,
            ini_y,
            raio_final,
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual
        )
    )


# ==========================================
#LÓGICA DO RETÂNGULO
# ==========================================

def iniciar_retangulo(event):
    global ini_x, ini_y

    ini_x = event.x
    ini_y = event.y


def atualizar_retangulo(event):
    global fim_x, fim_y

    fim_x = event.x
    fim_y = event.y

    desenhar_figuras()

    canvas.create_rectangle(
        ini_x,
        ini_y,
        fim_x,
        fim_y,
        outline=cores.cor_borda_atual,
        fill=cores.cor_preenchimento_atual
    )


def finalizar_retangulo(event):
    fim_x = event.x
    fim_y = event.y

    figuras.append(
        (
            'retangulo',
            ini_x,
            ini_y,
            fim_x,
            fim_y,
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual
        )
    )


# ==========================================
#LÓGICA DO OVAL
# ==========================================

def iniciar_oval(event):
    global ini_x, ini_y

    ini_x = event.x
    ini_y = event.y


def atualizar_oval(event):
    global fim_x, fim_y

    fim_x = event.x
    fim_y = event.y

    # Redesenha as figuras já finalizadas
    desenhar_figuras()

    # Mostra o oval enquanto o mouse é arrastado
    canvas.create_oval(
        ini_x,
        ini_y,
        fim_x,
        fim_y,
        outline=cores.cor_borda_atual,
        fill=cores.cor_preenchimento_atual
    )


def finalizar_oval(event):
    fim_x = event.x
    fim_y = event.y

    figuras.append(
        (
            'oval',
            ini_x,
            ini_y,
            fim_x,
            fim_y,
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual
        )
    )


# ==========================================
#CONTROLE DOS EVENTOS
# ==========================================
def iniciar_figura(event):
    if ferramenta_atual == "circulo":
        iniciar_circulo(event)

    elif ferramenta_atual == "retangulo":
        iniciar_retangulo(event)

    elif ferramenta_atual == "oval":
        iniciar_oval(event)


def atualizar_figura(event):
    if ferramenta_atual == "circulo":
        atualizar_circulo(event)

    elif ferramenta_atual == "retangulo":
        atualizar_retangulo(event)

    elif ferramenta_atual == "oval":
        atualizar_oval(event)


def finalizar_figura(event):
    if ferramenta_atual == "circulo":
        finalizar_circulo(event)

    elif ferramenta_atual == "retangulo":
        finalizar_retangulo(event)

    elif ferramenta_atual == "oval":
        finalizar_oval(event)
# ==========================================
#REDESENHO GERAL DAS FIGURAS
# ==========================================

def desenhar_figuras():
    canvas.delete("all")

    for figura in figuras:
        tipo = figura[0]

        if tipo == 'circulo':
            _, x, y, raio_figura, cor_borda, cor_preenchimento = figura
            canvas.create_oval(
                x - raio_figura,
                y - raio_figura, 
                x + raio_figura,
                y + raio_figura,
                outline=cor_borda,
                fill=cor_preenchimento
            )
        
        elif tipo == 'retangulo':
            _, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento = figura
            canvas.create_rectangle(
                x_inicial,
                y_inicial,
                x_final,
                y_final,
                outline=cor_borda,
                fill=cor_preenchimento
            )
        
        elif tipo == 'oval':
            _, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento = figura
            canvas.create_oval(
                x_inicial, 
                y_inicial,
                x_final,
                y_final,
                outline=cor_borda,
                fill=cor_preenchimento
            )

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

figuras = []

raio = None
ini_x = None
ini_y = None
fim_x = None
fim_y = None

root = Tk()
root.title("Editor de figuras")

# Barra de ferramentas
frame_ferramentas = Frame(root)
frame_ferramentas.pack(
    side="top",
    fill="x",
    padx=5,
    pady=5
)

# Cria a paleta usando o módulo de cores
cores.criar_paleta(frame_ferramentas)

#Botões para selecionar a figura
botao_circulo = Button(
    frame_ferramentas,
    text="◯ Cículo",
    width=10,
    command=selecionar_circulo
)

botao_retangulo = Button(
    frame_ferramentas,
    text="▭ Retângulo",
    width=10,
    command=selecionar_retangulo
)

botao_oval = Button(
    frame_ferramentas,
    text="⬭ Oval",
    width=10,
    command=selecionar_oval
)

botao_circulo.config(relief=SUNKEN)

# Posicionamento dos botões
botao_circulo.grid(row=0, column=8, padx=5, pady=2)
botao_retangulo.grid(row=1, column=8, padx=5, pady=2)
botao_oval.grid(row=2, column=8, padx=5, pady=2)

# Área de desenho
canvas = Canvas(
    root,
    bg="white",
    width=600,
    height=600
)
canvas.pack()

canvas.bind("<ButtonPress-1>", iniciar_figura)
canvas.bind("<B1-Motion>", atualizar_figura)
canvas.bind("<ButtonRelease-1>", finalizar_figura)

root.mainloop()
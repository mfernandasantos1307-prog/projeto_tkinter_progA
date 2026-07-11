from tkinter import *

import cores

# ==========================================
#SELEÇÃO DE FERRAMENTAS
# ==========================================

ferramenta_atual = "circulo"

def selecionar_circulo():
    global ferramenta_atual
    ferramenta_atual = "circulo"


def selecionar_retangulo():
    global ferramenta_atual
    ferramenta_atual = "retangulo"


def selecionar_oval():
    global ferramenta_atual
    ferramenta_atual = "oval"


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
    circulos.append(
        (
            ini_x,
            ini_y,
            raio,
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual
        )
    )


# Redesenha todos os círculos já finalizados
def desenhar_circulos():
    for circulo in circulos:
        x, y, raio_circulo, cor_borda, cor_preenchimento = circulo

        canvas.create_oval(
            x - raio_circulo,
            y - raio_circulo,
            x + raio_circulo,
            y + raio_circulo,
            outline=cor_borda,
            fill=cor_preenchimento
        )


# ==========================================
#LÓGICA DO RETÂNGULO
# ==========================================
retangulos = []


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

    retangulos.append(
        (
            ini_x,
            ini_y,
            fim_x,
            fim_y,
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual
        )
    )


def desenhar_retangulos():
    for retangulo in retangulos:
        (
            x_inicial,
            y_inicial,
            x_final,
            y_final,
            cor_borda,
            cor_preenchimento
        ) = retangulo

        canvas.create_rectangle(
            x_inicial,
            y_inicial,
            x_final,
            y_final,
            outline=cor_borda,
            fill=cor_preenchimento
        )
# ==========================================
#LÓGICA DO OVAL
# ==========================================

ovais = []


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

    ovais.append(
        (
            ini_x,
            ini_y,
            fim_x,
            fim_y,
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual
        )
    )


def desenhar_ovais():
    for oval in ovais:
        (
            x_inicial,
            y_inicial,
            x_final,
            y_final,
            cor_borda,
            cor_preenchimento
        ) = oval

        canvas.create_oval(
            x_inicial,
            y_inicial,
            x_final,
            y_final,
            outline=cor_borda,
            fill=cor_preenchimento
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

    desenhar_circulos()
    desenhar_retangulos()
    desenhar_ovais()

    # ADICIONAR desenhar_retangulos()
    # ACIDICIONAR desenhar_ovais()


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

circulos = []

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
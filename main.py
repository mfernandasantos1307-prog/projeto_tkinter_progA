from tkinter import *

import cores
from figuras_POO import Circulo, Linha, Oval, Poligono, Rabisco, Retangulo

# ==========================================
# SELETOR DE FERRAMENTAS
# ==========================================

ferramenta_atual = "circulo"

def selecionar_circulo():
    global ferramenta_atual
    cancelar_poligono_em_andamento()
    ferramenta_atual = "circulo"

    botao_circulo.config(relief=SUNKEN)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=RAISED)
    botao_poligono.config(relief=RAISED)


def selecionar_retangulo():
    global ferramenta_atual
    cancelar_poligono_em_andamento()
    ferramenta_atual = "retangulo"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=SUNKEN)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=RAISED)
    botao_poligono.config(relief=RAISED)


def selecionar_oval():
    global ferramenta_atual
    cancelar_poligono_em_andamento()
    ferramenta_atual = "oval"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=SUNKEN)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=RAISED)
    botao_poligono.config(relief=RAISED)


def selecionar_linha():
    global ferramenta_atual
    cancelar_poligono_em_andamento()
    ferramenta_atual = "linha"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=SUNKEN)
    botao_rabisco.config(relief=RAISED)
    botao_poligono.config(relief=RAISED)


def selecionar_rabisco():
    global ferramenta_atual
    cancelar_poligono_em_andamento()
    ferramenta_atual = "rabisco"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=SUNKEN)
    botao_poligono.config(relief=RAISED)


def selecionar_poligono():
    global ferramenta_atual
    ferramenta_atual = "poligono"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=RAISED)
    botao_poligono.config(relief=SUNKEN)


# ==========================================
# LÓGICA DO CÍRCULO
# ==========================================

def iniciar_circulo(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y


def atualizar_circulo(event):
    global fim_x, fim_y, raio

    fim_x = event.x
    fim_y = event.y

    desenhar_figuras()

    raio = (
        (ini_x - fim_x) ** 2
        + (ini_y - fim_y) ** 2
    ) ** 0.5

    canvas.create_oval(
        ini_x - raio,
        ini_y - raio,
        ini_x + raio,
        ini_y + raio,
        outline=cores.cor_borda_atual,
        fill=cores.cor_preenchimento_atual
    )


def finalizar_circulo(event):
    fim_x = event.x
    fim_y = event.y

    raio_final = (
        (ini_x - fim_x) ** 2
        + (ini_y - fim_y) ** 2
    ) ** 0.5

    figuras.append(
        Circulo(
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual,
            ini_x,
            ini_y,
            raio_final
        )
    )


# ==========================================
# LÓGICA DO RETÂNGULO
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
        Retangulo(
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual,
            ini_x,
            ini_y,
            fim_x,
            fim_y
        )
    )


# ==========================================
# LÓGICA DO OVAL
# ==========================================

def iniciar_oval(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y


def atualizar_oval(event):
    global fim_x, fim_y

    fim_x = event.x
    fim_y = event.y

    desenhar_figuras()

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
        Oval(
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual,
            ini_x,
            ini_y,
            fim_x,
            fim_y
        )
    )


# ==========================================
# LÓGICA DA LINHA E RABISCO (NOVO)
# ==========================================

def iniciar_linha_rabisco(event):
    global figura_nova
    if ferramenta_atual == "linha":
        figura_nova = Linha(
            cores.cor_borda_atual,
            None,
            event.x,
            event.y,
            event.x,
            event.y
        )
    elif ferramenta_atual == "rabisco":
        figura_nova = Rabisco(
            [(event.x, event.y)],
            cores.cor_borda_atual
        )


def atualizar_linha_rabisco(event):
    global figura_nova
    if isinstance(figura_nova, Rabisco):
        figura_nova.pontos.append((event.x, event.y))
    elif isinstance(figura_nova, Linha):
        figura_nova.fim_x = event.x
        figura_nova.fim_y = event.y

    desenhar_figuras()
    desenhar_figura_nova()


def finalizar_linha_rabisco(event):
    global figura_nova
    if not incompleta(figura_nova):
        figuras.append(figura_nova)
    desenhar_figuras()
    figura_nova = None


def desenhar_figura_nova():
    figura_nova.desenhar(canvas)


def incompleta(figura):
    if isinstance(figura, Linha):
        return (figura.ini_x, figura.ini_y) == (figura.fim_x, figura.fim_y)
    elif isinstance(figura, Rabisco):
        return len(figura.pontos) <= 1

    return True


# ==========================================
# LÓGICA DO POLÍGONO
# ==========================================

def adicionar_ponto_poligono(event):
    pontos_poligono.append((event.x, event.y))
    desenhar_figuras()
    desenhar_poligono_em_andamento()


def desenhar_poligono_em_andamento():
    if len(pontos_poligono) >= 2:
        canvas.create_polygon(
            pontos_poligono,
            outline=cores.cor_borda_atual,
            fill=""
        )

    for x, y in pontos_poligono:
        canvas.create_oval(
            x - 3,
            y - 3,
            x + 3,
            y + 3,
            fill="red",
            outline="red"
        )


def finalizar_poligono(event):
    global pontos_poligono

    if ferramenta_atual != "poligono":
        return

    if len(pontos_poligono) >= 3:
        figuras.append(
            Poligono(
                list(pontos_poligono),
                cores.cor_borda_atual,
                cores.cor_preenchimento_atual
            )
        )

    pontos_poligono = []
    desenhar_figuras()
    return "break"


def cancelar_poligono_em_andamento():
    global pontos_poligono

    if pontos_poligono:
        pontos_poligono = []
        desenhar_figuras()


# ==========================================
# CONTROLE DOS EVENTOS
# ==========================================

def iniciar_figura(event):
    if ferramenta_atual == "circulo":
        iniciar_circulo(event)
    elif ferramenta_atual == "retangulo":
        iniciar_retangulo(event)
    elif ferramenta_atual == "oval":
        iniciar_oval(event)
    elif ferramenta_atual in ["linha", "rabisco"]:
        iniciar_linha_rabisco(event)
    elif ferramenta_atual == "poligono":
        adicionar_ponto_poligono(event)


def atualizar_figura(event):
    if ferramenta_atual == "circulo":
        atualizar_circulo(event)
    elif ferramenta_atual == "retangulo":
        atualizar_retangulo(event)
    elif ferramenta_atual == "oval":
        atualizar_oval(event)
    elif ferramenta_atual in ["linha", "rabisco"]:
        atualizar_linha_rabisco(event)


def finalizar_figura(event):
    if ferramenta_atual == "circulo":
        finalizar_circulo(event)
    elif ferramenta_atual == "retangulo":
        finalizar_retangulo(event)
    elif ferramenta_atual == "oval":
        finalizar_oval(event)
    elif ferramenta_atual in ["linha", "rabisco"]:
        finalizar_linha_rabisco(event)


# ==========================================
# REDESENHO GERAL DAS FIGURAS
# ==========================================

def desenhar_figuras():
    canvas.delete("all")

    for figura in figuras:
        figura.desenhar(canvas)


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

figuras = []
figura_nova = None
pontos_poligono = []

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

# Botões para selecionar a figura
botao_circulo = Button(
    frame_ferramentas,
    text="◯ Círculo",
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

botao_linha = Button(
    frame_ferramentas,
    text="╱ Linha",
    width=10,
    command=selecionar_linha
)

botao_rabisco = Button(
    frame_ferramentas,
    text="✎ Rabisco",
    width=10,
    command=selecionar_rabisco
)

botao_poligono = Button(
    frame_ferramentas,
    text="⬠ Polígono",
    width=10,
    command=selecionar_poligono
)

botao_circulo.config(relief=SUNKEN)

# Posicionamento dos botões (seguindo o layout grid do seu projeto)
botao_circulo.grid(row=0, column=8, padx=5, pady=2)
botao_retangulo.grid(row=1, column=8, padx=5, pady=2)
botao_oval.grid(row=2, column=8, padx=5, pady=2)
botao_linha.grid(row=3, column=8, padx=5, pady=2)
botao_rabisco.grid(row=4, column=8, padx=5, pady=2)
botao_poligono.grid(row=5, column=8, padx=5, pady=2)

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
canvas.bind("<Double-Button-1>", finalizar_poligono)

root.mainloop()

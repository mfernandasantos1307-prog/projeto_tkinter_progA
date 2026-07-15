from tkinter import *

import cores

# ==========================================
# SELETOR DE FERRAMENTAS
# ==========================================

ferramenta_atual = "circulo"

def selecionar_circulo():
    global ferramenta_atual
    ferramenta_atual = "circulo"

    botao_circulo.config(relief=SUNKEN)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=RAISED)


def selecionar_retangulo():
    global ferramenta_atual
    ferramenta_atual = "retangulo"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=SUNKEN)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=RAISED)


def selecionar_oval():
    global ferramenta_atual
    ferramenta_atual = "oval"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=SUNKEN)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=RAISED)


def selecionar_linha():
    global ferramenta_atual
    ferramenta_atual = "linha"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=SUNKEN)
    botao_rabisco.config(relief=RAISED)


def selecionar_rabisco():
    global ferramenta_atual
    ferramenta_atual = "rabisco"

    botao_circulo.config(relief=RAISED)
    botao_retangulo.config(relief=RAISED)
    botao_oval.config(relief=RAISED)
    botao_linha.config(relief=RAISED)
    botao_rabisco.config(relief=SUNKEN)


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
# LÓGICA DA LINHA E RABISCO (NOVO)
# ==========================================

def iniciar_linha_rabisco(event):
    global figura_nova
    if ferramenta_atual == "linha":
        figura_nova = ("linha", [event.x, event.y, event.x, event.y], cores.cor_borda_atual)
    elif ferramenta_atual == "rabisco":
        figura_nova = ("rabisco", [(event.x, event.y)], cores.cor_borda_atual)


def atualizar_linha_rabisco(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha":
        figura_nova[1][2] = event.x
        figura_nova[1][3] = event.y

    desenhar_figuras()
    desenhar_figura_nova()


def finalizar_linha_rabisco(event):
    if not incompleta(figura_nova):
        figuras.append(figura_nova)
    desenhar_figuras()


def desenhar_figura_nova():
    tipo, values, cor = figura_nova
    if tipo == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], fill=cor, dash=(4, 2))
    elif tipo == "rabisco":
        canvas.create_line(values, fill=cor, dash=(4, 2))


def incompleta(figura):
    tipo, values, _ = figura
    if tipo == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif tipo == "rabisco":
        return len(values) <= 1


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
            
        elif tipo == 'linha':
            _, values, cor_borda = figura
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_borda)
            
        elif tipo == 'rabisco':
            _, values, cor_borda = figura
            canvas.create_line(values, fill=cor_borda)


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

figuras = []
figura_nova = None

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

botao_circulo.config(relief=SUNKEN)

# Posicionamento dos botões (seguindo o layout grid do seu projeto)
botao_circulo.grid(row=0, column=8, padx=5, pady=2)
botao_retangulo.grid(row=1, column=8, padx=5, pady=2)
botao_oval.grid(row=2, column=8, padx=5, pady=2)
botao_linha.grid(row=3, column=8, padx=5, pady=2)
botao_rabisco.grid(row=4, column=8, padx=5, pady=2)

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

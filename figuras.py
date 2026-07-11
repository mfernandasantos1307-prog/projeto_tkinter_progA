from tkinter import *

import cores


# ==========================================
# LÓGICA DE DESENHO
# ==========================================

# Quando o mouse é pressionado
def inicia_desenho(event):
    global ini_x, ini_y

    ini_x = event.x
    ini_y = event.y


# Quando o mouse é movido com o botão pressionado
def atualiza_desenho(event):
    global fim_x, fim_y, raio

    fim_x = event.x
    fim_y = event.y

    # Redesenha os círculos já finalizados
    desenhar()

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


# Quando o mouse é solto
def finalizar_desenho(event):
    circulos.append(
        (
            ini_x,
            ini_y,
            raio,
            cores.cor_borda_atual,
            cores.cor_preenchimento_atual
        )
    )


# Redesenha todos os círculos finalizados
def desenhar():
    canvas.delete("all")

    for circulo in circulos:
        x, y, r, cor_borda, cor_preenchimento = circulo

        canvas.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            outline=cor_borda,
            fill=cor_preenchimento
        )


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

# Cria a paleta usando o módulo cores.py
cores.criar_paleta(frame_ferramentas)

# Área de desenho
canvas = Canvas(
    root,
    bg="white",
    width=600,
    height=600
)
canvas.pack()

# Eventos do mouse
canvas.bind("<ButtonPress-1>", inicia_desenho)
canvas.bind("<B1-Motion>", atualiza_desenho)
canvas.bind("<ButtonRelease-1>", finalizar_desenho)

root.mainloop()
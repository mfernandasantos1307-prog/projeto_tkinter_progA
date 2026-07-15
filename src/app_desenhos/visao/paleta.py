from tkinter import Button, colorchooser, RAISED, SUNKEN


#VARIÁVEIS GLOBAIS


cor_borda_atual = "black"
cor_preenchimento_atual = ""
modo_cor = "preenchimento"



#LÓGICA DAS CORES


def selecionar_cor(cor_escolhida):
    global cor_preenchimento_atual
    global cor_borda_atual
    global modo_cor

    if modo_cor == "preenchimento":
        cor_preenchimento_atual = cor_escolhida
    else:
        cor_borda_atual = cor_escolhida


def ativar_modo_borda():
    global modo_cor
    modo_cor = "borda"

    selecionar_borda.config(relief=SUNKEN)
    selecionar_preenchimento.config(relief=RAISED)


def ativar_modo_preenchimento():
    global modo_cor
    modo_cor = "preenchimento"

    selecionar_borda.config(relief=RAISED)
    selecionar_preenchimento.config(relief=SUNKEN)

def escolher_cor_extra():
    global cor_preenchimento_atual
    global cor_borda_atual
    global modo_cor

    cor = colorchooser.askcolor(title="Outras cores")

    if cor[1]:
        if modo_cor == "preenchimento":
            cor_preenchimento_atual = cor[1]
        else:
            cor_borda_atual = cor[1]

#INTERFACE DA PALETA

def criar_paleta(frame):

    global selecionar_borda
    global selecionar_preenchimento

    selecionar_borda = Button(
        frame,
        text="Borda",
        command=ativar_modo_borda
    )

    selecionar_preenchimento = Button(
        frame,
        text="Preenchimento",
        command=ativar_modo_preenchimento
    )

    selecionar_mais_cores = Button(
        frame,
        text="Mais cores",
        command=escolher_cor_extra
    )

    botao_preto = Button(frame, bg="black", width=2,
                         command=lambda: selecionar_cor("black"))

    botao_branco = Button(frame, bg="white", width=2,
                          command=lambda: selecionar_cor("white"))

    botao_vermelho = Button(frame, bg="red", width=2,
                            command=lambda: selecionar_cor("red"))

    botao_verde = Button(frame, bg="green", width=2,
                         command=lambda: selecionar_cor("green"))

    botao_azul = Button(frame, bg="blue", width=2,
                        command=lambda: selecionar_cor("blue"))

    botao_amarelo = Button(frame, bg="yellow", width=2,
                           command=lambda: selecionar_cor("yellow"))

    botao_rosa = Button(frame, bg="pink", width=2,
                        command=lambda: selecionar_cor("pink"))

    botao_roxo = Button(frame, bg="purple", width=2,
                        command=lambda: selecionar_cor("purple"))

    botao_marrom = Button(frame, bg="brown", width=2,
                          command=lambda: selecionar_cor("brown"))

    botao_cinza = Button(frame, bg="gray", width=2,
                         command=lambda: selecionar_cor("gray"))

    botao_laranja = Button(frame, bg="orange", width=2,
                           command=lambda: selecionar_cor("orange"))

    botao_transparente = Button(frame, text="X", bg="lightgray", width=2,
                                command=lambda: selecionar_cor(""))

    #ORGANIZAÇÃO

    selecionar_borda.grid(row=2, column=0, padx=5, pady=2)
    selecionar_preenchimento.grid(row=3, column=0, padx=5, pady=2)

    botao_preto.grid(row=2, column=1)
    botao_vermelho.grid(row=2, column=2)
    botao_azul.grid(row=2, column=3)
    botao_rosa.grid(row=2, column=4)
    botao_marrom.grid(row=2, column=5)
    botao_laranja.grid(row=2, column=6)

    botao_transparente.grid(row=3, column=1)
    botao_branco.grid(row=3, column=2)
    botao_verde.grid(row=3, column=3)
    botao_amarelo.grid(row=3, column=4)
    botao_roxo.grid(row=3, column=5)
    botao_cinza.grid(row=3, column=6)

    selecionar_mais_cores.grid(row=2, column=7, rowspan=2, padx=5, pady=2)

  

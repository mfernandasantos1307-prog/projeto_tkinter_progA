from tkinter import Button, RAISED, SUNKEN
from tkinter import colorchooser

class PaletaCores:
    # --- INICIALIZAÇÃO (Configuração inicial e variáveis) ---
    def __init__(self, frame):
        self.frame = frame
        
        self._cor_borda_atual = "black"
        self._cor_preenchimento_atual = ""
        self._modo_cor = "preenchimento"
        
        self.criar_paleta()

    # --- LÓGICA DAS CORES ---
    def selecionar_cor(self, cor_escolhida):
        if self._modo_cor == "preenchimento":
            self._cor_preenchimento_atual = cor_escolhida
        else:
            self._cor_borda_atual = cor_escolhida

    def obter_cor_borda(self):
        return self._cor_borda_atual

    def obter_cor_preenchimento(self):
        return self._cor_preenchimento_atual

    def ativar_modo_borda(self):
        self._modo_cor = "borda"
        self.selecionar_borda.config(relief=SUNKEN)
        self.selecionar_preenchimento.config(relief=RAISED)

    def ativar_modo_preenchimento(self):
        self._modo_cor = "preenchimento"
        self.selecionar_borda.config(relief=RAISED)
        self.selecionar_preenchimento.config(relief=SUNKEN)

    def escolher_cor_extra(self):
        cor = colorchooser.askcolor(title="Outras cores")
        if cor[1]:
            if self._modo_cor == "preenchimento":
                self._cor_preenchimento_atual = cor[1]
            else:
                self._cor_borda_atual = cor[1]

    # --- INTERFACE DA PALETA ---
    def criar_paleta(self):
        self.selecionar_borda = Button(
            self.frame,
            text="Borda",
            command=self.ativar_modo_borda
        )

        self.selecionar_preenchimento = Button(
            self.frame,
            text="Preenchimento",
            command=self.ativar_modo_preenchimento
        )

        selecionar_mais_cores = Button(
            self.frame,
            text="Mais cores",
            command=self.escolher_cor_extra
        )

        botao_preto = Button(self.frame, bg="black", width=2,
                             command=lambda: self.selecionar_cor("black"))

        botao_branco = Button(self.frame, bg="white", width=2,
                              command=lambda: self.selecionar_cor("white"))

        botao_vermelho = Button(self.frame, bg="red", width=2,
                                command=lambda: self.selecionar_cor("red"))

        botao_verde = Button(self.frame, bg="green", width=2,
                             command=lambda: self.selecionar_cor("green"))

        botao_azul = Button(self.frame, bg="blue", width=2,
                            command=lambda: self.selecionar_cor("blue"))

        botao_amarelo = Button(self.frame, bg="yellow", width=2,
                               command=lambda: self.selecionar_cor("yellow"))

        botao_rosa = Button(self.frame, bg="pink", width=2,
                            command=lambda: self.selecionar_cor("pink"))

        botao_roxo = Button(self.frame, bg="purple", width=2,
                            command=lambda: self.selecionar_cor("purple"))

        botao_marrom = Button(self.frame, bg="brown", width=2,
                              command=lambda: self.selecionar_cor("brown"))

        botao_cinza = Button(self.frame, bg="gray", width=2,
                             command=lambda: self.selecionar_cor("gray"))

        botao_laranja = Button(self.frame, bg="orange", width=2,
                               command=lambda: self.selecionar_cor("orange"))

        botao_transparente = Button(self.frame, text="X", bg="lightgray", width=2,
                                    command=lambda: self.selecionar_cor(""))

        # --- ORGANIZAÇÃO (Grid) ---
        self.selecionar_borda.grid(row=2, column=0, padx=5, pady=2)
        self.selecionar_preenchimento.grid(row=3, column=0, padx=5, pady=2)

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

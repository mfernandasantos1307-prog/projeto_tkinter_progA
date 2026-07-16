from tkinter import * 
from .paleta import PaletaCores

class EditorView:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Editor de Desenhos')
        self.janela.geometry('600x600')

        self.controlador = None 

        #Frame para barra de ferramentas (esquerda)
        self.barra_ferramentas = Frame(self.janela, bd=2, relief=RAISED)
        self.barra_ferramentas.pack(fill=Y, side=LEFT, padx=5, pady=5)

        #Canvas de desenho 
        self.canvas = Canvas(self.janela, bg='white', highlightthickness=1, highlightbackground='gray')
        self.canvas.pack(fill=BOTH, expand=True, side=RIGHT, padx=5, pady=5)

        titulo_botoes = Label(self.barra_ferramentas, text='Ferramentas')
        titulo_botoes.pack(pady=10)

        #Guardando os botões de ferramentas 
        self.botoes = {}
        self.criar_botoes_ferramentas()

        #divisor visual
        divisor = Frame(self.barra_ferramentas, height=2, bd=1, relief=SUNKEN)
        divisor.pack(fill=X, pady=15)

        # Instancição da paleta de cores
        self.frame_paleta = Frame(self.barra_ferramentas)
        self.frame_paleta.pack(pady=5)
        self.paleta = PaletaCores(self.frame_paleta)

    def criar_botoes_ferramentas(self):
        ferramentas = ['Rabiscos', 'Linha', 'Retangulo', 'Circulo', 'Oval','Poligono']

        for nome in ferramentas:

            btn = Button(
                self.barra_ferramentas,
                text=nome,
                width=12,
                relief=RAISED,
                command=lambda n=nome: self.ao_clicar_ferramenta(n)
            )
            btn.pack(pady=3, padx=5)

            self.botoes[nome] = btn

    def ao_clicar_ferramenta(self, nome_feramenta):
        if self.controlador:
            self.controlador.selecionar_ferramenta(nome_feramenta)

    def destacar_ferramenta(self, ferramenta):
        for nome, botao in self.botoes.items():
            if nome == ferramenta:
                botao.config(relief=SUNKEN)
            else:
                botao.config(relief=RAISED)

    def conectar_controlador(self, controlador):
        self.controlador = controlador

        # clique do botão esquerdo do mouse 
        self.canvas.bind('<Button-1>', self.controlador.iniciar_figura)

        #arrastar o mouse com o botão pressionado
        self.canvas.bind('<B1-Motion>', self.controlador.atualizar_figura)

        #soltãr o botão esquerdo do mouse 
        self.canvas.bind('<ButtonRelease-1>', self.controlador.finalizar_figura)

        # duplo clique para finalizar o polígono 
        self.canvas.bind('<Double-Button-1>', self.controlador.finalizar_poligono)

    def obter_cor_borda(self):
        return self.paleta.cor_borda_atual

    def obter_cor_preenchimento(self):
        return self.paleta.cor_preenchimento_atual  

    def redesenhar(self, figuras):
        self.canvas.delete('all')

        for fig in figuras:
            fig.desenhar(self.canvas)

    def iniciar(self):
        self.janela.mainloop()

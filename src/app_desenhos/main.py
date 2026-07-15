import tkinter as tk

import src.app_desenhos.cores as cores
from src.app_desenhos.model.desenho import Desenho
from src.app_desenhos.model.figuras import Circulo, Linha, Oval, Poligono, Rabisco, Retangulo


class EditorDesenho:
    """Interface principal e controle do editor de figuras."""

    def __init__(self, root):
        self.root = root
        self.root.title("Editor de figuras")

        self.ferramenta_atual = "circulo"
        self.desenho = Desenho()
        self.figura_nova = None
        self.pontos_poligono = []

        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None

        self.botoes_ferramentas = {}
        self.criar_interface()

    # ==========================================
    # INTERFACE E SELEÇÃO DE FERRAMENTAS
    # ==========================================

    def criar_interface(self):
        frame_ferramentas = tk.Frame(self.root)
        frame_ferramentas.pack(
            side="top",
            fill="x",
            padx=5,
            pady=5
        )

        self.paleta = cores.PaletaCores(frame_ferramentas)

        ferramentas = (
            ("circulo", "◯ Círculo"),
            ("retangulo", "▭ Retângulo"),
            ("oval", "⬭ Oval"),
            ("linha", "╱ Linha"),
            ("rabisco", "✎ Rabisco"),
            ("poligono", "⬠ Polígono"),
        )

        for linha, (nome, texto) in enumerate(ferramentas):
            botao = tk.Button(
                frame_ferramentas,
                text=texto,
                width=10,
                command=lambda ferramenta=nome: self.selecionar_ferramenta(
                    ferramenta
                )
            )
            botao.grid(row=linha, column=8, padx=5, pady=2)
            self.botoes_ferramentas[nome] = botao

        self.botoes_ferramentas["circulo"].config(relief=tk.SUNKEN)

        self.canvas = tk.Canvas(
            self.root,
            bg="white",
            width=600,
            height=600
        )
        self.canvas.pack()

        self.canvas.bind("<ButtonPress-1>", self.iniciar_figura)
        self.canvas.bind("<B1-Motion>", self.atualizar_figura)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_figura)
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)

    def selecionar_ferramenta(self, ferramenta):
        if self.ferramenta_atual == "poligono" and ferramenta != "poligono":
            self.concluir_poligono_em_andamento()

        self.ferramenta_atual = ferramenta

        for nome, botao in self.botoes_ferramentas.items():
            relevo = tk.SUNKEN if nome == ferramenta else tk.RAISED
            botao.config(relief=relevo)

    # ==========================================
    # CÍRCULO
    # ==========================================

    def iniciar_circulo(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def atualizar_circulo(self, event):
        self.fim_x = event.x
        self.fim_y = event.y
        self.desenhar_figuras()

        raio = self.calcular_raio(self.fim_x, self.fim_y)
        self.canvas.create_oval(
            self.ini_x - raio,
            self.ini_y - raio,
            self.ini_x + raio,
            self.ini_y + raio,
            outline=self.paleta.cor_borda_atual,
            fill=self.paleta.cor_preenchimento_atual
        )

    def finalizar_circulo(self, event):
        raio = self.calcular_raio(event.x, event.y)
        self.desenho.adicionar_figura(
            Circulo(
                self.paleta.cor_borda_atual,
                self.paleta.cor_preenchimento_atual,
                self.ini_x,
                self.ini_y,
                raio
            )
        )
        self.desenhar_figuras()
        
    def calcular_raio(self, fim_x, fim_y):
        return (
            (self.ini_x - fim_x) ** 2
            + (self.ini_y - fim_y) ** 2
        ) ** 0.5

    # ==========================================
    # RETÂNGULO
    # ==========================================

    def iniciar_retangulo(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def atualizar_retangulo(self, event):
        self.fim_x = event.x
        self.fim_y = event.y
        self.desenhar_figuras()

        self.canvas.create_rectangle(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            outline=self.paleta.cor_borda_atual,
            fill=self.paleta.cor_preenchimento_atual
        )

    def finalizar_retangulo(self, event):
        self.desenho.adicionar_figura(
            Retangulo(
                self.paleta.cor_borda_atual,
                self.paleta.cor_preenchimento_atual,
                self.ini_x,
                self.ini_y,
                event.x,
                event.y
            )
        )
        self.desenhar_figuras()

    # ==========================================
    # OVAL
    # ==========================================

    def iniciar_oval(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def atualizar_oval(self, event):
        self.fim_x = event.x
        self.fim_y = event.y
        self.desenhar_figuras()

        self.canvas.create_oval(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            outline=self.paleta.cor_borda_atual,
            fill=self.paleta.cor_preenchimento_atual
        )

    def finalizar_oval(self, event):
        self.desenho.adicionar_figura(
            Oval(
                self.paleta.cor_borda_atual,
                self.paleta.cor_preenchimento_atual,
                self.ini_x,
                self.ini_y,
                event.x,
                event.y
            )
        )
        self.desenhar_figuras()
    
    # ==========================================
    # LINHA E RABISCO
    # ==========================================

    def iniciar_linha_rabisco(self, event):
        if self.ferramenta_atual == "linha":
            self.figura_nova = Linha(
                self.paleta.cor_borda_atual,
                None,
                event.x,
                event.y,
                event.x,
                event.y
            )
        elif self.ferramenta_atual == "rabisco":
            self.figura_nova = Rabisco(
                [(event.x, event.y)],
                self.paleta.cor_borda_atual
            )
    
    def atualizar_linha_rabisco(self, event):
        if isinstance(self.figura_nova, Rabisco):
            self.figura_nova.pontos.append((event.x, event.y))
        elif isinstance(self.figura_nova, Linha):
            self.figura_nova.fim_x = event.x
            self.figura_nova.fim_y = event.y

        self.desenhar_figuras()
        if self.figura_nova is not None:
            self.figura_nova.desenhar(self.canvas)

    def finalizar_linha_rabisco(self, _event):
        if not self.figura_incompleta(self.figura_nova):
            self.desenho.adicionar_figura(self.figura_nova)

        self.desenhar_figuras()
        self.figura_nova = None

    @staticmethod
    def figura_incompleta(figura):
        if isinstance(figura, Linha):
            return (figura.ini_x, figura.ini_y) == (figura.fim_x, figura.fim_y)
        if isinstance(figura, Rabisco):
            return len(figura.pontos) <= 1
        return True

    # ==========================================
    # POLÍGONO
    # ==========================================

    def adicionar_ponto_poligono(self, event):
        self.pontos_poligono.append((event.x, event.y))
        self.desenhar_figuras()
        self.desenhar_poligono_em_andamento()

    def desenho_poligono_em_andamento(self):
        # Correção do nome do método para manter compatibilidade interna
        self.desenhar_poligono_em_andamento()

    def desenhar_poligono_em_andamento(self):
        if len(self.pontos_poligono) >= 2:
            self.canvas.create_polygon(
                self.pontos_poligono,
                outline=self.paleta.cor_borda_atual,
                fill=""
            )

        for x, y in self.pontos_poligono:
            self.canvas.create_oval(
                x - 3,
                y - 3,
                x + 3,
                y + 3,
                fill="red",
                outline="red"
            )

    def finalizar_poligono(self, _event):
        if self.ferramenta_atual != "poligono":
            return None

        self.concluir_poligono_em_andamento()
        return "break"

    def concluir_poligono_em_andamento(self):
        if not self.pontos_poligono:
            return

        if len(self.pontos_poligono) >= 3:
            self.desenho.adicionar_figura(
                Poligono(
                    list(self.pontos_poligono),
                    self.paleta.cor_borda_atual,
                    self.paleta.cor_preenchimento_atual
                )
            )

        self.pontos_poligono = []
        self.desenhar_figuras()

    # ==========================================
    # CONTROLE DOS EVENTOS
    # ==========================================

    def iniciar_figura(self, event):
        if self.ferramenta_atual == "circulo":
            self.iniciar_circulo(event)
        elif self.ferramenta_atual == "retangulo":
            self.iniciar_retangulo(event)
        elif self.ferramenta_atual == "oval":
            self.iniciar_oval(event)
        elif self.ferramenta_atual in ("linha", "rabisco"):
            self.iniciar_linha_rabisco(event)
        elif self.ferramenta_atual == "poligono":
            self.adicionar_ponto_poligono(event)

    def atualizar_figura(self, event):
        if self.ferramenta_atual == "circulo":
            self.atualizar_circulo(event)
        elif self.ferramenta_atual == "retangulo":
            self.atualizar_retangulo(event)
        elif self.ferramenta_atual == "oval":
            self.atualizar_oval(event)
        elif self.ferramenta_atual in ("linha", "rabisco"):
            self.atualizar_linha_rabisco(event)

    def finalizar_figura(self, event):
        if self.ferramenta_atual == "circulo":
            self.finalizar_circulo(event)
        elif self.ferramenta_atual == "retangulo":
            self.finalizar_retangulo(event)
        elif self.ferramenta_atual == "oval":
            self.finalizar_oval(event)
        elif self.ferramenta_atual in ("linha", "rabisco"):
            self.finalizar_linha_rabisco(event)

    def desenhar_figuras(self):
        self.canvas.delete("all")
        self.desenho.desenhar_todos(self.canvas)


def main():
    root = tk.Tk()
    EditorDesenho(root)
    root.mainloop()


if __name__ == "__main__":
    main()

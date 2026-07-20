from app_desenhos.controlador.estados.estado_circulo import EstadoCirculo
from app_desenhos.controlador.estados.estado_linha import EstadoLinha
from app_desenhos.controlador.estados.estado_oval import EstadoOval
from app_desenhos.controlador.estados.estado_poligono import EstadoPoligono
from app_desenhos.controlador.estados.estado_rabisco import EstadoRabisco
from app_desenhos.controlador.estados.estado_retangulo import EstadoRetangulo


class EditorController:

    def __init__(self, desenho, view):
        self.desenho = desenho
        self.view = view
        self.caminho_arquivo = None

        self.estados = {
            "circulo": EstadoCirculo(),
            "retangulo": EstadoRetangulo(),
            "oval": EstadoOval(),
            "linha": EstadoLinha(),
            "rabisco": EstadoRabisco(),
            "poligono": EstadoPoligono(),
        }
        self.nome_ferramenta_atual = "circulo"
        self.estado_atual = self.estados[self.nome_ferramenta_atual]

    @property
    def cor_borda(self):
        return self.view.obter_cor_borda()

    @property
    def cor_preenchimento(self):
        return self.view.obter_cor_preenchimento()

    def selecionar_ferramenta(self, ferramenta):
        novo_estado = self.estados[ferramenta]

        if novo_estado is not self.estado_atual:
            self.estado_atual.ao_sair(self)
            self.estado_atual = novo_estado
            self.nome_ferramenta_atual = ferramenta

        self.view.destacar_ferramenta(ferramenta)

    def iniciar_figura(self, event):
        self.estado_atual.ao_pressionar(self, event)

    def atualizar_figura(self, event):
        self.estado_atual.ao_arrastar(self, event)

    def finalizar_figura(self, event):
        self.estado_atual.ao_soltar(self, event)

    def finalizar_poligono(self, event):
        return self.estado_atual.ao_duplo_clique(self, event)

    def atualizar_view(self):
        self.view.redesenhar(self.desenho.obter_figuras())

    def salvar_arquivo(self):
        if self.caminho_arquivo is None:
            self.salvar_como()
            return

        self._salvar_no_caminho(self.caminho_arquivo)

    def salvar_como(self):
        caminho = self.view.escolher_arquivo_para_salvar()
        if not caminho:
            return

        self._salvar_no_caminho(caminho)

    def _salvar_no_caminho(self, caminho):
        try:
            self.desenho.salvar_em_arquivo(caminho)
        except Exception as erro:
            self.view.mostrar_erro(f"Não foi possível salvar o desenho: {erro}")
            return

        self.caminho_arquivo = caminho
        self.view.mostrar_mensagem("Desenho salvo com sucesso.")

    def abrir_arquivo(self):
        caminho = self.view.escolher_arquivo_para_abrir()
        if not caminho:
            return

        try:
            self.desenho.carregar_de_arquivo(caminho)
        except Exception as erro:
            self.view.mostrar_erro(f"Não foi possível abrir o desenho: {erro}")
            return

        self.estado_atual.cancelar(self)
        self.caminho_arquivo = caminho
        self.atualizar_view()
        self.view.mostrar_mensagem("Desenho aberto com sucesso.")

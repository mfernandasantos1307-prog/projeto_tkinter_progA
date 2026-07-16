from .controlador.editor_controller import EditorController
from .model.desenho import Desenho
from .visao.editor_view import EditorView


def main():
    desenho = Desenho()
    view = EditorView()
    controller = EditorController(desenho, view)

    view.conectar_controlador(controller)
    controller.selecionar_ferramenta("circulo")
    view.iniciar()


if __name__ == "__main__":
    main()

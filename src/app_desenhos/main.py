from src.app_desenhos.controlador.editor_controller import EditorController
from src.app_desenhos.model.desenho import Desenho
from src.app_desenhos.visao.editor_view import EditorView


def main():
    desenho = Desenho()
    view = EditorView()
    controller = EditorController(desenho, view)

    view.conectar_controlador(controller)
    controller.selecionar_ferramenta("circulo")
    view.iniciar()


if __name__ == "__main__":
    main()

import sys
from pathlib import Path


# Permite executar este arquivo diretamente pelo botão Run da IDE.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


from app_desenhos.controlador.editor_controller import EditorController
from app_desenhos.model.desenho import Desenho
from app_desenhos.visao.editor_view import EditorView


def main():
    desenho = Desenho()
    view = EditorView()
    controller = EditorController(desenho, view)

    view.conectar_controlador(controller)
    controller.selecionar_ferramenta("circulo")
    view.iniciar()


if __name__ == "__main__":
    main()

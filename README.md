# Projeto de Programação A — Aplicativo de Desenho

Aplicativo desenvolvido em Python com Tkinter para a disciplina Programação A — 2026.1.

## Integrantes

- Maria Luíse das Virgens Menezes
- Maria Fernanda de Jesus Santos
- Eloísa Santos Zeferino

## Funcionalidades

- Desenho de círculos, retângulos, ovais e polígonos
- Criação de linhas e desenhos à mão livre
- Seleção de cores de borda e preenchimento
- Estrutura orientada a objetos com uma hierarquia de figuras
- Classe abstrata `Figura`, com implementações específicas para cada figura
- Organização da aplicação segundo o padrão MVC (Model-View-Controller)

## Execução

Na pasta principal do projeto, execute:

```bash
python -m src.app_desenhos.main
```

No Windows, caso o comando usado para iniciar o Python seja `py`, execute:

```powershell
py -m src.app_desenhos.main
```

## Estrutura principal

- `src/app_desenhos/main.py`: cria e conecta os componentes da aplicação
- `src/app_desenhos/model/`: classes do modelo, como `Desenho` e a hierarquia de figuras
- `src/app_desenhos/visao/`: interface gráfica e paleta de cores
- `src/app_desenhos/controlador/`: controlador das ferramentas e eventos de desenho

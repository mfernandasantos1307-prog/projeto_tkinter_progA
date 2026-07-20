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
- Uso do padrão State para representar as ferramentas de desenho
- Funcionalidades para salvar e abrir desenhos

## Execução

O programa pode ser iniciado diretamente pelo botão Run da IDE com o arquivo
`src/app_desenhos/main.py` aberto.

Também é possível executar pelo terminal. Entre na pasta `src`:

```bash
cd src
```

Em seguida, execute:

```bash
python -m app_desenhos.main
```

No Windows, caso o comando usado para iniciar o Python seja `py`:

```powershell
py -m app_desenhos.main
```

## Estrutura principal

- `src/app_desenhos/main.py`: cria e conecta os componentes da aplicação
- `src/app_desenhos/model/`: classes do modelo, com cada figura em seu próprio módulo
- `src/app_desenhos/visao/`: interface gráfica e paleta de cores
- `src/app_desenhos/controlador/`: controlador e estados das ferramentas de desenho

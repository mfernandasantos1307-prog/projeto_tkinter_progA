from tkinter import Button, colorchooser

cor_borda_atual = 'black'
cor_preenchimento_atual = 'white'
modo_cor = 'preenchimento'

# Função para preenchimento com a tabela
def selecionar_cor(cor_escolhida):
  global cor_preenchimento_atual
  global cor_borda_atual
  global modo_cor
  
  if modo_cor == 'preenchimento':
    cor_preenchimento_atual = cor_escolhida
    return cor_preenchimento_atual
  elif modo_cor == 'borda':
    cor_borda_atual = cor_escolhida
    return cor_borda_atual 

# Selecão do modo (borda ou preenchimento)
def ativar_modo_borda():
  global modo_cor
  modo_cor = 'borda'
  return modo_cor

def ativar_modo_preenchimento():
  global modo_cor
  modo_cor = 'preenchimento'
  return modo_cor

# Funçôes para preenchimento com o botão Mais cores
def escolher_cor_extra():
  global cor_preenchimento_atual
  global cor_borda_atual
  global modo_cor

  cor = colorchooser.askcolor(title='Outras cores')
  if modo_cor == 'preenchimento':
    if cor[1]:
      cor_preenchimento_atual = cor[1]
      return cor_preenchimento_atual
  elif modo_cor == 'borda':
    if cor[1]:
      cor_borda_atual = cor[1]
      return cor_borda_atual

# Botões respectivos a cada função
selecionar_borda = Button(frame, text="Borda", command=ativar_modo_borda)
selecionar_preenchimento = Button(frame, text='Preenchimento', command=ativar_modo_preenchimento)
selecionar_mais_cores = Button(frame, text="Mais cores", command=escolher_cor_extra)

# Quadradinhos da paleta de cores
botao_preto = Button(frame, bg="black", width=2, command=lambda: selecionar_cor("black"))
botao_branco = Button(frame, bg="white", width=2, command=lambda: selecionar_cor("white"))
botao_vermelho = Button(frame, bg="red", width=2, command=lambda: selecionar_cor("red"))
botao_verde = Button(frame, bg="green", width=2, command=lambda: selecionar_cor("green"))
botao_azul = Button(frame, bg="blue", width=2, command=lambda: selecionar_cor("blue"))
botao_amarelo = Button(frame, bg="yellow", width=2, command=lambda: selecionar_cor("yellow"))
botao_rosa = Button(frame, bg="pink", width=2, command=lambda: selecionar_cor("pink"))
botao_roxo = Button(frame, bg="purple", width=2, command=lambda: selecionar_cor("purple"))
botao_marrom = Button(frame, bg="brown", width=2, command=lambda: selecionar_cor("brown"))
botao_cinza = Button(frame, bg="gray", width=2, command=lambda: selecionar_cor("gray"))

# 7. Organização do Grid na linha 2 e linha 3 (Abaixo do Canvas)
# Botões de modo (Coluna 0)
selecionar_borda.grid(row=2, column=0, padx=5, pady=2, sticky=W)
selecionar_preenchimento.grid(row=3, column=0, padx=5, pady=2, sticky=W)

# Quadradinhos de cores - Fileira de cima (Linha 2)
botao_preto.grid(row=2, column=1, padx=2, pady=2)
botao_vermelho.grid(row=2, column=2, padx=2, pady=2)
botao_azul.grid(row=2, column=3, padx=2, pady=2)
botao_rosa.grid(row=2, column=4, padx=2, pady=2)
botao_marrom.grid(row=2, column=5, padx=2, pady=2)

# Quadradinhos de cores - Fileira de baixo (Linha 3)
botao_branco.grid(row=3, column=1, padx=2, pady=2)
botao_verde.grid(row=3, column=2, padx=2, pady=2)
botao_amarelo.grid(row=3, column=3, padx=2, pady=2)
botao_roxo.grid(row=3, column=4, padx=2, pady=2)
botao_cinza.grid(row=3, column=5, padx=2, pady=2)

selecionar_mais_cores.grid(row=2, column=6, rowspan=2, padx=5, pady=2)

# Função para preenchimento
from tkinter import colorchooser

cor_borda_atual = 'black'
cor_preenchimento_atual = 'white'

def escolher_cor_preenchimento():
  global cor_preenchimento_atual
  cor = colorchooser.askcolor(Title='Escolha a cor de preenchimento')
  if cor[1]:
    cor_preenchimento_atual = cor[1]

# Função para borda

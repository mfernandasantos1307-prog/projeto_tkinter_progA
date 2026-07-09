# Função para preenchimento
from tkinter import colorchooser

cor_borda_atual = 'black'
cor_preenchimento_atual = 'white'

def escolher_cor_preenchimento():
  global cor_preenchimento_atual
  cor = colorchooser.askcolor(title='Escolha a cor de preenchimento')
  if cor[1]:
    cor_preenchimento_atual = cor[1]
  return cor_preenchimento_atual

# Função para borda

def escolher_cor_borda():
  global cor_borda_atual
  cor = colorchooser.askcolor(title='Escolha a cor da borda')
  if cor[1]:
    cor_borda_atual = cor[1]
  return cor_borda_atual

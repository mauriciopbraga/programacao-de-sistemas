import math

numeroBinario = '101001'
tamanhoBinario = len(numeroBinario) # Função len retorna o tamanho de caracteres
numeroDecimal = 0
indice = 0
controle = tamanhoBinario - 1

while indice < tamanhoBinario:
  expoente = controle - (indice)
  print(numeroBinario[indice], '^2 |', expoente)
  numeroCalculado = int(numeroBinario[indice]) * math.pow(2, expoente)
  numeroDecimal = numeroDecimal + numeroCalculado
  indice = indice + 1

print('\nO numero binário', numeroBinario, 'convertido para decimal vale: ', numeroDecimal)
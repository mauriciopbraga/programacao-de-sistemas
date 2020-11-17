frase = input('Digite uma frase para ser descriptografada: ')
saida = []
tamanhoFrase = len(frase)
indice = 0

while indice < tamanhoFrase:
  if frase[indice] == ' ':
    saida.append(' ')
  else:
    valorDoCaractere = ord(frase[indice])

    if valorDoCaractere <= 67: # Se o valor ascii do caractere digitado for menor ou igual ao caractere 67 (C), o mesmo será decrementado para o alfabeto de trás para frente
      convertido = (valorDoCaractere + 26) - 3
    else:
      convertido = valorDoCaractere - 3 
      
    saida.append(chr(convertido))

  indice = indice + 1

print() # Quebra de linha
print(''.join(saida))
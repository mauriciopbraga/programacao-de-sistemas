frase = input('Digite uma frase para ser criptografada: ')
saida = [] # Vetor onde será escrita a saída da cifragem
tamanhoFrase = len(frase) # len retorna o tamanho da entrada de caracteres
indice = 0

while indice < tamanhoFrase:
  if frase[indice] == ' ': # Se o caractere for espaço em branco, escreve ' ' na saída
    saida.append(' ') # Coloca na última posição do vetor saída o caractere convertido
  else: # Se não for espaço em branco, converte
    valorDoCaractere = ord(frase[indice])

    if valorDoCaractere >= 88:
      convertido = (valorDoCaractere - 26) + 3
    else:
      convertido = valorDoCaractere + 3 
      
    saida.append(chr(convertido)) # Coloca na última posição do vetor saída o caractere convertido

  indice = indice + 1

print() # Quebra de linha
print(''.join(saida))
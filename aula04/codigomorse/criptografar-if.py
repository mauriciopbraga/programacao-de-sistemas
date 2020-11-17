frase = input('Digite um texto para ser criptografado: ').upper()
tamanhoFrase = len(frase)
saida = []
indice = 0

while indice < tamanhoFrase:
  if frase[indice] == ' ':
    saida.append('/')
  elif frase[indice] == 'A':
    saida.append('.-')
  elif frase[indice] == 'B':
    saida.append('-...')
  elif frase[indice] == 'C':
    saida.append('-.-.')
  elif frase[indice] == 'D':
    saida.append('-..')
  elif frase[indice] == 'E':
    saida.append('.')
  elif frase[indice] == 'F':
    saida.append('..-.')
  elif frase[indice] == 'G':
    saida.append('--.')
  elif frase[indice] == 'H':
    saida.append('....')
  elif frase[indice] == 'I':
    saida.append('..')
  elif frase[indice] == 'J':
    saida.append('.---')
  elif frase[indice] == 'K':
    saida.append('-.-')
  elif frase[indice] == 'L':
    saida.append('.-..')
  elif frase[indice] == 'M':
    saida.append('--')
  elif frase[indice] == 'N':
    saida.append('-.')
  elif frase[indice] == 'O':
    saida.append('---')
  elif frase[indice] == 'P':
    saida.append('.--.')
  elif frase[indice] == 'Q':
    saida.append('--.-')
  elif frase[indice] == 'R':
    saida.append('.-.')
  elif frase[indice] == 'S':
    saida.append('...')
  elif frase[indice] == 'T':
    saida.append('-')
  elif frase[indice] == 'U':
    saida.append('..-')
  elif frase[indice] == 'V':
    saida.append('...-')
  elif frase[indice] == 'W':
    saida.append('.--')
  elif frase[indice] == 'X':
    saida.append('-..-')
  elif frase[indice] == 'Y':
    saida.append('-.--')
  elif frase[indice] == 'Z':
    saida.append('--..')
  elif frase[indice] == '0':
    saida.append('-----')
  elif frase[indice] == '1':
    saida.append('.----')
  elif frase[indice] == '2':
    saida.append('..---')
  elif frase[indice] == '3':
    saida.append('....--')
  elif frase[indice] == '4':
    saida.append('....-')
  elif frase[indice] == '5':
    saida.append('.....')
  elif frase[indice] == '6':
    saida.append('-....')
  elif frase[indice] == '7':
    saida.append('--...')
  elif frase[indice] == '8':
    saida.append('---..')
  elif frase[indice] == '9':
    saida.append('----.')
  elif frase[indice] == '.':
    saida.append('.-.-.-')
  elif frase[indice] == ',':
    saida.append('--..--')
  elif frase[indice] == '?':
    saida.append('..--..')

  indice = indice + 1
  
print(' '.join(saida))
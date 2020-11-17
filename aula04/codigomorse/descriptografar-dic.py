# Descriptografar
# O dicionário funciona bem no sentido literal. Basicamente um tradutor para o caractere setado 
dicionario = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
              '-..': 'D',      '.': 'E',   '..-.': 'F',
              '-.': 'G',   '....': 'H',     '..': 'I',  
              '.---': 'J',    '-.-': 'K',   '.-..': 'L',
              '--': 'M',     '-.': 'N',    '---': 'O', 
              '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
              '...': 'S',      '-': 'T',    '..-': 'U', 
              '...-': 'V',    '.--': 'W',   '-..-': 'X',
              '-.--': 'Y',   '--..': 'Z',  '-----': '0', 
              '.----': '1',  '..---': '2',  '...--': '3',
              '....-': '4',  '.....': '5',  '-....': '6', 
              '--...': '7',  '---..': '8',  '----.': '9'}

print('Use / para substituir os espaços.\nEx: --- .-.. .- / -- ..- -. -.. ---\n')

texto = input('Digite um texto para ser descriptografado: ')              
saida = []
caractere = []
j = -1

for i in texto.split(' / '):
    j = j + 1
    caractere = caractere + [i.split(' ')]

    for k in range(len(caractere[j])):
        saida += dicionario.get(caractere[j][k], '?') # get é usado para pegar os valores definidos no dicionário, caso esse valor não esteja definido ele irá exibir a chave setada, no caso '?'
    saida += ' '

print('') # Quebra de linha
print(''.join(saida)) # .join para entrar dentro do array
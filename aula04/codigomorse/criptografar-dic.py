# Criptografar
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
              '--...': '7',  '---..': '8',  '----.': '9',
              '/': ' '}

# Inverter dicionário
dicionarioInverso = {}
for k, v in dicionario.items():
  dicionarioInverso[v] = dicionarioInverso.get(v, []) + [k]

texto = input('Digite um texto para ser criptografado: ')

saida = []

for caractere in texto:
  saida = saida + dicionarioInverso[caractere.upper()] 

print(' '.join(saida))
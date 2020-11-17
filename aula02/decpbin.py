numeroBinario = [] # Vetor representando número binário
numeroDecimal = 45
numero = numeroDecimal
dividido = int(numero / 2)

while dividido != 0:
  diferenca = numero  - (dividido * 2)
  numeroBinario.append(diferenca) # Colocar na ultima posição do numeroBinario a diferença
  numero = dividido
  print(numero)
  dividido = int(numero / 2)

numeroBinario.append(dividido + 1)

# Ao contrário pode ser numerBinario = numeroBinario[::-1] - Irá inverter o print

resultado = []
i = len(numeroBinario)

while i > 0:
  resultado.append(numeroBinario[i - 1])
  i = i - 1

print('\nO número decimal', numeroDecimal, 'convertido para binário vale:', resultado)
#memória
numRegistros=11
registradores = []#inicialmente utilizaremos de R0 até R10
acumulador = [] #usar somente a posição 0(zero)
#abre o arquivo com os comandos para executar
entrada = open('aula08\exercicio.txt')
programa = entrada.readlines()


controle = 1 #indica qual o número da linha do programa está sendo executado

def inicializa():
  global registradores
  indice=0
  while indice < numRegistros:
    registradores.append(0)
    indice = indice + 1

def mostraMemoria():
  global registradores
  global acumulador
  indice =0
  print('ACCU:',acumulador)
  while indice < numRegistros:
    print('R'+str(indice),registradores[indice])#str(valor) converte valor para string
    indice = indice + 1

def trataSparam(sparam):
    if sparam.startswith('#'):#startswith testa se a string começa com ...
      #print('é um número')
      valor = sparam[1:] #valor a armazenar sem o '#'
      valor = int(valor)#converte o valor para número inteiro
      #print(valor)
    if sparam.startswith('R'):
      #print('é um registro')
      end = sparam[1:]#endereço do Registrador de origem tirando o 'R'
      end = int(end)#converte para inteiro
      valor_reg_origem = registradores[end]
      valor = valor_reg_origem
    return valor

'''
Método que executa as instruções a cada clock do sistema (uma instrução por clock no nosso exemplo)
Recebe como parâmetro o controle para identificar a linha do programa que deve executar
'''
def clock(controle):
  global registradores
  global acumulador
  instrucao = programa[controle-1]#controle - 1 pois o índice no vetor 'programa' inicia em zero!
  elementos = instrucao.split(' ')
  comando = elementos[0]
  if len(elementos)>1:
    pparam = elementos[1]
    if len(elementos)>2:
      sparam = elementos[2]
      print('comando:',comando,'1 param:',pparam,'2 param:',sparam)
    else:
      print('comando:',comando,'1 param:',pparam)
  else:
    print('comando:',comando)

  if comando == 'STORE':
    valor = trataSparam(sparam)    
    destino = pparam[1:] #onde vai ser armazenado o valor, sem o 'R'
    destino = int(destino)#valor do endereço do destino

    #operação de STORE
    registradores[destino] = valor

  #################################################################

  if comando == 'LOAD':
    print('carrega valor do registro->para um registro/para acumulador!')
    if len(elementos)>2:
      origem = int(sparam[1:])#retira o R do segundo parâmetro
      destino = int(pparam[1:])#retira o R do primeiro parâmetro
      
      #carregando da origem para o destino!
      registradores[destino]=registradores[origem]

    else:
      origem = int(pparam[1:])#retira o R do primeiro parâmetro

      #carregando da origem para o acumulador
      acumulador = registradores[origem]


  if comando == 'CMP':
    print('compara se iguais')
    posicao1=int(pparam[1:])#retiro o R do primeiro parâmetro
    valorA = registradores[posicao1]
    if sparam.startswith('#'):
      numero = int(sparam[1:])#segundo parâmetro era um número
    elif sparam.startswith('R'):
      destino = int(sparam[1:])
      numero = registradores[destino]
    if valorA == numero:
      print('são iguais')
      return controle+1 #manda executar a próxima linha
    else:
      print('não são iguais')
      return controle+2 #pula a próxima linha

  if comando == 'CME':
    print('compara se menor')    
    posicao1=int(pparam[1:])#retiro o R do primeiro parâmetro
    valorA = registradores[posicao1]
    if sparam.startswith('#'):
      numero = int(sparam[1:])#segundo parâmetro era um número
    elif sparam.startswith('R'):
      destino = int(sparam[1:])
      numero = registradores[destino]
    if valorA < numero:
      print('valorA é menor')
      return controle+1 #manda executar a próxima linha
    else:
      print('valorA não é menor')
      return controle+2 #pula a próxima linha

  if comando == 'CMA':
    print('compara se maior ')
    posicao1=int(pparam[1:])#retiro o R do primeiro parâmetro
    valorA = registradores[posicao1]
    if sparam.startswith('#'):
      numero = int(sparam[1:])#segundo parâmetro era um número
    elif sparam.startswith('R'):
      destino = int(sparam[1:])
      numero = registradores[destino]
    if valorA > numero:
      print('valorA é maior')
      return controle+1 #manda executar a próxima linha
    else:
      print('valorA não é maior')
      return controle+2 #pula a próxima linha
  #################################################################

  if comando == 'ADD':
    valor = trataSparam(sparam)
    destino = pparam[1:]
    destino = int(destino)

    #operacao de ADD
    registradores[destino] = registradores[destino]+valor

  if comando == 'SUB':
    valor = trataSparam(sparam)
    destino = pparam[1:]
    destino = int(destino)

    #operacao de SUB
    registradores[destino] = registradores[destino]-valor

  if comando == 'MULT':
    valor = trataSparam(sparam)
    destino = pparam[1:]
    destino = int(destino)

    #operacao de MULT
    registradores[destino] = registradores[destino]*valor

  if comando == 'DIV':  
    valor = trataSparam(sparam)
    destino = pparam[1:]
    destino = int(destino)

    #operacao de DIV
    registradores[destino] = registradores[destino]/valor

  if comando == 'JMP':
    destino = int(pparam)
    return destino #DESTINO É A LINHA PARA QUAL O PROGRAMA IRÁ PULAR!
    print('Jump')
  
  return 0

inicializa()
mostraMemoria()

#EXECUTA TODAS AS LINHAS DO PROGRAMA

while controle <= len(programa):

  retorno = clock(controle)
  mostraMemoria()
  if retorno != 0:
    controle = retorno - 1
  controle = controle + 1
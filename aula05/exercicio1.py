'''
Considere o número 3.256.102

Escreva por extenso a quantidade de milhões
 Escreva por extenso a quantidade de milhares
'''

numero = '3.256.102'

valores = numero.split('.')
milhoes = valores[0]
milhares = valores[1]
centenas = valores[2]

numeroPorExtenso = {'1':'um','2':'dois','3':'três','4':'quatro','5':'cinco','6':'seis','7':'sete','8':'oito','9':'nove'}

# Para escrever por extenso os milhões:
print(numeroPorExtenso[milhoes], 'milhões')


centenaPorExtenso = {'1':'cento','2':'duzentos','3':'trezentos','4':'quatrocentos',
                     '5':'quinhentos','6':'seiscentos','7':'setecentos','8':'oitocentos','9':'novecentos'}

dezenaPorExtenso = {'1':'?','2':'vinte','3':'trinta','4':'quarenta',
                '5':'cinquenta','6':'sessenta','7':'setenta','8':'oitenta','9':'noventa'}

dezenas = {'10':'dez','11':'onze','12':'doze','13':'treze','14':'quatorze','15':'quinze','16':'dezesseis',
           '17':'dezessete','18':'dezoito','19':'dezenove'}

if milhares[1] == '1':
  duasUltimasCasas = milhares[1] + milhares[2]
  print(centenaPorExtenso[milhares[0]],'e',dezenas[duasUltimasCasas])

else:
  print(centenaPorExtenso[milhares[0]],',',dezenaPorExtenso[milhares[1]],',',numeroPorExtenso[milhares[2]])
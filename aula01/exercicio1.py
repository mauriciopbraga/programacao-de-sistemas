# Solicitar ao usuário o ano que ele nasceu e mostrar se o usuário é maior ou menor de idade

ano = (int(input("Digite o ano que nasceu: "))); # Entrada de dados (É Possível também converter para inteiro usando "ano = int(ano)")

# Cálculo para descobrir a idade
idade = 2020 - ano;

if idade >= 18:
  print("Você tem {} anos. Você é maior de idade!" .format(idade));
else:
  print("Você tem {} anos. Você é menor de idade!" .format(idade));
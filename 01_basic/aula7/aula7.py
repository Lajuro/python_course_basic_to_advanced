# 20 - Introdução à formatação de Strings

nome = 'Roberto Camargo'  # String
idade = 25  # Integer
altura = 1.70  # Float
peso = 82.0  # Float
e_maior = idade > 18  # Boolean
imc = float("{:.2f}".format(peso / altura ** 2))

print(f"{nome} tem {idade} anos de idade e seu IMC é {imc}!")
print("{nome} tem {idade} anos de idade e seu IMC é {imc}!".format(nome=nome, idade=idade, imc=imc))

# 18 - Variáveis

"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Roberto Camargo'  # String
idade = 25  # Integer
altura = 1.70  # Float
peso = 82.0  # Float
e_maior = idade > 18  # Boolean
imc = float("{:.2f}".format(peso / altura ** 2))

print(f"{nome} tem {idade} anos de idade e seu IMC é {imc}!")

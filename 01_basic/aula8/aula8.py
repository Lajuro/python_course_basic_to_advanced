"""
* Criar variáveis para nome (str), idade (int),
  altura (float) e peso (float) de uma pessoa

* Criar variável com o ano atual (int)

* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)

* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)

* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

# 1 - Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa

nome = 'Roberto Camargo'
idade = 25
altura = 1.70
peso = 82.0

# 2 - Criar variável com o ano atual (int)

ano_atual = 2021

# 3 - Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)

ano_nascimento = ano_atual - idade

# 4 - Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)

imc = float(f"{(peso / altura ** 2):.2f}")

# 5 - Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é de {imc}.")
print(f"{nome} nasceu em {ano_nascimento}.")


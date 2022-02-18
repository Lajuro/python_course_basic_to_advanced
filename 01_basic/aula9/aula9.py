"""
Entrada de Dados - Aula 9
"""

nome = input("Qual o seu nome?\n-> ")
idade = input("Qual a sua idade?\n-> ")

ano_nascimento = 2022 - int(idade)

print(f"\nO seu nome é {nome}!")
print(f"A sua idade é {idade}!")
print(f"Você possivelmente nasceu entre {ano_nascimento - 1} e {ano_nascimento}!")

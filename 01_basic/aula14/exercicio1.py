"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o 
usuário não digite um número inteiro, informe que não é um número inteiro.
"""

print("Exercício: Verificar se o número é inteiro, se for, verificar se é par ou ímpar\n")

numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    ehPar = numero % 2 == 0

    if ehPar:
        print("É par!")
    else:
        print("É ímpar!")

else:
    print("Não é um número inteiro!")

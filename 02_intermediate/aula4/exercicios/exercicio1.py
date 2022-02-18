"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada
"""


def funcao1(callback):
    callback()


def funcao2():
    print("A função 2 foi executada!")


funcao1(funcao2)

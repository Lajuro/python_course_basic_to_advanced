"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1
executar duas funções que recebam um número diferente de argumentos.
"""

def funcao1(callback):
    callback(5, 2, 3)
    callback(20, 35, 15, 10, 15, 5)


def soma(*args):
    total = 0
    for num in args:
        total += num
    print(f'TOTAL: {total}')


def exibe_valores(*args):
    print(args)


funcao1(soma)
funcao1(exibe_valores)

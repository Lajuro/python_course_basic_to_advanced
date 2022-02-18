"""
3 - Crie uma função que recebe 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o
valor do primeiro número somado do aumento do percentual do mesmo.
"""


def bonus(valor=0.00, percentual=100):
    percentual = percentual / 100
    return valor + (valor * percentual)


print(bonus(10.50, 30))

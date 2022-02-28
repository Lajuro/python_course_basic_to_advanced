"""
Funções decoradoras e decoradores
"""


def master(funcao):
    def executor(*args, **kwargs):

        if funcao.__name__ == 'soma':
            print(f"Somando os números: {' + '.join([str(numero) for numero in args])}")

        return funcao(*args, **kwargs)
    return executor


@master
def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero

    return total


resultado = soma(1, 2, 4, 5, 6)
print(resultado)

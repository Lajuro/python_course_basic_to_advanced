"""
Geradores, Iteradores e Iteráveis em Python
iter() - Transforma em um iterável strings, tuplas, dicionários, listas e sets
next() - Vai para o próximo item da lista

"""

# Exemplo com next() quando uma lista é um iter()
lista = [0, 1, 2, 3, 4, 5]
lista = iter(lista)

print(next(lista))  # [0]
print(next(lista))  # [1]
print(next(lista))  # [2]
print(next(lista))  # [3]
print(next(lista))  # [4]
print(next(lista))  # [5]

print(hasattr(lista, '__next__'))


def gerador():
    # Exemplo com geradores
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


resultado = gerador()

for valor in resultado:
    print(valor)

# Criar um gerador
gerador = (x for x in range(1000))
for v in gerador:
    print(v)

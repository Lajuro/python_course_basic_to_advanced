"""
Funções Lambda (Funções anônimas) - Parte 5
"""


def multiplicar(x, y):
    return x * y


print("Função convencional:", multiplicar(10, 5))

# Não é uma boa prática criar uma expressão lambda que possui uma variável, convencionalmente são anônimas
multiplicar_lambda = lambda x, y: x * y

print("Lambda:", multiplicar_lambda(10, 5))

# Sem função
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
lista.sort()  # Não mudou nada, pois não soube como ordenar.
print(lista)

# Com função
def func(item):
    return item[1]

lista.sort(key=func)
print(lista)  # Crescente
print(lista[::-1])  # Decrescente

# Com lambda
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1])
print(lista)
"""
Count - Itertools
"""

from itertools import count

contador = count(start=9, step=-1)

for valor in contador:
    print(valor)

    if valor >= 10 or valor <= -10:
        break

indice = count(1)
lista_nomes = ['Luiz', 'João', 'Maria']
lista_nomes = zip(indice, lista_nomes)

print(list(lista_nomes))

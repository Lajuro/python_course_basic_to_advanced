"""
Reduce
"""

from functools import reduce
from dados import produtos, pessoas, lista

soma = reduce(lambda acumulador, valor: valor + acumulador, lista, 0)
print(f'Soma dos números da lista: {soma}')

media_preco_produto = round(reduce(lambda acumulador, produto: produto['preco'] + acumulador, produtos, 0) / len(produtos), 2)
print(f'Média do preço dos produtos: {media_preco_produto}')

media_idade_pessoas = round(reduce(lambda acumulador, pessoa: pessoa['idade'] + acumulador, pessoas, 0) / len(pessoas))
print(f'Média da idade das pessoas: {media_idade_pessoas}')


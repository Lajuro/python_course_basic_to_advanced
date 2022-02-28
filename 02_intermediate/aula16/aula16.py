"""
Map
"""

from dados import produtos, pessoas, lista

nova_lista = list(map(lambda x: x * 2, lista))
print(nova_lista)


def aumenta_preco(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto


print(produtos)
precos = list(map(aumenta_preco, produtos))
# precos = [
#     {
#         'nome': produto['nome'],
#         'preco': round(produto['preco'] * 1.05, 2)
#     } for produto in produtos
# ]
print(precos)



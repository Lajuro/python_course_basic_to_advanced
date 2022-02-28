"""
Filter
"""

from dados import produtos, pessoas, lista

# Lista
maior_5 = list(filter(lambda numero: numero > 5, lista))
# maior_5 = [numero for numero in lista if numero > 5]
print(maior_5)

# Produtos
barato = list(filter(lambda produto: produto['preco'] <= 10, produtos))
# barato = [produto for produto in produtos if produto['preco'] <= 10]
print(barato)

# Pessoas
pessoas_comeca_letra_e = list(filter(lambda pessoa: pessoa['nome'][0].lower() == 'e', pessoas))
# pessoas_comeca_letra_e = [pessoa for pessoa in pessoas if pessoa['nome'][0].lower() == 'e']
print(pessoas_comeca_letra_e)

# menor_18 = list(filter(lambda pessoa: pessoa['idade'] < 18, pessoas))
menor_18 = [pessoa for pessoa in pessoas if pessoa['idade'] < 18]
print(menor_18)

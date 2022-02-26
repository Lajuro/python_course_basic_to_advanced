"""
Zip  - Unindo iteráveis
Zip_longest - Itertools
"""

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro', 'Goiânia']
estados = ['SP', 'MG', 'BA', 'RJ']

cidades_estados = zip(indice, cidades, estados)
# cidades_estados_longest = zip_longest(indice, cidades, estados,fillvalue="UF")

print(list(cidades_estados))
# print(list(cidades_estados_longest))

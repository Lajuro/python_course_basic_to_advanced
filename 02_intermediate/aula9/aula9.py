"""
List Comprehension em Python
"""

# Listas que serão usadas
lista_pares = [2, 4, 6, 8, 10, 12, 14]
lista_nomes = ['Roberto', 'Gabriel', 'Maria', 'Antônio']
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
lista_100_numeros = list(range(100))

# Exemplo 1: A partir da lista_pares, criar uma lista com os valores dobrados de cada posição
lista_pares_dobrados = [valor * 2 for valor in lista_pares]
print('lista_pares_dobrados:', lista_pares_dobrados)

# Exemplo 2: A partir da lista_pares, criar uma lista de coordenadas utilizando dois loops for... in
lista_coordenadas = [(x, y) for x in lista_pares for y in range(3)]
print('lista_coordenadas:', lista_coordenadas)

# Exemplo 3: A partir da lista_nomes, criar uma nova lista com os nomes trocando a letra "A" por "@"
lista_nomes_arroba = [palavra.lower().replace('a', '@').capitalize() for palavra in lista_nomes]
print('lista_nomes_arroba:', lista_nomes_arroba)

# Exemplo 4: A partir da tupla criada, criar um dicionário com o "valor" de chave/valor como "chave" e a "chave" como
# "valor"
dicionario = dict([(y, x) for x, y in tupla])
print("dicionario:", dicionario)

# Exemplo 5: A partir da lista_100_numeros, criar outra lista com apenas os números divisíveis por 2
divisiveis_por_2 = [numero for numero in lista_100_numeros if numero % 2 == 0]
print("divisiveis_por_2:", divisiveis_por_2)
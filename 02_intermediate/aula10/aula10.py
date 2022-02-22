"""
Dictionary Comprehension (Compreensao de Dicionários)
"""

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

# Exemplo 1
exemplo1 = {x: y * 2 for x, y in lista}
print(exemplo1)

# Exemplo 2
exemplo2 = {(x + 1, y) for x, y in enumerate(range(0, 10))}
print(exemplo2)

# Exemplo 3
exemplo3 = {f'chave_{x}': x**2 for x in range(5)}
print(exemplo3)

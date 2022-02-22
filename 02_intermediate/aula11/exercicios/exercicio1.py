"""
Exercicio 1: Utilizando list comprehension para fazer a soma das compras do carrinho
"""

carrinho = []

carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 2', 30))
carrinho.append(('Produto 3', 50))

print(carrinho)

total = sum([float(preco) for produto, preco in carrinho])
print(total)

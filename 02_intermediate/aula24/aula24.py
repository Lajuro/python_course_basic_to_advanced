"""
Criação de pacotes próprios
"""

from vendas.calcula_precos import aumento, reducao

preco = 2.50

print(f'Aumento de 25% no preço {preco}: {aumento(preco, 25)}')
print(f'Redução de 25% no preço {preco}: {reducao(preco, 25)}')

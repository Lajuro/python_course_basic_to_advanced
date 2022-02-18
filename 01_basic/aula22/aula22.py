"""
For / Else em Python
"""

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.startswith("J"):
        print(f"{valor} começa com J")
    else:
        print(f"{valor} não começa com J")
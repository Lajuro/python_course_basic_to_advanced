"""
Exercício 1: Utilizando List Comprehension para fatiar uma string e depois juntando as listas por  "."
"""

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
step = 10

lista = [string[i: i + step] for i in range(0, len(string), step)]
print(lista)

string_pontos = '.'.join(lista)
print(string_pontos)

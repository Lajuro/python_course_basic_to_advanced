"""
Tuplas
São como as listas, porém são imutáveis
"""

# Formas de criar uma tupla
#        0  1  2  3  4
lista = (1, 2, 3, 4, 5)
lista2 = 1, 2, 3, 4, 5
print(lista, type(lista))
print(lista[3])

print(lista2, type(lista2))

# Adicionando uma tupla na outra
tupla_1 = 1, 2, 3, 'Roberto', False
tupla_2 = [1, 2, 4], 5, 8
tupla_3 = tupla_1 + tupla_2

# Tranformar uma tupla em lista
lista_tupla = list(tupla_3)
lista_tupla.append(500)
lista_tupla.append('José')

print(lista_tupla)


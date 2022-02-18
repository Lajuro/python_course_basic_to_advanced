"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

texto = "Valor"

lista = ['A', 'B', 'C', 'D', 'E', 'F']

lista[1] = "Roberto"
print(lista)

print(lista[1:4])

# Inverter lista
print(lista[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.append(7) # Adiciona ao fim da lista
l3 = l1 + l2
l3.insert(3, "banana")
l1.extend(l2) # Mesma coisa que a variável l3

l3.pop() # Remove o último elemento

print(l3)
print(l1)

#     0  1  2  3  4  5  6  7  8
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l4)

del(l4[0])

print(l4)

# Cria uma lista de 1 até 10
l5 = list(range(0, 15))
print(l5)

print(min(l5), max(l5))

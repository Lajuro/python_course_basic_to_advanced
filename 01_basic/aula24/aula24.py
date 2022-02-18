"""
Desempacotamento de listas em Python
"""

lista = [
    "João",
    "Pedro",
    "Maria",
    "Carla",
    "Felipe"
]

primeiro, *resto, ultimo = lista

print(primeiro)
print(resto)
print(ultimo)

print("\n ### Outra forma de desempacotar")

*primeiros, antepenultimo, penultimo, ultimo = lista

print(primeiros)
print(antepenultimo)
print(penultimo)
print(ultimo)

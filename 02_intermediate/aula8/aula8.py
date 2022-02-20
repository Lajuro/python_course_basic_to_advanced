"""
Sets em Python (Conjuntos)
# add (adiciona), update(atualiza), clear, discard
# union | (une)
# intersection & (Todos os elementos presentes em dois sets)
# difference - (Elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

A função set() remove elementos duplicados
"""

s1 = {1, 2, 3, 4, 5}

print(s1)

for v in s1:
    print(v)

print("\n### Métodos:")
set_vazio = set()
set_vazio.add(1)
set_vazio.add(2)
set_vazio.add(3)
print("Resultado após o add()", set_vazio)
set_vazio.discard(2)
print("Resultado após o discard()", set_vazio)

set_vazio.clear()
print("Resultado após o clear()", set_vazio)

set_vazio.update([3, 7, 9, 10], {5, 9, 10, 4})
print("Resultado após o update()", set_vazio)  # Observe que removeu os duplicados

print("\n### Usando símbolos | & - ^:")

new_set1 = {1, 2, 3, 4, 5, 7}
new_set2 = {1, 2, 3, 4, 5, 6}
union_set = new_set1 | new_set2
intersection_set = new_set1 & new_set2
difference_set = new_set1 - new_set2
symmetric_difference_set = new_set1 ^ new_set2


print('SET 1:', new_set1)
print('SET 2:', new_set2)

print("\nResultado após o union |", union_set)
print("Resultado após o intersection &", intersection_set)
print("Resultado após o difference -", difference_set)
print("Resultado após o symmetric_difference ^", symmetric_difference_set)



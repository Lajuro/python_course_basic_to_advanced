"""
Split, Join, Enumerate
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""

string = "O Brasil é o país do futebol, o país Brasil é o país penta."
lista_1 = string.split(" ")
lista_2 = string.split(",")

print(lista_1)
print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if (qtd_vezes > contagem):
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra {palavra} foi a que mais apareceu na frase, apareceu {contagem}x na frase.")

lista = ['O', 'Brasil', 'é', 'penta!']
string2 = ' '.join(lista)

print(string2)

for indice, valor in enumerate(lista):
    print(f'Índice: [{indice}] | Valor: {valor}')

lista_listas = [
    [1, 2, 3],
    [5, 6, 7],
    [10, 11, 12]
]

for lista_atual in lista_listas:
    print(lista_atual)
    for item_lista_atual in lista_atual:
        print(item_lista_atual)

# Desempacotamento

dados = ["Roberto", "Camargo", 21, 1.69, 80, "21/05/1996"]
nome, sobrenome, idade, altura, peso, nascimento = dados

print(nome, sobrenome, idade, altura, peso, nascimento)
"""
Faça um programa que peça o primeiro nome do usuário e exiba uma mensagem de acordo com as condições abaixo:

- Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto";
- Se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal";
- Se o nome tiver mais que 6 letras, escreva "Seu nome é muito grande".
"""

print("Exercício: Verifica o nome digitado e exibe uma mensagem de acordo com o seu tamanho.\n")

nome = input("Digite apenas o seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
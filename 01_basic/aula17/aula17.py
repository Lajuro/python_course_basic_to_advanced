"""
while em Python
Utilizado para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

print("Exemplo com loop WHILE")

continuar = True

while continuar:
    opcao = input("Deseja continuar o loop? [S/N]\n-> ")
    if opcao.upper() == "S":
        print("Continuando...")
    elif opcao.upper() == "N":
        print("Encerrando...")
        continuar = False
    else:
        print("Opção inválida, as opções válidas são S e N.")

print("Você saiu do loop!")

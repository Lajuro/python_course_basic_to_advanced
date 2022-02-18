"""
Documentação e funções built-in úteis
Acesse a documentação em https://docs.python.org/pt-br/3.9/library/stdtypes.html?highlight=isnumeric
"""

print("### Exemplo de Soma - Com erro ###")

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

if num1.isnumeric() and num2.isnumeric():
    print(f"O resultado da soma de {num1} + {num2} = {int(num1) + int(num2)}")
else:
    print("Não foi digitado um número válido!")

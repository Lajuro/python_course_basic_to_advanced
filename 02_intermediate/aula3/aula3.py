"""
Funções em Python - *args **kwargs - Parte 3
"""


def soma(*args):
    total = 0
    for num in args:
        total += num

    return total


resultado = soma(1, 2, 3, 4, 5)
print(resultado)


def keyword_arguments(**kwargs):
    print("<KWARGS>")
    if 'nome' in kwargs:
        print(f"\tOlá, {kwargs['nome']}!")

    if 'idade' in kwargs:
        print(f"\tFoi passado a idade, o valor informado foi: {kwargs['idade']}")

    print("</KWARGS>\n")


keyword_arguments(nome="Roberto Camargo", idade=15)
keyword_arguments(nome="Roberto Camargo")
keyword_arguments(idade=35)
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""


def saudacao(saudacao="Olá", nome="Fulano"):
    print(f"{saudacao}, {nome}!")


saudacao(nome="José")
saudacao(saudacao="Hey")
saudacao("Hola", "Alejandro")
saudacao()
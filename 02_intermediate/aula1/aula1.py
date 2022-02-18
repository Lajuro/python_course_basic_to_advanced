"""
Funções - def em Python (Parte 1)
"""


def saudacao(msg="Olá", nome="Fulano"):
    nome = nome.lower().replace('o', '0').replace('e', '3').replace('a', '4').replace('t', '7').replace('i', '1').upper()
    print(f"{msg}, {nome}!")


saudacao(nome='Roberto')
saudacao('Hallo', 'Pedro')
saudacao('Hello', 'Maria')
saudacao()

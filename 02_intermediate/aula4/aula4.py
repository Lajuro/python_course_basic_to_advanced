"""
Funções em Python - Escopo - Parte 4
"""

# Variável global
nome = "Roberto Camargo"


def funcao1():
    global nome  # Permite que mude o valor da variável global
    nome = "Pedro"
    print("funcao1", nome)

def funcao2():
    print("funcao2", nome)

def funcao3():
    # Variável local
    nome = "Carlos"
    print("funcao3", nome)


print("global", nome)
funcao3()
funcao2()
funcao1()
funcao3()
print("global", nome)

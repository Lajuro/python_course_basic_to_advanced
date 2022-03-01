"""
Herança Simples

Associação - Usa
Agregação - Tem
Composição - É dono
Herança - É
"""

from classes import *

cliente1 = Cliente('Roberto Camargo', 25)
print(cliente1.nome)
cliente1.falar()
cliente1.comprar()
print()

aluno1 = Aluno('José Pereira', 31)
print(aluno1.nome)
aluno1.falar()
aluno1.estudar()
print()

pessoa1 = Pessoa('João Silva', 29)
print(pessoa1.nome)
pessoa1.falar()
print()
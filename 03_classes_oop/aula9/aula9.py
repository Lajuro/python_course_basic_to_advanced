"""
Composição
É quando uma classe pertence a outra classe
"""

from classes import Cliente, Endereco

cliente1 = Cliente('Roberto Camargo', 25)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria Santos', 58)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João da Silva', 35)
cliente3.insere_endereco('Belo Horizonte', 'MG')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print(f"{'':#<50}\n")






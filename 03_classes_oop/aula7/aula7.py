"""
Associação
"""

from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Roberto Camargo')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)

escritor.ferramenta = caneta

escritor.ferramenta.escrever()  # Associação
maquina.escrever()

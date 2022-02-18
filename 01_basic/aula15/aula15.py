"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Flutuantes (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2
print('Format: {:.2f}'.format(divisao))
print(f'F Strings: {divisao:.2f}')

# Para que tenha 10 casas o número

print(f'{num1:->10}')
print(f'{num1:0>10.2f}')

#########################################

nome = 'Roberto Camargo'
segundo_nome = 'José da Silva'

print(f'{" " + nome + " ":#^50}')
print(f'{" " + nome:#>50}')
print(f'{nome + " ":#<50}')
print(f'{" " + segundo_nome + " ":#^50}')
# nome_formatado = pass

"""
Manipulação de arquivos
"""

# 1 - Modo não tão recomendável para manipulação de arquivos
# file = open('abc.txt', 'w+')
#
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# print(f"{' Lendo linhas ':#^50}")
# file.seek(0, 0)
# print(file.read())
# print(f"{'':#^50}")
#
# file.seek(0, 0)
# print(f"{file.readline()}", end='')
# print(f"{file.readline()}", end='')
# print(f"{file.readline()}", end='')
#
# file.seek(0, 0)
# print(file.readlines())
#
# file.close()

# 2 - Modo Python de manipulação de arquivos

import os

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

# Remove o arquivo
# os.remove('abc.txt')
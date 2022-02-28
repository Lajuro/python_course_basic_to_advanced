"""
Groupby - Itertools
"""

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'Cláudio', 'nota': 'D'},
    {'nome': 'Valéria', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'A'},
    {'nome': 'Bruna', 'nota': 'C'},
    {'nome': 'Vagner', 'nota': 'C'},
    {'nome': 'Moisés', 'nota': 'B'},
    {'nome': 'Nair', 'nota': 'A'},
    {'nome': 'Flávia', 'nota': 'D'},
    {'nome': 'Laís', 'nota': 'B'}
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    quantidade = 0
    alunos = []

    for aluno in valores_agrupados:
        alunos.append(aluno['nome'])
        quantidade += 1

    print(f'Agrupamento: {agrupamento} ({quantidade})')

    for aluno in alunos:
        print(f"\tAluno: {aluno}")



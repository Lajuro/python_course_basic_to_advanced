"""
Dicionários
dicionario.values() - Pega os valores do dicionario
dicionario.keys() - Pega as chaves do dicionário
dicionario.items() - Pega cada item (chave e valor) do dicionário
dicionario.copy() - Cria uma cópia de um dicionário, porém faz uma cópia rasa, pois ainda sim mantém a referência, não
funcionando ao tentar alterar valores de listas, para isso é necessário importar o múdulo "copy".

Importando copy pode usar deepcopy para ter uma real cópia, totalmente separado do dicionário copiado como referência.

dicionario.pop() - Exclui alguma chave/valor de acordo com o número informado no parâmetro, se não for passado o
parâmetro, exclui o último do dicionario.
"""

pessoa = {
    'nome': 'Roberto',
    'sobrenome': 'Camargo',
    'idade': 25,
    'nascimento': "21/05/1996",
    'estado_civil': "solteiro",
    'maior_idade': True
}

print(pessoa['nome'])
print(pessoa['maior_idade'])

print('Roberto' in pessoa.values())
print('estado_civil in pessoa.values()', 'estado_civil' in pessoa.values())
print('estado_civil in pessoa.keys()', 'estado_civil' in pessoa.keys())

for k in pessoa.items():
    print(k)

cliente = {
    'id': 1,
    'nome': 'João',
    'idade': 20
}

# Ao atribuir um dicionário a outra variável na verdade está sendo criado uma referência, então caso altere algum valor
# do dicionário, será mudado em ambos os lugares.
cliente2 = cliente

cliente2['id'] = 2 # Modificado na variável 'cliente2', porém reflete em ambos os dicionários.
cliente['nome'] = 'Pedro'  # Modificado na variável 'cliente', porém reflete em ambos os dicionários.

print(cliente)
print(cliente2)

cliente2 = cliente.copy()

cliente2['idade'] = 25

print(cliente)
print(cliente2)  # Como agora é uma cópia, reflete apenas o valor no dicionário criado com base no outro, e não nos dois
# pois deixou de ser uma referência e se tornou uma cópia, com sua própria localização na memória.

"""
Faça uma lista de tarefas com as seguintes opções:
    Adicionar tarefa
    Listar tarefa
    Opção de desfazer (A cada vez que chamarmos, desfaz a última ação)
    Opção de refazer (A cada vez que chamarmos, refaz a última ação)

    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer

    input <- Nova tarefa
"""

from time import sleep

lista_tarefas = []
lista_refazer = ["Ir ao banheiro"]


def mostra_opcoes():
    print('Selecione uma das opções abaixo:')
    print('[1] Criar tarefa')
    print('[2] Listar tarefas')
    print('[3] Refazer')
    print('[4] Desfazer')
    print('[5] Sair')


def seleciona_opcao():
    opcao_selecionada = input("\n-> ")
    opcoes_validas = ['1', '2', '3', '4', '5']
    if opcao_selecionada not in opcoes_validas:
        raise Exception('Opção inválida')

    return opcao_selecionada


def cria_tarefa():
    global lista_tarefas
    while True:
        try:
            print('[INFO] Digite ":q" para sair sem criar uma tarefa\n')
            tarefa = input("Tarefa -> ")
            print(tarefa)

            if tarefa == "":
                raise Exception("É necessário informar alguma coisa como tarefa.")

            if tarefa == ':q':
                break
            else:
                lista_tarefas.append(tarefa)
                print(f'\t[SUCESSO] Tarefa "{tarefa}" criada com sucesso!\n')

        except Exception as erro_criar_tarefa:
            print(f"\n[ERRO] {erro_criar_tarefa}\n")


def listar_tarefas():

    if len(lista_tarefas) == 0:
        print('\t[INFO] Não existem tarefas criadas no momento\n')
    else:
        contador = 1
        print("## Tarefas ##\n")
        for tarefa in lista_tarefas:
            print(f'[{contador}] {tarefa}')
            contador += 1
        print("\n#############\n")
        sleep(2)


def refazer():
    if not lista_refazer:
        print("\t[INFO] Não há nada a refazer.\n")
    else:
        ultimo_item = lista_refazer.pop()
        lista_tarefas.append(ultimo_item)
        print(f'\t[SUCESSO] A tarefa "{ultimo_item}" foi adicionada de volta a lista.\n')


def desfazer():
    if not lista_tarefas:
        print(f'\t[INFO] Não há nada para ser desfeito.\n')
    else:
        tarefa_retirada = lista_tarefas.pop()
        lista_refazer.append(tarefa_retirada)
        print(f'\t[SUCESSO] A tarefa "{tarefa_retirada}" foi retirada da lista de tarefas.\n')


while True:
    try:
        mostra_opcoes()
        opcao = seleciona_opcao()

        if opcao == '1':  # Criar tarefa
            print("\n[1] Criar tarefa\n")
            cria_tarefa()

        elif opcao == '2':  # Lista tarefas
            print("\n[2] Listar tarefas\n")
            listar_tarefas()

        elif opcao == '3':  # Refazer
            print("\n[3] Refazer\n")
            refazer()

        elif opcao == '4':  # Desfazer
            print("\n[4] Desfazer\n")
            desfazer()

        elif opcao == '5':  # Sair
            print("\n[5] Sair\n")
            print('Obrigado por utilizar a ferramenta de tarefas! Até logo!')
            break

    except Exception as erro_selecionar_opcoes:
        print(f"\n[ERRO] {erro_selecionar_opcoes}\n")
        sleep(2)

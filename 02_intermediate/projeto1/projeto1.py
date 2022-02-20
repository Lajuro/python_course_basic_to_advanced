"""
Sistema de Perguntas e Respostas com Dicionários em Python
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 x 2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10 x 1? ',
        'respostas': {'a': '10', 'b': '5', 'c': '20'},
        'resposta_certa': 'a'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1 - 5? ',
        'respostas': {'a': '-6', 'b': '4', 'c': '-4'},
        'resposta_certa': 'c'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 6 ÷ 2? ',
        'respostas': {'a': '12', 'b': '3', 'c': '2'},
        'resposta_certa': 'b'
    },

}

respostas_certas = 0
qtd_perguntas = len(perguntas)

for pergunta_chave, pergunta_valor in perguntas.items():
    print(f'\n{pergunta_chave}: {pergunta_valor["pergunta"]}')

    print('\nEscolha as opções abaixo:')
    for resposta_chave, resposta_valor in pergunta_valor['respostas'].items():
        print(f'[{resposta_chave}]: {resposta_valor}')

    opcoes_validas = ['a', 'b', 'c']

    while True:
        resposta_usuario = input('Resposta: ')

        if (resposta_usuario not in opcoes_validas):
            print('\n[ERRO] Opção inválida, deve ser somente a, b ou c!')
            continue
        else:
            if resposta_usuario == pergunta_valor['resposta_certa']:
                print(f"\n[SUCESSO] Você acertou, a resposta é {pergunta_valor['respostas'][pergunta_valor['resposta_certa']]}")
                respostas_certas += 1
            else:
                print(f"\n[FALHA] Você errou, a resposta certa era a \"[{pergunta_valor['resposta_certa']}]: {pergunta_valor['respostas'][pergunta_valor['resposta_certa']]}\"")
            break

porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f"\n[INFO] Você acertou: {respostas_certas} de {qtd_perguntas}")
print(f"[INFO] Sua porcentagem de acerto é de: {porcentagem_acerto:.0f}%")
print("\n[INFO] Acabou as perguntas, obrigado!")
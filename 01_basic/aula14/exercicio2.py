"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

print("Exercício: Pergunta qual o horário e responde de acordo, com uma saudação.\n")

hora = input("Digite um horário de 0 até 23: ")

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print(f"Foi informado um horário que não está entre 0 e 23, foi informado: {hora}")
    else:
        if hora <= 11:
            print(f"Bom dia!")
        elif hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
else:
    print(f"É necessário informar um número inteiro, foi informado {hora}")

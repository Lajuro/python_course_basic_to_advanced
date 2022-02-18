"""
While / Else
Contadores
Acumuladores
"""

contador = 0
acumulador = 0

while contador < 100:
    print(contador, acumulador)

    if (contador == 110):
        print("O contador chegou em 50!")
        break

    acumulador += contador
    contador += 1
else:
    print("[Mensagem do else] Sou executado apenas se a condição do loop for False.")

print("Acabou de executar")
if (contador < 100):
    print("A mensagem do else não foi mostrada pois o contador ainda é menor que 100.")
else:
    print("A mensagem do else foi mostrada porque a condição do loop já não é mais verdadeira.")
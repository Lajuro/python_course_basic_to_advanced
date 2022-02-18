"""
Iterando em strings com while em Python
"""

frase = "O rato roeu a roupa do rei de roma"
tamanho_frase = len(frase)

print(f"[FRASE] {frase}")
print(f"[TAMANHO DA FRASE] {tamanho_frase}")

isInvalid = True

while isInvalid:
    letra_para_mudar = input("Digite a letra que deseja mudar: ")

    if len(letra_para_mudar) > 1 or len(letra_para_mudar) < 1:
        print("Por favor, digite somente uma única letra [a-z]")
    elif not letra_para_mudar.isalpha():
        print("Por favor, digite uma letra [a-z], outros caracteres são inválidos.")
    else:
        letra_para_mudar = letra_para_mudar.lower()
        isInvalid = False

i = 0
nova_frase = ""
letra_encontrada = False

while i < tamanho_frase:
    letra = frase[i]
    if letra == letra_para_mudar:
        nova_frase += letra_para_mudar.upper()
        letra_encontrada = True
    else:
        nova_frase += letra
    i += 1

if not letra_encontrada:
    print(f"Não foi encontrado a letra {letra_para_mudar} para mudar.")
else:
    print(f"[NOVA FRASE] {nova_frase}")

print("Fim do Loop")
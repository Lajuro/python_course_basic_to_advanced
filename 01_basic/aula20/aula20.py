"""
For in em Python
Iterando strings com for
Função range (start=0, stop, step=1)
"""
texto = 'Python'

print("\nCom letra")
for letra in texto:
    print(letra)

print("\nCom índice e letra")
for n, letra in enumerate(texto):
    print(n, letra)

print("\nCom somente o fim")
for n in range(10):
    print(n)

print("\nCom começo e fim")
for n in range(1, 10):
    print(n)

print("\nCom começo, fim e step")
for n in range(1, 10, 2):
    print(n)

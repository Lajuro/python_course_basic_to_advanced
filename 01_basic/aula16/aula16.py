"""
Manipulando strings
* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...

Essas funções podem ser usadas diretamente em cada tipo.
"""

#  Para retirar a barra final
url = "https://www.google.com.br/"
print(url[:-1])

# Para fatiar uma string
#       [0123456789]
texto = "Amo Python"
novo_texto = texto[4:10]
print(novo_texto)

texto_inicio = texto[:3]
print(texto_inicio)

ultima_letra = texto[-1]
print(ultima_letra)

step_texto = texto[0:3:2]
print(step_texto)

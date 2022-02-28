"""
Try... Except.. - Tratando exceções em Python
"""

try:
    a = {}
    print(a[0])
except NameError as erro:
    print(erro)
except (IndexError, KeyError) as erro:
    print("Erro de índice ou chave")
except Exception as erro:
    print("Ocorreu um erro inesperado")
    print(erro)
    print(type(erro))
else:  # Executado quando o try foi executado sem erros.
    print('Seu código foi executado com sucesso')
finally:  # Com erro ou não, é sempre executado
    print("Terminou de rodar")

print("Continuando...")

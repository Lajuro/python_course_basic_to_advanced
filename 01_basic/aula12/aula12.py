"""
Quantidade de Caracteres
len()
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

MIN_CHARS = 6

print(f"{bcolors.OKCYAN}{bcolors.BOLD}################################")
print(f"### Quantidade de Caracteres ###")
print(f"################################{bcolors.ENDC}\n")

print(bcolors.HEADER + "# SISTEMA DE CADASTRO #\n")

usuario = input(f"{bcolors.OKBLUE}Usuário [{MIN_CHARS} caracteres mínimo]:{bcolors.ENDC} ")

if len(usuario) < MIN_CHARS:
    print(bcolors.FAIL + "\n[ERRO]", end=bcolors.ENDC + " ")
    print("Quantidade de caracteres inválido!", end=bcolors.ENDC + "\n")

    print(bcolors.WARNING + "[WARNING]", end=bcolors.ENDC + " ")
    print(f"Deve possuir no mínimo {MIN_CHARS} caracteres!", end=bcolors.ENDC + "\n")

else:
    print(bcolors.OKGREEN + "\n[SUCCESS]", end=bcolors.ENDC + " ")
    print(f'Usuário "{usuario}" cadastrado com sucesso!', end=bcolors.ENDC + "\n")




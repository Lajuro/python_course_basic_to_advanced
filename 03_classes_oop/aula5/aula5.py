"""
Atributos de Classe
"""


class A:
    vc = 123

    def __init__(self):
        self.vc = 321


a1 = A()
a2 = A()

print(a1.vc)  # Utiliza o atributo da classe se não tiver sido definido o valor na instância
print(a2.vc)  # Utiliza o atributo da classe se não tiver sido definido o valor na instância
print(A.vc)  # Utiliza o atributo da classe

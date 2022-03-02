"""
Herança Múltipla


Ordem de Herança

Tendo as classes A, B, C, D, sendo a classe A a principal, a qual é herda a classe B e C e a classe D tem a herança
múltipla de B e C.

1 - Busca dentro de si mesmo o método e atributo
2 - Se não achar e herda de duas ou mais classes, procura na ordem dos parâmetros passados, ou seja, da esquerda para a
    direita.
    Exemplo:
    class D(B, C)

    - Vai buscar primeiro na classe D, se não achar, vai ver na B e se não achar, vai ver na C.
3 - Caso não ache nas classes dos parâmetros, vai olhar dentro da herança de alguma das classes.

    Exemplo:

    class A() [Como a classe B ou a C herda de A, se encontrar aqui irá utilizar o que foi encontrado aqui.]
        ...

    class B(A) [Não encontrou aqui]
        ...

    class C(A) [Não encontrou aqui]
        ...

    class D(C, B) [Não encontrou aqui]
        ...

    - Como não encontrou dentro de si mesmo, vai olhar então na classe C, se não achou, vai procurar na B, caso não
    achou também, vai procurar na classe que alguma das duas possui herança, que no caso é a classe A, se encontrar na
    classe A, vai executar o que encontrou.

4 - Caso dentro da classe D tenha o método ou atributo que está sendo chamado, e nele é passado a chamada de outra
    classe, será executado na ordem que for passado.

5 - Se for passado dentro da classe D o método super(), vai utilizar o método ou atributo encontrado na primeira classe
    passada como parâmetro.
"""


class A:
    def falar(self):
        print("Falando... Estou em A.")


class B(A):
    def falar(self):
        print("Falando... Estou em B")
    pass


class C(A):
    def falar(self):
        print("Falando... Estou em C")
    pass


class D(B, C):
    def falar(self):
        super().falar()  # Vai chamar o método falar da classe B, passada no parâmetro da classe | class D(B, C):
        print("\tFalando... Estou em D")
    pass


d = D()
d.falar()

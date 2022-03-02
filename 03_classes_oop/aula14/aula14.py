"""
Polimorfismo
É o princípio pelo qual duas ou mais classes derivadas de uma mesma superclasse podem invocar métodos que
têm a mesma identificação (assinatura) mas comportamentos distintos, especializados para cada classe derivada, usando
para tanto uma referência a um objeto do tipo da superclasse.
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg): pass


class B(A):
    def falar(self, msg):
        print(f'B está falando sobre {msg}')


class C(A):
    def falar(self, msg):
        print(f'C está falando sobre {msg}')


b = B()
c = C()

b.falar('um assunto')
c.falar('outro assunto')
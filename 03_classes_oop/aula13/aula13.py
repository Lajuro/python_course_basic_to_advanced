"""
Classes Abstratas
É um tipo de classe especial que não pode ser instanciada, apenas herdada.
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print("Falando... B...")


# a = A()
# a.falar()
# [ERROR] TypeError: Can't instantiate abstract class A with abstract method falar

b = B()
b.falar()

"""
Em Python, tudo é um objeto: Incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!???)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Você precisa criar um método b_fala na classe {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não um atributo da classe {name}.')

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr = 'Valor'

    def fala(self):
        self.b_fala()


class B(A):
    # b_fala = 'Olá'

    @staticmethod
    def b_fala():
        print('Class B está falando...')

    def sei_la(self):
        pass


# a = A()
# b = A()
# c = A()
#
# print(a.attr)
# print(b.attr)
# print(c.attr)
#
#
b = B()
b.b_fala()
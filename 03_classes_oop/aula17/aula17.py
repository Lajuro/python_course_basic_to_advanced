"""
Métodos Mágicos
https://rszalski.github.io/magicmethods/
"""


class A:

    def __new__(cls, *args, **kwargs):
        print("Eu sou o new")
        cls.nome = "Roberto Camargo"

        def haha(*args, **kwargs):
            print('Ha ha')

        cls.haha = haha

        return object.__new__(cls)

    def __init__(self):
        print('Eu sou INIT')


class B:
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self):
        print('Eu sou INIT')


class C:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def __setattr__(self, key, value):
        print('Foi criado um novo atributo!')
        print(key, value)
        self.__dict__[key] = value


a = A()
print(a.nome)
a.haha()

b = B()
b2 = B()
b3 = B()

c = C()

c(1, 2, 3, 4, 5, 6, nome="Roberto")

c.nome = "Roberto Camargo"
print(c.nome)

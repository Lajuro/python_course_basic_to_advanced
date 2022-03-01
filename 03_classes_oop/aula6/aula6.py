"""
Encapsulamento
public - Métodos e atributos que podem ser acessados dentro e fora da classe
protected (_)- Métodos e atributos que podem ser acessados somente dentro da classe e pelas filhas da classe
private (__) - Métodos e atributos que pode ser acessado apenas dentro da própria classe
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        print(f"\n{' Base de Clientes ':#^40}")
        for id, nome in self.__dados['clientes'].items():
            print(f'[{id}] {nome}')
        print(f"{'':#^40}\n")

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Roberto')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

bd.lista_clientes()

bd.apaga_cliente(3)

bd.lista_clientes()

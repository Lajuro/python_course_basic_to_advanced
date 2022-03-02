from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser númerico")

        self._saldo = round(valor, 2)

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do depósito precisa ser númerico")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'{" Detalhes da Conta ":#^30}')
        print(f'Agência: {self.agencia}')
        print(f'Conta..: {self.conta}')
        print(f'Saldo..: {self.saldo:.2f}')
        print(f'{"":#^30}\n')

    @abstractmethod
    def sacar(self, valor):
        pass


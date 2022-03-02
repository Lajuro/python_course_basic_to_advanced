from classes.Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Limite precisa ser númerico")

        self._limite = valor

    def detalhes(self):
        print(f'{" Detalhes da Conta Corrente ":#^30}')
        print(f'Agência: {self.agencia}')
        print(f'Conta..: {self.conta}')
        print(f'Saldo..: {self.saldo:.2f}')
        print(f'Limite.: {self.limite:.2f}')
        print(f'{"":#^30}\n')

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente!')
            return

        self.saldo -= valor
        self.detalhes()

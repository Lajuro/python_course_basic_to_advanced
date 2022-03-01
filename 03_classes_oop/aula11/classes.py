class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse} falando...")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeclasse} está comprando!")

    def falar(self):
        print(f"Estou falando da classe Cliente, meu nome é {self.nome}")


class ClienteVIP(Cliente):

    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def comprar(self):
        super().comprar()
        print(f"{self.nomeclasse} está comprando com desconto, porque ele é VIP!")
              
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome} está falando!')


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nomeclasse} está estudando!")

from classes.ContaPoupanca import ContaPoupanca
from classes.ContaCorrente import ContaCorrente

conta_poupanca = ContaPoupanca(1111, 2222, 0)

conta_poupanca.depositar(10)
conta_poupanca.depositar(60)
conta_poupanca.depositar(30)
conta_poupanca.sacar(40)
conta_poupanca.sacar(70)

conta_corrente = ContaCorrente(3333, 3333, 0)
conta_corrente.depositar(10)
conta_corrente.depositar(60)
conta_corrente.depositar(30)
conta_corrente.sacar(40)
conta_corrente.sacar(70)
conta_corrente.sacar(70)
conta_corrente.sacar(20)
conta_corrente.sacar(10)
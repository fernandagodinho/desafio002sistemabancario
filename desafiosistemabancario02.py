
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

    def extrato(self):
        print(f"Titular: {self.titular}\nSaldo: R${self.saldo:.2f}")

# Exemplo de uso:
conta = ContaBancaria('João Silva')
conta.depositar(100)
conta.sacar(50)
conta.extrato()


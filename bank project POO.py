import time

class BankAccount:
    def __init__(self):
        self.balance = 0.0
        self.statement = []

    def deposit(self, deposit_value=None):
        if deposit_value is None:
            deposit_value = float(input('Valor de depósito: '))
        self.balance += deposit_value
        self.statement.append(f'Depósito: +R${deposit_value}')
        return self.balance

    def withdraw(self, withdraw_value=None):
        if withdraw_value is None:
            withdraw_value = float(input('Valor de saque: '))

        if withdraw_value <= self.balance:
            self.balance -= withdraw_value
            self.statement.append(f'Saque: -R${withdraw_value}')
            return self.balance
        else:
            print('Operação inválida. Saldo insuficiente.')
            return self.balance

print(''' OPÇÕES:
[1] DEPÓSITO
[2] SAQUE
[3] SALDO
[4] EXTRATO
[5] FECHAR
''')

account = BankAccount()

while True:
    option = int(input("Escolha a opção que deseja efetuar: "))
    
    if option == 1:
        deposit_amount = float(input('Valor de depósito: '))
        balance = account.deposit(deposit_amount)
        print(f'Operação realizada. Saldo atual: {balance}')

    elif option == 2:
        withdraw_amount = float(input('Valor de saque: '))
        balance = account.withdraw(withdraw_amount)
        print(f'Operação realizada. Saldo atual: {balance}')

    elif option == 3:
        print(f'Saldo atual: {account.balance}')

    elif option == 4:
        print('Extrato:')
        for transaction in account.statement:
            print(transaction)

    elif option == 5:
        print('Finalizando sessão...')
        time.sleep(2)
        break

    else:
        print('Opção inválida. Tente novamente.')
        print('Finalizando sessão...')
        time.sleep(2)
        break
import time
statement = []
def deposit(balance, deposit_value = None):
    if deposit_value is None:
        deposit_value = float(input('Valor de depósito: '))
    new_balance = balance + deposit_value
    statement.append(f'Depósito: +R${deposit_value}')
    return new_balance
def withdraw(balance, withdraw=None):
    if withdraw is None:
        withdraw_value=float(input('Valor de saque: '))
        if withdraw_value<=balance:
            new_balance = balance - withdraw_value
            statement.append(f'Saque: -R${withdraw_value}')
            return new_balance
        else:
            print('operação invalida, tente novamente...')
            print('finalizando seção...')
            time.sleep(5)
# Initialize balance
balance = 0.0

print(''' OPÇÕES:
[1] DEPOSITO
[2] SAQUE
[3] SALDO
[4] EXTRATO
[5] FECHAR
''')
while True:
    option = int(input("Escolha a opção que deseja efetuar:"))
    if option == 1:
        balance = deposit(balance)
        print(f'Operação realizada, saldo atual: {balance}')
    if option == 2:
        balance = withdraw(balance)
        print(f'Operação realizada, saldo atual: {balance}')
    if option == 3:
        print(f'saldo atual: {balance}')
    if option == 4:
        print(f'''
--EXTRATO--
{('\n'.join(statement))}
Saldo atual:{balance}
''')
    if option == 5:
        print('finalizando seção...')
        time.sleep(5)
        break
    else:
        print('operação invalida, tente novamente...')
        print('finalizando seção...')
        time.sleep(5)
        break

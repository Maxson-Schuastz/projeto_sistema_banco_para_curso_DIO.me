print(''' OPÇÕES:
[1] DEPOSITO
[2] SAQUE
[3] SALDO
[4] EXTRATO
[5] FECHAR
''')
balance = float(0)
statement = []
while True:
    option = int(input())
    if option == 1:
        deposit = float(input('quanto quer depositar: '))
        if deposit>0:
            balance+=deposit
            print('operação realizada!')
            statement.append(f'Depósito: +R${deposit}')
        else:
            print('opção invalida tente novamente')
            break
    if option == 2:
        withdraw= float(input('quanto quer sacar: '))
        if withdraw>0 and balance >= withdraw:
            balance -= withdraw
            print('operação realizada!')
            statement.append(f'Saque: -R${withdraw}')
        else:
            print('opção invalida tente novamente')
            break
    if option == 3:
        print('saldo total:', balance)
    if option == 4:
        print(statement)
    if option ==5:
        break

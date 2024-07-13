import getpass
import os
import accounts
import money

while True:
    print(" ")
    print("*****************************************************")
    print("************ Caixa Eletrônico - MQS *****************")
    print("*****************************************************")
    account_typed = input("Insira sua Conta: ")
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts.account_list and password_typed == accounts.account_list[account_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("*****************************************************")
        print("************ Caixa Eletrônico - MQS *****************")
        print("*****************************************************")
        print(" ")
        print("************* Menu de opções ************************")
        print("1 - Saldo")
        if accounts.account_list[account_typed]['admin'] == False:
            print("2 - Deposito")
        print("3 - Saque")
        if accounts.account_list[account_typed]['admin']:
            print("10 - Incluir cédulas")
        print("*****************************************************")
        print(" ")
        name = accounts.account_list[account_typed]['name']
        print("Seja bem-vindo ao banco XPTO Sr(a) " + name)
        option_typed = input('Escolha uma das opções acima: ')
        print(" ")
        if option_typed == '1':
            print("Seu saldo é: R$ %s" % accounts.account_list[account_typed]['value'])

        elif option_typed == '2' and accounts.account_list[account_typed]['admin'] == False:
            amount_type = input("Digite valor do deposito: R$ ")
            print(" ")
            print("Saldo Anterior: R$ %s" % accounts.account_list[account_typed]['value'])
            accounts.account_list[account_typed]['value'] += int(amount_type)
            print("Saldo atualizado: R$ %s" % accounts.account_list[account_typed]['value'])

        elif option_typed == '3':
            value_type = input("Digite valor do saque: R$ ")
            value_int = int(value_type)

            if value_int // 100 > 0 and value_int // 100 <= money.money_slips['100']:
                money.money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money.money_slips['50']:
                money.money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money.money_slips['20']:
                money.money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print("O caixa não tem cédulas disponíveis para este valor!")
                print(" ")
            else:
                for money_bill in money.money_slips_user:
                    money.money_slips[money_bill] -= money.money_slips_user[money_bill]
                print("Pegue as notas: ")
                print(money.money_slips_user)

            print("Saldo Anterior: R$ %s" % accounts.account_list[account_typed]['value'])
            print("")
            if int(value_type) <= accounts.account_list[account_typed]['value']:
                accounts.account_list[account_typed]['value'] -= int(value_type)
            else:
               print("Saldo insuficiente para a operação!")
               print("")
            print("Saldo atualizado: R$ %s" % accounts.account_list[account_typed]['value'])

        elif option_typed == '10' and accounts.account_list[account_typed]['admin']:
            amount_type = input("Digite a quantidade de cédulas: ")
            money_bill_type = input("Digite o valor da tipo de cédulas: ")
            money.money_slips[money_bill_type] += int(amount_type)
            print(" ")

            print('Saldo Anterior R$ %s' % accounts.account_list[account_typed]['value'])
            accounts.account_list[account_typed]['value'] += int(amount_type) * int(money_bill_type)
            print('Saldo Atualizado R$ %s' % accounts.account_list[account_typed]['value'])
    else:
        print("Conta inválida!")

    print(" ")
    input('Precione <<ENTER>> para continuar')

    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)
    
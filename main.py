import getpass
import accounts

while True:
    print("*****************************************************")
    print("************ Caixa Eletrônico - MQS *****************")
    print("*****************************************************")
    account_typed = input("Insira sua Conta: ")
    password_typed = getpass.getpass('Digite sua senha: ')
    print("*****************************************************")
    print("*****************************************************")
    #print(account_typed)
    #print(password_typed)

    if account_typed in accounts.account_list and password_typed == accounts.account_list[account_typed]['password']:
        print("*****************************************************")
        print("************ Caixa Eletrônico - MQS *****************")
        print("*****************************************************")
        print("1 - Saldo")
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1':
            name = accounts.account_list[account_typed]['name']
            #print("Seu saldo é: " + accounts.account_list[account_typed]['value'])
            print("Seu saldo "+ name +" é: %s" % accounts.account_list[account_typed]['value'])
    else:
        print("Conta inválida!")



#Outra forma de fazer validação
#flag = False
#for account in accounts.account_list:
#    if account_typed == account['agency'] and password_typed == account['password']:
#        flag = True
#        print('Conta válida')
#if not flag:
#    print('Conta Inválida')
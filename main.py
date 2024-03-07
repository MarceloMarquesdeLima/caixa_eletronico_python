import getpass
import os
import accounts

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
        print("*****************************************************")
        print(" ")
        name = accounts.account_list[account_typed]['name']
        print("Seja bem-vindo ao banco XPTO Sr(a) " + name)
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1':
            #print("Seu saldo é: " + accounts.account_list[account_typed]['value'])
            print("Seu saldo é: R$ %s" % accounts.account_list[account_typed]['value'])
    else:
        print("Conta inválida!")

    input('Precione <<ENTER>> para continuar')

    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)




#Outra forma de fazer validação
#flag = False
#for account in accounts.account_list:
#    if account_typed == account['agency'] and password_typed == account['password']:
#        flag = True
#        print('Conta válida')
#if not flag:
#    print('Conta Inválida')

    # Outra forma de limpar tela
    #if os.name == 'nt': #Windows
    #    os.system('cls')
    #else:
    #    os.system("clear")
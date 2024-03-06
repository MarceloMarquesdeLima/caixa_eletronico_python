import getpass
import accounts

print("*****************************************************")
print("************ Caixa Eletrônico - MQS *****************")
print("*****************************************************")
account_typed = input("Insira sua Conta: ")
password_typed = getpass.getpass('Digite sua senha: ')
#print(account_typed)
#print(password_typed)
print("*****************************************************")
print("*****************************************************")

if account_typed in accounts.account_list and password_typed == accounts.account_list[account_typed]['password']:
    print("Conta válida!")
else:
    print("Conta inválida!")
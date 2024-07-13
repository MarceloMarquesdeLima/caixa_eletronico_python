import accounts
import getpass

def auth_account():
    account_typed = input("Insira sua Conta: ")
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts.account_list and password_typed == accounts.account_list[account_typed]['password']:
        return account_typed
    else:
        return False
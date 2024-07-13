import os

def limpar():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)
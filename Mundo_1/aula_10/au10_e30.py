# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

num = int(input(f"{bcolors.PINK}Me diga um número qualquer: {bcolors.ENDC}"))

if num % 2 == 0:
    print(f"O número {num} é {bcolors.BLUE}PAR{bcolors.ENDC}")
else:
    print(f"O número {num} é {bcolors.BLUE}ÍMPAR{bcolors.ENDC}")
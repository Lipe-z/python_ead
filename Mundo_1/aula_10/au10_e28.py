# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
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

from random import randint
from time import sleep

num = randint(0, 5)
print(f"{bcolors.YELLOW}-=-{bcolors.ENDC}" * 20)
print(f"{bcolors.CYAN}Vou pensar em um número entre 0 e 5. Tente adivinhar...{bcolors.ENDC}")
print(f"{bcolors.YELLOW}-=-{bcolors.ENDC}" * 20)

palpite = int(input("Em que número eu pensei? "))
print(f"{bcolors.PINK}PROCESSANDO...{bcolors.ENDC}")
sleep(1)
if palpite == num:
    print(f"{bcolors.GREEN}PARABÉNS! Você conseguiu me vencer!{bcolors.ENDC}")
else:
    print(f"{bcolors.RED}GANHEI! Eu pensei no número {num} e não no {palpite}!{bcolors.ENDC}")
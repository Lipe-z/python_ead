# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
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

velocidade = int(input("Qual é a velocidade atual do carro? "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"{bcolors.RED}MULTADO! Você excedeu o limite permitido que é de 80Km/h{bcolors.ENDC}")
    print(f"{bcolors.RED}Você deve pagar uma multa de{bcolors.ENDC} {bcolors.YELLOW}R${multa:.2f}{bcolors.ENDC}")
print(f"{bcolors.GREEN}Tenha um bom dia! Dirija com segurança!{bcolors.ENDC}")
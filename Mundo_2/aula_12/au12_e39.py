# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nasc = int(input("Em que ano você nasceu? "))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade < 18:
    print("\033[1;33mVocê ainda precisará se alistar ao serviço militar\033[0m")
elif idade == 18:
    print("\033[1;32mJá está na hora de se alistar ao serviço militar\033[0m")
else:
    print("\033[1;31mJá passou da hora de se alistar ao serviço militar\033[0m")
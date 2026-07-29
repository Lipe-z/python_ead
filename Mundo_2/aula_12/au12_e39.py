# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nasc = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade == 18:
    print(f"\033[1;32mJá está na hora de se alistar ao serviço militar\033[0m")
elif idade < 18:
    saldo = 18 - idade
    print(f"\033[1;33mQuem nasceu em {nasc} tem {idade} em {ano_atual} \nAinda faltam {saldo} anos para o alistamento\033[0m")
    print(f"\033[1;33mSeu alistamento será em {ano_atual + saldo}\033[0m")
else:
    saldo = idade - 18
    print(f"\033[1;31mQuem nasceu em {nasc} tem {idade} em {ano_atual} \nVocê ja deveria ter se alistado há {saldo} anos\033[0m")
    print(f"\033[1;31mSeu alistamento foi em {ano_atual - saldo}\033[0m")
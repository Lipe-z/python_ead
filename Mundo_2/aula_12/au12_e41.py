# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9anos: MIRIM
# - Até 14anos: INFANTIL
# - Até 19anos: JUNIOR
# - Até 20anos: SÊNIOR
# - Acima: MASTER
from datetime import date

nasc = int(input("Em que ano o atleta nasceu? "))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade <= 9:
    print("\033[1;36mMIRIM\033[0m")
elif idade <= 14:
    print("\033[1;36mINFANTIL\033[0m")
elif idade <= 19:
    print("\033[1;36mJUNIOR\033[0m")
elif idade == 20:
    print("\033[1;36mSÊNIOR\033[0m")
else:
    print("\033[1;36mMASTER\033[0m")

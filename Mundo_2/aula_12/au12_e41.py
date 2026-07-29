# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
from datetime import date

nasc = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nasc

print(f"O atleta tem \033[1;36m{idade} anos.\033[0m")
if idade <= 9: 
    print("Classificação: \033[1;36mMIRIM\033[0m")
elif idade <= 14:
    print("Classificação: \033[1;36mINFANTIL\033[0m")
elif idade <= 19:
    print("Classificação: \033[1;36mJUNIOR\033[0m")
elif idade == 25:
    print("Classificação: \033[1;36mSÊNIOR\033[0m")
else:
    print("Classificação: \033[1;36mMASTER\033[0m")

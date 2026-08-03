#Crie um programa que leia o ano de nascimento de SETE PESSOAS. No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.
from datetime import date

atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input(f"Em que ano a {pess}ª pessoa nasceu: "))
    idade = atual - nasc
    if idade >= 18:
       maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"E também tivemos {menor} pessoas menores de idade")

#Crie um programa que leia o ano de nascimento de SETE PESSOAS. No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.

maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input("Digite um ano de nascimento: "))
    idade = 2026 - ano
    if idade >= 18:
       maior += 1
    else:
        menor += 1
print(f"{menor} pessoas ainda não atingiram a maior idade")
print(f"{maior} pessoas já são maiores")
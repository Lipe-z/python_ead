#Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lidos.

maior = 0
menor = 0

for c in range(1, 6):
    num = float(input("Digite o peso da pessoa: "))

    if c == 1:
        maior = num
    else:
        if num > maior:
            maior = num

    if c == 1:
        menor = num
    else:
        if num < menor:
            menor = num
print(f"A pessoa mais pesada tem o peso de: {maior:.2f}Kg")
print(f"A pessoa mais leve tem o peso de : {menor:.2f}Kg")
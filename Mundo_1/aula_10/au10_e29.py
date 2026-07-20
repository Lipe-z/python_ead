# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Qual a velocidade você estava em km/h? "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"Você foi multado em R${multa:.2f}!")
else:
    print("Tudo certo")
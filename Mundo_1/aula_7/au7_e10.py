#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$5,20

real = float(input('Quanto dinheiro voce tem na carteira? R$'))

print(f'Com R${real:.2f} voce pode comprar US${real / 5.20:.2f}')
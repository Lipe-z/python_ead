#Faça um programa que leia o preço de um produto e diga seu valor a vista com 10% de desconto, 
#e pracelado com 8% de aumento.

preço = float(input('Qual é o preço do seu produto? R$ '))
a_vista = preço - (preço * 10/100)
parcelado = preço + (preço * 8/100)

print(f'Pagando a vista seu produto sai por R${a_vista:.2f}, e parcelando sai por R${parcelado:.2f}.')
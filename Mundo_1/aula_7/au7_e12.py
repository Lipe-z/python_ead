#Faça um algoritimo que leia o preço de um produto e mostre seu novo
#preço, com 5% de desconto.

preço = float(input('Qual é o preço do seu produto? R$ '))
novo = preço - (preço * 5/100)

print(f'Voce ganhou um desconto de 5%! Com desconto, seu produto sai por R${novo:.2f}')
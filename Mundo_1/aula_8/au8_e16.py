#Crie um programa que leia um número Real qualquer pelo teclado e 
#mostre na tela a sua porção Inteira. EX: 6.127 -> Parte inteira = 6
from math import trunc

num = float(input("Digite um número real: "))
print(f"A parte inteira de {num} é igual a {trunc(num)}")
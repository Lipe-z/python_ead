#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = 'Luis'
n2 = 'Brenda'
n3 = 'Jake'
n4 = 'Pandora'
lista = [n1, n2, n3, n4]
escolhido = shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
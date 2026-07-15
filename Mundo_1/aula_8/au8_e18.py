#Faça um programa que leia um ângulo qualquer e mostre na tela o 
#valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'O angulo de {angulo:.2f}° tem:\nO SENO de {seno:.2f}\nO COSSENO de {coss:.2f}\nE a TANGENTE de {tang:.2f} ')
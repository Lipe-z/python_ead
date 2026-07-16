#Faça um programa que leia um ângulo qualquer e mostre na tela o 
#valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

angulo_graus = int(input("Digite o ângulo que deseja: "))
angulo_radianos = radians(angulo_graus)

seno = sin(angulo_radianos)
print(f"O ângulo tem o seno: {seno:.2} ")
cosseno = cos(angulo_radianos)
print(f"O ângulo tem o cosseno: {cosseno:.2}")
tangente = tan(angulo_radianos)
print(f"O ângulo tem a tangente: {tangente:.2}")
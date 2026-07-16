#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#--Ex:
#Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

num = str(input("Digite um número entre 0 e 9999: "))

separar = list(num)
print(f"Unidade: {separar[3]}")
print(f"Dezena: {separar[2]}")
print(f"Centena: {separar[1]}")
print(f"Milhar: {separar[0]}")

#SÓ ESTÁ FUNCIONANDO COM NÚMEROS DE 4 DÍGITOS
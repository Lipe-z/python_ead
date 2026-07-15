#Escreva um programa que leia um valor em metros e o exiba convertido em
#centímetros e milímetros.

m = float(input('Uma distância em metros: '))
#cm = m * 100
#mm = m * 1000

print(f'{m} metros, equivalem a {m * 100:.0f}cm e {m * 1000:.0f}mm')
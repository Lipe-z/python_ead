#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
#(Calculo de °C para °F: °C x 1,8 + 32).

C = int(input('Qual sua temperatura atual em °C? '))
F = C * 1.8 + 32

print(f'{C}°C equivalem a {F:.1f}°F!')
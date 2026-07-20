# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas.

distancia = int(input("Quantos km tem sua viagem? "))

if distancia <= 200:
    print(f"Sua passagem custará R${distancia * 0.50:.2f}")
else:
    print(f"Sua passagem custará R${distancia * 0.45:.2f}")
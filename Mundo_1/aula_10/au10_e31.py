# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas.

distancia = float(input("Quantos é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia:.1f}Km.")

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"E o preço da sua passagem será de R${preco:.2f}")

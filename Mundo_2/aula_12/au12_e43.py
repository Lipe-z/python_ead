# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input("Qual é seu peso? (Kg): "))
altura = float(input("Qual é sua altura? (m): "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de \033[1;36m{imc:.1f}\033[0m")

if imc < 18.5:
    print("Você está \033[1;36mABAIXO DO PESO\033[0m normal")
elif 18.5 <= imc < 25:
    print("PARABÉNS, você está na faixa de \033[1;36mPESO IDEAL\033[0m")
elif 25 <= imc < 30:
    print("Você está em \033[1;36mSOBREPESO\033[0m")
elif 30 <= imc < 40:
    print("Você está em \033[1;36mOBESIDADE\033[0m cuidado!")
else:
    print("Você está em \033[1;36mOBESIDADE MÓRBIDA\033[0m cuidado!")

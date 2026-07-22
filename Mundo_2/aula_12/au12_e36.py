# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual é o valor da casa? R$"))
salario = float(input("Qual é o seu salário? R$"))
anos = int(input("Em quantos anos você pretende pagar? "))

meses = anos * 12
valor_parcela = valor_casa / meses
limite = salario * (30 / 100)

if valor_parcela <= limite:
    print("\033[1;32mEmpréstimo aceito\033[0m")
else:
    print("\033[1;31mEmpréstimo negado\033[0m")
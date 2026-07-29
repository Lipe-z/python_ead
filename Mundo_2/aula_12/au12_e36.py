# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))

valor_parcela = casa / (anos * 12)
limite = salario * (30 / 100)

if valor_parcela <= limite:
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${valor_parcela:.2f} \n\033[1;32mEmpréstimo pode ser CONCEDIDO!\033[0m")
else:
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${valor_parcela:.2f} \n\033[1;31mEmpréstimo NEGADO!\033[0m")
 
#Faça um algoritimo que leia o sálario de um funcionário e mostre
#seu novo sálario, com 15% de aumento.

salario = float(input('Qual é o seu sálario: R$'))
novo = salario + (salario * 15/100)
print(f'Você recebeu 15% de aumento, seu novo salário agora é de R${novo:.2f}!')

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# - À vista dinheiro/pix: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print("=========== LOJAS YUKKI ===========")
preco = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / PIX
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = preco - (preco * (10 / 100))
    print(f"Sua compra de R${preco} vai custar R${total:.2f} no final")
elif opcao == 2:
    total = preco - (preco * (5 / 100))
    print(f"O produto teve um desconto de 5%, saindo por R${total:.2f}")
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Sua compra será parcelda em 2x de {parcela:.2f} SEM JUROS")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc}x de {parcela:.2f} COM JUROS")
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente Novamente!')
print(f"Sua compra de R${preco} vai custar R${total:.2f} no final")
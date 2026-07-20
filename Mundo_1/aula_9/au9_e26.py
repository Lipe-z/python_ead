#Faça um programa que leia uma frase pelo teclado e mostre:
#--Quantas vezes aparece a letra "A".
#--Em que posição aparece a primeira vez.
#--Em que posição ela aparece a última vez.

frase = str(input("Digite sua frase: ")).strip().lower()

#Contar quantidade de "a"
print(f"A letra A aparece {frase.count("a")} vezes na frase")

#Posição que aparece a primeira vez
print(f"A primeira letra A apareceu na posição: {frase.find("a")+1}")

#Posição que aparece a última vez
print(f"A última letra A apareceu na posição: {frase.rfind("a")+1}")
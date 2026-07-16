#Crie um programa que leia o nome completo de uma pessoa e mostre:
#--O nome com todas as letras maiúsculas
#--O nome com todas minúsculas
#--Quantas letras ao todo (sem considerar espaços)
#--Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome: "))

#Maiúsculas e Minúsculas
print(f"Maiúsculas: {nome.strip().upper()}")
print(f"Minúsculas: {nome.strip().lower()}")

#Letras ao Todo
print(f"Contagem de caracteres: {len(nome.replace(" ", ""))}")

#Letras primeiro nome
dividir_nome = nome.split()
print(f"Contagem de caracteres (primeiro nome): {len(dividir_nome[0])}")
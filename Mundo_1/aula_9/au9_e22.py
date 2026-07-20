#Crie um programa que leia o nome completo de uma pessoa e mostre:
#--O nome com todas as letras maiúsculas
#--O nome com todas minúsculas
#--Quantas letras ao todo (sem considerar espaços)
#--Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()

#Maiúsculas e Minúsculas
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")

#Letras ao Todo
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")

#Letras primeiro nome
dividir_nome = nome.split()
print(f"Seu primeiro nome é {dividir_nome[0]} e ele tem {len(dividir_nome[0])} letras")
# print(f"Seu primeiro nome é {dividir_nome[0]} e ele tem {nome.find(' ')} letras") --ALTERNATIVA--
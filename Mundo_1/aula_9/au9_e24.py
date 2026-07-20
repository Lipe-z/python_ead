#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Em que cidade vc nasceu? ")).strip()
dividir_nome = cidade.split()
print("SANTO" in dividir_nome[0].upper())

# print(cidade[:5].upper() == "SANTO") --ALTERNATIVA--

# if "SANTO" in dividir_nome[0].upper():
#     print('Começa com "Santo"')
# else:
#     print('Não começa com "Santo"')
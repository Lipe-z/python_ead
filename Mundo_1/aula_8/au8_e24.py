#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Qual o nome da sua cidade? ')
primeiro_nome = cidade.upper().split()

if primeiro_nome[0] == 'SANTOS':
    print('Começa com "Santos"')
else:
    print('Não começa com "Santos"')
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0:
#     REPROVADO
# - Média entre 5.0 e 6.9:
#     RECUPERAÇÃO
# - Média 7.0 ou superior:
#     APROVADO

nt1 = float(input("Primeira nota: "))
nt2 = float(input("Segunda nota: "))
media = (nt1 + nt2) / 2

if media < 5.0:
    print(f"\033[1;31mTirando {nt1} e {nt2}, a média do aluno é {media}\033[0m")
    print("\033[1;31mO aluno foi REPROVADO\033[0m")
elif 7 > media >= 5:
    print(f"\033[1;33mTirando {nt1} e {nt2}, a média do aluno é {media}\033[0m")
    print("\033[1;33mO aluno está de RECUPERAÇÃO\033[0m")
else:
    print(f"\033[1;32mTirando {nt1} e {nt2}, a média do aluno é {media}\033[0m")
    print("\033[1;32mO aluno está APROVADO.\033[0m")
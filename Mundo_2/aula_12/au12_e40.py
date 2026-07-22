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
    print("\033[1;31mREPROVADO\033[0m")
elif 5.0 <= media <= 6.9:
    print("\033[1;33mRECUPERAÇÃO\033[0m")
else:
    print("\033[1;32mAPROVADO\033[0m")
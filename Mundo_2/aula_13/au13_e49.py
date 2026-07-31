#Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para ver sua tabuada: '))
for t in range(1, 11):
    print(f"{n} X {t} = {n * t}")
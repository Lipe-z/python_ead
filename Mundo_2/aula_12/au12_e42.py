# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equiláreto: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('\033[1;33m-=\033[0m' * 12)
print("\033[1;35mAnalisador de Triângulos\033[0m")
print('\033[1;33m-=\033[0m' * 12)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima \033[1;32mPODEM FORMAR\033[0m um triângulo", end=' ')
    if r1 == r2 == r3:
        print("\033[1;36mEQUILÁTERO\033[0m")
    elif r1 != r2 != r3 != r1:
        print("\033[1;36mESCALENO\033[0m")
    else:
        print("\033[1;36mISÓSCELES\033[0m")
else:
    print("Os segmentos acima \033[1;31mNÃO PODEM FORMAR\033[0m um triângulo")
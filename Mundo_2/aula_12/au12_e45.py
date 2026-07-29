# Crie um programa que faça o computador jogar JOKENPÔ com você.
from random import randint
from time import sleep
itens = ('Pedra 🪨', 'Papel 📄', 'Tesoura ✂️')

pc = randint(0, 2)
print("""Suas Opções
[ 0 ] PEDRA 🪨
[ 1 ] PAPEL 📄
[ 2 ] TESOURA ✂️""")
player = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")

print('-=' * 11)
print(f"Computador jogou {itens[pc]}")
print(f"Jogador jogou {itens[player]}")
print('-=' * 11)

if pc == 0: # computador jogou PEDRA
    if player == 0:
        print("EMPATE")
    elif player == 1:
        print("VITORIA DO JOGADOR")
    elif player == 2:
        print("VITORIA DO COMPUTADOR")
    else:
        print("JOGADA INVÁLIDA")
elif pc == 1: # computador jogou PAPEL
    if player == 0:
        print("VITORIA DO COMPUTADOR")
    elif player == 1:
        print("EMPATE")
    elif player == 2:
        print("VITORIA DO JOGADOR")
    else:
        print("JOGADA INVÁLIDA")
elif pc == 2: # computador jogou TESOURA
    if player == 0:
        print("VITORIA DO JOGADOR")
    elif player == 1:
        print("VITORIA DO COMPUTADOR")
    elif player == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")

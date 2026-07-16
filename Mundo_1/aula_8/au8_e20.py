#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample

alunos = ["Luis", "Brenda", "Jake", "Pandora"]
sortear = sample(alunos, len(alunos))
print(f"A ordem de apresentação dos trabalhos será: \n{sortear}")
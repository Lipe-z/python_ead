#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

alunos = ["Luis", "Brenda", "Jake", "Pandora"]
sortear = choice(alunos)
print(f"O aluno escolhido para apagar o quadro foi {sortear}")

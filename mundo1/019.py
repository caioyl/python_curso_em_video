"""
Desafio 019

Problema: Um professor quer sortear um dos seus quatro alunos para
          apagar o quadro. Faça um programa que ajude ele, lendo o
          nome dos alunos e escrevendo na tela o nome do escolhido.

Resolução do problema:
"""
import random
from random import choice

aluno_1 = input(f'Primeiro aluno: ')
aluno_2 = input(f'Segundo aluno: ')
aluno_3 = input(f'Terceiro aluno: ')
aluno_4 = input(f'Quarto aluno: ')
lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

aluno_escolhido = random.choice(lista_alunos)

print(f'O aluno escolhido foi: {aluno_escolhido}')
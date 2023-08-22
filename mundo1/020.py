"""
Desafio 020

Problema: O mesmo professor do desafio 019 quer sortear a ordem
          de apresentação de trabalhos dos alunos. Faça um programa
          que leia o nome dos quatro alunos e mostre a ordem sorteada.

Resolução do problema:
"""
from random import shuffle
aluno_1 = input(f'Primeiro aluno: ')
aluno_2 = input(f'Segundo aluno: ')
aluno_3 = input(f'Terceiro aluno: ')
aluno_4 = input(f'Quarto aluno: ')
lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_alunos) # Embaralha os elementos de uma lista imediatamente, não é necessário armazenar o resultado
print(f'Lista sorteada: {lista_alunos}')

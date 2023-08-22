"""
Desafio 022

Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.

Resolução do problema:
"""
nome = input('Nome completo: ')
# nome_sem_espaco = nome.replace(' ','')

print(f'Nome em minúsculas: {nome.lower()}')
print(f'Nome em maiúsculas: {nome.upper()}')
#print(f'O nome tem {len(nome_sem_espaco)} letras')
print(f'O nome tem {len(nome) - nome.count(" ")} letras.')
print(f'O primeiro nome tem {nome.find()} letras.')

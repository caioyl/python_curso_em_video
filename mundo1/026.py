"""
Desafio 026

Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.

Resolução do problema:
"""
frase = input('Digite uma frase: ')
print(f'A letra "A" aparece {frase.upper().count("A")} vezes na frase.')
print(f'A primeira vez que a letra "A" aparece é na posição {frase.upper().find("A")+1}')
print(f'A última vez que a letra "A" aparece é na posição {frase.upper().rfind("A")+1}')



"""
Desafio 004

Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela.

Resolução do problema:
"""
objeto = input('Digite algo: ')
print(f'O tipo deste objeto é:',type(objeto))
print(f'Só tem espaços?',objeto.isspace())
print(f'É um número?',objeto.isnumeric())
print(f'É alfabético?',objeto.isalpha()) # E não tem espaços
print(f'É alfanumérico?',objeto.isalnum()) # E nãõ tem espaços
print(f'Está em maiúsculas?',objeto.isupper())
print(f'Está em minúsculas?',objeto.islower())
print(f'Está capitalizada?',objeto.istitle())
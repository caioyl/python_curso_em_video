"""
Desafio 017

Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa.

Resolução do problema:
"""
cat_oposto = float(input('Cateto oposto: '))
cat_adjacente = float(input('Cateto adjacente: '))
hipotenusa = (cat_oposto**2+cat_adjacente**2) ** (1/2)
print(f'Hipotenusa: {hipotenusa}')

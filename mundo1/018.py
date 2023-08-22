"""
Desafio 018

Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo.

Resolução do problema:
"""
from math import *
angulo_radiano = float(input('Ângulo (em graus): '))
angulo_graus = radians(angulo_radiano)
print(angulo_graus)
seno = sin(angulo_graus)
cosseno = cos(angulo_graus)
tangente = tan(angulo_graus)
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')
"""
Desafio 008

Problema: Escreva um programa que leia um valor em metros e o
          exiba convertido em centímetros e milímetros.

Resolução do problema:
"""
valor = float(input('Digite um valor em metros: '))
valor_cm = valor * 100
valor_mm = valor * 1000
print(f'Valor em cm: {valor_cm}')
print(f'Valor em mm: {valor_mm}')

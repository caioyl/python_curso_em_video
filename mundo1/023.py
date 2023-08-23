"""
Desafio 023

Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Resolução do problema:
"""
n = int(input('Digite um número inteiro entre 0 e 9999: '))
unidade = n % 10
dezena = n % 100
centena = n % 1000
milhar = n % 1000
print(unidade)
print(dezena)
print(centena)
print(milhar)

"""
Desafio 025

Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

Resolução do problema:
"""
nome = input('Digite o nome completo de uma pessoa: ')
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
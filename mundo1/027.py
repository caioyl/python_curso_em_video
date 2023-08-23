"""
Desafio 027

Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.

Resolução do problema:
"""
nome_completo = input('Nome completo: ')
nome_dividido = nome_completo.split()
print(f'Primeiro nome: {nome_dividido[0]}\nÚltimo nome: {nome_dividido[-1]}')


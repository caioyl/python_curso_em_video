"""
Desafio 015

Problema: Escreva um programa que pergunte a quantidade de Km
          percorridos por um carro alugado e a quantidade de dias
          pelos quais ele foi alugado. Calcule o preço a pagar,
          sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Resolução do problema:
"""
km_percorridos = float(input('Digite quantos kms foram percorridos: '))
dias_alugados = float(input('Digite por quantos dias o carro foi alugado: '))
preco = (60*dias_alugados) + (km_percorridos * 0.15)
print(f'Preço a se pagar: R${preco:.2f}')

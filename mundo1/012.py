"""
Desafio 012

Problema: Faça um algoritmo que leia o preço de um produto e
          mostre seu novo preço, com 5% de desconto.

Resolução do problema:
"""
preco_antigo = float(input('Digite o preço antigo: R$'))
preco_novo = preco_antigo * 0.95
print(f'Aplicando um desconto de 5%, o preço atual do produto é: R${preco_novo:.2f}')
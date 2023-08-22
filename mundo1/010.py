"""
Desafio 010

Problema: Crie um programa que leia quanto dinheiro uma pessoa tem
          na carteira e mostre quantos dólares ela pode comprar.


Resolução do problema:
"""
reais = float(input('Digite quantos reais você tem na carteira: '))
dolares = reais/3.27
print(f'Considerando que US$1.00 equivale à R$3.27, você pode comprar US${dolares:.2f}')
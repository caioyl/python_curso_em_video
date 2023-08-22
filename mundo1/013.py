"""
Desafio 013

Problema: Faça um algoritmo que leia o salário de um funcionário
          e mostre seu novo salário, com 15% de aumento.

Resolução do problema:
"""
salario_antigo = float(input('Digite o novo salário: '))
salario_novo = salario_antigo * 1.15
print(f'Aplicando um aumento de 15%, o salário atual é R${salario_novo:.2f}')
"""
Desafio 014

Problema: Escreva um programa que converta uma temperatura
          digitando em graus Celsius e converta para graus Fahrenheit.

Resolução do problema:
"""
temp_celsius = float(input('Digite a temperatura em graus Celsius: '))
temp_fahrenheit = ((9*temp_celsius)/5) + 32
print(f'{temp_celsius}ºC = {temp_fahrenheit}ºF')
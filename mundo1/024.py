"""
Desafio 024

Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

Resolução do problema:
"""
cidade = input('Digite o nome de uma cidade: ')
# Método 1

# Imprime o resultado booleano da expressão que verifica a igualdade das cinco
# primeiras letras da cidade
print(cidade[:5].upper() == 'SANTO')


# Método 2
# cidade = cidade.upper().split()
#if cidade[0] == 'SANTO':
# #print('Esta cidade começa com "SANTO".')

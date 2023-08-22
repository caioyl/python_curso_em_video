"""
Desafio 011

Problema: Faça um programa que leia a largura e a altura de uma
          parede em metros, calcule a sua área e a quantidade de
          tinta necessária para pintá-la, sabendo que cada litro
          de tinta pinta uma área de 2 metros quadrados.

Resolução do problema:
"""
largura = float(input('Largura da parede (em metros): '))
altura = float(input('Altura da parede (em metros): '))
area = largura * altura
quantidade_tinta = area / 2
print(f'Considerando que cada litro de tinta pinta uma área de 2 metros quadrados, com uma área de {area} metros,'
      f'você precisará de {quantidade_tinta} litros para pintar a parede inteira.')
"""
Desafio 021

Problema: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

Resolução do problema:
"""

import pygame
pygame.init()
pygame.mixer.music.load('08ver.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

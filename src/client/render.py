"""Renderiza o jogo utilizando pygame"""
import pygame
from board import create_board
from draw import *

WIDTH = 650
HEIGHT = 650
SCREENSIZE = (WIDTH, HEIGHT)

board = create_board()

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
pygame.display.set_caption("Batalha Naval Online")
screen.fill((100,100,100)) # Background provisorio


# TABULEIRO BLOCO
# If you want to draw another instruction you have to fill the text, blit it and then write another one.
text = draw_instruction('Escolha a posição dos seus navios:')
screen.blit(text, (0, 0))
text.fill((100,100,100))
screen.blit(text, (0, 0))
pygame.display.update()

draw_board(screen, board)
pygame.display.update()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
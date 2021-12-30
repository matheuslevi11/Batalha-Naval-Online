"""Renderiza o jogo utilizando pygame"""
import pygame
from board import create_board
from draw import *
import time

WIDTH = 650
HEIGHT = 650
SCREENSIZE = (WIDTH, HEIGHT)
board = create_board() # Criando o tabuleiro do jogador

# Iniciado o pygame
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
pygame.display.set_caption("Batalha Naval Online")


# If you want to draw another instruction you have to fill the text, blit it and then write another one.
text = draw_instruction('Escolha a posição dos seus navios:', (0,100,0))
screen.blit(text, (0, 0))
text.fill((100,100,100))
screen.blit(text, (0, 0))
pygame.display.update()
#-----------------------------------------------------------------------------------------------------------

page = 'home'
draw_homepage(screen)
pygame.display.update()

# Main loop do pygame
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Request pro servidor perguntando a quantidade de jogadores
        players = 2 #INSERIR REQUEST
        if players == 2 and page == 'home':
            page = 'board'
            time.sleep(5)
            board_buttons = draw_board(screen, board)
        
        if page == 'board':
            if e.type == pygame.MOUSEBUTTONDOWN:
                for row in board_buttons:
                    for button in row:
                        if button.collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(screen, (100,0,0), button)

        pygame.display.update()
        
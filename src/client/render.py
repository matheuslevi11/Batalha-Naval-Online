"""Renderiza o jogo utilizando pygame"""
import pygame
from board import create_board
from draw import *
from main import *
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
        
        if page == 'home':
            start_button = pygame.Rect(180, 426, 265, 80)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(pygame.mouse.get_pos()):
                    page = 'wait'
        
        if page == 'wait':
            draw_wait(screen)
            pygame.display.update()
            # Request pro servidor perguntando a quantidade de jogadores
            players = 2 #INSERIR REQUEST
            page = 'board'
            time.sleep(15)
            board_buttons = draw_board(screen, board)
        
        if page == 'board':
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range(10):
                    for j in range(10):
                        button = board_buttons[i][j]
                        if button.collidepoint(pygame.mouse.get_pos()):
                            # Se for o turno dele, jogar!
                            board = handle_play(button, board, i, j, screen)
                            draw_board(screen, board)

        pygame.display.update()
        
"""Renderiza o jogo utilizando pygame"""
import pygame

from board import create_board, create_placement_board
from draw import *
from main import *
from client import Socket, connect_player, get_turn, get_score

WIDTH = 650
HEIGHT = 650
SCREENSIZE = (WIDTH, HEIGHT)
placement_board = create_placement_board() # Tabuleiro em branco que aparecerá na tela do jogador
board = create_board() # Criando o tabuleiro do jogador

# Iniciado o pygame
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
pygame.display.set_caption("Batalha Naval Online")

#-----------------------------------------------------------------------------------------------------------

page = 'home'
player = 99 # Neste ponto ainda não está definido se este jogador será 1 ou 2
turn = 1
cliente = None
won = 0

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
                    cliente = Socket()      
                    page = 'wait'
        
        elif page == 'board':
            if turn == player:
                draw_text("Seu turno", (0, 100, 0), screen)
            else:
                draw_text("Turno do oponente", (100, 0, 0), screen)
            played = 0
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range(10):
                    for j in range(10):
                        button = board_buttons[i][j]
                        if button.collidepoint(pygame.mouse.get_pos()):
                            turn = get_turn(cliente)
                            if turn == player:
                                # Enviando a jogada para o servidor
                                placement_board, board, result = handle_play(board, i, j, placement_board)
                                cliente.send_to_server(f"play {player} {result} {i} {j}")
                                played = 1
            # Verificando se houve alguma jogada
            if not played:
                current = turn
                turn = get_turn(cliente)
                if current != turn:
                    draw_board(screen, placement_board)
                    score = get_score(cliente)
                    if score[0] == "winner":
                        if int(score[1]) == player:
                            won = 1
                        page = 'end'
                    draw_score(screen, score)
                

        elif page == 'wait':
            if player == 99:
                draw_wait(screen)
                pygame.display.update()
            # Jogador 1 ficará na função connect_player até o jogador 2 se conectar
            player = connect_player(cliente)
            page = 'board'
            board_buttons = draw_board(screen, placement_board)
        
        elif page == 'end':
            draw_end(screen, won)
        
        pygame.display.update()
        
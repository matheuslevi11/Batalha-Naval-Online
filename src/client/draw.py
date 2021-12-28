"""Desenha componentes na tela: tabuleiro, letras, páginas"""

import pygame

def draw_letter(letter):  
    opensans = pygame.font.SysFont('opensanscondensed', 20)
    text = opensans.render(letter, True, (255, 255, 255))
    return text

def draw_number(number):  
    opensans = pygame.font.SysFont('opensanscondensed', 20)
    text = opensans.render(str(number), True, (255, 255, 255))
    return text

def draw_instruction(title):
    opensans = pygame.font.SysFont('opensanscondensed', 25)
    text = opensans.render(title, True, (0, 100, 0))
    return text

def draw_board(screen, board):
    init_x = 80
    init_y = 100
    rect_size = 50

    x = init_x
    y = init_y
    
    for i in range(1, 11):
        screen.blit(draw_number(i), (x+18, y-35))
        x += rect_size

    x = init_x
    y = init_y
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    for i, l in enumerate(letters):
        
        screen.blit(draw_letter(l), (x-20, y+10))
        
        for j in range(10):
            color = (0,0,0)
            if board[i][j]['type'] == 'water':
                color = (0, 105, 148)
            if board[i][j]['type'] == 'ship':
                color = (0, 0, 0)
            retangulo = pygame.Rect(x, y, rect_size, rect_size)
            pygame.draw.rect(screen, color, retangulo)
            x += rect_size+1
        
        y += rect_size+1
        x = init_x
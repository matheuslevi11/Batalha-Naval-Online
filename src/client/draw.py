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

def draw_instruction(title, color):
    opensans = pygame.font.SysFont('opensanscondensed', 25)
    text = opensans.render(title, True, color)
    return text

def get_color(id):
    # Submarinos
    if id <= 4:
        return (0, 49, 82)
    # Contra-torpedeiros
    elif id <= 7:
        return (15, 64, 1)
    # Navios-tanque
    elif id <= 9:
        return (0,0,0)
    #Porta-aviões
    else:
        return (201, 188, 187)

def draw_board(screen, board):
    board_buttons = []
    screen.fill((100,100,100))
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
        row = []
        for j in range(10):
            if board[i][j]['type'] == 'water':
                color = (0, 105, 148)
            if board[i][j]['type'] == 'ship':
                color = get_color(board[i][j]['id'])
            retangulo = pygame.Rect(x, y, rect_size, rect_size)
            row.append(retangulo)
            pygame.draw.rect(screen, color, retangulo)
            x += rect_size+1
        
        y += rect_size+1
        x = init_x
        board_buttons.append(row)
    return board_buttons

def draw_homepage(screen):
    screen.fill((196, 187, 2))
    text = draw_instruction('Aguardando o outro jogador...', (0,0,0))
    screen.blit(text, (200, 300))

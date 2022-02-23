"""Desenha componentes na tela: tabuleiro, letras, navios"""

import pygame
from images import get_image, get_images

images = get_images()

def draw_letter(letter):  
    opensans = pygame.font.SysFont('opensanscondensed', 20)
    text = opensans.render(letter, True, (255, 255, 255))
    return text

def draw_number(number):  
    opensans = pygame.font.SysFont('opensanscondensed', 20)
    text = opensans.render(str(number), True, (255, 255, 255))
    return text

def draw_text(title, color, screen):
    opensans = pygame.font.SysFont('opensanscondensed', 25)
    text = opensans.render(title, True, color)
    screen.blit(text, (20, 20))
    pygame.display.update()

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
    bd = images['game']
    screen.blit(bd, (0,0))
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
            tile = board[i][j]
            img = False
            if tile['type'] == 'water' and tile['shot']:
                img = images['watershot']
            elif tile['type'] == 'water':
                color = (14, 55, 128)
            elif tile['type'] == 'ship' and tile['shot']:
                if tile['axis'] == 0:
                    if not tile['tip']:
                        img = images['boat_h']
                    else:
                        if tile['tip'] == 1:
                            img = images['boat_left']
                        else:
                            img = images['boat_right']
                else:
                    if not tile['tip']:
                        img = images['boat_v']
                    else:
                        if tile['tip'] == 1:
                            img = images['boat_top']
                        else:
                            img = images['boat_bottom']
                
           
            retangulo = pygame.Rect(x, y, rect_size, rect_size)
            row.append(retangulo)
            
            if img:
                screen.blit(img, retangulo)
            else:
                pygame.draw.rect(screen, color, retangulo)
            
            x += rect_size+2
        
        y += rect_size+2
        x = init_x
        board_buttons.append(row)
    return board_buttons

def draw_homepage(screen):
    bd = get_image('home.png', (650,650))
    screen.blit(bd, (0,0))

def draw_wait(screen):
    bd = images['wait']
    screen.blit(bd, (0,0))

def draw_score(screen, score):
    opensans = pygame.font.SysFont('opensanscondensed', 30)
    text = opensans.render(f"1P {score[0]} X {score[1]} 2P", True, (0, 0, 100))
    screen.blit(text, (520, 20))
    pygame.display.update()

def draw_end(screen, won):
    if won:
        bd = images['won']
    else:
        bd = images['lose']
    screen.blit(bd, (0,0))
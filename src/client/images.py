"""Importa todas as imagens que o jogo precisa e cria funções para desenhá-las"""

import pygame

def get_image(filename, scale):
    image_src = pygame.image.load(f'../images/{filename}').convert_alpha()
    image = pygame.transform.scale(image_src, scale)
    return image

def get_images():
    images = dict()
    images['wait'] = get_image('wait.png', (650,650))
    images['won'] = get_image('won.png', (650, 650))
    images['lose'] = get_image('lose.png', (650, 650))
    images['game'] = get_image('gamebd.png', (650,650))
    images['watershot'] = get_image('watershot.png', (50,50))
    images['boat_h'] = get_image('boat_h.png', (50,50))
    images['boat_v'] = get_image('boat_v.png', (50,50))
    images['boat_left'] = get_image('boat_left.png', (50,50))
    images['boat_right'] = get_image('boat_right.png', (50,50))
    images['boat_bottom'] = get_image('boat_bottom.png', (50,50))
    images['boat_top'] = get_image('boat_top.png', (50,50))
    return images
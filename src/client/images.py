"""Importa todas as imagens que o jogo precisa e cria funções para desenhá-las"""

import pygame

def get_image(filename, scale):
    background_src = pygame.image.load(f'../images/{filename}').convert_alpha()
    background = pygame.transform.scale(background_src, scale)
    return background
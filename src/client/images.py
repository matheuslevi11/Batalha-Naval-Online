"""Importa todas as imagens que o jogo precisa e cria funções para desenhá-las"""

import pygame

def get_image(filename, scale):
    image_src = pygame.image.load(f'../images/{filename}').convert_alpha()
    image = pygame.transform.scale(image_src, scale)
    return image
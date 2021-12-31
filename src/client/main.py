"""Arquivo principal do jogo, contendo a lógica do jogo"""

import pygame

def handle_play(tile, board, x, y, screen):
    if board[x][y]['type'] == 'ship':
        id = board[x][y]['id']
        for i in range(10):
            for j in range(10):
                if board[i][j]['id'] == id:
                    board[i][j]['shot'] = 1
    return board
"""Arquivo principal, contendo a lógica do jogo"""

import pygame

def handle_play(board, x, y, placement_board):
    result = 'errou'
    # Se a jogada acertou um alvo
    if board[x][y]['type'] == 'ship':
        result = 'acertou'
        id = board[x][y]['id']
        for i in range(10):
            for j in range(10):
                if board[i][j]['id'] == id:
                    board[i][j]['shot'] = 1
                    placement_board[i][j]['shot'] = 1
                    placement_board[i][j]['type'] = 'ship'

    else:
        board[x][y]['shot'] = 1
        placement_board[x][y]['shot'] = 1          
    
    return placement_board, board, result
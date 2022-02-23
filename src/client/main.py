"""Arquivo contendo a lógica do jogo"""

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
                    placement_board[i][j]['axis'] = board[i][j]['axis']
                    placement_board[i][j]['tip'] = board[i][j]['tip'] if board[i][j]['tip'] else 0

    else:
        board[x][y]['shot'] = 1
        placement_board[x][y]['shot'] = 1          
    
    return placement_board, board, result
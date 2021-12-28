"""Cria e retorna o tabuleiro do jogador"""

import random

def place_ship(board, size):
    positioned = 0
    while not positioned:
        ship_pos = []
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        ship_pos.append([x,y])
        axis = random.randint(0, 1)
        
        for i in range(size-1):
            if x < 0 or y < 0 or x > 9 or y > 9:
                continue
            if board[x][y]['type'] != 'water':
                continue
            if axis == 0:
                y += 1
            if axis == 1:
                x += 1
            ship_pos.append([x,y])

        positioned = 1
    print(ship_pos)
    return ship_pos

def create_board():
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append({'type': 'water', 'id': '0'})
        board.append(row)

    # Colocar de forma randômica os navios
    # Cada navio tem o seu identificador
    id = 1

    # Colocando um navio de tamanho 2
    positions = place_ship(board, 2)
    for pos in positions:
        x, y = pos[0], pos[1]
        board[x][y]['type'] = 'ship'
        board[x][y]['id'] = id

    return board


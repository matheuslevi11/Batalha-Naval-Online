"""Cria e retorna o tabuleiro do jogador"""

import random

def place_ship(board, size):
    positioned = 0
    
    while not positioned:
        ship_pos = []
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if board[x][y]['type'] == 'water': break
        axis = random.randint(0, 1)
        
        positioned = 1
        
        for i in range(size):
            if x < 0 or y < 0 or x > 9 or y > 9:
                positioned = 0
                continue
            if board[x][y]['type'] != 'water':
                positioned = 0
                continue
            ship_pos.append([x,y, axis])
            
            if axis == 0:
                y += 1
            if axis == 1:
                x += 1

    return ship_pos

def create_board():
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append({'type': 'water', 'id': 0, 'shot': 0, 'tip': 0})
        board.append(row)

    # Colocar de forma randômica os navios
        # id de um navio identifica todas as posições que pertecem a ele
    
    for id in range(1, 11):
        # Submarinos
        if id <= 4:
            positions = place_ship(board, 2)
            for pos in positions:
                x, y = pos[0], pos[1]
                axis = pos[2]
                board[x][y]['axis'] = axis
                board[x][y]['type'] = 'ship'
                board[x][y]['id'] = id
            board = place_tips(positions, board)

        # Contra-torpedeiros
        elif id <= 7:
            positions = place_ship(board, 3)
            for pos in positions:
                x, y = pos[0], pos[1]
                axis = pos[2]
                board[x][y]['axis'] = axis
                board[x][y]['type'] = 'ship'
                board[x][y]['id'] = id
            board = place_tips(positions, board)
        # Navios-tanque
        elif id <= 9:
            positions = place_ship(board, 4)
            for pos in positions:
                x, y = pos[0], pos[1]
                axis = pos[2]
                board[x][y]['axis'] = axis
                board[x][y]['type'] = 'ship'
                board[x][y]['id'] = id
            board = place_tips(positions, board)
        #Porta-aviões
        else:
            positions = place_ship(board, 5)
            for pos in positions:
                x, y = pos[0], pos[1]
                axis = pos[2]
                board[x][y]['axis'] = axis
                board[x][y]['type'] = 'ship'
                board[x][y]['id'] = id
            board = place_tips(positions, board)

    return board

def create_placement_board():
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append({'type': 'water', 'id': 0, 'shot': 0, 'tip': 0})
        board.append(row)
    
    return board

def place_tips(positions, board):
    for i, pos in enumerate(positions):
        if i == 0:
            x, y = pos[0], pos[1]
            board[x][y]['tip'] = 1 # esquerda ou cima
        
        if i == len(positions) - 1:
            x, y = pos[0], pos[1]
            board[x][y]['tip'] = 2 # direita ou baixo
    return board
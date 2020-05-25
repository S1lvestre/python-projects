#!/usr/bin/env python
# coding: utf-8

import numpy as np

sudoku = [[0, 4, 0, 0, 0, 0, 1, 7, 9],
          [0, 0, 2, 0, 0, 8, 0, 5, 4],
          [0, 0, 6, 0, 0, 5, 0, 0, 8],
          [0, 8, 0, 0, 7, 0, 9, 1, 0],
          [0, 5, 0, 0, 9, 0, 0, 3, 0],
          [0, 1, 9, 0, 6, 0, 0, 4, 0],
          [3, 0, 0, 4, 0, 0, 7, 0, 0],
          [5, 7, 0, 1, 0, 0, 2, 0, 0],
          [9, 2, 8, 0, 0, 0, 0, 6, 0]]

def pickEmpty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return False

def isPossible(pos, value, grid):
    if value == 0:
        return False
    
    # check line
    for a in range(9):
        if grid[pos[0]][a] == value and pos[1] != a:
            return False
        
    # check column
    for b in range(9):
        if grid[b][pos[1]] == value and pos[0] != b:
            return False
    
    # check cell
    y, x = (pos[0]//3)*3, (pos[1]//3)*3
    for c in range(3):
        for d in range(3):
            if grid[ y + c ][ x + d ] == value and pos != [c, d]:
                return False
    
    return True

def solve(board):
    if not pickEmpty(board): # se não encontra nenhum vazio é poque chegou ao fim e está resolvido.
        return True
    
    else:
        pos = pickEmpty(board)
        
    for val in range(1, 10):
        if isPossible(pos, val, board):
            board[pos[0]][pos[1]] = val # bota o valor possivel na posição e...
            
            if solve(board):
                # corre o solve() outra vez. caso tenha chegado ao fim ele vai logo devolver um True (linha 48)
                # e este "nivel" da recursão devolve True também
                return True
            
            # caso contrário, e o próximo nivel tenha corrido os valores todos e não teha encontrado nenhum,
            # então este val, nesta posição, não é posível e é metido a zero.**vai ao fim ver**
            board[pos[0]][pos[1]] = 0
            
    return False

print(np.matrix(sudoku), "\n")

solve(sudoku)

print(np.matrix(sudoku))

# ** de repente podes estar a pensar porque é que é metido a zeros se o "for" vai só continuar a aincrementar para o valor seguinte ignorando o zero.
#    metes a zero porque caso aquilo corra o resto dos valores até ao 9 e tenha de andar um quadrado/nivel pra trás. como deixaste este a zero ele vai ser apanhado pela função isEmpty()



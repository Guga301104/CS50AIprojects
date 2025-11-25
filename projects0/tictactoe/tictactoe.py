"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    countX = sum(cell == X for row in board for cell in row)
    countO = sum(cell == O for row in board for cell in row)
    if (countX == countO): return X
    else: return O


def actions(board):
    if (terminal(board)): return set()
    return {(i,j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    if action not in actions(board): raise Exception("Invalid action")
    turn = player(board)
    newBoard = [row.copy() for row in board]
    newBoard[action[0]][action[1]] = turn
    return newBoard


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    count = all(cell != EMPTY for row in board for cell in row)
    if (winner(board)): return True
    if (count): return True
    return False


def utility(board):
    w = winner(board)
    if w == X: return 1
    elif w == O: return -1
    return 0


def minimax(board):
    if terminal(board): return None
    turn = player(board)    
    if turn == X:
        ac = None
        bestValue = float('-inf')
        for action in actions(board):
            m = minValue(result(board, action))
            if m > bestValue:
                bestValue = m
                ac = action
        return ac
    elif turn == O:
        ac = None
        bestValue = float('inf')
        for action in actions(board):
            m = maxValue(result(board, action))
            if m < bestValue:
                bestValue = m
                ac = action
        return ac 


def maxValue(board):
    if terminal(board): return utility(board)
    best = float('-inf')
    for action in actions(board): best = max(best, minValue(result(board, action)))
    return best


def minValue(board):
    if terminal(board): return utility(board)
    best = float('inf')
    for action in actions(board): best = min(best, maxValue(result(board, action)))
    return best

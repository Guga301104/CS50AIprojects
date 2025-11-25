X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY]
            [EMPTY, EMPTY, EMPTY]
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    contX = sum(cell == X for row in board for cell in row)
    contO = sum(cell == O for row in board for cell in row)
    if (contX ==  contO): return X
    else: return O

def actions(board):
    if terminal(board): return set()
    lista = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                lista.append((i,j))
    return set(lista)

def result(board, action):
    if action not in actions(board):
        return ("Acao invalida")
    turn = player(board)
    auxBoard = [row.copy() for row in board]
    auxBoard[action[0]][action[1]] = turn
    return auxBoard

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
    cheio = all(cell != EMPTY for row in board for cell in row)
    if winner(board) or cheio:
        return True
    return False

def utility(board):
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
    return 0

def minimax(board):
    if terminal(board):
        return None
    turn = player(board)
    if turn == X:
        ac = None
        best = float('-inf')
        for action in actions(board):
            r = maxValue(result(board, action))
            if r > best:
                best = r
                ac = action
        return ac
    else:
        ac = None
        best = float('inf')
        for action in actions(board):
            r = minValue(result(board, action))
            if r < best:
                best = r
                ac = action
        return action

def maxValue(board):
    if terminal(board):
        return utility(board)
    best = float('-inf')
    for action in actions(board):
        best = max(best, minValue(result(board, action)))
    return best

def minValue(board):
    if terminal(board):
        return utility(board)
    best = float('inf')
    for action in actions(board):
        best = min(best, maxValue(result(board, action)))
    return best
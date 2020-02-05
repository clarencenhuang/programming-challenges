

Player1, Player2 = 'x', 'o'

def won(board, player):
    for i in range(3):
        if board[i] == [player] * 3:
            return True
    for c in range(3):
        col = []
        for r in range(3):
            col.append(board[r][c])
        if col == [player] * 3:
            return True

    d1, d2 = [], []
    for i in range(3):
        d1.append(board[i][i])
        d2.append(board[i][2-i])
    if d1 == [player] * 3 or d2 == [player] * 3:
        return True
    return False

def moves_left(board):
    counter = 0
    for r in board:
        for c in r:
            if c is None:
                counter += 1
    return counter

def play(board, player=Player1):
    pass
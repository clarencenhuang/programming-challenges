import math

Player1, Player2 = 'x', 'o'

next_player = {
    Player1: Player2,
    Player2: Player1
}


def has_moves_left(b):
    for r in b:
        for c in r:
            if c != '-':
                return True
    else:
        return False


def won(b, player=Player1):
    won_player = '-'
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2]:
            won_player = b[i][0]
            break
        elif b[0][i] == b[1][i] == b[2][i]:
            won_player = b[0][i]
            break
    if (b[0][0] == b[1][1] == b[2][2] or
            b[0][2] == b[1][1] == b[2][0]):
        won_player = b[1][1]
    if won_player is '-':
        return 0
    elif won_player == player:
        return 10
    else:
        return -10


def play(board, player=Player1, level=1):
    score = won(board, player)
    if score != 0:
        return score
    if not has_moves_left(board):
        return 0
    best = -math.inf
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c == '-':
                board[i][j] = player
                best = max(best, play(board, next_player[player], level+1))
                board[i][j] = '-'
    return best


empty_board = [['-'] * 3 for _ in range(3)]
empty_board[0][0] = 'o'
print(play(empty_board))


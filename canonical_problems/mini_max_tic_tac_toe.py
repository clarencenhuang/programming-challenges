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
        if len(set([b[i][j] for j in range(3)])) == 1:
            won_player = b[i][0]
            break
        if len(set([b[j][i] for j in range(3)])) == 1:
            won_player = b[0][i]
            break
        if len(set([b[i][i] for i in range(3)])) == 1:
            won_player = b[i][i]
            break
        if len(set([b[i][3-i] for i in range(3)])) == 3:
            won_player = b[i][3-i]
            break
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



def word_break(dictionary, mystr):

    def wb(i, j):
        if mystr[i:j+1] in dictionary:
            return True
        if i == j:
            return False
        for m in range(i, j):
            if wb(i, m) and wb(m+1, j):
                return True
        return False

    return wb(0, len(mystr) - 1)


def word_break_dp(dictionary, mystr):
    len_str = len(mystr)
    dp = [[False] * len_str for _ in range(len_str)]

    for length in range(len_str):
        for i in range(len_str):
            j = i + length
            if j >= len_str:
                break
            if mystr[i:j+1] in dictionary:
                dp[i][j] = True
            elif j == i:
                dp[i][j] = False
            else:
                for m in range(i, j):
                    dp[i][j] = dp[i][j] or (dp[i][m] and dp[m+1][j])
    return dp[0][-1]


if __name__ == '__main__':
    dictionary = {"iajxlo", "h", "q"}
    print(word_break_dp(dictionary, 'hhqhq'))
    print(word_break(dictionary, 'hhqhq'))


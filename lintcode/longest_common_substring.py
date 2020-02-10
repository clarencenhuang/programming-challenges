def lcs(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    dp = [[0] * len(b) for _ in range(len(a))]

    for i, l_a in enumerate(a):
        for j, l_b in enumerate(b):
            prev = 0
            if i > 0 and j > 0:
                prev = dp[i - 1][j - 1]
            if l_a == l_b:
                dp[i][j] = prev + 1

    return max([x for y in dp for x in y])

if __name__ == '__main__':
    print(lcs('ABCDE', 'CBCDE'))
'''
for 2 strings s, t

if s[i] == t[j]:
    lcs[i,j].length = 1 + lcs[i-1, j-1].length
    lcs[i,j].seq = lcs[i-1, j-1].seq + s[i]
else:
    lcs[i,j].length = max(lcs[i-1, j].length, lcs[i, j-1].length)
    lcs[i,j].seq = lcs_max[i_max, j_max].seq


lcs recover

'''

def find_lcs_2(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = len(s), len(t)
    buffer = ''
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j-1] + 1:
            buffer += s[i-1]
            i, j = i - 1, j - 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1
    return buffer[::-1]


def find_lcs(s, t):
    Len, Seq = range(2)
    ilen = len(s)
    jlen = len(t)
    dp = [[[0, ''] for _ in range(jlen + 1)] for _ in range(ilen + 1)]
    for i in range(1, ilen + 1):
        for j in range(1, jlen + 1):
            i_letter = s[i - 1]
            j_letter = t[j - 1]
            if i_letter == j_letter:
                dp[i][j][Len] = dp[i-1][j-1][Len] + 1
                dp[i][j][Seq] = dp[i - 1][j - 1][Seq] + i_letter
            else:
                l1, l2 = dp[i-1][j][Len], dp[i][j-1][Len]
                if l1 >= l2:
                    dp[i][j][Len] = l1
                    dp[i][j][Seq] = dp[i-1][j][Seq]
                else:
                    dp[i][j][Len] = l2
                    dp[i][j][Seq] = dp[i][j-1][Seq]
    return dp[-1][-1][Seq]


def read_input():
    s = str(input())
    t = str(input())
    print(find_lcs(s, t))

if __name__ == '__main__':
    assert find_lcs_2('axyb', 'abyxb') in {'axb', 'ayb'}
    assert find_lcs_2('aa', 'xayaz') == 'aa'
    print(find_lcs_2('a', 'z'))







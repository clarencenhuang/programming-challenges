# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/discuss/483782/Detailed-explanation-on-optimizing-a-3D2D-DP-to-1D
'''

First DP formulation

dp_1[i][j]: the minimum cost if we the wrote the last i to j th letter with finger 1
dp_2[i][j]: the minimum cost if we worte hte last i to jth letter with finger 0


dp_x[i][j] = min of
    dp_x[i-1][j-1] + cost of moving from cost(j-1, j)
    dp_y[k][j-1] + cost of moving from to cost(k-1, j) for each k < i

alternative DP formulation


dp[i][j] = min cost of having finger on i and j, left being i and right being j
dp[i][j] = 

'''
import math
import functools


def min_dist_type(word):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l2c = {}
    for i, l in enumerate(letters):
        x = i % 6
        y = i // 6
        l2c[l] = x, y

    def cost(i, j):
        l1, l2 = word[i], word[j]
        (x0, y0), (x1, y1) = l2c[l1], l2c[l2]
        amt = abs(x0 - x1) + abs(y0 - y1)
        #print(l1, l2, amt)
        return amt
    cumsum = {0: 0}
    for i in range(1, len(word)):
        cumsum[i] = cumsum[i-1] + cost(i, i-1)

    dp = [[[0, 0] for i in range(len(word))] for j in range(len(word))]
    for j in range(len(word)):
        for i in range(0, j + 1):
            for f in [0, 1]:
                if j == 0:
                    dp[i][j][f] = 0
                elif i == 0:
                    dp[i][j][f] = cumsum[j]
                elif i == j:
                    min_amt = math.inf
                    for k in range(i):
                        min_amt = min(min_amt, dp[k][i-1][1-f] + (cost(k-1, j) if k > 0 else 0))
                    dp[i][j][f] = min_amt
                else:
                    dp[i][j][f] = dp[i][j - 1][f] + cost(j - 1, j)
    min_val = math.inf
    for i in range(len(word)):
        min_val = min(min_val, dp[i][len(word)-1][0], dp[i][len(word)-1][1])
    return min_val


if __name__ == '__main__':
    print(min_dist_type("HAPPY"))

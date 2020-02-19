# https://leetcode.com/problems/triangle/

'''
dp[i][j] denotes the shortest path to node i on level j

'''

import math
import functools


def min_path_sum(tri):

    @functools.lru_cache(None)
    def dp(i, j):
        if j == -1:
            return 0
        if i < 0 or i >= len(tri[j]):
            return math.inf
        return min(dp(i - 1, j - 1), dp(i, j-1)) + tri[j][i]

    return min([dp(i, len(tri)-1) for i in range(len(tri[-1]))])


if __name__ == '__main__':
    tri = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    print(min_path_sum(tri))

import math
from functools import lru_cache


def dg_game(dungeon):
    m, n = len(dungeon), len(dungeon[0])

    # first element is life left after move, second one is cumulative life changes
    @lru_cache(None)
    def dp(i, j):
        num = dungeon[i][j]
        if i == m - 1 and j == n - 1:
            if num < 1:
                return 1 - num # must enter last cell with at least
            else:
                return 1
        else:
            exit_num = math.inf
            if i < m - 1:
                exit_num = min(exit_num, dp(i+1, j))
            if j < n - 1:
                exit_num = min(exit_num, dp(i, j+1))
            enter_num = exit_num - num
            if enter_num < 1:
                enter_num = 1
            return enter_num

    return dp(0, 0)


if __name__ == '__main__':
    print(dg_game([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
    print(dg_game([[1 ,-3, 3], [0, -2, 0], [-3 ,-3,-3]]))
    print(dg_game([[100]]))

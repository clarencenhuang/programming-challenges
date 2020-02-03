from collections import deque
from bisect import bisect
from copy import deepcopy
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        nrows, ncols = len(forest), len(forest[0])
        steps = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        )

        trees = []
        for i, r in enumerate(forest):
            for j, n in enumerate(r):
                if n > 1:
                    val = (n, i, j)
                    trees.insert(bisect(trees, val), val)

        def bfs(grid, initial, target):
            q = deque([(initial, 0)])
            while q:
                (i, j), hist = q.popleft()
                if forest[i][j] == target:
                    return hist
                for ii, jj in steps:
                    ii, jj = ii + i, jj + j
                    if (0 <= ii < nrows and
                        0 <= jj < ncols and
                        grid[ii][jj] != 0
                    ):
                        q.append(((ii, jj), hist + 1))
                        grid[ii][jj] = 0
            return -1

        total_moves = 0
        last_coord = (0, 0)
        for tree, i, j in trees:
            grid = deepcopy(forest)
            moves = bfs(grid, last_coord, tree)
            if moves == -1:
                return -1
            total_moves += moves
            forest[i][j] = 1
            last_coord = (i, j)

        return total_moves



if __name__ == '__main__':
    s = Solution()
    forest = [[1,2,3],[0,0,4],[7,6,5]]
    print(s.cutOffTree(forest))

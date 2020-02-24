from collections import defaultdict
import itertools


def count_servers_communicate(grid):
    if len(grid) == 0:
        return 0
    by_row = defaultdict(set)
    by_col = defaultdict(set)
    results = set()
    nrows, ncols = len(grid), len(grid[0])
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 1:
                by_row[i].add((i, j))
                by_col[j].add((i, j))
    for idxes in itertools.chain(by_row.values(), by_col.values()):
        if len(idxes) >= 2:
            results.update(idxes)
    return len(results)


if __name__ == '__main__':
    print(count_servers_communicate([[1,0],[1,1]]))

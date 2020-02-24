import math
import functools

def min_largest(arr, n):

    cumsum = {-1: 0}
    for i, v in enumerate(arr):
        cumsum[i] = cumsum[i-1] + v

    # min largest sum by splitting into j parts for array in 0 to i inclusive
    @functools.lru_cache(None)
    def dp(i, j):
        if j == 1:
            return cumsum[i]
        # we can only split first i into i + 1 parts
        if j > i + 1:
            return math.inf
        min_max_val = math.inf
        smallest_k = j - 2
        for k in range(smallest_k, i):
            min_max_val = min(min_max_val, max(dp(k, j-1), cumsum[i] - cumsum[k]))
        return min_max_val

    return dp(len(arr) - 1, n)

if __name__ == '__main__':
    print(min_largest([7,2,5,10,8], 2))
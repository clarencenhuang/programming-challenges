import math
import functools


smart_cache = {}


def sed_iter(k, n):
    dp = dict.fromkeys([(k_i, n_i) for k_i in range(1, k + 1) for n_i in range(1, n + 1)], 1)
    for ni in range(n + 1):
        dp[(0, ni)] = 1
    for ki in range(k + 1):
        dp[(ki, 0)] = 1

    for k_i in range(2, k + 1):
        for n_i in range(2, n + 1):
            best_so_far = math.inf
            for i in range(1, n_i + 1):
                break_moves = 1 + dp[(k_i - 1, i - 1)]
                no_break_moves = 1 + dp[(k_i, n_i - i)]
                safe_moves = max(break_moves, no_break_moves)
                best_so_far = min(safe_moves, best_so_far)
            dp[(k_i, n_i)] = best_so_far
    return dp[(k, n)]


def sed(k, n):
    #print((k, n))
    # base case: 1 egg left, n floors
    if k == 1:
        return n

    # base case, only 1 or less floor, 1 drop sufficient
    if n <= 1:
        return n

    if (k, n) in smart_cache:
        return smart_cache[(k, n)]

    best_so_far = math.inf
    for i in range(1, n + 1):
        # if it breaks
        break_moves = 1 + sed(k - 1, i - 1)

        # if it does not break
        no_break_moves = 1 + sed(k, n - i)

        safe_moves = max(break_moves, no_break_moves)

        best_so_far = min(safe_moves, best_so_far)
    # print(f"best so far: {best_so_far} for n:{n} k: {k}  ")
    smart_cache[(k, n)] = best_so_far
    return best_so_far


if __name__ == '__main__':
    print(sed(4, 500))
    #print(sed_iter(4, 500))
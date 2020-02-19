import math
import functools

def max_product(arr):


    @functools.lru_cache(None)
    def max_pos(i):
        if i == 0:
            return arr[i]
        if arr[i] > 0:
            return max(arr[i] * max_pos(i-1), arr[i])
        elif arr[i] < 0:
            return max(arr[i] * min_neg(i-1), arr[i])
        else:
            return 0

    @functools.lru_cache(None)
    def min_neg(i):
        if i == 0:
            return arr[i]
        if arr[i] > 0:
            return min(arr[i] * min_neg(i - 1), arr[i])
        elif arr[i] < 0:
            return min(arr[i] * max_pos(i - 1), arr[i])
        else:
            return 0

    max_so_far = -math.inf
    for i in range(len(arr)):
        max_so_far = max(max_so_far, max_pos(i))
    return max_so_far


if __name__ == '__main__':
    print(max_product([2,3,-2,4]))
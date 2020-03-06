import functools

def eq_subset_sum(arr):
    k = sum(arr)
    if k % 2 != 0:
        return False
    k = k // 2

    # is it possible to sum up to j using first i numbers
    @functools.lru_cache(None)
    def dp(i, j):
        if j == 0:
            return True
        if j < 0 or i == 0:
            return False
        # we either use the ith number, or we don't use it
        return dp(i-1, j) or dp(i-1, j-arr[i])

    return dp(len(arr)-1, k)

if __name__ == '__main__':
    print(eq_subset_sum([1, 5, 11, 5, 3]))
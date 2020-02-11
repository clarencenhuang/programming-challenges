# https://www.lintcode.com/problem/subarray-sum/description?_from=ladder&&fromId=2
from collections import defaultdict

def subarray_sum(arr):
    cum_sums = defaultdict(set)
    cum_sums[0].add(-1)
    cs = 0
    indices = []
    for i, n in enumerate(arr):
        cs += n
        for prev_i in cum_sums[cs]:
            indices.append([prev_i + 1, i])
        cum_sums[cs].add(i)
    return indices

if __name__ == '__main__':
    print(subarray_sum([-3, 1, 2, -3, 4, 0]))

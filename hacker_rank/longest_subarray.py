# this was done as a part of the hackerrank timed test for certification
from collections import defaultdict

# longest subarray no more than 2 distinct subvalue
def longest_subarray(arr):
    i = 0
    max_len = 0
    window = defaultdict(lambda: 0)
    for j, v in enumerate(arr):
        window[v] += 1
        while len(window) > 2:
            fv = arr[i]
            window[fv] -= 1
            if window[fv] == 0:
                del window[fv]
            i += 1
        max_len = max(max_len, j - i + 1)
    return max_len

def longest_verify(arr):
    ml = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            window = set(arr[i:j + 1])
            if len(set(window)) <= 2:
                ml = max(ml, j - i + 1)
    return ml

if __name__ == '__main__':
    # print(longest_subarray([1,2,3,4,5]))
    # print(longest_subarray([2,2,1]))
    print('\n'.join([str(k + 195593457) for k in [2, 2, 1, 0, 2, 2, 1, 2, 1, 2, 0, 1, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0,
                            0, 0, 2, 2, 2, 1, 1, 1, 1, 1, 0, 2, 2, 1, 0, 2, 2, 0, 2, 2, 0, 0, 2, 2, 0, 2, 1, 1, 1, 0,
                            1, 1, 1, 1, 0, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0,
                            1, 0, 1, 1, 0, 2, 0, 0, 2, 0, 2, 2, 1, 0, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 0, 2, 1, 0, 0, 0,
                            1, 0, 2, 0, 1, 2, 1, 1, 2, 0, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0, 0, 2, 1, 2, 1, 0]]))
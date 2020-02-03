import math
import collections

def am_windows(n, queries):
    posts = collections.defaultdict(lambda: 0)
    for s, e, val in queries:
        posts[s] += val
        posts[e + 1] -= val

    max_val = - math.inf
    cur_val = 0
    for i in range(1, n+1):
        if i in posts:
            cur_val += posts[i]
            max_val = max(max_val, cur_val)
    return max_val

if __name__ == '__main__':
    n = 10
    queries = [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1]
    ]
    print(am_windows(n, queries))
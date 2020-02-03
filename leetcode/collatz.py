import functools
import math


@functools.lru_cache(maxsize=None)
def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n/2)
    else:
        return 1 + collatz(3 * n + 1)

if __name__ == '__main__':
    max_len =  -math.inf
    for i in range(1000000, 1, -1):
        max_len = max(max_len, collatz(i))
    print(max_len)
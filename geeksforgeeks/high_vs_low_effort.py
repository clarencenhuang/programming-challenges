# https://practice.geeksforgeeks.org/problems/high-effort-vs-low-effort/0
import functools


def hi_low_effort(lo, hi):
    days = len(lo)

    @functools.lru_cache(None)
    def perform(d):
        if d <= 0:
            return 0
        # we can perform a high, perform a lo, or do nothing
        do_hi = hi[d - 1] + perform(d - 2)
        do_lo = lo[d - 1] + perform(d - 1)
        do_nothing = perform(d - 1)
        return max(do_hi, do_lo, do_nothing)

    return perform(days)

def hi_low_effort_dp(lo, hi):
    days = len(lo)

    dp = [0] * (days + 1)
    for i in range(1, days + 1):
        do_hi = hi[i-1] + dp[max(0, i - 2)]
        do_lo = lo[i-1] + dp[i-1]
        dp[i] = max(do_lo, do_hi)
    return dp[-1]

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        input()
        hi = list(map(int, input().split()))
        lo = list(map(int, input().split()))
        print(hi_low_effort(lo, hi))


if __name__ == '__main__':
    hi = list(map(int, '3 6 8 7 6'.split()))
    lo = list(map(int, '1 5 4 5 3'.split()))
    print(hi_low_effort_dp(lo, hi))
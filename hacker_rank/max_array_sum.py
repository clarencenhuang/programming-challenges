# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
import functools

def max_subset_sum(arr):

    @functools.lru_cache(None)
    def max_ssum(i):
        if i < 0:
            return 0
        return max(max_ssum(i - 2) + arr[i], arr[i], max_ssum(i - 1))
    return max_ssum(len(arr) - 1)

# the top down recursion version gets stack overflow, FML
def max_ss_iter(arr):
    dp = [0] * (len(arr) + 2)
    for j in range(len(arr)):
        i = j + 2
        dp[i] = max(dp[i-2] + arr[j], arr[j], dp[i-1])
    return dp[-1]


if __name__ == '__main__':
    print(max_ss_iter([2, 1, 5, 8, 4]))
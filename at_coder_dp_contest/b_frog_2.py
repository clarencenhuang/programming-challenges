# https://atcoder.jp/contests/dp/tasks/dp_b
'''
dp[i] = min(dp[j < i] + cost_of_jump(j, i))
'''

def b_frog_2(stones, k):
    dp = [10e5+1] * len(stones)
    dp[0] = 0
    for i in range(1, len(stones)):
        for j in range(max(0, i - k), i):
            dp[i] = min(dp[i], dp[j] + abs(stones[i] - stones[j]))
    return dp[-1]


def main2():
    N, K = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print(b_frog_2(h, K))

if __name__ == '__main__':
    assert b_sol([10, 30, 40, 50, 20], 3) == 30
    assert b_sol([10, 20, 10], 1) == 20
    assert b_sol([10, 10], 100) == 0
    assert b_sol([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4) == 40

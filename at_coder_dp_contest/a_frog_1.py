# https://atcoder.jp/contests/dp/tasks/dp_a
'''
1,2.... N
height of stone hi

can jump to i+i or i+2 cost of hi - hj is incured

dp[i] = min(dp[i-1] + cost(i-1 to i), dp[i-2] + cost(i - 2, to, i))

base case dp[i] = 0 for i = 0

'''
def dp_a_frog1(stones):
    if len(stones) == 0:
        return 0
    dp = [0] * len(stones)
    for i in range(1, len(stones)):
        cost_jump = dp[i-1] + abs(stones[i-1] - stones[i])
        if i > 1:
            cost_jump_2 = dp[i-2] + abs(stones[i-2] - stones[i])
            cost_jump = min(cost_jump, cost_jump_2)
        dp[i] = cost_jump
    return dp[len(stones) - 1]

if __name__ == '__main__':
    assert dp_a_frog1([10, 30, 40, 20]) == 30
    assert dp_a_frog1([10, 10]) == 0
    assert dp_a_frog1([30, 10, 60, 10, 60, 50]) == 40


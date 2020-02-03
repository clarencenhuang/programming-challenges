
'''
dp[w][i], whether we can sum up to w using all ith numbers
dp[w][i]  = dp[w][i-1] // not use this
            or dp[w - nums[i]][i - 1] // use this

'''


def eq_sum(nums) -> bool:
    target_sum = sum(nums) // 2
    dp = [[False] * (len(nums) + 1) for _ in range(target_sum + 1)]
    for i in range(len(nums) + 1):
        dp[0][i] = True # its always possible to sum to 0 by not picking any of the numbers in the set

    for w in range(1, target_sum + 1):
        for i in range(1, len(nums) + 1):
            num_i = nums[i - 1]
            dp[w][i] = dp[w][i-1]
            if w >= num_i:
                dp[w][i] = dp[w][i] or dp[w - num_i][i - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    s = [7,5,2,50]
    print(eq_sum(s))
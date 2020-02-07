1

def wiggle_subsequence(nums):

    dp = [[1, 1] for _ in nums]
    for i in range(1, len(nums)):
        next_up, next_down = (-math.inf, -math.inf)
        num = nums[i]
        for j in range(i):
            up, down = dp[j]
            if num > nums[j]:
                next_down = max(next_down, up + 1)
            elif num < nums[j]:
                next_up = max(next_up, down + 1)
        dp[i] = [next_up, next_down]
    return max([i for hi_lo in dp for i in hi_lo])


if __name__ == '__main__':
    print(wiggle_subsequence([1,17,5,10,13,15,10,5,16,8]))



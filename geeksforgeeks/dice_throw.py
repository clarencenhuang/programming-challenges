# https://practice.geeksforgeeks.org/problems/dice-throw/0


# n dices of m faces
def dice_throw(m, n, x):
    def num_ways(num_dice, num):
        if num_dice == 1:
            if 1 <= num <= m:
                return 1
            else:
                return 0
        ways = 0
        for i in range(1, m + 1):
            ways += num_ways(num_dice - 1, num - i)
        return ways

    return num_ways(n, x)

def dice_throw_dp_table(m, n, x):
    dp = [[0] * (n+1) for _ in range(x + 1)]
    for i in range(1, m + 1):
        dp[i][1] = 1  # 1 dice and numbers that one dice can reach
    for i in range(1, x + 1):
        for j in range(2, n + 1):  # number of dice
            for k in range(1, m + 1):
                if i > k:
                    dp[i][j] += dp[i-k][j-1]
    return dp[-1][-1]


if __name__ == '__main__':
    #print(dice_throw(6, 3, 12))
    #print(dice_throw(10, 8, 25))
    #print(dice_throw_dp_table(6, 3, 12))
    print(dice_throw_dp_table(10, 8, 25))

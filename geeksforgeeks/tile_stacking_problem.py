# https://www.geeksforgeeks.org/tile-stacking-problem/


# build tower height n, with m bricks, at most k of each
def build_tower(n, m, k):

    def num_ways(n, m):
        if n == 0: # we finished building the tower... wohoo
            return 1
        if m <= 0: # we either ran out of material to build or something was wierd
            return 0
        n_ways = 0
        # don't use k
        n_ways += num_ways(n, m - 1)
        for i in range(1, k + 1):
            n_ways += num_ways(n - i, m - 1) # we use m for i times
        return n_ways

    return num_ways(n, m)


def build_tower_dp(n, m, k):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for x in range(m+1):
        dp[0][x] = 1 # we can always build a tower of size 0, just don't use any brickz
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] += dp[i][j-1] # don't use the j-th brick
            for y in range(1, k+1):
                if i >= y:
                    dp[i][j] += dp[i - y][j - 1] # use the jth brick i-times
    return dp[-1][-1]


if __name__ == '__main__':
    print(build_tower_dp(3, 3, 2))
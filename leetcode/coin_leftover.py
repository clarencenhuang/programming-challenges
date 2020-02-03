def getWays(n, c):
    cache = {}
    def get_ways(left, coins):
        if left < 0 or len(coins) == 0:
            return 0
        if left == 0:
            return 1
        key = (left, tuple(sorted(coins)))
        if key in cache:
            return cache[key]
        total_ways = 0
        coin = list(coins)[0]
        total_ways += get_ways(left - coin, coins)
        total_ways += get_ways(left, coins - {coin})
        cache[key] = total_ways
        return total_ways
    # Write your code here
    print(get_ways(n, set(c)))

if __name__ == '__main__':
    getWays(4, [1,2,3])




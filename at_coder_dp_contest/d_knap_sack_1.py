'''
V[i,w] max value for i items considered and weight w
V[i,w] = max( do_pick_item, do_not_pick_item)

do_pick_item = V[i - 1, w - w[i]] + value[i]
do_not_pick_item = V[i - 1, w]

'''
def knap_sack_1(weight_and_value, w):
    n = len(weight_and_value)
    dp = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for w in range(1, w + 1):
        for i in range(1, len(weight_and_value) + 1):
            w_i, v_i = weight_and_value[i-1]
            if w >= w_i:
                dp[i][w] = max(dp[i][w], dp[i-1][w - w_i] + v_i)
            dp[i][w] = max(dp[i][w], dp[i-1][w])
    return dp[-1][-1]

def get_input():
    n, k = list(map(int, input().split()))
    data = []
    for i in range(n):
        el = list(map(int, input().split()))
        data.append(el)
    return data

if __name__ == '__main__':
    assert knap_sack_1([[3,30], [4, 50], [5, 60]], 8) == 90
    assert knap_sack_1([[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]], 5) == 5000000000
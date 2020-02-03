'''
dp[w]: max number of legal segments in rod of length k
l = {l1, l2, l3}
dp[0] = 0

if all l > w:
    dp[w] = 0
dp[w] = max_over_l(dp[w-l]) + 1
'''
def dp_rod(rod_len, segments):
    dp = [0] * (rod_len + 1)
    for w in range(1, rod_len + 1):
        w_minus_l = []
        for s in segments:
            if w >= s:
                left = w - s
                if dp[left] >= 0:
                    w_minus_l.append((dp[left], s))
        if len(w_minus_l) == 0:
            dp[w] = -1
        else:
            val, cut = max(w_minus_l)
            dp[w] = 1 + val
    if dp[-1] == -1:
        return 0
    return dp[-1]


def dp_rod2(rod_len, segments):
    dp = [0] * (rod_len + 1)
    for i in range(rod_len + 1):
        for s in segments:
            if i == 0 and s <= rod_len:
                dp[s] = 1
            elif dp[i] != 0:
                if i + s <= rod_len:
                    dp[i + s] = max(dp[i + s], dp[i] + 1)
    return dp[-1]


if __name__ == '__main__':
    print(dp_rod(3119, [3515, 1021, 7]))
    print(dp_rod2(3119, [3515, 1021, 7]))
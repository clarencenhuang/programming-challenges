import functools


def num_distinct(s, t):
    if len(t) == 0:
        return 1
    if len(s) == 0 or len(s) < len(t):
        return 0
    s_1 = s[1:]
    if s[0] == t[0]:
        return num_distinct(s_1, t[1:]) + num_distinct(s_1, t)
    else:
        return num_distinct(s_1, t)


def num_distinct2(s, t):

    def num_dist(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if s[i] == t[j]:
            return num_dist(i + 1, j + 1) + num_dist(i + 1, j)
        else:
            return num_dist(i + 1, j)

    return num_dist(0, 0)

def num_distinct3(s, t):
    dp = {}
    for j in range(len(t)):
        dp[(-1, j)] = 0
    for i in range(len(s)):
        dp[(i, 0)] = dp[(i - 1, 0)]
        if s[i] == t[0]:
            dp[(i, 0)] += 1

    for j in range(1, len(t)):
        for i in range(0, len(s)):
            if s[i] == t[j]:
                dp[(i, j)] = dp[(i-1, j-1)] + dp[(i-1, j)]
            else:
                dp[(i, j)] = dp[(i-1, j)]
    return dp[(len(s)-1, len(t)-1)]



if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    print(num_distinct3(s, t))
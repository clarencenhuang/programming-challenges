'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

SOLUTION:

dp[i, c] number of ways to end the character with char


dp[i, c] = dp[i - 1, c_i]

'''
from collections import defaultdict

to_mod = 10**9 + 7

def get_combinations(n):
    letters = list(range(5))
    a, e, i, o, u = letters
    FollowMap = {a: {e}, e: {a, i}, i: {a, e, o, u}, o: {i, u}, u: {a}}
    EmissionMap = defaultdict(set)
    for pre, posts in FollowMap.items():
        for post in posts:
            EmissionMap[post].add(pre)

    dp = [[0] * len(letters) for _ in range(n)]
    for l in letters:
        dp[0][l] = 1

    for i in range(1, n):
        for l in letters:
            can_emit_from = EmissionMap[l]
            for le in can_emit_from:
                dp[i][l] += dp[i-1][le]

    return sum(dp[-1]) % to_mod

if __name__ == '__main__':
    print(get_combinations(5))







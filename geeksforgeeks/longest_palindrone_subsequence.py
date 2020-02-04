from functools import lru_cache

def longest_plain_sb(s):

    @lru_cache(None)
    def long_palin(i, j):
        if i == j:
            return 1
        is_end_same = s[i] == s[j]
        if j == i + 1 and is_end_same:
            return 2
        if is_end_same:
            return 2 + long_palin(i+1, j-1)
        else:
            return max(long_palin(i+1, j), long_palin(i, j-1))

    return long_palin(0, len(s)-1)

if __name__ == '__main__':
    print(longest_plain_sb('BBABCBCAB'))
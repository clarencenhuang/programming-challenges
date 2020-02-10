import functools

to_mod = 10**9 + 7


def count_palin(s):
    seen = set()
    for i in range(len(s)):
        for l in range(1, len(s) + 1):
            j = i + l - 1
            if j > len(s) - 1:
                break
            if j == i:
                s_i = s[i]
                seen.add(s_i)
                return s_i
            if j == i + 1:






if __name__ == '__main__':
    print(count_palin('bccb'))
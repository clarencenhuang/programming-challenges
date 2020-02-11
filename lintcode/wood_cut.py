# https://www.lintcode.com/problem/wood-cut/description?_from=ladder&&fromId=2

def wood_cut(logs, k):

    def can_cut(length):
        return sum([l//length for l in logs]) >= k

    max_len = sum(logs) // k
    if max_len < 1:
        return 0
    l, r = 1, max_len
    while r > l + 1:
        print(l, r)
        m = (l + r) // 2
        if can_cut(m):
            l = m
        else:
            r = m
    return l


if __name__ == '__main__':
    wood_cut([232, 12, 456], 10)
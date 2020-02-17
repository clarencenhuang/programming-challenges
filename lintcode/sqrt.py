
def find_sqrt(x):
    l, r = 1, x
    while r > l:
        m = l + (r - l + 1) // 2
        if m * m > x:
            r = m - 1
        else:
            l = m
    return l

if __name__ == '__main__':
    print(find_sqrt(9))
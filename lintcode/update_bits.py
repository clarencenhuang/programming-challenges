

def update_bits(n, m, i, j):
    is_negative = n < 0
    n = abs(n)
    mask = (2 ** 32 - 1) - (2**(j+1) - 1) + (2**i - 1)
    res = (mask & n) + (m << i)

    if is_negative:
        res = -res
    return res


if __name__ == '__main__':
    print(update_bits(-2, 10, 24, 27))

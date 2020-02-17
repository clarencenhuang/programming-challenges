def fast_pow(a, b, n):

    def pow2(a, n):
        if n == 0:
            return 1
        if n == 1:
            return a
        p2 = pow2(a, n//2)
        if n % 2 == 0:
            return (p2 * p2) % b
        else:
            return (p2 * p2 * a) % b

    return pow2(a, n) % b

if __name__ == '__main__':
    print(fast_pow(3, 7, 5))

# https://www.lintcode.com/problem/o1-check-power-of-2/description?_from=ladder&&fromId=2
import math

def check_pow_2(n):
    if n == 0:
        return False
    k = math.log(n, 2)
    return k == int(k)

if __name__ == '__main__':
    print(check_pow_2(5))
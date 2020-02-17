# https://www.lintcode.com/problem/trailing-zeros/description?_from=ladder&&fromId=2


# 0 can only be formed by 5*2, there are an abundance of 2s,
# so count number of 5s, number of 25s, number of 125s..etc
def num_zeros(n):
    total = 0
    divisor = 5
    while n // divisor > 0:
        total += n // divisor
        divisor *= 5
    return total


if __name__ == '__main__':
    print(num_zeros(5))
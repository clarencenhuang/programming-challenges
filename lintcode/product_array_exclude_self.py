# https://www.lintcode.com/problem/product-of-array-exclude-itself/description?_from=ladder&&fromId=2


def product_not_self(arr):
    left, cl = [1], 1
    right, cr = [1], 1
    for i in range(1, len(arr)):
        cl *= arr[i-1]
        left.append(cl)

    for j in range(len(arr) - 2, -1, -1):
        cr *= arr[j+1]
        right.insert(0, cr)

    return [l * r for l, r in zip(left, right)]


if __name__ == '__main__':
    print(product_not_self([1,2,3,4]))
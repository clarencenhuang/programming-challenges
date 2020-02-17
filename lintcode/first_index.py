# https://www.lintcode.com/problem/first-position-of-target/description?_from=ladder&&fromId=2

def first_index(arr, target):
    l, r = 0, len(arr) - 1
    while r > l:
        m = l + (r - l + 1)//2
        if arr[m] > target:
            r = m - 1
        else:
            l = m
    if arr[r] == target:
        return r
    return -1


if __name__ == '__main__':
    print(first_index([1,1,1,2,2,2,2,2,3], 2))

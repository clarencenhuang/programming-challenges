# https://www.lintcode.com/problem/search-insert-position/description?_from=ladder&&fromId=2

def find_insert(arr, target):
    if len(arr) == 0:
        return 0
    if target > arr[-1]:
        return len(arr)
    l, r = 0, len(arr) - 1
    while True:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m
        if r == l:
            return l
        if arr[m] < target:
            l = m + 1
        else:
            r = m

if __name__ == '__main__':
    print(find_insert([1,3,5,6], 3))
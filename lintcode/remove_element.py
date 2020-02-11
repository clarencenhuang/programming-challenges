# https://www.lintcode.com/problem/remove-element/description?_from=ladder&&fromId=2


def remove(arr, k):
    i = 0
    while i < len(arr):
        if arr[i] == k:
            del arr[i]
        else:
            i += 1
    return len(arr)
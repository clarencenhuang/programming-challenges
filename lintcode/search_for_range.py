

def search(arr, target):
    l, r = 0, len(arr)
    # search left
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    first_occurance = l
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    last_occurance = r
    return first_occurance, last_occurance




if __name__ == '__main__':
    print(search([5, 7, 7, 8, 8,8,8, 10, 10], 10))

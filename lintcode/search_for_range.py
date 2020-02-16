def search_asym(arr, target):
    l, r = 0, len(arr) - 1
    while r > l:
        m = (l + r) //2
        if arr[m] < target:
            l = m + 1
        else:
            r = m
    l0 = l
    r = len(arr) - 1
    while r > l:
        m = (l+r+1) // 2
        # why the + 1? consider(10, 10), l=0, r=1, m=0, in this case, we want l to go to r, the + 1 forces that
        if arr[m] > target:
            r = m - 1
        else:
            l = m
    return l0, r




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
    print(search_asym([5, 7, 7, 8, 8,8,8, 10, 10], 8))

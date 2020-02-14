def find_pivot(arr):
    l = 0
    r = len(arr)
    while r > l + 1:
        m = (l + r) // 2
        if arr[l] < arr[m]:
            l = m
        else:
            r = m
    return r


def find_value(arr, target, l=0, r=None):
    if r is None:
        r = len(arr)
    while r > l:
        m = (l + r) // 2
        if target < arr[m]:
            r = m
        else:
            l = m + 1
        if arr[m] == target:
            return m
    return -1

def get_value(arr, target):
    p = find_pivot(arr)
    return max(find_value(arr, target, 0, p), find_value(arr, target, p, len(arr)))

def search_rotated(arr, target):
    l, r = 0, len(arr) - 1
    while True:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m
        if r <= l:
            return -1
        if arr[l] <= arr[m]:  # left half is sorted
            if arr[l] <= target <= arr[m]:
                r = m - 1
            else:
                l = m + 1
        elif arr[m] <= arr[r]:  # right half is sorted
            if arr[m] <= target <= arr[r]:
                l = m + 1
            else:
                r = m - 1

if __name__ == '__main__':
    #print(get_value([4, 5, 1, 2, 3], 4))
    print(search_rotated([4, 5, 1, 2, 3], 5))



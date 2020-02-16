

def search_rotated_2(arr, target):
    l, r = 0, len(arr)-1
    while True:
        m = l + (r-l)//2
        if arr[m] == target:
            return m
        if l >= r:
            return -1

        if arr[m] <= arr[r]: # right half is sorted
            if arr[m] <= target <= arr[r]:
                l = m + 1
            else:
                r = m - 1
        if arr[l] <= arr[m]: # left half is sorted
            if arr[l] <= target <= arr[m]:
                r = m - 1
            else:
                l = m + 1



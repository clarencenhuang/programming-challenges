

def search_min(arr):
    l, r = 0, len(arr) - 1
    while r > l:
        if arr[r] > arr[l]:
            return arr[l]
        m = l + (r - l) // 2
        if arr[m] >= arr[r]:
            l = m + 1
        else:
            r = m
    return arr[r]

if __name__ == '__main__':
    print(search_min([1,1,-1,1]))
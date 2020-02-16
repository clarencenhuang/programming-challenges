


def find_peak(arr):
    l, r = 0, len(arr) - 1
    while r > l:
        m = l + (r - l) // 2
        if arr[m + 1] > arr[m]:
            l = m + 1
        else:
            r = m
    return l

if __name__ == '__main__':
    print(find_peak([1, 2, 1, 3, 4, 5, 7, 6]))



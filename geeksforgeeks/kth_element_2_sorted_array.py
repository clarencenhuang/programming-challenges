def find_kth(arr1, arr2, k):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    i = len(arr1)

    # special case
    if len(arr2) == 0:
        return arr1[k-1]
    if arr2[-1] < arr1[0]:
        return (arr2 + arr1)[k-1]
    elif arr1[-1] < arr2[0]:
        return (arr1 + arr2)[k-1]

    while True:
        j = k - i
        ii = i - 1
        jj = j - 1
        num = arr1[ii]
        n_upper = arr1[ii + 1] if ii < len(arr1) - 1 else 10**8
        comp_lower = arr2[jj]
        comp_upper = arr2[jj+1] if jj < len(arr2) -1 else 10**8
        if comp_lower <= num <= comp_upper:
            return num
        elif num <= comp_lower <= n_upper:
            return comp_lower
        elif num >= comp_upper:
            i = (1 + i) // 2
        elif num <= comp_lower:
            i = (len(arr1) + i) // 2


if __name__ == '__main__':
    a1 = list(map(int, '2 3 6 7 9'.split()))
    a2 = list(map(int, '1 4 8 10'.split()))
    print(find_kth([1, 10, 10, 25, 40, 54, 79], [15, 24, 27, 32, 33, 39, 48, 68, 82, 88, 90], 15))
    print(list(sorted([1, 10, 10, 25, 40, 54, 79] + [15, 24, 27, 32, 33, 39, 48, 68, 82, 88, 90]))[14])
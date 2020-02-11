# https://www.lintcode.com/problem/remove-duplicates-from-sorted-array/?_from=ladder&&fromId=2

def remove_duplicates(arr):
    m = len(arr)
    i = 0
    pos = 0
    while i < len(arr):
        arr[pos] = arr[i]
        pos += 1
        i += 1
        while i > 0 and i < len(arr) and arr[i] == arr[i-1]:
            i += 1

    return pos, arr

if __name__ == '__main__':
    print(remove_duplicates([1, 1, 1, 1]))

n = [2, 1, 3, 1, 2]


def merge(a1, a2):
    arr = []
    while len(a1) or len(a2):
        if len(a1) == 0:
            arr.extend(a2)
            a2 = []
        elif len(a2) == 0:
            arr.extend(a1)
            a1 = []
        else:
            if a1[0] <= a2[0]:
                arr.append(a1.pop(0))
            else:
                arr.append(a2.pop(0))
    return arr


def mergesort(arr):
    if len(arr) == 1:
        return arr
    else:
        m = len(arr) // 2
        a1, a2 = arr[:m], arr[m:]
        return merge(mergesort(a1), mergesort(a2))

if __name__ == '__main__':
    arr = [3, 4,2, 3, 5, 7, 4,6, 8,3, 4]
    print(mergesort(arr))



n = [2, 1, 3, 1, 2]

def inversions(arr):

    def merge(i1, m, i2):
        i = i1
        while i < i2:



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
'''
1,2,3,4
1,2,4,3
1,3,2,4
1,3,4,2

'''

def next_perm(arr):
    # if everything goes down like 4,3,2,1, we just reverse the damn thing

    # otherwise there is a way 1,2,3,4
    to_invert = 0
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            to_swap = i - 1
            for j in range(len(arr)-1, to_swap, -1):
                if arr[j] > arr[to_swap]:
                    arr[j], arr[to_swap] = arr[to_swap], arr[j]
                    break
            to_invert = i
            break
    res = arr[:to_invert] + list(reversed(arr[to_invert:]))
    return res

if __name__ == '__main__':
    print(next_perm([1, 3, 2]))
    print(next_perm([1, 2, 3, 4]))
    print(next_perm([1, 2, 4, 3]))
    print(next_perm([4, 3, 2, 1]))
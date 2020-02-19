# https://leetcode.com/problems/subarray-product-less-than-k/

def less_k(arr, k):
    i = 0
    num_w = 0
    window = 1
    for j, n in enumerate(arr):
        window *= n
        while window >= k and i <= j:
            window /= arr[i]
            i += 1
        if j >= i:
            num_w += (j - i + 1)
    return num_w

if __name__ == '__main__':
    #print(less_k([10, 5, 2, 6], 100))
    print(less_k([1,1,1], 0))





'''
j == 0: 0
if char[j] != char[j-1]
    longest[j] = longest[j-1] + 2 if longest[j-1] is 0
    else longest[j-1] + 1
'''
def longest_alt_subarray(arr):
    dp = [0] * len(arr)
    for i in range(1, len(arr)):
        if arr[i] * arr[i-1] < 0:
            if dp[i-1] == 0:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    v, i = max([(v, i) for i,v in enumerate(dp)])
    return arr[i - v + 1: i + 1]


if __name__ == '__main__':
    print(longest_alt_subarray([1, -2, 6, 4, -3, 2, -4, -3]))




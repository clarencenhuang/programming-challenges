#
# K(i, A) = max(K(i-1, B), K(i-1, C)) + gains_of(A[i])
# K(i, B) = max(K(i-1, A), K(i-1, C)) + gains_of(B[i])
# K(i, C) = max(K(i-1, B), K(i-1, C)) + gains_of(C[i])
#


def get_vacation(vacation_data):
    A, B, C = range(3)
    dp = [[-1 for i in range(3)] for j in range(len(vacation_data))]
    dp[0] = vacation_data[0]
    for i in range(1, len(vacation_data)):
        a, b, c = vacation_data[i]
        dp[i][A] = max(dp[i - 1][B], dp[i - 1][C]) + a
        dp[i][B] = max(dp[i - 1][A], dp[i - 1][C]) + b
        dp[i][C] = max(dp[i - 1][A], dp[i - 1][B]) + c
    return max(dp[-1])


def get_input():
    n = int(input())
    data = []
    for i in range(n):
        el = list(map(int, input().split()))
        data.append(el)
    return data

if __name__ == '__main__':
    assert get_vacation([[10, 40, 70],
                        [20, 50, 80],
                        [30, 60, 90]]) == 210
    assert get_vacation([[100, 10, 1]]) == 100
    assert get_vacation([[6,7,8],
                         [8,8,3],
                         [2,5,2],
                         [7,8,6],
                         [4,6,8],
                         [2,3,4],
                         [7,5,1]]) == 46
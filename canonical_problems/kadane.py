
def kadane(arr):
    cumsum = 0
    max_cumsum = 0
    for i, a in enumerate(arr):
        cumsum = max(a, a + cumsum)
        max_cumsum = max(max_cumsum, cumsum)
    return max_cumsum


if __name__ == '__main__':
    print(kadane([-2, -3, 4, -1, -2, 1, 5, -3]))
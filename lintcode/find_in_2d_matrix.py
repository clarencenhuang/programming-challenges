

def find_2d(mat, target):
    nrows, ncols = len(mat), len(mat[0])
    l, r = 0, nrows * ncols - 1
    while True:
        m = l + (r-l)//2
        row, col = m // ncols, m % ncols
        if mat[row][col] == target:
            return True
        if l >= r:
            return False
        if mat[row][col] < target:
            l = m + 1
        else:
            r = m - 1

if __name__ == '__main__':
    mat = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(find_2d(mat, 8))

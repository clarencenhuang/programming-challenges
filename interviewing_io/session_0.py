# https://start.interviewing.io/interview/54BWnkqzYdZS/replay

def is_toeplitz(mat):
    nrows, ncols = len(mat), len(mat[0])
    is_toeplitz_mat = True
    for i in range(1, nrows):
        for j in range(1, ncols):
            is_toeplitz_mat = is_toeplitz_mat and mat[i][j] == mat[i-1][j-1]
    return is_toeplitz_mat


def cd(path):
    if path[:3] == '../':

    elif path[:2] == './':

    elif path[1] == '/':

    else:



if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
     [5, 1, 2, 3],
     [6, 5, 1, 2]]
    print(is_toeplitz(mat))
    mat_bad = [[1,2,3,4],
     [5,1,9,3],
     [6,5,1,2]]
    print(is_toeplitz(mat_bad))
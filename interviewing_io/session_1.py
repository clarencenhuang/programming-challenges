# https://start.interviewing.io/interview/hgHjxNtFBni1/replay


def num_subseq(a, b):
    # ABAB   AB
    def num_sub(i, j):
        if j == -1:
            return 1
        if i == -1:
            return 0
        if a[i] == b[j]:
            return num_sub(i-1, j) + num_sub(i-1, j-1)
        else:
            return num_sub(i-1, j)

    return num_sub(len(a)-1, len(b)-1)

if __name__ == '__main__':
    print(num_subseq('ABAB', 'AB'))


def merge2(a, m, b):
    assert isinstance(a, list)
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if i < len(a) and (j > len(b) - 1 or a[i] < b[j]):
            i += 1
        else:
            a.insert(i, b[j])
            i += 1
            j += 1
    return a


if __name__ == '__main__':
    print(merge2([1, 2, 3], [4, 5]))
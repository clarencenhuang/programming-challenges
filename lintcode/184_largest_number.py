import functools


def largest_number(arr):
    arr1 = sorted(arr, key=functools.cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))))
    return str(int(''.join(map(str, arr1))))


if __name__ == '__main__':
    print(largest_number([1, 20, 23, 4, 8]))
# boyer moore samplng

def majority_el(arr):
    el = arr[0]
    counter = 1
    for i in range(1, len(arr)):
        if counter == 0:
            el = arr[i]

        if arr[i] == el:
            counter += 1
        else:
            counter -= 1
    return el


if __name__ == '__main__':
    print(majority_el([1, 1, 1, 1, 2, 2, 2]))

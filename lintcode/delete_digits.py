

def del_digits(arr, k):
    stack = []
    removed = 0
    for n in arr:
        while stack and n < stack[-1] and removed < k:
            stack.pop()
            removed += 1
        if not stack and n == "0":
            pass
        else:
            stack.append(n)
    while removed < k and stack:
        stack.pop()
        removed += 1
    return ''.join(stack)


if __name__ == '__main__':
    print(del_digits('178542', 4))
    print(del_digits('568431', 3))
    print(del_digits("90249", 2))



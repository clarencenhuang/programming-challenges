

def reverse_bracket(mystr):
    stack = []
    for c in mystr:
        if c == ')':
            buffer = ''
            while stack:
                char = stack.pop()
                if char == '(':
                    break
                buffer += char
            for k in buffer:
                stack.append(k)
        else:
            stack.append(c)
    return ''.join(stack)

if __name__ == '__main__':
    print(reverse_bracket('ab(sd(love)f)12'))


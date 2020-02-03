# c3[a2[b]]d expand to cabbabbabbd


def do_expand(strlist, expand_num=1):
    buffer = ''
    while strlist:
        head = strlist.pop(0)
        if head == '[':
            pass
        elif head in 'abcdefghijklmnopqrstuvwxyz':
            buffer += head
        elif head in '01234567890':
            next_expand_num = int(head)
            buffer += do_expand(strlist, next_expand_num)
        elif head == ']':
            break
        else:
            raise RuntimeError(f"encountered unexpected thing ${head}")

    return expand_num * buffer


if __name__ == '__main__':
    test_in = 'c3[a2[b]]d'
    print(do_expand(list(test_in)))




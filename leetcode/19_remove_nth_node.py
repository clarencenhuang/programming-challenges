from functools import reduce


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        n  = self
        ls = []
        while n:
            ls.append(n.val)
            n = n.next
        return repr(f'[{",".join(ls)}]')


def makelist(ls):
    return reduce(lambda a, x: ListNode(x, a), reversed(ls), None)


def remove(n, left):
    if n.next is None:
        return n, left - 1
    nex, d = remove(n.next, left)
    if d == 0:
        n.next = nex.next
    else:
        n.next = nex
    return n, d - 1


if __name__ == '__main__':
    ls = [1,2,3,4,5]
    k = makelist(ls)
    n, d = remove(k, 2)
    pass
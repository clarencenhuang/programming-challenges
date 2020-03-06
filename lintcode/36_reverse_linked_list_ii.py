import functools

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def make(arr):
        return functools.reduce(lambda acc, x: ListNode(x, acc), reversed(arr), None)

    def __repr__(self):
        return repr(self.val)


def reverse2(l, m, n):
    node_m = l
    node_m_prev = None
    while m > 1:
        node_m_prev, node_m = node_m, node_m.next
        m -= 1
        n -= 1
    a, b = node_m, node_m.next
    while n > 1:
        a_next, b_next = b, b.next
        b.next = a
        a, b = a_next, b_next
        n -= 1
    node_m.next = b
    if node_m_prev:
        node_m_prev.next = a
        return l
    return a

if __name__ == '__main__':
    # arr = [1,2,3,4,5]
    # l = ListNode.make(arr)
    # reverse2(l, 2, 4)

    # arr = [5]
    # l = ListNode.make(arr)
    # reverse2(l, 1,1)

    arr = [1,2,3,4,5]
    l = ListNode.make(arr)
    reverse2(l, 1, 4)